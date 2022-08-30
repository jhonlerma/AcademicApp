from db.repository import Repository
from models.department_model import DepartmentModel


class DepartmentRepository(Repository[DepartmentModel]):
    def __init__(self):
        super().__init__()
