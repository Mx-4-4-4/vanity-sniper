import time
import requests

class printbcolors:
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class Asciipicture:
    def drawSnipe(module, color, latency):
        if type(color) != str:
            print(printbcolors.FAIL + "/!\ Erreur: La couleur doit être une chaine de caractère.\n    -> ('drawSnipe()')")
            module.running = False
            exit()
            
        if type(latency) != float and type(latency) != int:
            print(printbcolors.FAIL + "/!\ Erreur: La latence doit être un nombre.\n    -> ('drawSnipe()')")
            module.running = False
            exit()
            
        if module.running:
            print(color + "                                      ____    _     __     _    ____")
            time.sleep(latency)
            print(color + "          ✨ VANITY SNIPER ✨        |####`--|#|---|##|---|#|--'##|#|")
            time.sleep(latency)
            print(color + "   _                                 |____,--|#|---|##|---|#|--.__|_|")
            time.sleep(latency)
            print(color + " _|#)_____________________________________,--'EEEEEEEEEEEEEE'_=-.")
            time.sleep(latency)
            print(color + "((_____((_________________________,--------[JW](___(____(____(_==)        _________")
            time.sleep(latency)
            print(color + "                               .--|##,----o  o  o  o  o  o  o__|/`---,-,-'=========`=+==.")
            time.sleep(latency)
            print(color + "       DEV BY ! 爪乂#0001      |##|_Y__,__.-._,__,  __,-.___/ J \\ .----.#############|##|")
            time.sleep(latency)
            print(color + "        discord.gg/ssdfr       |##|              `-.|#|##|#|`===l##\\   _\\############|##|")
            time.sleep(latency)
            print(color + "                              =======-===l          |_|__|_|     \\##`-\"__,=======.###|##|")
            time.sleep(latency)
            print(color + "                                                                  \\__,\"          '======'")
            time.sleep(latency)

