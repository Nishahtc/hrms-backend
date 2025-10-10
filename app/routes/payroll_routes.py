
from fastapi import APIRouter, Query, HTTPException
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id
from app.config.config import PAYROLL_FILE, IMAGE_URL

router = APIRouter()

@router.get("/")
def get_payrolls(id: int | None = Query(None)):
    # Read payroll JSON
    data = read_data(PAYROLL_FILE)
    
    # Payrolls list inside JSON
    payrolls = data.get("payrolls", [])

    # Add full image URL
    for payroll in payrolls:
        if "img" in payroll and not payroll["img"].startswith("http"):
            payroll["img"] = f"{IMAGE_URL}/{payroll['img']}"

    # If ID is provided, return that record
    if id is not None:
        payroll_item = get_data_by_id(payrolls, id)
        if not payroll_item:
            raise HTTPException(status_code=404, detail="Payroll not found")
        return payroll_item

    # Otherwise return full list
    return payrolls

   








  





