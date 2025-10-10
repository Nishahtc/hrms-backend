from fastapi import APIRouter, Query, HTTPException
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id
from app.config.config import VACANCY_DETAILS_FILE, IMAGE_URL

router = APIRouter()

@router.get("/")
def get_vacancy_details(id: int | None = Query(None)):
   
    data = read_data(VACANCY_DETAILS_FILE)
    vacancies_details = data.get("vacanciesDetails", [])  # Make sure this key matches your JSON

    # Add full image URL for each record if needed
    for vac_detail in vacancies_details:
        if "img" in vac_detail and not vac_detail["img"].startswith("http"):
            vac_detail["img"] = f"{IMAGE_URL}/{vac_detail['img']}"

    # If ID is provided, return that specific record
    if id is not None:
        vac_detail = get_data_by_id(vacancies_details, id)
        if not vac_detail:
            raise HTTPException(status_code=404, detail="Vacancy detail not found")
        return vac_detail

    return vacancies_details
