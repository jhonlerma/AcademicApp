from functools import wraps
from flask import request, jsonify

def logger(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    print(f"Path: {request.full_path}")
    method = request.method
    print(f"Method {method}")
    print(f"Query params: {request.args.to_dict()}")
    if method.lower() == "post":
      print(f"Body: {request.get_json()}")
    result = f(*args, **kwargs)
    print(f"Result: {result.get_json()}")
    return result
  return decorated