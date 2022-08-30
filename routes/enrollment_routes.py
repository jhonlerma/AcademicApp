from flask import jsonify, request, Blueprint
from controllers.enrollment_controller import EnrollmentController

enrollment_module = Blueprint('enrollments', __name__)
controller = EnrollmentController()


@enrollment_module.get('/')
def get_enrollment():
    return jsonify(controller.get(request.args))


@enrollment_module.post('/materias/<string:subject_id>/estudiantes/<string:student_id>')
def create_enrollment(subject_id, student_id):
    return jsonify(controller.create(request.get_json(), subject_id, student_id)), 201


@enrollment_module.get('/<string:id>')
def show_enrollment(id):
    return jsonify(controller.get_by_id(id))


@enrollment_module.put('/<string:id>')
def update_enrollment(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204


@enrollment_module.delete('/<string:id>')
def delete_enrollment(id):
    controller.delete(id)
    return jsonify({}), 204


@enrollment_module.get('/estudiantes')
def get_students():
    return jsonify(controller.get_students(request.args.to_dict()))


@enrollment_module.get('/avg')
def get_avg():
    return jsonify(controller.avg(request.args.to_dict()))
