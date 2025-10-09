from fastapi import APIRouter, Query
from app.utils.read_data import read_data
from app.config.config import CANDIDATE_FILE , IMAGE_URL
from app.utils.common_query import get_data_by_id
router = APIRouter()

@router.get('/')
def get_candidate(id: int | None = Query(None)):
    data = read_data(CANDIDATE_FILE)  
    candidate = data.get("candidateData", [])
    for candidate in data:
        if "img" in candidate and not candidate["img"].startswith("http"):
            candidate["img"] = f"{IMAGE_URL}/{candidate['img']}"

    # common query function
    result = get_data_by_id(candidate, id)
    return result