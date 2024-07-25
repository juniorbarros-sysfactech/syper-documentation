# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'My Software'
author = 'Your Name'
release = '0.1'

# Extensions
extensions = [
    'sphinx_rtd_theme',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
