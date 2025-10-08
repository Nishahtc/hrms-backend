from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.payroll_routes import router as payroll_router
from app.routes.employees_routes import router as employee_router
from app.routes.vacancies_routes import router as vacancies_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(payroll_router, prefix="/payrolls")
app.include_router(employee_router, prefix="/employees")
app.include_router(vacancies_router, prefix="/vacancies")

# @app.get("/")
# def home():
#     return {"msg": "Backend Running"}

