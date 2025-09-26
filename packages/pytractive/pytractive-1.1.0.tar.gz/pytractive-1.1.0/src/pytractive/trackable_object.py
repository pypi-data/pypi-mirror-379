from datetime import datetime
from typing import Any

from .data_object import DataObject


class TrackableObject(DataObject):
    async def details(self) -> dict[str, Any]:
        return await self._api.request(f"trackable_object/{self._id}")

    async def day_overview(self, date: datetime) -> Any:
        params = {
            "local_day": date.day,
            "local_month": date.month,
            "local_year": date.year,
        }
        return await self._api.request(
            f"pet/{self._id}/activity/day_overview", params=params
        )

    async def week_overview(self, date: datetime) -> Any:
        params = {
            "local_day": date.day,
            "local_month": date.month,
            "local_year": date.year,
        }
        return await self._api.request(
            f"pet/{self._id}/activity/week_overview", params=params
        )

    async def health_overview(self) -> Any:
        return await self._api.request(
            f"pet/{self._id}/health/overview",
            api_url="https://aps-api.tractive.com/api/",
            api_version=1,
        )
