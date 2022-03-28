import csv

# for consumption data
CONSUMPTION_INDEX = 4
DATE_INDEX = 2
HOUR_INDEX = 3

# for weather data
T_INDEX = -1
C_DATE_INDEX = 4

# consumption data transformation
consumptions_per_hour = {}

file = open(
    'data/eCO2mix_RTE_Annuel-Definitif_2018.csv', mode='r', encoding='utf-8'
)
reader = csv.reader(file, delimiter=';')
next(reader)
for raw in reader:
    hour_value = raw[HOUR_INDEX]
    if hour_value == '':
        break
    minutes = hour_value.split(':')[1]
    if minutes == '00':
        hour = int(hour_value.split(':')[0])
        consumption = int(raw[CONSUMPTION_INDEX])
        if consumptions_per_hour.get(hour):
            consumptions_per_hour[hour].append(consumption)
        else:
            consumptions_per_hour[hour] = [consumption]

# we have a total of 365 consumptions for each hour




# output_file = open('hourly_consumption_temperature.csv', mode='w',
#                    encoding='utf-8')
# fieldnames = ['time', 'temperature', 'consumption']
# writer = csv.DictWriter(output_file, fieldnames=fieldnames)
# writer.writeheader()

