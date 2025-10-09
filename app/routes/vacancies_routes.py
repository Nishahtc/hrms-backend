from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import VACANCY_FILE, IMAGE_URL

router = APIRouter()

@router.get("/")
def get_vacancies():
    data = read_data(VACANCY_FILE)
    for vacancy in data:
        if "img" in vacancy:
            vacancy["img"] = f"{IMAGE_URL}/{vacancy['img']}"
    return data



