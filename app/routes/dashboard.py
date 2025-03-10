from flask import Blueprint, render_template, current_app, request, url_for, redirect
import requests

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route("/", methods=["GET"])
def index():
    api_url = current_app.config["API_GET_TOP_USERS"]
    response = requests.get(api_url)
    api_url = current_app.config["API_GET_TOP_DISEASES"]
    response_2 = requests.get(api_url)
    api_url = current_app.config["API_GET_ADVICES_COUNT"]
    response_3 = requests.get(api_url)
    api_url = current_app.config["API_GET_GLOBAL_COUNT"]
    response_4 = requests.get(api_url)
    if (
        response.status_code == 200
        and response_2.status_code == 200
        and response_3.status_code == 200
        and response_4.status_code == 200
    ):
        data = response.json()
        top_users = data["data"]
        data = response_2.json()
        top_diseases = data["data"]
        data = response_3.json()
        advices_count = data["data"]
        data = response_4.json()
        global_count = data["data"]
        return render_template(
            "dashboard/dashboard.html",
            top_users=top_users,
            top_diseases=top_diseases,
            advices_count=advices_count,
            global_count=global_count,
        )
    return "Error al obtener los nombres de las enfermedades.", 500
