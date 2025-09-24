# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MaterialUpdateParams"]


class MaterialUpdateParams(TypedDict, total=False):
    reference_title: Annotated[str, PropertyInfo(alias="referenceTitle")]
    """Reference title"""

    reference_url: Annotated[str, PropertyInfo(alias="referenceUrl")]
    """Reference URL"""
