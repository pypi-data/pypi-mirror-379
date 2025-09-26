"""Base Pipeline Preset Config.

Authors:
    Ryan Ignatius Hadiwijaya (ryan.i.hadiwijaya@gdplabs.id)

References:
    NONE
"""

from typing import Any

from pydantic import BaseModel, Field

from glchat_plugin.config.constant import (
    WEB_SEARCH_BLACKLIST_DEFAULT,
    WEB_SEARCH_WHITELIST_DEFAULT,
    ReferenceFormatterType,
    SearchType,
)


class BasePipelinePresetConfig(BaseModel):
    """A Pydantic model representing the base preset configuration of all pipelines.

    Attributes:
        pipeline_preset_id (str): The pipeline preset id.
        supported_models (dict[str, Any]): The supported models.
        supported_agents (list[str]): The supported agents.
        support_pii_anonymization (bool): Whether the pipeline supports pii anonymization.
        support_multimodal (bool): Whether the pipeline supports multimodal.
        use_docproc (bool): Whether to use the document processor.
        search_types (list[SearchType]): The supported search types.
        anonymize_em (bool): Whether to anonymize before using the embedding model.
        anonymize_lm (bool): Whether to anonymize before using the language model.
        augment_context (bool): Whether context augmentation from the knowledge base is allowed.
        chat_history_limit (int): The chat history limit. If the value is negative, no limit will be applied.
        enable_guardrails (bool): Whether to enable guardrails.
        enable_smart_search_integration (bool): Whether to enable smart search integration.
        normal_search_top_k (int): The top k for normal search. Must be greater than or equal to 1.
        prompt_context_char_threshold (int): The character limit above which the prompt is assumed
            to have contained the context.
        reference_formatter_batch_size (int): The reference formatter batch size.
        reference_formatter_threshold (float): The reference formatter threshold.
        reference_formatter_type (ReferenceFormatterType): The reference formatter type.
        rerank_kwargs (str): The rerank kwargs.
        rerank_type (str): The rerank type.
        smart_search_top_k (int): The top k for smart search. Must be greater than or equal to 1.
        use_cache (bool): Whether to use cache.
        use_model_knowledge (bool): Whether to use model knowledge.
        vector_weight (float): The vector weight. Must be between 0 and 1 (inclusive).
        web_search_blacklist (str): The web search blacklist.
        web_search_top_k (int): The top k for web search. Must be greater than or equal to 1.
        web_search_whitelist (str): The web search whitelist.
    """

    pipeline_preset_id: str
    supported_models: dict[str, Any]
    supported_agents: list[str]
    support_pii_anonymization: bool
    support_multimodal: bool
    use_docproc: bool
    search_types: list[SearchType]
    anonymize_em: bool
    anonymize_lm: bool
    augment_context: bool
    chat_history_limit: int
    enable_guardrails: bool = False
    enable_smart_search_integration: bool = False
    normal_search_top_k: int = Field(ge=1)
    prompt_context_char_threshold: int = 32000
    reference_formatter_batch_size: int = Field(ge=1)
    reference_formatter_threshold: float = Field(ge=0, le=1)
    reference_formatter_type: ReferenceFormatterType
    rerank_kwargs: str = "{}"
    rerank_type: str = ""
    smart_search_top_k: int = Field(ge=1)
    use_cache: bool
    use_model_knowledge: bool
    vector_weight: float = Field(ge=0, le=1)
    web_search_blacklist: str = Field(default=WEB_SEARCH_BLACKLIST_DEFAULT)
    web_search_top_k: int = Field(ge=1)
    web_search_whitelist: str = Field(default=WEB_SEARCH_WHITELIST_DEFAULT)
