from typing import List, Optional, Annotated
from pydantic import (
    BaseModel,
)

from adeptid.models import Date

CandidateID = Annotated[str, "Candidate ID"]


class Education(BaseModel):
    level: str
    degree_type: Optional[str] = None
    subject: Optional[str] = None
    start_date: Optional[Date] = None
    end_date: Optional[Date] = None
    institution: Optional[str] = None
    gpa: Optional[float] = None
    summary: Optional[str] = None


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
    education: List[Education]
