from bs4 import BeautifulSoup
import sys 
import pandas as panda
from urllib.error import HTTPError,URLError
import urllib.request
import os 
os.chdir('csv')


with urllib.request.urlopen('view-source:https://www.google.fr/maps/search/commerces+%C3%A0+proximit%C3%A9+du+12%C3%A8me+arrondissement/@48.8249223,2.3717893,13z/data=!3m1!4b1?dcr=0')^as sock:
		page=sock.read()
		soup=BeautifulSoup(page)


