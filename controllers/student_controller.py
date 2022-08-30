from models.student_model import StudentModel
from db.student_repository import StudentRepository


class StudentController():

    def __init__(self) -> None:
        self.repo = StudentRepository()

    def get(self, args):
        params = args.to_dict()
        filter = {}

        if 'university' in params:
            if not '$and' in filter:
                filter['$and'] = []
            filter['$and'].append({
                'university': {
                    '$regex': f"^{params['university']}",
                    '$options': 'i'
                }
            })

        if 'age' in params:
            if not '$and' in filter:
                filter['$and'] = []
            filter['$and'].append({
                'age': {
                    '$gte': int(params['age'])
                }
            })
        if len(filter.keys()) == 0:
            return self.repo.get_all()
        return self.repo.query(filter)

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data):
        student = StudentModel(data)
        # Validate some fields
        return {
            "id": self.repo.save(student)
        }

    def update(self, id, data):
        student = StudentModel(data)
        self.repo.update(id, student)

    def delete(self, id):
        self.repo.delete(id)
