import csv

CONSUMPTION_INDEX = 4
DATE_INDEX = 2
HOUR_INDEX = 3

file = open(
    'data/eCO2mix_RTE_Annuel-Definitif_2018.csv', mode='r', encoding='utf-8'
)

reader = csv.reader(file, delimiter=';')
