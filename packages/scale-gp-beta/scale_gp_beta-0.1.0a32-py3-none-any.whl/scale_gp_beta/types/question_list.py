# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .question import Question

__all__ = ["QuestionList"]


class QuestionList(BaseModel):
    has_more: bool
    """Whether there are more items left to be fetched."""

    items: List[Question]

    total: int
    """The total of items that match the query.

    This is greater than or equal to the number of items returned.
    """

    limit: Optional[int] = None
    """The maximum number of items to return."""

    object: Optional[Literal["list"]] = None
