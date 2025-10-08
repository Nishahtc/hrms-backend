from fastapi import APIRouter
from app.utils.read_data import read_data
from app.config.config import LEAVES_FILE, IMAGE_URL

router = APIRouter()

@router.get("/")
def get_leaves():
    data = read_data(LEAVES_FILE)
    for leave in data:
        if "img" in leave:
            leave["img"] = f"{IMAGE_URL}/{leave['img']}"
    return data
