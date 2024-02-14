# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import datetime
import os
import re
import sys

import toml

sys.path.insert(0, os.path.abspath("../.."))

import equation_database

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

try:
    info = toml.load("../../pyproject.toml")
except FileNotFoundError:
    info = toml.load("pyproject.toml")
project = info["tool"]["poetry"]["name"]
copyright = str(datetime.datetime.now().year) + ", Alexander Puck Neuwirth"
author = ", ".join(info["tool"]["poetry"]["authors"])
version = re.sub("^", "", os.popen("git describe --tags").read().strip())
rst_epilog = f""".. |project| replace:: {project} \n\n"""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.doctest",
    "matplotlib.sphinxext.plot_directive",
    #'numpydoc',
    "sphinx_math_dollar",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "nbsphinx",
    "jupyter_sphinx",
    #'jupyter_sphinx.execute'
    # "autoapi.extension",
]

autosummary_generate = True

autoapi_type = "python"
autoapi_dirs = ["../../equation_database"]
autoapi_python_class_content = "both"


templates_path = ['_templates']
exclude_patterns = []





# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
