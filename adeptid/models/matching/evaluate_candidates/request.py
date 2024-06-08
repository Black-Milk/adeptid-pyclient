from pydantic import BaseModel
from typing import Optional, List
from adeptid.models import Candidate


class Education(BaseModel):
    level: str
    degree_type: Optional[str] = None
    subject: Optional[str] = None
    required: bool


class DestinationJob(BaseModel):
    title: str
    naics: Optional[str] = None
    employer_name: Optional[str] = None
    skills: List[str]
    education: List[Education]


class EvaluateCandidatesRequest(BaseModel):
    skill_count: Optional[int]
    candidates: List[Candidate]
    destination_job: DestinationJob
