# -*- coding: utf-8 -*-
# Copyright (c) 2021 Linh Pham
"""Flask WSGI startup file"""

from app import app

if __name__ == "__main__":
    app.run(debug=False)
