from upm import pyupm_jhd1313m1 as lcd
from bs4 import BeautifulSoup
import requests
import time

url = 'http://www2.correios.com.br/sistemas/rastreamento/resultado.cfm'

params = { 'objetos': 'codigo-de-rastreamento' }
headers = { 'Referer': 'http://www2.correios.com.br/sistemas/rastreamento/default.cfm' }

html = requests.post(url, data=params, headers=headers)

soup = BeautifulSoup(html.text, 'html.parser')
text = soup.strong.text.encode('utf-8')

myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.write(text)

while True:
    time.sleep(100)
