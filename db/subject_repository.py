from db.repository import Repository
from models.subject_model import SubjectModel


class SubjectRepository(Repository[SubjectModel]):
    def __init__(self):
        super().__init__()
