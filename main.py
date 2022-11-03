"""
Created on Thu Oct 27 10:19:20 2022

@author: m.knaust
"""

import pandas as pd
import numpy as np
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d.%m.%Y %H:%M:%S")

trennsymbol = ' '
csv_trenner = ';' # \t oder , oder ;
temp_array = []

while True:
    input('Daten in Mappe1.csv? Press Enter')
    break

df = pd.read_csv('Mappe1.csv',sep=";")

namen = [item for item in list(df['Name']) if not(pd.isnull(item)) == True]
funktionen = [item for item in list(df['Funktion']) if not(pd.isnull(item)) == True]
adressen = [item for item in list(df['Haupt/Mittel_Gruppe']) if not(pd.isnull(item)) == True]
start_adressen = [item for item in list(df['Start_Addr'].astype('Int64')) if not(pd.isnull(item)) == True]


for i, word in enumerate(namen):
        namen[i]=word.strip()

for i, word in enumerate(funktionen):
        funktionen[i]=word.strip()

for i, word in enumerate(adressen):
        adressen[i]=word.strip()

for i, word in enumerate(adressen):
        temp_array = adressen[i].split('/')
        if int(temp_array[0]) > 31 and int(temp_array[0]) < 0:
            input("Falsche Hauptgruppenadresse. Zum beenden Taste drücken")
            quit()
        if int(temp_array[1]) > 7 and int(temp_array[1]) < 0:
            input("Falsche Mittelgruppenadresse. Zum beenden Taste drücken")
            quit()

for number in start_adressen:
        if int(number) < 0:
            input("Falsche Untergruppenadresse. Zum beenden Taste drücken")
            quit()

# ETS6 will ANSI code,  ÄäÜüÖö und so ...
with open("output.txt", "w", encoding='iso8859-1') as output_file:
    output_file.write("Generiert am: " + dt_string + "\n" + "\n")
    for j in range(len(namen)):
         for i in range(len(funktionen)):
                if (start_adressen[i] + j) > 255:
                    output_file.truncate(0)
                    input("Falsche Untergruppenadresse. Zum beenden Taste drücken")
                    quit()
                print( namen[j] + trennsymbol + funktionen[i] + ' ' + adressen[i] + '/' + str(start_adressen[i] + j))
                output_file.write( '\u0022' + namen[j] + trennsymbol + funktionen[i] + '\u0022'  + csv_trenner +'\u0022' + adressen[i] + '/' + str(start_adressen[i] + j)+'\u0022' + csv_trenner +'\u0022' +'\u0022'+ csv_trenner +'\u0022' +'\u0022' + csv_trenner +'\u0022' +'\u0022'+ csv_trenner +'\u0022' +'\u0022'+ csv_trenner +'\u0022'+'Auto'+'\u0022''\n')

output_file.close()
print('')
print('...alles generiert ')
input("Zum beenden Taste drücken")
quit()
