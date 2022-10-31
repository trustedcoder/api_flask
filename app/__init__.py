from flask import Blueprint
from flask_restx import Api
import os
from .main.endpoints.zuri_endpoint import zuri_namespace


# version 1
core_blueprint = Blueprint("api", __name__, url_prefix="/api/v1")


authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}}


api = Api(
    core_blueprint,
    title="Zuri Api",
    version="1.0",
    authorizations=authorizations,
    doc="/doc/",
    description=(
        "Zuri task 1"
    ),
)
api.add_namespace(zuri_namespace)