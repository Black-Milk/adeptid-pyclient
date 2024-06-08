from typing import List, Optional, Any
from pydantic import (
    BaseModel,
)

from adeptid.models.custom_types import Date


class WorkHistory(BaseModel):
    title: str
    naics: Optional[str] = None
    employer_name: Optional[str] = None
    start_date: Optional[Date] = None
    end_date: Optional[Date] = None


class Candidate(BaseModel):
    id: str
    skills: List[str]
    work_history: List[WorkHistory]


class RecommendDestinationOccupationsRequest(BaseModel):
    skill_count: Optional[int]
    offset: Optional[int]
    limit: Optional[int]
    candidates: List[Candidate]
