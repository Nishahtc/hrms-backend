from fastapi import APIRouter, Query, HTTPException
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id
from app.config.config import VACANCY_FILE, IMAGE_URL

router = APIRouter()


@router.get("/")
def get_vacancies(id: int | None = Query(None)):
    data = read_data(VACANCY_FILE)
    vacancies = data.get("vancaniesData", [])

    # Add full image URL for each record
    for vacancie in vacancies:
        if "img" in vacancie and not vacancie["img"].startswith("http"):
            vacancie["img"] = f"{IMAGE_URL}/{vacancie['img']}"

    # Search by ID if provided
    if id is not None:
        vacancie = get_data_by_id(vacancies, id)
        if not vacancie:
            raise HTTPException(status_code=404, detail="vacancie not found")
        return vacancie

    return vacancies


   


