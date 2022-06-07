from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from datetime import date
from datetime import datetime
from threading import Thread
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import sys, os
import chromedriver_autoinstaller
#chromedriver_autoinstaller.install(cwd=True)
def resource_path(relative_path):
	
	driver = webdriver.Chrome(chromedriver_autoinstaller.install())
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.dirname(__file__)
	return os.path.join(base_path, relative_path)
root=Tk()
root.geometry("700x900")
framef= LabelFrame(root,pady=12,padx=40,borderwidth =0,highlightthickness =0)
framef.grid(row=0,column=0)
frame1= LabelFrame(framef,pady=12,padx=12,borderwidth =0,highlightthickness =0)
frame1.grid(row=0,column=0)
frame2=LabelFrame(framef,pady=12,padx=12,borderwidth =0,highlightthickness =0)
frame2.grid(row=0,column=1)
frame3=LabelFrame(root,pady=12,padx=40,borderwidth =0,highlightthickness =0)
frame3.grid(row=2,column=0)
frame4=LabelFrame(root,pady=12,padx=40,borderwidth =0,highlightthickness =0)
frame4.grid(row=3,column=0)
frame5=LabelFrame(root,pady=12,padx=40,borderwidth =0,highlightthickness =0)
frame5.grid(row=4,column=0)
frame6=LabelFrame(root,pady=12,padx=40,borderwidth =0,highlightthickness =0)
frame6.grid(row=5,column=0)
e =Entry(frame1,width=25)
e.grid(row=0,column=0,pady=10)
listel= Listbox(frame1,width=25,height=13)
listel.grid(row=2,column=0,pady=10)
def Ajouter():
	listel.insert(END,e.get())
def supprimer():
	listel.delete(ANCHOR)
ajouter=Button(frame2,padx=25,pady=3,text="ajouter",command=Ajouter)
ajouter.grid(row=1,column=2)
supprimer=Button(frame2,padx=25,pady=3,text="supprimer",command=supprimer)
supprimer.grid(row=1,column=3,padx=12)
t=StringVar()
t.set("moins d'une heure")
every=StringVar()
every.set("30min")

re=Label(frame4,text="Afficher les résultat pour: ")
re.grid(row=0,column=0)
T=OptionMenu(frame4,t,"moins d'une heure","moins de 4 heures","moins d'un jour","7 derniers jours","30 derniers jours","90 derniers jours","12 derniers mois")
T.grid(row=0,column=1)
re2=Label(frame4,text="dans chaque :")
re2.grid(row=1,column=0)
E=OptionMenu(frame4,every,"30min","1h","2h","5hs","12h")
E.grid(row=1,column=1)
lister= Listbox(frame6,width=35,height=13)
lister2= Listbox(frame6,width=35,height=13)
lister.grid(row=0,column=0,padx=25)
lister2.grid(row=0,column=1,padx=25)
def  tol(x,i):
	s=x[0]+"-"+x[1:]
	
	if i==0:
		
		lister.insert(END,s)
	else:
		
		lister2.insert(END,s)

def search(elems,links):
	today = date.today()
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
	with open(str(today)+'.txt','a') as f:
		f.write("\n"+str(current_time)+":"+"\n")
	driver = webdriver.Chrome(chromedriver_autoinstaller.install(), options=chrome_options)
	i=0
	lister.insert(END,str(current_time)+":")
	lister2.insert(END,str(current_time)+":")	

	for link in links:
		with open(str(today)+'.txt','a') as f:
			f.write(elems[i]+"\n")
		
		lister.insert(END,elems[i]+":")
		lister2.insert(END,elems[i]+":")
		i=i+1
		driver.get(link)
		time.sleep(5)
		driver.get(link)
		time.sleep(2)
		items =driver.find_elements_by_class_name('item')
		
		
		i=0
		j=0
		for item in items:

			a=str(item.text)
			if "Record" in a:
				x=a.split("Record")
			else:
				x=a.split("+")
			if int(a[0])<j:
				i=1
			tol(str(a),i)
			j=int(a[0])
			
			with open(str(today)+'.txt','a') as f:
				f.write(str(a))
			
			
	driver.close()
def st(elems,links,h):
	global K
	while k==0:
		search(elems,links)
		root.update()
		time.sleep(h)

def prg(elems,a,b):
	links=[]
	
	for elem in elems:
		if a=="moins d'une heure":
			links.append("https://trends.google.com/trends/explore?date=now%201-H&geo=US&q=\""+elem+"\"")
		elif a=="moins de 4 heures":
			links.append("https://trends.google.com/trends/explore?date=now%204-H&geo=US&q=\""+elem+"\"")
		elif a=="moins d'un jour":
			links.append("https://trends.google.com/trends/explore?date=now%201-d&geo=US&q=\""+elem+"\"")
		elif a=="7 derniers jours":
			links.append("https://trends.google.com/trends/explore?date=now%207-d&geo=US&q=\""+elem+"\"")
		elif a=="30 derniers jours":
			links.append("https://trends.google.com/trends/explore?date=today%201-m&geo=US&q=\""+elem+"\"")
		elif a=="90 derniers jours":
			links.append("https://trends.google.com/trends/explore?date=today%203-m&geo=US&q=\""+elem+"\"")
		elif a=="12 derniers mois":
			links.append("http://trends.google.com/trends/explore?q=\""+elem+"\"&geo=US")
		elif a=="8":
			links.append("https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=\""+elem+"\"")
		elif a=="9":
			links.append("https://trends.google.com/trends/explore?date=all&geo=US&q=\""+elem+"\"")
	h=0		
	if b=="30min":
		h=1800
	elif b=="1h":
		h=3600
	elif b=="2h":
		h=3600*2
	elif b=="5hs":
		h=3600*5
	elif b=="12h":
		h=3600*12
	
	p1=Thread(target=lambda:st(elems,links,h))
	p1.start()

def start():
		n=listel.size()
		global k
		k=0
		elems=[]
		for i in range(0,n):
			elems.append(listel.get(i))
			

		
		prg(elems,t.get(),every.get())
	

def stop():
	
	global k
	k=1

global k
start=Button(frame5,padx=25,pady=3,text="start",command=start)
start.grid(column=0,row=0,padx=25)
stop=Button(frame5,padx=25,pady=3,text="stop",command=stop)
stop.grid(column=1,row=0,padx=25)
root.mainloop()