from db.enrollment_repository import EnrollmentRepository
from db.student_repository import StudentRepository
from db.subject_repository import SubjectRepository

from models.enrollment_model import EnrollmentModel
from models.student_model import StudentModel
from models.subject_model import SubjectModel


class EnrollmentController():

    def __init__(self) -> None:
        self.repo = EnrollmentRepository()
        self.repo_subject = SubjectRepository()
        self.repo_student = StudentRepository()

    def get(self, args):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data, subject_id, student_id):
        enrollment = EnrollmentModel(data)
        student = self.repo_student.get_by_id(student_id)
        enrollment.student = StudentModel(student)

        subject = self.repo_subject.get_by_id(subject_id)
        enrollment.subject = SubjectModel(subject)

        return {
            "id": self.repo.save(enrollment)
        }

    def update(self, id, data):
        subject = EnrollmentModel(data)
        self.repo.update(id, subject)

    def delete(self, id):
        self.repo.delete(id)

    def get_students(self, args):
        return self.repo.get_students(args['year'], args['semester'], args['subject_id'])

    def avg(self, args):
        return self.repo.avg(args['year'], args['semester'], args['subject_id'])
