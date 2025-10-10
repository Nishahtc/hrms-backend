from fastapi import APIRouter, Query, HTTPException
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id
from app.config.config import CANDIDATE_FILE, IMAGE_URL

router = APIRouter()

@router.get("/")
def get_candidates(id: int | None = Query(None)):
    """
    Get all candidates or a single candidate by ID.
    """
    data = read_data(CANDIDATE_FILE)
    candidates = data.get("candidateData", [])  

    # Add full image URL for each record if needed
    for candidate in candidates:
        if "img" in candidate and not candidate["img"].startswith("http"):
            candidate["img"] = f"{IMAGE_URL}/{candidate['img']}"

    # If ID is provided, return that specific record
    if id is not None:
        candidate_item = get_data_by_id(candidates, id)
        if not candidate_item:
            raise HTTPException(status_code=404, detail="Candidate not found")
        return candidate_item

    return candidates


