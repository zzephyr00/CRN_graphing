from py2cytoscape.data.cyrest_client import CyRestClient

from IPython.display import Image

import networkx as nx
import pandas as pd

import pymaid

rm = pymaid.CatmaidInstance('server_url', 'api_token', 'http_user', 'http_password')

print('pymaid version:', pymaid.__version__)