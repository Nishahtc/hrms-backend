from fastapi import APIRouter, Query
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id  
from app.config.config import VACANCY_FILE, IMAGE_URL

router = APIRouter()

# Route to get all vacancies or by ID using query string
@router.get("/")
def get_vacancies(id: int | None = Query(None)):
    data = read_data(VACANCY_FILE)
    vacancies = data.get("vancaniesData", []) 

    #  add full image URL for each record
    for vac in vacancies:
        if "img" in vac and not vac["img"].startswith("http"):
            vac["img"] = f"{IMAGE_URL}/{vac['img']}"

    #  use reusable common query function
    result = get_data_by_id(vacancies, id)
    return result


