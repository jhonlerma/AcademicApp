from db.repository import Repository
from models.student_model import StudentModel

class StudentRepository( Repository[StudentModel] ):
  def __init__(self):
    super().__init__()