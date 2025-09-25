import logging, os
import argparse
import sys
from typing import List, Dict, Any, Set, Tuple, Optional
from collections.abc import Sequence

import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import (
    AutoTokenizer,
    AutoConfig,
    BertConfig,
    AutoModel,
    Pipeline,
    PreTrainedModel,
)
from transformers.modeling_outputs import TokenClassifierOutput

from impresso_pipelines.newsagencies.config import AGENCY_LINKS

log_level = os.environ.get("LOGLEVEL", "WARNING").upper()  # Set logging level
logging.basicConfig(level=getattr(logging, log_level, logging.DEBUG), force=True)
logger = logging.getLogger(__name__)


class NewsAgencyTokenClassifier(PreTrainedModel):
    """
    A custom token classification model for identifying entities in text.

    Attributes:
        config_class (type): Configuration class for the model.
        num_labels (int): Number of classification labels.
        bert (nn.Module): Backbone encoder model./
        dropout (nn.Dropout): Dropout layer for regularization.
        token_classifier (nn.Linear): Linear layer for token classification.
    """

    config_class = BertConfig
    _keys_to_ignore_on_load_missing = [r"position_ids"]

    def __init__(self, config: BertConfig):
        """
        Initialize the token classifier model.

        Args:
            config (BertConfig): Configuration object for the model.
        """
        super().__init__(config)
        self.num_labels = len(config.id2label)

        self.bert = AutoModel.from_config(config)

        dropout_prob = (
            getattr(config, "classifier_dropout", None)
            or getattr(config, "hidden_dropout_prob", 0.0)
            or 0.0
        )
        self.dropout = nn.Dropout(dropout_prob)
        self.token_classifier = nn.Linear(config.hidden_size, self.num_labels)

        self.post_init()

    def forward(
        self,
        input_ids: Optional[torch.Tensor] = None,
        attention_mask: Optional[torch.Tensor] = None,
        token_type_ids: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.Tensor] = None,
        head_mask: Optional[torch.Tensor] = None,
        inputs_embeds: Optional[torch.Tensor] = None,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: bool = True,
    ) -> TokenClassifierOutput:
        """
        Perform a forward pass through the model.

        Args:
            input_ids (Optional[torch.Tensor]): Input token IDs.
            attention_mask (Optional[torch.Tensor]): Attention mask.
            token_type_ids (Optional[torch.Tensor]): Token type IDs.
            position_ids (Optional[torch.Tensor]): Position IDs.
            head_mask (Optional[torch.Tensor]): Head mask.
            inputs_embeds (Optional[torch.Tensor]): Input embeddings.
            output_attentions (Optional[bool]): Whether to return attentions.
            output_hidden_states (Optional[bool]): Whether to return hidden states.
            return_dict (bool): Whether to return a dictionary.

        Returns:
            TokenClassifierOutput: Model output containing logits, hidden states, and attentions.
        """
        outputs = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        # Dropout is not active during inference (model.eval()), but is kept to match the model structure
        sequence_output = self.dropout(outputs[0])

        # Compute logits for token classification
        logits = self.token_classifier(sequence_output)

        # Return logits and optionally hidden states and attentions
        if not return_dict:
            return (logits,) + outputs[2:]

        return TokenClassifierOutput(
            logits=logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )


