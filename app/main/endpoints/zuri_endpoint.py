import logging
from flask_restx import Resource
from app.main.business.zuri_business import AppBusiness
from app.main.util.dto import ZuriDto

zuri_namespace = ZuriDto.api

audit_logger = logging.getLogger(__name__)


@zuri_namespace.route("/zuri")
class Zuri(Resource):
    @zuri_namespace.response(200, "ok")
    @zuri_namespace.doc("Get zuri profile")
    def get(self):
        return AppBusiness.get_zuri_profile()
