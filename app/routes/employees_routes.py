from fastapi import APIRouter, Query, HTTPException
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id
from app.config.config import EMPLOYEE_FILE, IMAGE_URL

router = APIRouter()

# Route to get all employees or by ID using query string
@router.get("/")
def get_employees(id: int | None = Query(None)):
    data = read_data(EMPLOYEE_FILE)
    employees = data.get("employees", [])

    # Add full image URL for each record
    for employee in employees:
        if "img" in employee and not employee["img"].startswith("http"):
            employee["img"] = f"{IMAGE_URL}/{employee['img']}"

    # Search by ID if provided
    if id is not None:
        employee = get_data_by_id(employees, id)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee

    return employees

