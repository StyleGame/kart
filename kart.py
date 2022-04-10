import requests,json,random,string
from bs4 import BeautifulSoup
from flask import Flask , request ,jsonify
app=Flask(name)
@app.route("/")
def f():
	return "<h1> السلام عليكم ورحمة الله وبركاته </h1>"
@app.route("/cards")
def f6():
	nono='5'
	number = '01032667914'
	pwd = '010Ana@@'
	with requests.Session() as req:
	       if nono == '5':
	           a='qwertyuioplkjhgfdsazxcvbnm'
	           c=str(''.join(random.choice(a) for i in range(10)))
	           url = f'https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce='+c+'&kc_locale=en'
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
    'username':number,
    'password':pwd
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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'} 
	               c = {
        'code': _code,
        'grant_type': 'authorization_code',
        'client_id': 'website',
        'redirect_uri': 'https://web.vodafone.com.eg/ar/KClogin'} 
	               am = req.post('https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token',headers=header,data=c)
	               access_token = am.json()['access_token']
	               
	               url1 = 'https://web.vodafone.com.eg/services/dxl/ramadanpromo/promotion?@type\u003dRamadanHub\u0026channel\u003dwebsite\u0026msisdn\u003d01032667914'
	               headers1 = {"Host": "web.vodafone.com.eg",
    "Connection": "keep-alive",
    "sec-ch-ua": "\" Not;A Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"91\", \"Chromium\";v\u003d\"91\"",
    "DNT": "1",
    "msisdn": "01032667914",
    "api-host": "PromotionHost",
    "Accept-Language": "AR",
    "sec-ch-ua-mobile": "?1",
    'Authorization':f'Bearer {access_token}',
    "Content-Type": "application/json",
    "Accept": "application/json",
    "clientId": "WebsiteConsumer",
    "x-dtpc": "22$104102625_297h12vAKAOOHQKDHUPCAEHHCRPLWUNGHKVLCCM-0e0",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; DRA-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "channel": "WEB",

"Save-Data": "on",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://web.vodafone.com.eg/spa/portal/hub",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "COOKIE_SUPPORT\u003dtrue; smapi_subject_id\u003d031a194f-e51e-4395-a71e-b7a3b84f9c07; smapi_install_id\u003d031a194f-e51e-4395-a71e-b7a3b84f9c07; mdLogger\u003dfalse; kampyle_userid\u003dd46b-680d-96cd-c2ef-d06a-61ea-7231-9b1c; mdigital_alternative_uuid\u003d9eb7-1c9e-94c8-f196-3d07-4379-efbc-7759; SUBMITTED_DATE\u003d1636915147165; DECLINED_DATE\u003d1647354222349; visit_01095171308\u003dNew; visit_01050406118\u003dNew; visit_01018261532\u003dNew; visit_01003551143\u003dNew; CONSENTMGR\u003dc1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1648163900278%7Cconsent:true; _gcl_au\u003d1.1.2018178592.1648163906; _gid\u003dGA1.3.1537330588.1648828645; _fbp\u003dfb.2.1648828646152.1359405786; cd_user_id\u003d17fe5d8ad3024-0dc3f202211717-6d333417-3f480-17fe5d8ad3158; LAST_INVITATION_VIEW\u003d1648828670562; GUEST_LANGUAGE_ID\u003dar_SA; s_ecid\u003dMCMID%7C62420690292677864400913961501896764115; s_fid\u003d13860960B799A76B-3DE530177A3EFE2F; mbox\u003dsession#bda67759f396461cb2a0efc21cbb4ea0#1648851608|PC#bda67759f396461cb2a0efc21cbb4ea0.37_0#1712093561; seamless\u003dfalse; smapi_session_id\u003ddae7cd71-807a-46dd-a3ac-1368f70e5bdf; 42f71aedaaf6f58bb7bf8e1bb9449ff3\u003d4e84853b3f72a77f4f0710e442c25a72; dtCookie\u003dv_4_srv_22_sn_61151CC7E0627FBD1B729F9AE3471D5D_perc_100000_ol_0_mul_1_app-3Aa294637573749774_0; rxVisitor\u003d16489040731713H60V8T0U32BH4LCG8DUG4T5GJJLL9DL; AMCVS_C6AA02BE532E6B0F0A490D4C%40AdobeOrg\u003d1; AMCV_C6AA02BE532E6B0F0A490D4C%40AdobeOrg\u003d-1124106680%7CMCIDTS%7C19084%7CMCMID%7C62420690292677864400913961501896764115%7CMCAAMLH-1649508875%7C6%7CMCAAMB-1649508875%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1648911275s%7CNONE%7CvVersion%7C5.2.0%7CMCAID%7CNONE; s_cc\u003dtrue; _gat_gtag_UA_120792002_1\u003d1; firstLogin\u003dtrue; kampylePageLoadedTimestamp\u003d1648904095632; TS362bb2a5027\u003d0838fe7682ab2000f7a98b6cf198cd95c0328ee7bf71c5310985b76874e72cced064c424f5b6531f08f68aec1e113000567ffb97de2efc45ad165cf3757c04aed1246d0ad869311a57c7a17e85cbbc4a6262e5980bc06dafd7e10b8efce974a0; 8549055b0e0d9b381b3bd98134c9a6bf\u003d20870cb0484f92189ba1909d7e402833; dtSa\u003d-; 3252354f8d3c7eb4efc36f79f0b4a345\u003dd9cd56daddc9fdd1fed1de4701560efa; JSESSIONID\u003d2A505E5913AA89BF109AAD250018C2BF; _ga\u003dGA1.1.1389393008.1648163906; kampyleUserSession\u003d1648904107005; kampyleUserSessionsCount\u003d169; s_sq\u003d%5B%5BB%5D%5D; 9e3eb9e5e128465c89b30b1ba7372b84\u003df0c08795772b1ec12f165ed49a6d8631; TS010dab0a\u003d01722e334e23e638ace257006da4300ccc2e4543c1513a73de7de21cc2d293091fa642f99d848b24f8e99a4f022ce40a556726f238123e2c97b52fab5c39849f5f724048f5c9744c1e3e89cda871415a4efb67af3e0ecaad2f6478a65440800ebcc82bb7df821e0fe7b0d1c6e12325fd6e431a7846d570037cfb80a1d0dc81745e422361ef7ccff0a0f161af15a2e053caa71405cc; TS95a20b30027\u003d0838fe7682ab20006e5b66c5ea909629637ce6ca2cfef96ed7c9e295c01fb55e28eac91a8f6f969708f31543601130004d4dbc77cdcfd1ae733a1e2481a88c149428715ebad5fa4e8f97f74dee0e6220db9b8e1b4d4967afbfc20d7b5a94c662; utag_main\u003dv_id:017fbe394b89002381ae3e188f8e00079002c07100450$_sn:7$_se:10$_ss:0$_st:1648905931646$vapi_domain:vodafone.com.eg$ses_id:1648903811060%3Bexp-session$_pn:5%3Bexp-session; kampyleSessionPageCounter\u003d3; dtLatC\u003d213; _ga_26LZ0HK0KL\u003dGS1.1.1648903868.6.1.1648904132.0; rxvt\u003d1648905934043|1648904073195; dtPC\u003d22$104102625_297h12vAKAOOHQKDHUPCAEHHCRPLWUNGHKVLCCM-0e0"}
	               
	              
	               r = requests.get(url1, headers=headers1)

	               mz = (r.json()[1])
	               h=mz['pattern'][0]
	               v=h['action'][0]
	               unit=v['characteristics'][1]['value']
	               user=v['characteristics'][2]['value']
	               card=v['characteristics'][3]['value']
	               return jsonify(Telegram="@Lengendvx3",unit=unit,user=user,card=card)
	           
app.run(host='0.0.0.0', port=8080)
