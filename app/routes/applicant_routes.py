from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import APPLICANT_FILE, IMAGE_URL

router = APIRouter()

@router.get('/')
def get_candidate():
    data = read_data(APPLICANT_FILE)  
    for applicant in data:
        if "img" in applicant:
            applicant["img"] = f"{IMAGE_URL}/{applicant['img']}"
    return data