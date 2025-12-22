# docs/source/conf.py
import os
import sys
from datetime import date

# Make your package importable for autodoc (optional)
sys.path.insert(0, os.path.abspath("../.."))

project = "FEDSRT"
author = "Ma Lab & Yue Lab & Shi Lab"
copyright = f"{date.today().year}, {author}"

extensions = [
    "myst_parser",
    "sphinx_design",
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"  # official RTD theme :contentReference[oaicite:1]{index=1}

html_theme_options = {
    # these are standard knobs supported by sphinx-rtd-theme :contentReference[oaicite:2]{index=2}
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "titles_only": False,
    "style_external_links": True,
}

html_static_path = ["_static"]
html_css_files = ["custom.css"]
