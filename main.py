try:
	from requests.structures import CaseInsensitiveDict
	import os
	import json, re, inquirer, requests, random, webbrowser
except:
	os.system('pip install inquirer')
	import json, re, inquirer, requests, random, webbrowser

#Banner
print('''
  ____  _             _        _      _____                      
 |  _ \| |           | |      | |    / ____|                     
 | |_) | | ___   ___ | | _____| |_  | |  __  __ _ _ __ ___   ___ 
 |  _ <| |/ _ \ / _ \| |/ / _ \ __| | | |_ |/ _` | '_ ` _ \ / _ \\
 | |_) | | (_) | (_) |   <  __/ |_  | |__| | (_| | | | | | |  __/
 |____/|_|\___/ \___/|_|\_\___|\__|  \_____|\__,_|_| |_| |_|\___|
  / ____|        | |       / ____|                               
 | |     ___   __| | ___  | |  __ _   _  ___  ___ ___  ___ _ __  
 | |    / _ \ / _` |/ _ \ | | |_ | | | |/ _ \/ __/ __|/ _ \ '__| 
 | |___| (_) | (_| |  __/ | |__| | |_| |  __/\__ \__ \  __/ |    
  \_____\___/ \__,_|\___|  \_____|\__,_|\___||___/___/\___|_|    

''')

#If cookie does not exist ask for it
if not os.path.exists('./bsidcookie'):
	open('./bsidcookie', 'w').write(input('Enter bsid cookie in this format "bsid=**************": '))
else:
#Else ask if user want to redo
	if inquirer.prompt([inquirer.List('redo', message="Redo bsid cookie?", choices=['No', 'Yes'])])['redo'] == 'Yes':
		open('./bsidcookie', 'w').write(input('Enter bsid cookie in this format "bsid=**************": '))

#Get the cookie
bsidcookie = open('./bsidcookie', 'r').read()

#Set url and headers
headers = CaseInsensitiveDict()
headers["cookie"] = bsidcookie

def isgame(gameid):
	return json.loads(requests.get('https://fb.blooket.com/c/firebase/id?id='+gameid, headers=headers).text)['success']

while True:
	gid = str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
	print(gid)
	if isgame(gid):
		print('GAME FOUND!!!!!')
		print(gid)
		if input('Type o and then <enter> to open browser, type anything else to exit: ').strip() == o:
			webbrowser.open('https://play.blooket.com/play?id='+gid)
		exit(0)
		break
