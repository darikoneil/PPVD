import os
import sys
import pathlib


# IMPORTS ps I can be done not so dumbly
sys.path.insert(0, os.path.dirname(os.path.dirname(os. getcwd())))

# get package details directly from pyproject
pyproject_file = os.path.join(os.path.dirname(os.path.dirname(os. getcwd())), "pyproject.toml")
package_details = toml.load(pyproject_file).get("project")

project = package_details.get("name")
copyright = "2023, Darik A. O'Neil"
author = "Darik A. O'Neil"
release = package_details.get("version")

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints"]

typehints_defaults = "comma"


source_suffix = ".rst"

language = "en"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/1.24/", None),
}

html_theme = "sphinx_rtd_theme"

pygments_style = "sphinx"

latex_engine = "pdflatex"

todo_include_todos = True
