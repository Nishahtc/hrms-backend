from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import EMPLOYEE_DETAILS_FILE, IMAGE_URL

router = APIRouter()

@router.get("/")
def get_employees():
    data = read_data(EMPLOYEE_DETAILS_FILE)
    for employeesDetails in data:

        if "img" in employeesDetails:
            employeesDetails["img"] = f"{IMAGE_URL}/{employeesDetails['img']}"
    return data
