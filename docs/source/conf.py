

# -- Project information

project = 'Sonarverse'
copyright = '2023, Sonarverse'
author = 'Sonarverse'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "myst_parser",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

multiproject_projects = {
    "user": {
        "use_config_file": False,
        "config": {
            "project": "Read the Docs user documentation",
            "html_title": "Read the Docs user documentation",
        },
    },
    "dev": {
        "use_config_file": False,
        "config": {
            "project": "Read the Docs developer documentation",
            "html_title": "Read the Docs developer documentation",
        },
    },
}

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# html_static_path = ["img"]
html_css_files = ["css/custom.css", "css/sphinx_prompt_css.css"]
html_js_files = ["js/expand_tabs.js"]
html_show_sphinx = False
html_show_copyright = False
html_theme_options = {
    'collapse_navigation': True,
    'navigation_depth': 3
}

# -- Options for EPUB output
# epub_show_urls = 'footnote'

# -- Options for myst_header
suppress_warnings = [
    "myst.header",
    "sphinx_design"
]

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

source_suffix = ['.rst', '.md']

source_doc = 'snowflake/index'
