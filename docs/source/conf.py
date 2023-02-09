import os
import sys
import pathlib

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../../'))


project = 'PPVD'
copyright = "2023, Darik A. O'Neil"
author = "Darik A. O'Neil"
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints']

typehints_defaults = 'comma'
templates_path = ['_templates']
exclude_patterns = []


language = '[en]'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

html_theme = 'sphinx_rtd_theme'

module_names = (
    "parsing",
    "style",
    "validation",
)

parent = str(pathlib.Path(os.getcwd()).parents[1])
sys.path.append("".join([parent, "\\src\\PPVD"]))
sys.path.append("".join([parent, "\\src"]))
for _module in module_names:
    sys.path.append("".join([parent, "\\src\\PPVD\\", _module]))
