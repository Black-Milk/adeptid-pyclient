from typing import List, Dict
from pydantic import (
    BaseModel,
)

from adeptid.models import Occupation, OccupationMatch, CandidateID


class RecommendDestinationOccupationsResponse(BaseModel):
    candidates: Dict[CandidateID, List[OccupationMatch]]
    classifications: Dict[str, Occupation]
    unknown_skills: List[str]
    operation_id: str
