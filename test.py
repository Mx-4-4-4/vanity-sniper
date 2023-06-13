import requests

running = True
while running:
    r = requests.get("https://discord.com/api/v9/invites/ssdfr")
    print(r.status_code)