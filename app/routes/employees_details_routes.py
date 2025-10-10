from fastapi import APIRouter, Query, HTTPException
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id
from app.config.config import EMPLOYEE_DETAILS_FILE, IMAGE_URL

router = APIRouter()

# Route to get all employee details or by ID using query string
@router.get("/")
def get_employees(id: int | None = Query(None)):
    data = read_data(EMPLOYEE_DETAILS_FILE)

    # Add full image URL for each record
    for employeeDetails in data:
        if "img" in employeeDetails and not employeeDetails["img"].startswith("http"):
            employeeDetails["img"] = f"{IMAGE_URL}/{employeeDetails['img']}"

    # Search by ID if provided
    if id is not None:
        employeeDetails = get_data_by_id(data, id)
        if not employeeDetails:
            raise HTTPException(status_code=404, detail="Employee details not found")
        return employeeDetails

    return data

