import os

import httpx
from dotenv import load_dotenv

from services.external_recipe.base import ExternalRecipeProvider


load_dotenv()


class TheMealDBProvider(ExternalRecipeProvider):

    def __init__(self):

        self.base_url = os.getenv(
            "THEMEALDB_BASE_URL",
            "https://www.themealdb.com/api/json/v1/1"
        )

        self.api_key = os.getenv(
            "THEMEALDB_API_KEY",
            "1"
        )

    async def _get(
        self,
        endpoint: str,
        params: dict | None = None
    ):

        url = (
            f"{self.base_url}/"
            f"{self.api_key}/"
            f"{endpoint}"
        )

        async with httpx.AsyncClient(
            timeout=10
        ) as client:

            response = await client.get(
                url,
                params=params
            )

            response.raise_for_status()

            return response.json()

    def _transform_meal(self,meal: dict) -> dict:
        ingredients = []

        for index in range(1, 21):

            ingredient = meal.get(
                f"strIngredient{index}"
            )

            measure = meal.get(
                f"strMeasure{index}"
            )

            if ingredient and ingredient.strip():

                ingredients.append(
                    {
                        "name": ingredient.strip(),
                        "quantity": measure.strip()
                        if measure
                        else None,
                        "unit": None
                    }
                )

        return {
            "external_id": meal.get("idMeal"),
            "source": "themealdb",
            "name": meal.get("strMeal"),
            "description": None,
            "instructions": meal.get(
                "strInstructions"
            ),
            "image_url": meal.get(
                "strMealThumb"
            ),
            "prep_time": None,
            "cook_time": None,
            "servings": None,
            "cuisine": meal.get(
                "strArea"
            ),
            "video_url": meal.get(
                "strYoutube"
            ),
            "category": meal.get(
                "strCategory"
            ),
            "ingredients": ingredients
        }

    async def search(
        self,
        query: str
    ):

        data = await self._get("search.php",{"s": query})

        meals = data.get("meals") or []

        return [
            self._transform_meal(meal)
            for meal in meals
        ]

    async def get_by_id(
        self,
        recipe_id: str
    ):

        data = await self._get(
            "lookup.php",
            {"i": recipe_id}
        )

        meals = data.get("meals") or []

        if not meals:
            return None

        return self._transform_meal(
            meals[0]
        )

    async def random(self):

        data = await self._get(
            "random.php"
        )

        meals = data.get("meals") or []

        if not meals:
            return None

        return self._transform_meal(
            meals[0]
        )

    async def search_by_ingredient(
        self,
        ingredient: str
    ):

        data = await self._get(
            "filter.php",
            {"i": ingredient}
        )

        meals = data.get("meals") or []

        return [
            {
                "external_id": meal.get(
                    "idMeal"
                ),
                "name": meal.get(
                    "strMeal"
                ),
                "image_url": meal.get(
                    "strMealThumb"
                ),
                "source": "themealdb"
            }
            for meal in meals
        ]

    async def categories(self):

        data = await self._get(
            "categories.php"
        )

        return data.get(
            "categories",
            []
        )