from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    current_app,
    flash,
)
import requests

bp = Blueprint("login", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        api_url = current_app.config["API_ADMIN_LOGIN_URL"]
        if email and password:
            response = requests.post(
                api_url, json={"email": email, "password": password}
            )
            if response.status_code == 200:
                data = response.json()
                if data.get("message") == "Login successful":
                    return redirect(url_for("main.dashboard.index"))
                else:
                    flash("Credenciales incorrectas", "error")
            else:
                flash("Credenciales incorrectas", "error")
    return render_template("login/index.html")
