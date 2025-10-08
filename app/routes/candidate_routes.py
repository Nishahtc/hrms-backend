from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import CANDIDATE_FILE , IMAGE_URL

router = APIRouter()

@router.get('/')
def get_candidate():
    data = read_data(CANDIDATE_FILE)  
    for candidate in data:
        if "img" in candidate:
            candidate["img"] = f"{IMAGE_URL}/{candidate['img']}"
    return data
