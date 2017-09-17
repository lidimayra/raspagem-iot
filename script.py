from upm import pyupm_jhd1313m1 as lcd
from bs4 import BeautifulSoup
import requests
import sys
import time

myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

def order_status():
    url = 'http://www2.correios.com.br/sistemas/rastreamento/resultado.cfm'
    params = { 'objetos': sys.argv[1] }
    headers = { 'Referer': 'http://www2.correios.com.br/sistemas/rastreamento/default.cfm' }
    html = requests.post(url, data=params, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup.strong.text.encode('utf-8')

def lcd_color(green, blue):
    red = 10
    myLcd.setColor(red, green, blue)

def lcd_write(word, line):
    myLcd.setCursor(line, 0)
    myLcd.write(word)

def run():
    words = order_status().split()
    lcd_color(70, 30) if words[1] == 'entregue' else lcd_color(30, 70)

    lcd_write(words[0], 0)
    lcd_write(words[1], 1)

    time.sleep(2)

while True:
    run() 
