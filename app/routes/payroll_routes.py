from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import PAYROLL_FILE, IMAGE_URL

router = APIRouter()

#  Route to get all payrolls
@router.get("/")
def get_payrolls():
    data = read_data(PAYROLL_FILE)
    payrolls = data.get("payrolls", [])  # Extract list from key

    for payroll in payrolls:
        if "img" in payroll:
            payroll["img"] = f"{IMAGE_URL}/{payroll['img']}"
    return payrolls


# Route to get payroll by ID
@router.get("/{payroll_id}")
def get_payroll_by_id(payroll_id: int):
    data = read_data(PAYROLL_FILE)
    payrolls = data.get("payrolls", [])

    for payroll in payrolls:
        if payroll["id"] == payroll_id:
            if "img" in payroll:
                payroll["img"] = f"{IMAGE_URL}/{payroll['img']}"
            return payroll

    return {"error": f"Payroll with id {payroll_id} not found"}

