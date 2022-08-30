import json
from flask import jsonify, request, Blueprint
from controllers.subject_controller import SubjectController

subject_module = Blueprint('subjects', __name__)
controller = SubjectController()


@subject_module.get('/')
def get_subjects():
    return jsonify(controller.get(request.args))


@subject_module.post('/facultades/<string:department_id>')
def create_subject(department_id):
    return jsonify(controller.create(request.get_json(), department_id)), 201


@subject_module.get('/<string:id>')
def show_subject(id):
    return jsonify(controller.get_by_id(id))


@subject_module.put('/<string:id>')
def update_subject(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204


@subject_module.delete('/<string:id>')
def delete_subject(id):
    controller.delete(id)
    return jsonify({}), 204
