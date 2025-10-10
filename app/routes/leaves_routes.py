from fastapi import APIRouter, Query, HTTPException
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id
from app.config.config import LEAVES_FILE, IMAGE_URL

router = APIRouter()

# Route to get all leaves or by ID using query string
@router.get("/")
def get_leaves(id: int | None = Query(None)):
    data = read_data(LEAVES_FILE)
    leaves = data.get("leaves", [])  

    # Add full image URL for each record
    for leave in leaves:
        if "img" in leave and not leave["img"].startswith("http"):
            leave["img"] = f"{IMAGE_URL}/{leave['img']}"

    # Search by ID if provided
    if id is not None:
        leave = get_data_by_id(leaves, id)
        if not leave:
            raise HTTPException(status_code=404, detail="Leave not found")
        return leave

    return leaves

