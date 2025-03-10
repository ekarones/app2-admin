from flask import (
    Blueprint,
    render_template,
    current_app,
    request,
    url_for,
    redirect,
    flash,
)
import requests

bp = Blueprint("admins", __name__, url_prefix="/admins")


@bp.route("/", methods=["GET"])
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 5
    api_url = current_app.config["API_ADMINS_URL"]
    api_url = f"{api_url}?page={page}&per_page={per_page}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        admins = data["data"]
        total_pages = data["total_pages"]
        return render_template(
            "admins/admins.html", admins=admins, page=page, total_pages=total_pages
        )
    return "Error al obtener administradores.", 500


@bp.route("/add_admin", methods=["POST", "GET"])
def add_admin():
    api_url = current_app.config["API_ADMINS_URL"]
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    admin_data = {"username": username, "email": email, "password": password}
    response = requests.post(api_url, json=admin_data)
    if response.status_code != 200:
        flash("Ya existe una cuenta con ese correo, intente otra vez", "error")
    return redirect(url_for("main.admins.index"))


@bp.route("/update_admin/<int:id>", methods=["POST"])
def update_admin(id):
    api_url = current_app.config["API_ADMINS_URL"]
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    admin_data = {"username": username, "email": email, "password": password}
    response = requests.put(f"{api_url}/{id}", json=admin_data)
    if response.status_code != 200:
        flash("Ya existe una cuenta con ese correo, intente otra vez", "error")
    return redirect(url_for("main.admins.index"))


@bp.route("/delete_admin/<int:id>", methods=["POST"])
def delete_admin(id):
    api_url = current_app.config["API_ADMINS_URL"]
    requests.delete(f"{api_url}/{id}")
    return redirect(url_for("main.admins.index"))