class Sniper:
    def __init__(self):
        self.running = True
        
        #innitialisation des propriétés
        self.vanities = False
        self.proxies = False
        self.webhook_url = False
        self.guild_id = False
        self.admin_token = False
        
        self.user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1"
        
        self.count = 0
    
    def stop(self):
        self.running = False
        exit()
    
    def setProxies(self, proxies):
        if type(proxies) != list or len(proxies) == 0:
            print(printbcolors.FAIL + "/!\ Erreur: Les proxies doivent être déclarées sous forme de liste.\n    -> ('setProxies()')")
            self.stop()
        
        self.proxies = []
        for proxy in proxies:
            if type(proxy) != str:
                print(printbcolors.FAIL + "/!\ Erreur: Les proxies doivent être des chaines de caractères.\n    -> ('setProxies()')")
                self.stop()
            
            self.proxies.append(proxy)
    
    def setVanities(self, vanities):
        if type(vanities) != list or len(vanities) == 0:
            print(printbcolors.FAIL + "/!\ Erreur: Les urls doivent être déclarées sous forme de liste.\n    -> ('setVanities()')")
            self.stop()
        
        self.vanities = []
        for vanity in vanities:
            if type(vanity) != str:
                print(printbcolors.FAIL + "/!\ Erreur: Les urls doivent être des chaines de caractères.\n    -> ('setVanities()')")
                self.stop()
            
            self.vanities.append(vanity)
    
    def setWebhook(self, object):
        if type(object) != dict or not len(object) == 1 or not "url" in object:
            print(printbcolors.FAIL + "/!\ Erreur: Le webhook doit être déclaré sous forme : setWebhook({\"url\": \"https://webhookURL\"}).\n    -> ('setWebhook()')")
            self.stop()
        
        self.webhook_url = object["url"]
        
        if type(self.webhook_url) != str:
            print(printbcolors.FAIL + "/!\ Erreur: Le webhook doit être déclaré sous forme : setWebhook({\"url\": \"https://webhookURL\"}).\n    -> ('setWebhook()')")
            self.stop()
    
    def setGuild(self, object):
        if type(object) != dict or not len(object) == 2 or not "id" in object or not "admin_token" in object:
            print(printbcolors.FAIL + "/!\ Erreur: Le serveur ou `guild` doit être déclaré sous forme : setGuild({\"id\": \"-guild-id-\", \"admin_token\": \"-le-token-d'un-administrateur-du-serveur-\"}).\n    -> ('setGuild()')")
            self.stop()
            
        self.guild_id = object["id"]
        self.admin_token = object["admin_token"]

        if type(self.guild_id) != str or type(self.admin_token) != str:
            print(printbcolors.FAIL + "/!\ Erreur: Le serveur ou `guild` doit être déclaré sous forme : setGuild({\"id\": \"-guild-id-\", \"admin_token\": \"-le-token-d'un-administrateur-du-serveur\"}).\n    -> ('setGuild()')")
            self.stop()
    
    def log(self, message, color = printbcolors.ENDC, time_format = "%H:%M:%S"):
        if type(message) != str or type(color) != str or type(time_format) != str:
            print(printbcolors.FAIL + "/!\ Erreur: La fonction log ne doit contenir que des chaines de caractères.\n    -> ('log()')")
            self.stop()
        print(printbcolors.OKBLUE + "- " + printbcolors.OKCYAN + f"[{time.strftime(time_format, time.localtime(time.time()))}]" + color + " " + message)
    
    def snipe_1_vanity(self, vanities, interval = 1):
        if not vanities or type(vanities) != list :
            print(printbcolors.FAIL + "/!\ Erreur: L'argument vanities doit être une liste (les vanities).\n    -> ('check_vanity()')")
            self.stop()
        headers = {
            "User-Agent": self.user_agent,
            "content-type": "application/json",
        }
        for vanity in vanities:
            response = requests.get(f"https://discord.com/api/v9/invites/{vanity}", headers=headers)
            match response.status_code:
                case 404:
                    self.claim(vanity)
                    self.stop()
                    break
                case 200:
                    self.log(f"URL [{vanity}] taken ❌")
                    time.sleep(interval)
                case 429:
                    self.log(f"Rate limite ⚠️")
                    print(response.content)
                    time.sleep(interval)
                case _:
                    self.log("Unknow Error :")
                    print(response.content)
                    time.sleep(interval)
    
    def claim(self, vanity):
        if type(vanity) != str :
            print(printbcolors.FAIL + "/!\ Erreur: La fonction claim ne doit contenir que des chaines de caractères (la vanity).\n    -> ('claim()')")
            self.stop()
        headers = {
            "User-Agent": self.user_agent,
            "authorization": self.admin_token,
            "content-type": "application/json",
        }
        
        response = requests.patch("https://ptb.discord.com/api/v9/guilds/%s/vanity-url" % (self.guild_id), json={"code": vanity}, headers=headers)
        if response.status_code == 200:
            self.log(f"URL [{vanity}] sniped ✅", printbcolors.OKGREEN)
            self.stop()
        else:
            self.log(f"/!\ Erreur: La request du changement de la vanity n'a pas fonctionné, voici la reponse : ", printbcolors.FAIL)
            print(printbcolors.ENDC)
            print(response.content)
    
    def run(self, interval = 1):
        root_format1 = printbcolors.OKBLUE + "> "
        Asciipicture.drawSnipe(self, printbcolors.OKCYAN, 0.025)
        
        if not self.vanities:
            print(printbcolors.FAIL + "/!\ Erreur: Les urls n'ont pas été déclarés.\n    -> ('run()')")
            self.stop()
        else:
            for vanity in self.vanities:
                time.sleep(0.5)
                print(root_format1 + printbcolors.OKGREEN + f"URL [{vanity}] initialisée ✅")
        
        if not self.guild_id or not self.admin_token:
            print(printbcolors.FAIL + "/!\ Erreur: Les paramètres du serveur ou `guild` n'ont pas été déclarés.\n    -> ('run()')")
            self.stop()
        else:
            if len(self.guild_id) < 4 or len(self.admin_token) < 4:
                print(printbcolors.FAIL + "/!\ Erreur: Un des paramètres du serveur ou `guild` n'est pas valable.\n    -> ('run()')")
                self.stop()
                
            time.sleep(0.5)
            token_censored = list(str(self.admin_token).strip())[0] + list(str(self.admin_token).strip())[1] + list(str(self.admin_token).strip())[2] + ((len(self.admin_token) - 3) * "*")
            print(root_format1 + printbcolors.OKGREEN + f"Serveur initialisés ✅ (ID : {self.guild_id}, TOKEN_ADMIN : {token_censored})")
        
        if self.proxies:
            time.sleep(0.5)
            print(root_format1 + printbcolors.OKGREEN + f"{len(self.proxies)} proxies initialisés ✅")
        else:
            time.sleep(0.5)
            print(root_format1 + printbcolors.WARNING + "Pas de proxies ❌")
        
        if self.webhook_url:
            time.sleep(0.5)
            print(root_format1 + printbcolors.OKGREEN + f"WebHook initialisés ✅ ({self.webhook_url})")
        else:
            time.sleep(0.5)
            print(root_format1 + printbcolors.WARNING + "Pas de webHook ❌")
        
        while self.running:
            self.snipe_1_vanity(self.vanities, interval=interval)