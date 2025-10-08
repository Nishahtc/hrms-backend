from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import LEAVES_FILE
router = APIRouter()

@router.get("/")
def get_leaves():
    data = read_data(LEAVES_FILE)
    return data