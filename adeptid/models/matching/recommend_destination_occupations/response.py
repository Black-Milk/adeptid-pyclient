from typing import List, Dict, Annotated
from pydantic import (
    BaseModel,
)

CandidateID = Annotated[str, "Candidate ID"]
ONetCode = Annotated[str, "ONet Code"]


class Occupation(BaseModel):
    code: ONetCode
    common_name: str
    common_name_singular: str
    name: str


class Gaps(BaseModel):
    category: str
    name: str
    skill_category: str
    skill_type: str
    value: float


class Overlaps(Gaps):
    pass


class Skills(BaseModel):
    gaps: List[Gaps]
    overlaps: List[Overlaps]


class OccupationMatch(BaseModel):
    match_score: float
    match_score_category: str
    occupation: Occupation
    skills: Skills


class RecommendDestinationOccupationResponse(BaseModel):
    candidates: Dict[CandidateID, List[OccupationMatch]]
    classifications: Dict[str, Occupation]
    operation_id: str
    unknown_skills: List[str]
