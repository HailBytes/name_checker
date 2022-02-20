import requests, json

url = "https://social-scanner.p.rapidapi.com/social-scan/"

u = input("Enter username: ")
t = int(input("Enter target count 1-25: "))

print("------------------------------------------")

payload = "username={}&target_count={}".format(u, t)
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "social-scanner.p.rapidapi.com",
    'x-rapidapi-key': "Put in your rapidapi key here"
    }

response = requests.request("POST", url, data=payload, headers=headers)


jsonFile = open("data.json", "w")
jsonFile.write(response.text)
jsonFile.close()

jsonFile = open("data.json", "r")
values = json.load(jsonFile)

for i in values['detected']:
	print(i['link'])
	
print("------------------------------------------")
website = "http://"+u+".com"
def website_check(website):
	try:
		get = requests.get(website)
		if get.status_code == 200:
			print(website, "is a website")
		else:
			print(website, "is not a website")
			
	except requests.ConnectionError as e:
		print(website, "is not a website")

website_check(website)

		
