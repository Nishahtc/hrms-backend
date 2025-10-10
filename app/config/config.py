import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

#  base url
BASE_URL = "https://hrms-backend-5vc1.onrender.com"
IMAGE_URL = f"{BASE_URL}/images/avatar"
PAYROLL_FILE = os.path.join(DATA_DIR, "payrolls", "payroll.json") 

LEAVES_FILE = os.path.join(DATA_DIR,"leaves" ,"leaves.json")

VACANCY_FILE = os.path.join(DATA_DIR, "vacancies", "vacancies.json")
VACANCY_LIST_FILE = os.path.join(DATA_DIR, "vacancies", "vacanciesList.json")
VACANCY_DETAILS_FILE = os.path.join(DATA_DIR, "vacancies", "vacanciesDetails.json")
CANDIDATE_FILE = os.path.join(DATA_DIR,  "vacancies", "candidate.json")

APPLICANT_CARD_FILE = os.path.join(DATA_DIR, "applicants", "applicantsCard.json")
APPLICANT_DATA_FILE = os.path.join(DATA_DIR, "applicants", "applicantsData.json")
APPLICANT_DETAILS_FILE = os.path.join(DATA_DIR, "applicants", "applicantsDetails.json")

EMPLOYEE_FILE = os.path.join(DATA_DIR, "employees", "employees.json")
EMPLOYEE_LIST_FILE = os.path.join(DATA_DIR,"employees", "employeesList.json")
EMPLOYEE_DETAILS_FILE = os.path.join(DATA_DIR, "employees", "employessDetail.json")


