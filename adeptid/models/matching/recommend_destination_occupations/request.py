from typing import List, Optional, Any
from pydantic import (
    BaseModel,
)

from adeptid.models import Candidate


class RecommendDestinationOccupationsRequest(BaseModel):
    skill_count: Optional[int]
    offset: Optional[int]
    limit: Optional[int]
    candidates: List[Candidate]
