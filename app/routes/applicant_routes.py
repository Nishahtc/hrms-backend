from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import APPLICANT_FILE

router = APIRouter()

@router.get('/')
def get_candidate():
    data = read_data(APPLICANT_FILE)  
    return data