from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import VACANCY_FILE

router = APIRouter()

@router.get("/")
def get_payrolls():
    data = read_data(VACANCY_FILE)
    return data
