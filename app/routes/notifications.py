from flask import Blueprint, render_template, current_app, request, url_for, redirect
import requests

bp = Blueprint("notifications", __name__, url_prefix="/notifications")


@bp.route("/", methods=["GET"])
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 5
    api_url = current_app.config["API_NOTIFICATIONS_URL"]
    api_url = f"{api_url}?page={page}&per_page={per_page}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        notifications = data["data"]
        total_pages = data["total_pages"]
        return render_template(
            "notifications/notifications.html",
            notifications=notifications,
            page=page,
            total_pages=total_pages,
        )
    return "Error al obtener notificaciones.", 500


@bp.route("/add_notification", methods=["POST", "GET"])
def add_advice():
    api_url = current_app.config["API_NOTIFICATIONS_URL"]
    title = request.form["title"]
    description = request.form["description"]
    notification_data = {"title": title, "description": description}
    requests.post(api_url, json=notification_data)
    return redirect(url_for("main.notifications.index"))


@bp.route("/update_notification/<int:id>", methods=["POST"])
def update_notification(id):
    api_url = current_app.config["API_NOTIFICATIONS_URL"]
    title = request.form["title"]
    description = request.form["description"]
    notification_data = {"title": title, "description": description}
    requests.put(f"{api_url}/{id}", json=notification_data)
    return redirect(url_for("main.notifications.index"))


@bp.route("/delete_notification/<int:id>", methods=["POST"])
def delete_notification(id):
    api_url = current_app.config["API_NOTIFICATIONS_URL"]
    requests.delete(f"{api_url}/{id}")
    return redirect(url_for("main.notifications.index"))
