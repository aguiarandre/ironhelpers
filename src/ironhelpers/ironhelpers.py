import os
import sys

from IPython.display import display, Markdown

def pprint(query):
    """Pretty print a SQL query in an interactive python environment. """
    display(Markdown(f'''```mysql \n {query}```'''))

    return
