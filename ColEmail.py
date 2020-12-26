import requests
import re
import time

def GetEmailBySite(SiteList):

	for i in SiteList:
		DataSite = requests.get(i)
		ReturnRegex = re.findall('[\w\.-]+\.\w+',DataSize.text)
		if ReturnRegex :
			return(list(set(ReturnRegex)))
		else:
			return None


sites = ["http://laboratiohacker.com.br"]


try:
	for x in sites:
		mails = (GetEmailBySite([x]))
		if (mails != "None" or mails != None):
			print (mails)
		cont_x = cont_x+1
except:
	print(x)
	pass
