from flask import Blueprint, render_template, current_app, request, url_for, redirect
import requests

bp = Blueprint("advices", __name__, url_prefix="/advices")


@bp.route("/", methods=["GET"])
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 5
    api_url = current_app.config["API_ADVICES_URL"]
    api_url = f"{api_url}?page={page}&per_page={per_page}"
    response = requests.get(api_url)
    names_diseases = get_names_diseases()
    if response.status_code == 200:
        data = response.json()
        advices = data["data"]
        total_pages = data["total_pages"]
        return render_template(
            "advices/advices.html",
            advices=advices,
            page=page,
            total_pages=total_pages,
            names_diseases=names_diseases,
        )
    return "Error al obtener consejos.", 500


@bp.route("/add_advice", methods=["POST", "GET"])
def add_advice():
    api_url = current_app.config["API_ADVICES_URL"]
    disease_name = request.form["disease_name"]
    description = request.form["description"]
    advice_data = {"disease_name": disease_name, "description": description}
    requests.post(api_url, json=advice_data)
    return redirect(url_for("main.advices.index"))


@bp.route("/update_advice/<int:id>", methods=["POST"])
def update_advice(id):
    api_url = current_app.config["API_ADVICES_URL"]
    disease_name = request.form["disease_name"]
    description = request.form["description"]
    advice_data = {"disease_name": disease_name, "description": description}
    requests.put(f"{api_url}{id}", json=advice_data)
    return redirect(url_for("main.advices.index"))


@bp.route("/delete_advice/<int:id>", methods=["POST"])
def delete_advice(id):
    api_url = current_app.config["API_ADVICES_URL"]
    requests.delete(f"{api_url}{id}")
    return redirect(url_for("main.advices.index"))


def get_names_diseases():
    api_url = current_app.config["API_DISEASES_NAMES_URL"]
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        names_diseases = data["data"]
        return names_diseases
    return "Error al obtener los nombres de las enfermedades.", 500
