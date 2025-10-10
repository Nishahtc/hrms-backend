from fastapi import APIRouter, Query, HTTPException
from app.utils.read_data import read_data
from app.utils.common_query import get_data_by_id
from app.config.config import APPLICANT_DATA_FILE, IMAGE_URL  

router = APIRouter()

@router.get("/")
def get_applicants(id: int | None = Query(None)):
    """
    Get all applicants or a single applicant by ID.
    """
    data = read_data(APPLICANT_DATA_FILE)
    applicants = data.get("applicantsData", [])  

    # Add full image URL for each record
    for applicant in applicants:
        if "img" in applicant and not applicant["img"].startswith("http"):
            applicant["img"] = f"{IMAGE_URL}/{applicant['img']}"

    # If ID is provided, return that specific record
    if id is not None:
        applicant_item = get_data_by_id(applicants, id)
        if not applicant_item:
            raise HTTPException(status_code=404, detail="Applicant not found")
        return applicant_item

    return applicants
