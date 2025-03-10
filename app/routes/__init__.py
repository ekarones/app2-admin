from flask import Blueprint
from . import login
from . import dashboard
from . import advices
from . import diseases
from . import users
from . import records
from . import notifications
from . import admins

main_bp = Blueprint("main", __name__)
main_bp.register_blueprint(login.bp)
main_bp.register_blueprint(dashboard.bp)
main_bp.register_blueprint(advices.bp)
main_bp.register_blueprint(diseases.bp)
main_bp.register_blueprint(users.bp)
main_bp.register_blueprint(records.bp)
main_bp.register_blueprint(notifications.bp)
main_bp.register_blueprint(admins.bp)