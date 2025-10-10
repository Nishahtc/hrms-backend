from fastapi import APIRouter, Query, HTTPException
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id
from app.config.config import EMPLOYEE_LIST_FILE, IMAGE_URL

router = APIRouter()

@router.get("/")
def get_employees_list(id: int | None = Query(None)):
    """
    Get all employees or a single employee by ID from the employee list.
    """
    data = read_data(EMPLOYEE_LIST_FILE)
    employees_list = data.get("employeesList", [])  

    # Add full image URL for each record if needed
    for employee in employees_list:
        if "img" in employee and not employee["img"].startswith("http"):
            employee["img"] = f"{IMAGE_URL}/{employee['img']}"

    # If ID is provided, return that specific record
    if id is not None:
        employee_item = get_data_by_id(employees_list, id)
        if not employee_item:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee_item

    return employees_list
