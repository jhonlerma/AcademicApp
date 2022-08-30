from db.repository import Repository
from models.enrollment_model import EnrollmentModel
from bson import ObjectId


class EnrollmentRepository(Repository[EnrollmentModel]):
    def __init__(self):
        super().__init__()

    def avg(self, year, semester, subject):
        filter = {
            "$match": {
                "$and": [
                    {"subject.$id": ObjectId(subject)},
                    {"year": int(year)},
                    {"semester": int(semester)}
                ]
            }
        }
        group = {
            "$group": {
                "_id": "$subject.$id",
                "average": {
                    "$avg": "$grade"
                }
            }
        }
        return self.query_aggregation([filter, group])[0]

    def get_students(self, year, semester, subject):
        filter = {
            "$and": [
                {"subject.$id": ObjectId(subject)},
                {"year": int(year)},
                {"semester": int(semester)}
            ]
        }
        data = self.query(filter)
        result = {}
        for d in data:
            if "students" not in result:
                result["students"] = []
                result["_id"] = d["_id"]
                result["semester"] = d["semester"]
                result["year"] = d["year"]
            result["students"].append(d["student"])
        return result
