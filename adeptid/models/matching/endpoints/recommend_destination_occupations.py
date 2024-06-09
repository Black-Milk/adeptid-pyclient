from typing import List, Dict, Optional
from pydantic import (
    BaseModel,
)

from adeptid.models import Candidate, Occupation, OccupationMatch, CandidateID


class RecommendDestinationOccupationsRequest(BaseModel):
    skill_count: Optional[int] = 5
    offset: Optional[int] = 1
    limit: Optional[int] = 10
    candidates: List[Candidate]


class RecommendDestinationOccupationsResponse(BaseModel):
    candidates: Dict[CandidateID, List[OccupationMatch]]
    classifications: Dict[str, Occupation]
    unknown_skills: List[str]
    operation_id: str
