from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import VACANCY_FILE, IMAGE_URL

router = APIRouter()

# Get all vacancies
@router.get("/")
def get_vacancies():
    vacancies = read_data(VACANCY_FILE)  

    for vac in vacancies:
        if "img" in vac:
            vac["img"] = f"{IMAGE_URL}/{vac['img']}"
    return vacancies

# Get vacancy by ID
@router.get("/{vacancy_id}")
def get_vacancy_by_id(vacancy_id: int):
    vacancies = read_data(VACANCY_FILE)

    for vac in vacancies:
        if vac.get("id") == vacancy_id:
            if "img" in vac:
                vac["img"] = f"{IMAGE_URL}/{vac['img']}"
            return vac

    return {"error": f"Vacancy with id {vacancy_id} not found"}




