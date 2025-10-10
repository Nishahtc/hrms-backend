from fastapi import APIRouter, Query, HTTPException
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id
from app.config.config import VACANCY_LIST_FILE, IMAGE_URL

router = APIRouter()

@router.get("/")
def get_vacancies_list(id: int | None = Query(None)):
   
    data = read_data(VACANCY_LIST_FILE)
    vacancies_list = data.get("vacanciesList", []) 

    # Add full image URL for each record if needed
    for vac in vacancies_list:
        if "img" in vac and not vac["img"].startswith("http"):
            vac["img"] = f"{IMAGE_URL}/{vac['img']}"

    # If ID is provided, return that specific record
    if id is not None:
        vac_item = get_data_by_id(vacancies_list, id)
        if not vac_item:
            raise HTTPException(status_code=404, detail="Vacancy list record not found")
        return vac_item

    return vacancies_list
