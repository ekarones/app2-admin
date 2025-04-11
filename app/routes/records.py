from flask import Blueprint, render_template, request, current_app, redirect, url_for
import requests

bp = Blueprint("records", __name__, url_prefix="/records")


@bp.route("/", methods=["GET"])
def index():
    api_url_images = current_app.config["API_GET_IMAGE_URL"]
    page = request.args.get("page", 1, type=int)
    per_page = 5
    api_url = current_app.config["API_RECORDS_URL"]
    api_url = f"{api_url}?page={page}&per_page={per_page}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        records = data["data"]
        total_pages = data["total_pages"]
        return render_template(
            "records/records.html",
            records=records,
            page=page,
            total_pages=total_pages,
            api_url_images=api_url_images,
        )
    return "Error al obtener registros.", 500


@bp.route("/delete_record/<int:id>", methods=["POST"])
def delete_record(id):
    api_url = current_app.config["API_RECORDS_URL"]
    requests.delete(f"{api_url}{id}")
    return redirect(url_for("main.records.index"))
