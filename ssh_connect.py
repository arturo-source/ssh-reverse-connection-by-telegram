import requests, os

#Define some variables
chat_id = 1234567
nextid_file = '/your/directory/where/nextid'
base_url = 'https://api.telegram.org/'
bot_id = 'your_bot_id'
port = '8899'
ssh_user_url = 'user@example.com'

#Only updates the nextid to the last messageid + 1
def updateOffset(updates):
	global nextid
	try:
		nextid = updates['result'][-1]['update_id'] + 1
	except:
		#One posible error is that there is not update
		print('Error while updating nextid')

#Read nextid because we dont want seen messages yet
nextid = 0
with open(nextid_file, 'r') as f:
	nextid = f.read()

#Get updates
response = requests.get(base_url + bot_id + '/getUpdates', params={'offset':nextid})
updates = response.json()

#Read updates
for update in updates['result']:
	#First we establish ssh reverse conection
	#Then we send a message to confirm reverse conection has been made
	if update['message']['chat']['id'] == chat_id and update['message']['text'] == '/ssh':
		os.system('ssh -R ' + port + ':localhost:22 ' + ssh_user_url)
		message = update['message']
		requests.get(base_url + bot_id + '/sendMessage', params={'chat_id':message['chat']['id'], 'text':'Reverse SSH contection established', 'reply_to_message_id': message['message_id']})

if(len(updates['result']) > 0):
	updateOffset(updates)
	#Write nextid because we dont want to see this messages again
	with open(nextid_file, 'w') as f:
		f.write(str(nextid))
