import json
from flask import jsonify, request, Blueprint
from controllers.student_controller import StudentController
from decorators.logger_decorator import logger

student_module = Blueprint('students', __name__)
controller = StudentController()


@student_module.get('/')
@logger
def get_students():
    return jsonify(controller.get(request.args))


@student_module.post('/')
@logger
def create_student():
    return jsonify(controller.create(request.get_json())), 201


@student_module.get('/<string:id>')
def show_student(id):
    return jsonify(controller.get_by_id(id))


@student_module.put('/<string:id>')
def update_student(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204


@student_module.delete('/<string:id>')
def delete_student(id):
    controller.delete(id)
    return jsonify({}), 204
