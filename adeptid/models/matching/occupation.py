from pydantic import BaseModel
from typing import Annotated, List


ONetCode = Annotated[str, "ONet Code"]


class Occupation(BaseModel):
    code: ONetCode
    common_name: str
    common_name_singular: str
    name: str


class Gap(BaseModel):
    category: str
    name: str
    skill_category: str
    skill_type: str
    value: float


class Overlap(Gap):
    pass


class Skills(BaseModel):
    gaps: List[Gap]
    overlaps: List[Overlap]


class OccupationMatch(BaseModel):
    match_score: float
    match_score_category: str
    occupation: Occupation
    skills: Skills
