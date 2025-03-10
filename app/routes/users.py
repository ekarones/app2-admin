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

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/", methods=["GET"])
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 5  # Puedes cambiar esto según lo que necesites
    api_url = current_app.config["API_USERS_URL"]
    api_url = f"{api_url}?page={page}&per_page={per_page}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        users = data["data"]
        total_pages = data["total_pages"]
        return render_template(
            "users/users.html", users=users, page=page, total_pages=total_pages
        )
    return "Error al obtener usuarios.", 500


@bp.route("/add_user", methods=["POST", "GET"])
def add_user():
    api_url = current_app.config["API_USERS_URL"]
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    user_data = {"username": username, "email": email, "password": password}
    response = requests.post(api_url, json=user_data)
    if response.status_code != 200:
        flash("Ya existe una cuenta con ese correo, intente otra vez", "error")
    return redirect(url_for("main.users.index"))


@bp.route("/update_user/<int:id>", methods=["POST"])
def update_user(id):
    api_url = current_app.config["API_USERS_URL"]
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    user_data = {"username": username, "email": email, "password": password}
    response = requests.put(f"{api_url}/{id}", json=user_data)
    if response.status_code != 200:
        flash("Ya existe una cuenta con ese correo, intente otra vez", "error")
    return redirect(url_for("main.users.index"))


@bp.route("/delete_user/<int:id>", methods=["POST"])
def delete_user(id):
    api_url = current_app.config["API_USERS_URL"]
    requests.delete(f"{api_url}/{id}")
    return redirect(url_for("main.users.index"))
