import json
from flask import jsonify, request, Blueprint
from controllers.department_controller import DepartmentController

department_module = Blueprint('departments', __name__)
controller = DepartmentController()


@department_module.get('/')
def get_department():
    return jsonify(controller.get(request.args))


@department_module.post('/')
def create_department():
    return jsonify(controller.create(request.get_json())), 201


@department_module.get('/<string:id>')
def show_department(id):
    return jsonify(controller.get_by_id(id))


@department_module.put('/<string:id>')
def update_department(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204


@department_module.delete('/<string:id>')
def delete_department(id):
    controller.delete(id)
    return jsonify({}), 204
