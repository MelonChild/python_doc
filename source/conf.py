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
import recommonmark


# -- Project information -----------------------------------------------------

project = '课窝直播平台使用手册'
copyright = '2019, Kewo'
author = 'KwTD Null'
version = 'V1.1'

# The full version, including alpha/beta/rc tags
release = 'V1.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_use_index = True
html_show_sphinx = False
html_title = "课窝直播平台手册"
html_short_title = "KEWO"
html_favicon = '_static/kewo.ico'
html_logo = '_static/logo.png'
html_show_sourcelink = False
html_search_language = 'zh'
html_search_options = {
    'type': 'mecab',
    'dic_enc': 'utf-8',
    'dict': '/path/to/jieba.dic',
}
html_use_opensearch = 'True'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
source_suffix = ['.rst', '.md']