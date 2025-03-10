from flask import Blueprint, render_template, current_app, request, url_for, redirect
import requests

bp = Blueprint("diseases", __name__, url_prefix="/diseases")


@bp.route("/", methods=["GET"])
def index():
    api_url_images = current_app.config["API_GET_IMAGE_ASSETS_URL"]
    page = request.args.get("page", 1, type=int)
    per_page = 5
    api_url = current_app.config["API_DISEASES_URL"]
    api_url = f"{api_url}?page={page}&per_page={per_page}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        diseases = data["data"]
        total_pages = data["total_pages"]
        return render_template(
            "diseases/diseases.html",
            diseases=diseases,
            page=page,
            total_pages=total_pages,
            api_url_images = api_url_images
        )
    return "Error al obtener enfermedades.", 500


@bp.route("/add_disease", methods=["POST", "GET"])
def add_disease():
    api_url = current_app.config["API_DISEASES_URL"]
    name = request.form["name"]
    description = request.form["description"]
    image = request.files["image"]
    files = {"image": (image.filename, image.stream, image.mimetype)}
    data = {"name": name, "description": description}
    response = requests.post(api_url, data=data, files=files)
    if response.status_code == 200:
        return redirect(url_for("main.diseases.index"))
    else:
        return "Error al enviar la enfermedad", 500


@bp.route("/update_disease/<int:id>", methods=["POST", "GET"])
def update_disease(id):
    api_url = f"{current_app.config['API_DISEASES_URL']}/{id}"
    name = request.form["name"]
    description = request.form["description"]
    image = request.files.get("image")  # La imagen puede ser opcional
    files = None
    if image and image.filename:  # Solo incluir archivo si se ha subido uno
        files = {"image": (image.filename, image.stream, image.mimetype)}
    data = {"name": name, "description": description}
    response = requests.put(api_url, data=data, files=files)
    if response.status_code == 200:
        return redirect(url_for("main.diseases.index"))
    else:
        return "Error al actualizar la enfermedad", 500


@bp.route("/delete_disease/<int:id>", methods=["POST"])
def delete_disease(id):
    api_url = current_app.config["API_DISEASES_URL"]
    requests.delete(f"{api_url}/{id}")
    return redirect(url_for("main.diseases.index"))