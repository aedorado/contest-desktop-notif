from all_imports import *

url = URL('https://contesttrackerapi.herokuapp.com/')
response = url.fetch()

jso = json.loads(response.read())
ongoing = jso['result']['ongoing']
upcoming = jso['result']['upcoming']

ongoing.append({'url':'https://github.com/aedorado/contest-desktop-notif', 'Platform':'Github', 'EndTime':'', 'Name':'Contest-Desktop-Notification'})

app = App(ongoing).root.mainloop()
