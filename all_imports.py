import json
import time
import datetime

from URL import *
from App import *

def monthToNumber(mon):
	if mon == 'Jan':
		return '01'
	elif mon == 'Feb':
		return '02'
	elif mon == 'Mar':
		return '03'
	elif mon == 'Apr':
		return '04'
	elif mon == 'May':
		return '05'
	elif mon == 'Jun':
		return '06'
	elif mon == 'Jul':
		return '07'
	elif mon == 'Aug':
		return '08'
	elif mon == 'Sep':
		return '09'
	elif mon == 'Oct':
		return '10'
	elif mon == 'Nov':
		return '11'
	elif mon == 'Dec':
		return '12'

def getTimeDiff(endtime):
	now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
	nowDateList = re.split('[- :]', now)

	endDateList = re.split('[ ,:]', endtime)[2:]
	endDateList[1] = monthToNumber(endDateList[1])

	if endDateList[2] == nowDateList[2]:	# same year
		if endDateList[1] == nowDateList[1]:	# same month
			if endDateList[0] == nowDateList[0]:	# same day
				if endDateList[3] == nowDateList[3]:	#same hour
					if endDateList[4] > nowDateList[4]:		# some minutes left
						return str(int(endDateList[4]) - int(nowDateList[4])) + ' minute(s) left.'
					else:
						return 'OVER'
				else:	# some hours left
					return str(int(endDateList[3]) - int(nowDateList[3])) + ' hour(s) left.'
			else:
				return str(int(endDateList[0]) - int(nowDateList[0])) + ' day(s) left.'
		else:
			return str(int(endDateList[1]) - int(nowDateList[1])) + ' month(s) left.'
	else:
		return str(int(endDateList[2]) - int(nowDateList[2])) + ' year(s) left.'
