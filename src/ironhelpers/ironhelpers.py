import os
import sys

from IPython.display import display, Markdown

def pprint(query):
	display(Markdown(f'''```mysql \n {query}```'''))
	
	return