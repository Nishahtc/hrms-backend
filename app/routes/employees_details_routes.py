from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import EMPLOYEE_DETAILS_FILE

router = APIRouter()

@router.get("/")
def get_employees():
    data = read_data(EMPLOYEE_DETAILS_FILE)
    return data
