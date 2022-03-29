import csv

# for consumption data
CONSUMPTION_INDEX = 4
DATE_INDEX = 2
HOUR_INDEX = 3

# for weather data
T_INDEX = -2
C_DATE_INDEX = 4

# consumption data transformation
consumptions_per_hour = {}

with open('data/eCO2mix_RTE_Annuel-Definitif_2018.csv', mode='r') as file:
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


# now let's deal with temperatures (hard level)
with open('filtered_stations.csv', mode='r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    temperatures_per_hour = {}
    for raw in reader:
        if not raw:
            continue
        datetime = raw[C_DATE_INDEX]
        hour_value = datetime.split(' ')[1]
        minutes = hour_value.split(':')[1]
        if minutes == '00':
            try:
                temperature = float(raw[T_INDEX])
            except Exception:
                continue
            date = datetime.split(' ')[0]
            hour = int(hour_value.split(':')[0])
            if temperatures_per_hour.get(hour):
                if temperatures_per_hour[hour].get(date):
                    temperatures_per_hour[hour][date].append(temperature)
                else:
                    temperatures_per_hour[hour][date] = [temperature]
            else:
                temperatures_per_hour[hour] = {date: [temperature]}


# transforming temperatures to average per day
for hour in temperatures_per_hour.keys():
    for date in temperatures_per_hour[hour].keys():
        temperatures = temperatures_per_hour[hour][date]
        temperatures_per_hour[hour][date] = sum(temperatures)/len(temperatures)

# merging two dicts
consumption_temperature_per_hour = {}
for hour in consumptions_per_hour.keys():
    consumptions = consumptions_per_hour[hour]
    averages = []
    for temperature in temperatures_per_hour[hour].values():
        averages.append(temperature)
    averages_and_consumptions = {
        'consumptions': consumptions,
        'avg_temperatures': averages
    }
    consumption_temperature_per_hour[hour] = averages_and_consumptions

print(consumption_temperature_per_hour)

# importing merge results in csv
with open('prepared_data.csv', mode='w') as export_file:
    writer = csv.writer(export_file, delimiter=';')
    header = ['hour', 'consumption', 'temperature']
    for hour in consumption_temperature_per_hour.keys():
        temperatures_and_consumptions = consumption_temperature_per_hour[hour]
        temperatures = temperatures_and_consumptions['avg_temperatures']
        consumptions = temperatures_and_consumptions['consumptions']
        for k in range(len(consumptions)):
            raw = [hour, consumptions[k], temperatures[k]]
            writer.writerow(raw)
