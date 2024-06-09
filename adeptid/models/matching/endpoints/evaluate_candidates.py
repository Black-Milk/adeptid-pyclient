from pydantic import BaseModel
from typing import Optional, List, Dict
from adeptid.models import Candidate, Occupation, OccupationMatch, CandidateID


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


CandidatesScores = Dict[CandidateID, List[OccupationMatch]]

Classifications = Dict[str, Occupation]


class EvaluateCandidatesResponse(BaseModel):
    candidates_scores: CandidatesScores
    classifications: Classifications
    unknown_skills: List[str]
    operation_id: str
