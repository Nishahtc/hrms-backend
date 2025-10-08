from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import VACANCY_FILE, IMAGE_URL

router = APIRouter()

@router.get("/")
def get_payrolls():
    data = read_data(VACANCY_FILE)
    for vacancies in data:
        if "img" in vacancies:
            vacancies["img"] = f"{IMAGE_URL}/{vacancies['img']}"
    return data
