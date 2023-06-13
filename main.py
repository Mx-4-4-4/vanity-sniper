import json
from src.sniper import Sniper

#load config json file
with open("./config.json") as config_file:
    config = json.load(config_file)

sniper = Sniper()

if __name__ == "__main__":
    sniper.setGuild({"id": config["guild_id"], "admin_token": config["admin_token"]})
    sniper.setVanities(config["vanities"])
    sniper.setWebhook({"url": config["webhook_url"]})
    sniper.run()