from db.subject_repository import SubjectRepository
from db.department_repository import DepartmentRepository
from models.department_model import DepartmentModel
from models.subject_model import SubjectModel


class SubjectController():

    def __init__(self) -> None:
        self.repo = SubjectRepository()
        self.repo_department = DepartmentRepository()

    def get(self, args):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data, department_id):
        subject = SubjectModel(data)
        department = self.repo_department.get_by_id(department_id)
        subject.department = DepartmentModel(department)
        return {
            "id": self.repo.save(subject)
        }

    def update(self, id, data):
        subject = SubjectModel(data)
        self.repo.update(id, subject)

    def delete(self, id):
        self.repo.delete(id)
