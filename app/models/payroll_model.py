
from pydantic import BaseModel
from datetime import date
from typing import Optional

class Payroll(BaseModel):
    id: int
    img: Optional[str] = None
    name: str
    email: str
    position: str
    positionColor: Optional[str] = None
    rateType: str
    rateAmount: str
    period: str
    periodStart: date
    periodEnd: date
    workingHours: str
    salary: str
    status: str
    statusColor: Optional[str] = None
