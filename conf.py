# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

project = 'MWE'
copyright = '2025, Gregor Vollmer'
author = 'Gregor Vollmer'

version = "1.0"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_c_autodoc",
    "sphinx_c_autodoc.viewcode",
    "sphinx.ext.napoleon",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for PlantUML
# https://sphinx-needs.readthedocs.io/en/latest/installation.html#id2
plantuml = 'java -jar %s' % os.path.join(os.path.dirname(__file__), ".utils", "plantuml-lgpl-1.2025.0.jar")
plantuml_output_format = 'png'

c_autodoc_roots = ['code']
c_autodoc_compilation_args = ["-DSPHINX_DOCS", "-DDOXYGEN"]
