from all_imports import *

url = URL('https://contesttrackerapi.herokuapp.com/')
response = url.fetch()

jso = json.loads(response.read())
ongoing = jso['result']['ongoing']
upcoming = jso['result']['upcoming']

