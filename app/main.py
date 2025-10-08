from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#  all routers
from app.routes.payroll_routes import router as payroll_router
from app.routes.employees_routes import router as employee_router
from app.routes.vacancies_routes import router as vacancies_router
from app.routes.leaves_routes import router as leaves_router
from app.routes.applicant_routes import router as applicant_router
from app.routes.candidate_routes import router as candidate_router
from app.routes.employees_details_routes import router as employees_details_router
from fastapi.staticfiles import StaticFiles
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory="app/images"), name="images")
app.include_router(payroll_router, prefix="/payrolls", tags=["Payrolls"])
app.include_router(employee_router, prefix="/employees", tags=["Employees"])
app.include_router(vacancies_router, prefix="/vacancies", tags=["Vacancies"])
app.include_router(leaves_router, prefix="/leaves", tags=["Leaves"])
app.include_router(applicant_router, prefix="/applicants", tags=["Applicants"])
app.include_router(candidate_router, prefix="/candidates", tags=["Candidates"])
app.include_router(employees_details_router, prefix="/employeesDetails", tags=["Employee Details"])


@app.get("/")
def home():
    return {"message": "HRMS Backend Running Successfully!"}




