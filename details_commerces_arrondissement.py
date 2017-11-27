from bs4 import BeautifulSoup
import sys
import pandas as panda
from urllib.error import HTTPError,URLError
import urllib.request
import os
os.chdir('csv')

#On recupere les données sur les commerces de chaque arrondissement
data_commerce=panda.read_csv('CommercesParArrondissement.csv',encoding='uft-8-sig')

#Création de la dataframe
Arrondissement=panda.DataFrame(columns=['num','année','alimentaire','non_alimentaire',
                                        'restauration','Service_commerciaux','locaux_vacants',
                                        'gros_commerce','','','',
                                        ''])

#Parcours de notre CSV

for i , row in 