from pydantic.functional_validators import AfterValidator
from typing import Annotated, Literal
import dateparser


def date_format_validator(v: str) -> str:
    """
    Validate that the date string is in the format MM/YYYY

    Args:
        v (str): The date string to validate
    """

    if v is not None:
        parsed_date = dateparser.parse(v)
        return parsed_date.strftime("%m/%Y")


Date = Annotated[str, AfterValidator(date_format_validator)]


EducationLevel = Literal[
    "DOCTORATE",
    "MASTERS",
    "BACHELORS",
    "ASSOCIATES",
    "HIGH_SCHOOL",
    "CERTIFICATE",
]

DegreeType = Literal[
    "GED",
    "HIGH SCHOOL DIPLOMA",
    "CERTIFICATE",
    "ASSOCIATE OF ARTS",
    "ASSOCIATE OF APPLIED SCIENCE",
    "ASSOCIATE OF SCIENCE",
    "ASSOCIATE OF NURSING",
    "ASSOCIATE DEGREE - GENERAL",
    "BACHELOR OF ARTS",
    "BACHELOR OF SCIENCE",
    "BACHELOR OF ENGINEERING",
    "BACHELOR OF FINE ARTS",
    "BACHELOR OF NURSING",
    "BACHELOR'S DEGREE - GENERAL",
    "MASTER OF ARTS",
    "MASTER OF SCIENCE",
    "MASTER OF ENGINEERING",
    "MASTER OF PHILOSOPHY",
    "MASTER OF BUSINESS ADMINISTRATION",
    "MASTER OF PUBLIC ADMINISTRATION",
    "MASTER OF LIBRARY SCIENCE",
    "MASTER OF SOCIAL WORK",
    "MASTER OF PUBLIC HEALTH",
    "MASTER OF FINE ARTS",
    "MASTER OF EDUCATION",
    "MASTER OF LAWS",
    "MASTER'S DEGREE - GENERAL",
    "DOCTOR OF CHIROPRACTIC",
    "DOCTOR OF DENTAL MEDICINE",
    "DOCTOR OF DENTAL SURGERY",
    "JURIS DOCTOR",
    "DOCTOR OF MEDICINE",
    "DOCTOR OF OSTEOPATHIC MEDICINE",
    "DOCTOR OF OPTOMETRY",
    "DOCTOR OF PHARMACY",
    "DOCTOR OF PODIATRY",
    "DOCTOR OF VETERINARY MEDICINE",
    "DOCTOR OF PHILOSOPHY",
    "DOCTOR OF SCIENCE",
    "DOCTOR OF EDUCATION",
    "DOCTOR'S DEGREE - GENERAL",
]
