import requests as req
from bs4 import BeautifulSoup as bs
import PySimpleGUI as sg
import time
face=[[sg.Button(button_text='Update')],[sg.Output(size=(70,40)),
      sg.Multiline(default_text='',size=(25,30),key='pred')]]
def u(x):
    return wind.Element('pred').update(x)
url='https://www.worldometers.info/coronavirus/'
head={'user-agent':'''Mozilla/5.0 (Windows NT 6.1; Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36''',
      'accept':'*/*'}
wind=sg.Window('Coronavirus',face)
while True:
    txt=bs(req.get(url,'html.parser',headers=head).text,
       features='lxml').find_all('div',class_='maincounter-number')
    txt1=bs(req.get(url,'html.parser',headers=head).text,
        features='lxml').find_all('div',class_='number-table-main')
    event,vls=wind.read()
    deaths=txt[1].getText()[1:-1]
    heal=txt[2].getText()[1:-1]
    now=txt1[0].getText()
    if event=='Update':
        print('Number of cases: '+txt[0].getText()[1:-2])
        print('Deaths: '+deaths)
        print('Recovery: '+heal)
        print('Active: '+now)
        print('Time: '+time.ctime())
        now,deaths,heal=int(now.replace(',','')),int(deaths.replace(',','')),int(heal.replace(',',''))
        pred=round(now*(deaths/(deaths+heal)))
        u(('Will die:\n'+str(pred)+'\n\nResult:\n'+str(deaths+pred)))
