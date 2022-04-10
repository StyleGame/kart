import requests,json,random,string,termcolor,time,pyfiglet,sys,os
from bs4 import BeautifulSoup
from flask import *
app = Flask(__name__)
with requests.Session() as req:
    def generationLink(stringLingth):
        latters = string.ascii_lowercase
        return ''.join(random.choice(latters) for i in range(stringLingth))
        
    url = f'https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce={generationLink(10)}&kc_locale=en'
    responsePageLogin = req.get(url)
    soup = BeautifulSoup(responsePageLogin.content, 'html.parser')
    getUrlAction = soup.find('form').get('action')
    headerRequest = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'web.vodafone.com.eg',
    'Origin': 'https://web.vodafone.com.eg',
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    formData = {
    'username': '01032667914',
    'password': '010Ana@@'
    }
    sendUserData = req.post(getUrlAction,headers=headerRequest,data=formData)
    checkRegistry = sendUserData.url
    _checkRegistry = checkRegistry.find('KClogin')
    if _checkRegistry != -1:
        code = checkRegistry
        _code = code[code.index('code=') + 5:]
        
        header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-type': 'application/x-www-form-urlencoded',
        'Host': 'web.vodafone.com.eg',
        'Origin': 'https://web.vodafone.com.eg',
        'Referer': 'https://web.vodafone.com.eg/ar/KClogin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        formDataAccessToken = {
        'code': _code,
        'grant_type': 'authorization_code',
        'client_id': 'website',
        'redirect_uri': 'https://web.vodafone.com.eg/ar/KClogin'
        }
        sendDataAccessToken = req.post('https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token',headers=header,data=formDataAccessToken)
        access_token = sendDataAccessToken.json()['access_token']
        
#--------------------------------------------------------------
hed = {
'Host': 'web.vodafone.com.eg',
'Connection': 'keep-alive',
'msisdn': '01032667914',
'Accept-Language': 'AR',
'Authorization':f'Bearer {access_token}',
'Content-Type': 'application/json',
'Accept': 'application/json',
'clientId': 'WebsiteConsumer',
'channel': 'WEB',
}

r = requests.get('https://web.vodafone.com.eg/services/dxl/ramadanpromo/promotion?@type=RamadanHub&channel=website&msisdn=01000000000',headers=hed).text
print(r)


if __name__ == "__main__":
    app.run()
