from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import PAYROLL_FILE, IMAGE_URL

router = APIRouter()

@router.get("/")
def get_payrolls():
    data =  read_data(PAYROLL_FILE)
    for payroll in data:
        if "img" in payroll:
            payroll["img"] = f"{IMAGE_URL}/{payroll['img']}"
    return data

