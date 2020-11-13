# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
from bs4 import BeautifulSoup
import requests
import wget
import datetime

resp = requests.get('https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/statistik-och-analyser/bekraftade-fall-i-sverige/')
if resp.ok:
    soup = BeautifulSoup(resp.text, 'html.parser')
    result = soup.find_all('a', {'title':'Excel-fil'})
else:
    print ("Boo! {}".format(resp.status_code))
    print (resp.text)

url = result[0].get('href')
outfile = 'fhm_download_'+str(datetime.date.today())+'.xlsx'

wget.download(url, out = outfile)
