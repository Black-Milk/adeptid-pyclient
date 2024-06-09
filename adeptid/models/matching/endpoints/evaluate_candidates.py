from pydantic import BaseModel
from typing import Optional, List, Dict, Literal
from adeptid.models import (
    EducationLevel,
    DegreeType,
    Candidate,
    Occupation,
    OccupationMatch,
    CandidateID,
    candidate_factory,
)


CandidatesScores = Dict[CandidateID, List[OccupationMatch]]

Classifications = Dict[str, Occupation]


class DestinationEducation(BaseModel):
    level: str | EducationLevel
    degree_type: Optional[str | DegreeType] = None
    subject: Optional[str] = None
    required: bool


class DestinationJob(BaseModel):
    title: str
    naics: Optional[str] = None
    employer_name: Optional[str] = None
    skills: List[str]
    education: List[DestinationEducation]


class EvaluateCandidatesRequest(BaseModel):
    skill_count: Optional[int]
    candidates: List[Candidate]
    destination_job: DestinationJob


class EvaluateCandidatesResponse(BaseModel):
    candidates_scores: CandidatesScores
    classifications: Classifications
    unknown_skills: List[str]
    operation_id: str


def destination_education_factory():
    return DestinationEducation(
        level="BACHELORS",
        degree_type="BACHELOR OF SCIENCE",
        subject="Computer Science",
        required=True,
    )


def destination_job_factory():
    destination_education = destination_education_factory()
    return DestinationJob(
        title="Software Engineer",
        employer_name="Google",
        skills=["Python", "Java", "C++"],
        education=[destination_education],
    )


def request_factory():
    candidate = candidate_factory()
    destination_job = destination_job_factory()
    return EvaluateCandidatesRequest(
        skill_count=5,
        candidates=[candidate],
        destination_job=destination_job,
    )
