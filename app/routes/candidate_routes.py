from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import CONDIDATE_FILE

router = APIRouter()

@router.get('/')
def get_condidate():
    data = read_data(CONDIDATE_FILE)
    return data