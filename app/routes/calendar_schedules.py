from fastapi import APIRouter, Query, HTTPException
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id
from app.config.config import CALENDAR_FILE

router = APIRouter()

@router.get("/")
def get_schedules(id: int | None = Query(None)):
    data = read_data(CALENDAR_FILE)
    schedules = data.get("schedules", [])

    # If ID is provided, return that specific schedule
    if id is not None:
        schedule_item = get_data_by_id(schedules, id)
        if not schedule_item:
            raise HTTPException(status_code=404, detail="Schedule not found")
        return schedule_item

    #  return all schedules
    return schedules

