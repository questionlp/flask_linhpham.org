# -*- coding: utf-8 -*-
# Copyright (c) 2021 Linh Pham
"""Flask application startup file"""

import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, request, Response, url_for
from flask.logging import create_logger
from werkzeug.exceptions import HTTPException

#region Flask App Initialization
load_dotenv(find_dotenv())
app = Flask(__name__)
app_logger = create_logger(app)
app.url_map.strict_slashes = False
app.jinja_options = Flask.jinja_options.copy()
app.jinja_options.update({"trim_blocks": True, "lstrip_blocks": True})
app.create_jinja_environment()
app.jinja_env.globals["ga_property_code"] = os.getenv("GA_PROPERTY_CODE")
app.jinja_env.globals["site_url"] = os.getenv("SITE_URL", default="/")
#endregion

#region Routes
@app.route("/")
def index():
    """Landing page"""
    return render_template("index.html")

@app.route("/favicon.ico")
def favicon():
    """Favicon Redirect"""
    return redirect(url_for("static", filename="img/favicon.png"), code=301)

@app.route("/sitemap.xml")
def sitemap():
    """Sitemap XML"""
    sitemap = render_template("core/sitemap.xml")
    return Response(sitemap, mimetype="text/xml")

#endregion

#region App Initialization
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="9251")

#endregion
