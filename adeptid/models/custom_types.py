from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated
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
