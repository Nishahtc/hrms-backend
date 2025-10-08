import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

PAYROLL_FILE = os.path.join(DATA_DIR, "payroll.json")
EMPLOYEE_FILE = os.path.join(DATA_DIR, "employees.json")
VACANCY_FILE = os.path.join(DATA_DIR, "vacancies.json")
CANDIDATE_FILE = os.path.join(DATA_DIR, "candidate.json")
APPLICANT_FILE = os.path.join(DATA_DIR, "applicants.json")
EMPLOYEE_DETAILS_FILE = os.path.join(DATA_DIR, "employessDetail.json")
LEAVES_FILE = os.path.join(DATA_DIR, "leaves.json")
