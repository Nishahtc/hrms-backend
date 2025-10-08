from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import EMPLOYEE_FILE, IMAGE_URL

router = APIRouter()

@router.get("/")
def get_employees():
    data = read_data(EMPLOYEE_FILE)
    for employee in data:
        if "img" in employee:
            employee["img"] = f"{IMAGE_URL}/{employee['img']}"
    return data
