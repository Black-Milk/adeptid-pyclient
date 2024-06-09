from pydantic import BaseModel
from typing import Optional, List, Dict

from adeptid.models import ONetCode


class RecommendSourceOccupationsRequest(BaseModel):
    occupation_code: ONetCode
    match_score_min: Optional[float] = 0.5
    skill_count: Optional[int] = 5
    offset: Optional[int] = 1
    limit: Optional[int] = 10
    occupation_subset: Optional[str] = None
    occupation_taxonomy: Optional[str] = "onet_2019"


class WageStats(BaseModel):
    wage_10th_percentile: int
    wage_90th_percentile: int
    wage_mean: int
    wage_median: int


class TransferableSkill(BaseModel):
    category: str
    name: str
    skill_category: str
    skill_type: str
    value: float


class SkillGap(BaseModel):
    skill_gap_category: str
    skill_gap_value: float
    skill_name: str


class DestinationOccupation(BaseModel):
    destination_wages: WageStats
    match_score: float
    match_score_category: str
    occupation_code: ONetCode
    occupation_common_name: str
    occupation_common_name_singular: str
    occupation_name: str
    skills_gap: List[SkillGap]
    skills_transferable: List[TransferableSkill]
    source_wages: WageStats


RecommendSourceOccupationsResponse = List[DestinationOccupation]
