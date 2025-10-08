from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import PAYROLL_FILE

router = APIRouter()

@router.get("/")
def get_payrolls():
    data = read_data(PAYROLL_FILE)
    return data

