# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MaterialCreateParams", "Content", "Reference"]


class MaterialCreateParams(TypedDict, total=False):
    content: Required[Content]
    """Content details"""

    name: Required[str]
    """Name of the material"""

    folder_id: Annotated[str, PropertyInfo(alias="folderId")]
    """Folder ID to place the material in"""

    references: Iterable[Reference]
    """References that this material cites"""


class Content(TypedDict, total=False):
    type: Required[Literal["text", "pdf", "video", "audio", "url"]]
    """Type of content"""

    source_url: Annotated[str, PropertyInfo(alias="sourceUrl")]
    """URL to fetch content from"""

    text: str
    """Text content (for text type)"""

    url: str
    """URL to the content (for url type)"""


class Reference(TypedDict, total=False):
    title: Required[str]
    """Reference title"""

    url: str
    """Reference URL"""
