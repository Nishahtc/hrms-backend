from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Routers
from app.routes.payroll_routes import router as payroll_router
from app.routes.leaves_routes import router as leaves_router
from app.routes.vacancies_routes import router as vacancies_router
from app.routes.vacancies_list_routes import router as vacancies_list_router
from app.routes.vacancies_details_routes import router as vacancies_details_router
from app.routes.candidate_routes import router as candidate_router
from app.routes.applicant_routes import router as applicants_card_router
from app.routes.applicant_data_routes import router as applicants_data_router
from app.routes.applicant_detail_routes import router as applicants_details_router
from app.routes.employees_routes import router as employee_router
from app.routes.employees_list_routes import router as employee_list_router
from app.routes.employees_details_routes import router as employees_details_router
from app.routes.calendar_schedules import router as schedules_router

# FastAPI app instance
app = FastAPI()

# CORS Middleware
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

# Static Files
app.mount("/images", StaticFiles(directory="app/images"), name="images")

# Include Routers 
app.include_router(payroll_router, prefix="/payrolls")                    
app.include_router(leaves_router, prefix="/leaves")                       
app.include_router(vacancies_router, prefix="/vacancies")                
app.include_router(vacancies_list_router, prefix="/vacanciesList")     
app.include_router(vacancies_details_router, prefix="/vacanciesDetails") 
app.include_router(candidate_router, prefix="/candidates")              
app.include_router(applicants_card_router, prefix="/applicantsCard") 
app.include_router(applicants_data_router, prefix="/applicantsData") 
app.include_router(applicants_details_router, prefix="/applicantsDetails") 
app.include_router(employee_router, prefix="/employees")                 
app.include_router(employee_list_router, prefix="/employeesList")   
app.include_router(employees_details_router, prefix="/employeesDetails") 
app.include_router(schedules_router, prefix="/calendarSchedules")
# Home route
@app.get("/")
def home():
    return {"message": "HRMS Backend Running Successfully!"}






