import requests, json
from optparse import OptionParser
#Login and Token Gaining code
parser=OptionParser()

parser.add_option("-u", "--username", 
				action="store", dest="username",
				help="Your TamTamy Username without replynet")

parser.add_option("-p", "--passsword", 
				action="store", dest="password",
				help="Your normal TamTamy Password")
(options, args)=parser.parse_args()

TT_Url = 'https://tamtamy.reply.eu/tamtamy/api/'
usname = options.username
pword = options.password
payload = {'userid': usname, 'password': pword, 'appName': 'Test'}
r = requests.get(TT_Url + '/login.json', params=payload)
json_data = r.json()
token = json_data['token']

#Other code
fname = '/home/ubuntu/replyusers/users'
with open(fname) as f:
    content = f.read().splitlines()
f.close

for item in content:
	payload = {'token': token}
	r = requests.get(TT_Url + 'user/' + item + '.xml', params=payload)
	try:
		company = r.text
		print company
	except:
		print 'user failed'
	
