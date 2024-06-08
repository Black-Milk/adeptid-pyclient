import httpx
import asyncio
import logging
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
import os
from dotenv import load_dotenv
from apiclient_pydantic import ModelDumped, serialize

from models import (
    RecommendDestinationOccupationsResponse,
    RecommendDestinationOccupationsRequest,
)

from models.matching.recommend_destination_occupations.request import (
    Candidate,
    WorkHistory,
)

from pprint import pprint


# placeholder for the AdeptIDClient class as a context manager
from contextlib import aclosing

load_dotenv(override=True)


# Pydantic models as defined above


class AdeptIDClient:
    def __init__(
        self, api_key: str, base_url: str = "https://api.adept-id.com"
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "X-API-KEY": f"{self.api_key}",
            "Content-Type": "application/json",
        }
        self.logger = logging.getLogger(__name__)
        self.client = httpx.AsyncClient()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.client.aclose()

    async def _request(
        self, method: str, endpoint: str, params: dict = None, json: dict = None
    ):
        url = f"{self.base_url}{endpoint}"
        try:
            response = await self.client.request(
                method, url, headers=self.headers, params=params, json=json
            )
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as exc:
            self.logger.error(
                f"An error occurred while requesting {exc.request.url!r}."
            )
            raise
        except httpx.HTTPStatusError as exc:
            self.logger.error(
                f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
            )
            raise

    @serialize(response=RecommendDestinationOccupationsResponse)
    async def recommend_destination_occupations(
        self, request_body: ModelDumped[RecommendDestinationOccupationsRequest]
    ):
        endpoint = "/v2/recommend-destination-occupations"

        return await self._request("POST", endpoint, json=request_body)

    async def close(self):
        await self.client.aclose()


def prepare_request_body():
    destination_occupation_payload = RecommendDestinationOccupationsRequest(
        skill_count=5,
        offset=1,
        limit=10,
        candidates=[
            Candidate(
                id="666",
                skills=["Python", "JavaScript", "React"],
                work_history=[
                    WorkHistory(
                        title="Software Engineer", employer_name="Google"
                    ),
                ],
            )
        ],
    )
    return destination_occupation_payload


async def main(
    request_body,
):
    async with AdeptIDClient(api_key=os.getenv("ADEPT_IO_ID")) as adept_client:
        # Create a request body that satisfies the Pydantic model
        response = await adept_client.recommend_destination_occupations(
            request_body=request_body
        )

        pprint(response)


if __name__ == "__main__":
    request = prepare_request_body()
    asyncio.run(main(request))
