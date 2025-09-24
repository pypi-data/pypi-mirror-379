"""Common component controllers."""

from __future__ import annotations

from pathlib import Path

import flask

from nummus.controllers import auth, base


def page_dashboard() -> flask.Response:
    """GET /.

    Returns:
        string HTML response

    """
    return base.page("page.jinja", "Dashboard")


@auth.login_exempt
def page_status() -> str:
    """GET /status.

    Returns:
        string HTML response

    """
    return "ok"


def page_style_test() -> flask.Response:
    """GET /style-test.

    Returns:
        string HTML response

    """
    return base.page(
        "shared/style-test.jinja",
        "Style test",
    )


def favicon() -> flask.Response:
    """GET /favicon.ico.

    Returns:
        string HTML response

    """
    path = Path(flask.current_app.static_folder or "static") / "img" / "favicon.ico"
    return flask.send_file(path)


ROUTES: base.Routes = {
    "/": (page_dashboard, ["GET"]),
    "/index": (page_dashboard, ["GET"]),
    "/favicon.ico": (favicon, ["GET"]),
    "/status": (page_status, ["GET"]),
    "/d/style-test": (page_style_test, ["GET"]),
}
