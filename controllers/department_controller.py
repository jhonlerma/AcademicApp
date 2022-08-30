from db.department_repository import DepartmentRepository
from models.department_model import DepartmentModel


class DepartmentController():

    def __init__(self) -> None:
        self.repo = DepartmentRepository()

    def get(self, args):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data):
        department = DepartmentModel(data)
        return {
            "id": self.repo.save(department)
        }

    def update(self, id, data):
        department = DepartmentModel(data)
        self.repo.update(id, department)

    def delete(self, id):
        self.repo.delete(id)
