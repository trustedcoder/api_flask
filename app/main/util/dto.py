from flask_restx import Namespace, fields


class ZuriDto:
    api = Namespace("zuri", description="Zuri related operations")