from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv, dotenv_values
from routes.students_route import student_module
from routes.subject_routes import subject_module
from routes.department_routes import department_module
from routes.enrollment_routes import enrollment_module
# se cargan las configuraciones por defecto del archivo .env en la raiz del proyecto
# load_dotenv() 

# se puede personalizar la ruta y el archivo .env para cargarlo desde otra localizacion o archivo
config = dotenv_values(".env")
app = Flask(__name__)
cors = CORS(app)

# importar rutas de students
app.register_blueprint(student_module, url_prefix='/estudiantes')
app.register_blueprint(subject_module, url_prefix="/materias")
app.register_blueprint(department_module, url_prefix="/facultades")
app.register_blueprint(enrollment_module, url_prefix="/inscripciones")


@app.route('/')
def hello_world():
    diccionario = {'mensaje':'Hola mundo!'}
    return jsonify(diccionario)

if __name__ == '__main__':
    app.run(host="localhost", port=config["PORT"], debug=True)
