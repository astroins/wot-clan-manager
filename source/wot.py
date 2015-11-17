import requests
import json
import datetime	
from flask import Flask

def get_account_id(nick):
	
	r = requests.get('https://api.worldoftanks.eu/wot/account/list/?application_id=demo&search=' + nick)
	data = json.loads(r.text)
	account_id = data["data"][0]["account_id"]
	
	return account_id

def member_since_days(account_id):

	r = requests.post("https://api.worldoftanks.eu/wgn/clans/membersinfo/?application_id=demo&account_id=" + str(account_id))
	data = json.loads(r.text)
	timestamp = data["data"][str(account_id)]["joined_at"]
	clan_join_date = datetime.datetime.fromtimestamp(int(str(timestamp)))
	current_date = datetime.datetime.now()
	delta = current_date - clan_join_date
	return delta.days

def get_total_resources(account_id):

	r = requests.get("https://api.worldoftanks.eu/wot/stronghold/accountstats/?application_id=demo&account_id=" + str(account_id))
	data = json.loads(r.text)
	total_resources_earned = data["data"][str(account_id)]["total_resources_earned"]
	return total_resources_earned

account_id = get_account_id("reibenus")
print(account_id)
days = member_since_days(account_id)
print(days)
total_resources_earned = get_total_resources(account_id)
print(total_resources_earned / days)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()