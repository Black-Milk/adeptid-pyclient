import httpx
import asyncio
import logging
import os
from dotenv import load_dotenv
from apiclient_pydantic import ModelDumped, serialize

from models import (
    EvaluateCandidatesRequest,
    EvaluateCandidatesResponse,
    RecommendSourceOccupationsRequest,
    RecommendSourceOccupationsResponse,
    RecommendDestinationOccupationsRequest,
    RecommendDestinationOccupationsResponse,
)

from models import (
    recommend_destination_occupations_request_factory,
    recommend_source_occupations_request_factory,
    evaluate_candidates_request_factory,
)

from pprint import pprint


# placeholder for the AdeptIDClient class as a context manager

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

    @serialize(response=EvaluateCandidatesResponse)
    async def evaluate_candidates(
        self, request_body: ModelDumped[EvaluateCandidatesRequest]
    ):
        endpoint = "/v2/evaluate-candidates"

        return await self._request("POST", endpoint, json=request_body)

    @serialize(response=RecommendDestinationOccupationsResponse)
    async def recommend_destination_occupations(
        self, request_body: ModelDumped[RecommendDestinationOccupationsRequest]
    ):
        endpoint = "/v2/recommend-destination-occupations"

        return await self._request("POST", endpoint, json=request_body)

    @serialize(response=RecommendSourceOccupationsResponse)
    async def recommend_source_occupations(
        self, request_body: ModelDumped[RecommendSourceOccupationsRequest]
    ):
        endpoint = "/v2/recommend-source-occupations"

        return await self._request("POST", endpoint, json=request_body)

    async def close(self):
        await self.client.aclose()


def request_factory_selector(endpoint: str):
    match endpoint:
        case "recommend_destination_occupations":
            return recommend_destination_occupations_request_factory()
        case "recommend_source_occupations":
            return recommend_source_occupations_request_factory()
        case "evaluate_candidates":
            return evaluate_candidates_request_factory()
        case _:
            raise ValueError("Invalid endpoint")


async def main(request_body):
    async with AdeptIDClient(api_key=os.getenv("ADEPT_IO_ID")) as adept_client:
        # Create a request body that satisfies the Pydantic model
        response = await adept_client.recommend_source_occupations(request_body)
        pprint(response)


if __name__ == "__main__":
    request = request_factory_selector("recommend_source_occupations")
    asyncio.run(main(request))