class ChunkAwareTokenClassification(Pipeline):
    """
    A custom pipeline for token classification with chunk handling.

    Attributes:
        min_score (float): Minimum confidence score for filtering entities.
    """

    def __init__(self, *args: Any, min_score: float = 0.50, **kwargs: Any):
        """
        Initialize the pipeline.

        Args:
            min_score (float): Minimum confidence score for filtering entities.
        """
        super().__init__(*args, **kwargs)
        self.min_score = min_score

    def _sanitize_parameters(
        self, **kwargs: Any
    ) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
        """
        Sanitize parameters for the pipeline.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]: Sanitized parameters.
        """
        return kwargs, {}, {}

    def preprocess(self, texts: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        Tokenize and prepare input text(s) for the model.

        Args:
            texts (str or List[str]): Input text(s).

        Returns:
            Dict[str, Any]: Tokenized input for the model.
        """
        if isinstance(texts, str):
            texts = [texts]
        return self.tokenizer(
            texts,
            return_tensors="pt",
            truncation=True,
            padding="max_length",
            max_length=self.tokenizer.model_max_length,
            stride=64,
            return_overflowing_tokens=True,
            return_offsets_mapping=True,
            return_attention_mask=True,
        )

    def _forward(
        self, inputs: Dict[str, torch.Tensor]
    ) -> Tuple[TokenClassifierOutput, Dict[str, torch.Tensor]]:
        """
        Perform a forward pass through the model.

        Args:
            inputs (Dict[str, torch.Tensor]): Tokenized inputs.

        Returns:
            Tuple[TokenClassifierOutput, Dict[str, torch.Tensor]]: Model outputs and inputs.
        """
        with torch.no_grad():
            outputs = self.model(
                input_ids=inputs["input_ids"].to(self.model.device),
                attention_mask=inputs["attention_mask"].to(self.model.device),
            )
        return outputs, inputs

    def postprocess(
        self,
        model_and_inputs: Tuple[TokenClassifierOutput, Dict[str, torch.Tensor]],
        **kwargs: Any,
    ) -> List[List[Dict[str, Any]]]:
        """
        Extract entities from model outputs.

        Args:
            model_and_inputs (Tuple[TokenClassifierOutput, Dict[str, torch.Tensor]]): Model outputs and inputs.

        Returns:
            List[List[Dict[str, Any]]]: List of extracted entities for each input text.
        """
        model_outputs, tokenised = model_and_inputs
        id2label = self.model.config.id2label
        batch_logits = model_outputs.logits

        # If batch is flattened due to overflow, group by 'overflow_to_sample_mapping'
        mapping = tokenised.get("overflow_to_sample_mapping", None)
        if mapping is not None:
            # Group results by sample index
            grouped_results = [[] for _ in range(max(mapping.tolist()) + 1)]
            seen_list = [set() for _ in grouped_results]
            for i in range(batch_logits.size(0)):
                logits = batch_logits[i]
                offsets = tokenised["offset_mapping"][i]
                att_mask = tokenised["attention_mask"][i]
                tokens = self.tokenizer.convert_ids_to_tokens(tokenised["input_ids"][i])
                sample_idx = mapping[i].item()
                current_word, current_logits, current_offsets = [], None, []
                for tok, mask, offs, logit in zip(tokens, att_mask, offsets, logits):
                    if mask.item() == 0 or tok in {"[CLS]", "[SEP]", "[PAD]"}:
                        continue
                    start, stop = offs.tolist()
                    if not tok.startswith("##"):
                        if current_word and current_logits is not None:
                            ent = self._finalise_word(
                                current_word,
                                current_logits,
                                current_offsets,
                                id2label,
                                seen_list[sample_idx],
                            )
                            if ent:
                                grouped_results[sample_idx].append(ent)
                        current_word = [tok]
                        current_logits = logit
                        current_offsets = [(start, stop)]
                    else:
                        current_word.append(tok)
                        current_offsets.append((start, stop))
                if current_word:
                    ent = self._finalise_word(
                        current_word, current_logits, current_offsets, id2label, seen_list[sample_idx]
                    )
                    if ent:
                        grouped_results[sample_idx].append(ent)
            return grouped_results
        else:
            # Single input fallback
            results: List[Dict[str, Any]] = []
            seen: Set[Tuple[int, int, str]] = set()
            for i in range(batch_logits.size(0)):
                logits = batch_logits[i]
                offsets = tokenised["offset_mapping"][i]
                att_mask = tokenised["attention_mask"][i]
                tokens = self.tokenizer.convert_ids_to_tokens(tokenised["input_ids"][i])
                current_word, current_logits, current_offsets = [], None, []
                for tok, mask, offs, logit in zip(tokens, att_mask, offsets, logits):
                    if mask.item() == 0 or tok in {"[CLS]", "[SEP]", "[PAD]"}:
                        continue
                    start, stop = offs.tolist()
                    if not tok.startswith("##"):
                        if current_word and current_logits is not None:
                            ent = self._finalise_word(
                                current_word,
                                current_logits,
                                current_offsets,
                                id2label,
                                seen,
                            )
                            if ent:
                                results.append(ent)
                        current_word = [tok]
                        current_logits = logit
                        current_offsets = [(start, stop)]
                    else:
                        current_word.append(tok)
                        current_offsets.append((start, stop))
                if current_word:
                    ent = self._finalise_word(
                        current_word, current_logits, current_offsets, id2label, seen
                    )
                    if ent:
                        results.append(ent)
            return [results]

    def _finalise_word(
        self,
        tokens: List[str],
        first_logits: torch.Tensor,
        offsets: List[Tuple[int, int]],
        id2label: Dict[int, str],
        seen: Set[Tuple[int, int, str]],
    ) -> Optional[Dict[str, Any]]:
        """
        Finalize a word by determining its entity label and confidence score.

        Args:
            tokens (List[str]): List of sub-tokens.
            first_logits (torch.Tensor): Logits for the first sub-token.
            offsets (List[Tuple[int, int]]): Character offsets for the tokens.
            id2label (Dict[int, str]): Mapping from label IDs to label names.
            seen (Set[Tuple[int, int, str]]): Set of seen entities to avoid duplicates.

        Returns:
            Optional[Dict[str, Any]]: Finalized entity or None if suppressed.
        """
        if first_logits is None:
            return None
        probs = F.softmax(first_logits, dim=-1)
        conf, idx = torch.max(probs, dim=-1)
        label = id2label[int(idx)]

        if label == "O" or conf < self.min_score:
            return None

        # Recalculate offsets based on the reconstructed word
        word = self.tokenizer.convert_tokens_to_string(tokens)
        start = offsets[0][0]
        end = offsets[-1][1]  # Internally still use 'end'

        key = (start, end, label)
        if key in seen:
            return None
        seen.add(key)

        logger.info(
            f"Surface='{word}'  Label={label}  Relevance={conf:.3f} "
            f" Offset=({start},{end})"
        )

        return {
            "word": word,
            "entity": label,
            "score": float(conf),
            "start": int(start),
            "stop": int(end),  # Externally represented as 'stop'
        }


class NewsAgenciesPipeline:
    """
    A pipeline for extracting news agency entities from text.

    Attributes:
        model: Pre-loaded token classification model.
        tokenizer: Pre-loaded tokenizer.
        ner: Pre-loaded NER pipeline.
        model_id: Model identifier used for loading.
    """

    def __init__(self, model_id: str = "impresso-project/ner-newsagency-bert-multilingual", 
                 min_relevance: float = 0.1, batch_size: int = 1):
        """
        Initialize the pipeline with pre-loaded models and components.
        
        Args:
            model_id (str): Model identifier.
            min_relevance (float): Default minimum confidence score for filtering entities.
            batch_size (int): Default batch size for processing.
        """
        self.model_id = model_id
        self.default_min_relevance = min_relevance
        self.default_batch_size = batch_size
        
        # Load model configuration and components once
        config = AutoConfig.from_pretrained(model_id)
        self.model = NewsAgencyTokenClassifier.from_pretrained(model_id, config=config)
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        
        # Set model to evaluation mode for inference
        self.model.eval()
        
        # Determine device once
        if torch.cuda.is_available():
            device = 0
        elif torch.backends.mps.is_available():
            device = "mps"
        else:
            device = -1
        
        # Initialize NER pipeline once
        self.ner = ChunkAwareTokenClassification(
            model=self.model,
            tokenizer=self.tokenizer,
            min_score=min_relevance,
            device=device,
            batch_size=batch_size,
        )

    def __call__(self, input_texts: Any, min_relevance: Optional[float] = None, 
                 diagnostics: bool = False, suppress_entities: Optional[Sequence[str]] = [], 
                 batch_size: Optional[int] = None) -> Any:
        """
        Run the pipeline to extract entities from text(s).

        Args:
            input_texts (str or List[str]): Input text(s) for processing.
            min_relevance (Optional[float]): Minimum confidence score for filtering entities. 
                                           If None, uses the default set during initialization.
            diagnostics (bool): Whether to include diagnostics in the output.
            suppress_entities (Optional[Sequence[str]]): Entities to suppress.
            batch_size (Optional[int]): Batch size for processing. If None, uses the default.

        Returns:
            List[Dict[str, Any]] or Dict[str, Any]: Extracted entities and summary for each input.
        """
        self.model.eval()
        if min_relevance is not None and min_relevance != self.ner.min_score:
            self.ner.min_score = min_relevance

        # Use provided batch_size or fall back to default
        current_batch_size = batch_size if batch_size is not None else self.default_batch_size

        suppress_entities = suppress_entities + ['org.ent.pressagency.unk', 'ag', 'pers.ind.articleauthor']

        # Accept single string or list of strings
        if isinstance(input_texts, str):
            input_texts = [input_texts]
        entities_batch = self.ner(input_texts, batch_size=current_batch_size)

        SUPPRESS = frozenset(suppress_entities)
        results = []

        for input_text, entities in zip(input_texts, entities_batch):
            if isinstance(entities, list) and all(isinstance(e, list) for e in entities):
                # Flatten nested lists if entities are grouped
                entities = [item for sublist in entities for item in sublist]

            merged: List[Dict[str, Any]] = []
            current: Optional[Dict[str, Any]] = None

            for tok in entities:
                if not isinstance(tok, dict):
                    logger.error(f"Invalid token format: {tok}")
                    continue
                entity = tok.get("entity", "")
                if not isinstance(entity, str):
                    logger.error(f"Invalid entity format: {entity}")
                    continue
                iob, base = entity.split("-", 1)
                if base in SUPPRESS:
                    continue
                if iob == "B":
                    if current:
                        merged.append(current)
                    start = tok["start"]
                    stop = tok["stop"]
                    current = {
                        "surface": input_text[start:stop],
                        "entity": base,
                        "start": start,
                        "stop": stop,
                        "relevance": round(tok["score"], 3),
                    }
                elif iob == "I":
                    if current and current["entity"] == base:
                        start = current["start"]
                        stop = tok["stop"]
                        current["surface"] = input_text[start:stop]
                        current["stop"] = stop
                        current["relevance"] = max(current["relevance"], tok["score"])
                        current["relevance"] = round(current["relevance"], 3)
                    else:
                        continue
            if current:
                merged.append(current)

            summary = {}
            for ent in merged:
                summary[ent["entity"]] = max(
                    summary.get(ent["entity"], 0.0), round(ent["relevance"], 3)
                )
            sorted_items = sorted(summary.items(), key=lambda item: item[1], reverse=True)
            summary = [
                {"uid": uid, "relevance": relevance}
                for uid, relevance in sorted_items
            ]
            merged.sort(key=lambda x: x["relevance"], reverse=True)
            for agency in merged:
                agency["wikidata_link"] = AGENCY_LINKS.get(agency['entity'].replace("org.ent.pressagency.", ""), None)
            for agency in summary:
                agency["wikidata_link"] = AGENCY_LINKS.get(agency['uid'].replace("org.ent.pressagency.", ""), None)
            merged_dict = {
                "agencies": merged,
            }
            summary_dict = {
                "agencies": summary,
            }
            if diagnostics:
                if 'agencies' in merged_dict and isinstance(merged_dict['agencies'], list):
                    new_agencies = []
                    for item in merged_dict['agencies']:
                        new_item = {}
                        for key in item:
                            if key == 'entity':
                                new_item['uid'] = item[key]
                            else:
                                new_item[key] = item[key]
                        new_agencies.append(new_item)
                    merged_dict['agencies'] = new_agencies
                results.append(merged_dict)
            else:
                results.append(summary_dict)
        # Return single result if input was a string, else list
        if len(results) == 1:
            return results[0]
        return results