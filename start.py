from all_imports import *

url = URL('https://contesttrackerapi.herokuapp.com/')
response = url.fetch()

jso = json.loads(response.read())
ongoing = jso['result']['ongoing']
upcoming = jso['result']['upcoming']

ongoing.append({'url':'https://github.com/aedorado/contest-desktop-notif', 'Platform':'Github', 'EndTime':'Wed, 31 Jul 2024 00:00', 'Name':'Contest-Desktop-Notification'})

for event in ongoing:
	event['EndTime'] = event['EndTime'] + '  ' + getTimeDiff(event['EndTime'])

app = App(ongoing).root.mainloop()
