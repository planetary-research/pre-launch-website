# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import datetime

# -- Project information -----------------------------------------------------

project = 'Planetary Research'
copyright = str(datetime.date.today().year)
author = 'Planetary Research'

# The full version, including alpha/beta/rc tags
# release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.youtube',
    'sphinx_copybutton',
    'sphinx_toolbox.collapse',
    'myst_parser',
]
myst_enable_extensions = [
    'attrs_block',
    'colon_fence',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

math_eqref_format = 'Eq.{number}'

numfig = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_theme = 'furo'  # 'sphinx_book_theme'
html_theme_options = {
    "announcement": "This is the <b>Planetary Research</b> pre-launch website. The journal is in development and will launch in January 2026.",
    "repository_branch": "master",
    "repository_url": "https://github.com/planetary-research/pre-launch-website",
    "use_repository_button": True,
    "use_sidenotes": False,
    "use_edit_page_button": False,
    "use_source_button": False,
    "use_issues_button": False,
    "use_download_button": False,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/planetary-research-journal",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-lg",
        },
    ],
    # "light_css_variables": {
    #    'color-announcement-background': '#e0c7ff',
    #    'color-announcement-text': '#222832',
    #},
    #"dark_css_variables": {
    #    'color-announcement-background': '#341a61',
    #    'color-announcement-text': '#ced6dd',
    #},
}

# html_theme_options = {
#     "stickysidebar": "true",
#     "description": "The reference documentation for all EMC-EFO software."
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_show_sphinx = False
html_title = "Planetary Research"
html_last_updated_fmt = '%b %d, %Y'
html_copy_source = False
html_show_sourcelink = False
