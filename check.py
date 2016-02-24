from all_imports import *

url = URL('https://contesttrackerapi.herokuapp.com/')
response = url.fetch()

jso = json.loads(response.read())
ongoing = jso['result']['ongoing']
upcoming = jso['result']['upcoming']

# filter upcoming to next 1 hour
for contest in ongoing:
	print contest

app = App(ongoing).root.mainloop()
