from typing import List, Dict, Optional
from pydantic import (
    BaseModel,
)

from adeptid.models import (
    Candidate,
    Occupation,
    Skills,
    CandidateID,
    candidate_factory,
)


class RecommendDestinationOccupationsRequest(BaseModel):
    """Request to recommend destination occupations."""

    skill_count: Optional[int] = 5
    offset: Optional[int] = 1
    limit: Optional[int] = 10
    candidates: List[Candidate]


Classifications = Dict[str, Occupation]


class DestinationOccupationMatch(BaseModel):
    match_score: float
    match_score_category: str
    occupation: Occupation
    skills: Skills


class RecommendDestinationOccupationsResponse(BaseModel):
    candidates: Dict[CandidateID, List[DestinationOccupationMatch]]
    classifications: Classifications
    unknown_skills: List[str]
    operation_id: str


def request_factory():
    candidate = candidate_factory()
    return RecommendDestinationOccupationsRequest(
        skill_count=5,
        offset=1,
        limit=10,
        candidates=[candidate],
    )
