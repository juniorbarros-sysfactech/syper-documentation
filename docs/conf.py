# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Configuration for Sphinx
project = 'My Software'
author = 'Your Name'
release = '0.1'

extensions = [
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
