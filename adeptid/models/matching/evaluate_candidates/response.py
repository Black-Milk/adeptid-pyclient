from pydantic import BaseModel
from typing import List, Dict
from adeptid.models import Occupation, OccupationMatch, CandidateID


class EvaluateCandidatesResponse(BaseModel):
    candidates_scores: Dict[CandidateID, List[OccupationMatch]]
    classifications: Dict[str, Occupation]
    unknown_skills: List[str]
    operation_id: str
