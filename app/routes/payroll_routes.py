from fastapi import APIRouter, Query
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id  
from app.config.config import PAYROLL_FILE, IMAGE_URL

router = APIRouter()

# Route to get all payrolls or by ID using query string
@router.get("/")
def get_payrolls(id: int | None = Query(None)):
    data = read_data(PAYROLL_FILE)
    payrolls = data.get("payrolls", [])

    # add image URL for each record
    for payroll in payrolls:
        if "img" in payroll and not payroll["img"].startswith("http"):
            payroll["img"] = f"{IMAGE_URL}/{payroll['img']}"

    # common query function
    result = get_data_by_id(payrolls, id)
    return result





