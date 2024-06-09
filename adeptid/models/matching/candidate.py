from typing import List, Optional
from pydantic import (
    BaseModel,
)
from typing_extensions import Annotated

from adeptid.models import Date, EducationLevel, DegreeType


CandidateID = Annotated[str, "Candidate ID"]


class Education(BaseModel):
    level: str | EducationLevel
    degree_type: Optional[str | DegreeType] = None
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
    id: CandidateID
    work_history: List[WorkHistory]
    skills: Optional[List[str]] = None
    education: Optional[List[Education]] = None


def work_history_factory() -> WorkHistory:
    return WorkHistory(
        title="Software Engineer",
        employer_name="Google",
        start_date="01/2019",
        end_date="01/2021",
    )


def education_factory() -> Education:
    return Education(
        level="BACHELORS",
        degree_type="BACHELOR OF SCIENCE",
        subject="Computer Science",
        start_date="01/2015",
        end_date="01/2019",
        institution="Stanford University",
        gpa=3.9,
        summary="Graduated with honors",
    )


def candidate_factory() -> Candidate:
    skills = ["Python", "Java", "C++"]
    work_history = [work_history_factory()]
    education = [education_factory()]
    return Candidate(
        id="123", skills=skills, work_history=work_history, education=education
    )
