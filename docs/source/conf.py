import os
import sys
import pathlib


# IMPORTS ps I can be done not so dumbly
sys.path.insert(0, os.path.dirname(os.path.dirname(os. getcwd())))

# get package details directly from pyproject
pyproject_file = "".join([os.path.dirname(os.path.dirname(os. getcwd())), "\\pyproject.toml"])
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

module_names = (
    "parsing",
    "style",
    "validation",
)

pygments_style = "sphinx"

latex_engine = "pdflatex"

todo_include_todos = True

parent = str(pathlib.Path(os.getcwd()).parents[1])
sys.path.append("".join([parent, "\\src\\PPVD"]))
sys.path.append("".join([parent, "\\src"]))
for _module in module_names:
    sys.path.append("".join([parent, "\\src\\PPVD\\", _module]))
