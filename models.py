import csv
import numpy as np
from sklearn.linear_model import LinearRegression

consumptions_and_temperatures_per_hour = {}
with open('prepared_data.csv', mode='r') as file:
    reader = csv.reader(file, delimiter=';')
    header = next(reader)
    for raw in reader:
        if not raw:
            continue
        hour = int(raw[0])
        consumption = int(raw[1])
        temperature = float(raw[2])
        if consumptions_and_temperatures_per_hour.get(hour):
            consumptions_and_temperatures_per_hour[hour]['consumptions'].append(consumption)
            consumptions_and_temperatures_per_hour[hour]['temperatures'].append(temperature)
        else:
            consumptions_and_temperatures_per_hour[hour] = {
                'consumptions': [consumption],
                'temperatures': [temperature]
            }

model_params = {}
for hour in consumptions_and_temperatures_per_hour.keys():
    consumptions = np.array(consumptions_and_temperatures_per_hour[hour]['consumptions'])
    temperatures = np.array(consumptions_and_temperatures_per_hour[hour]['temperatures']).reshape((-1, 1))
    model = LinearRegression().fit(temperatures, consumptions)
    params = {
        'intercept': model.intercept_,
        'slope': model.coef_,
        'R2': model.score(temperatures, consumptions)
    }
    model_params[hour] = params


with open('models.csv', mode='w') as export_file:
    writer = csv.writer(export_file, delimiter=';')
    header = ['hour', 'R2', 'intercept', 'slope']
    writer.writerow(header)
    for hour in model_params.keys():
        R2 = model_params[hour]['R2']
        intercept = model_params[hour]['intercept']
        slope = model_params[hour]['slope'][0]
        writer.writerow([hour, R2, intercept, slope])
