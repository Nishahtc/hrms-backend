import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PAYROLL_FILE = os.path.join(BASE_DIR, "data", "payroll.json")
EMPLOYEE_FILE = os.path.join(BASE_DIR, "data", "employees.json")
VACANCY_FILE = os.path.join(BASE_DIR, "data", "vacancies.json")
CONDIDATE_FILE = os.path.join(BASE_DIR, "data", "candidate.json")
