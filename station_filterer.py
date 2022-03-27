import csv

file = open('data/SE2018.csv', mode='r', encoding='utf-8', newline='')
reader = csv.reader(file)

LON_MAX = 8.18  # right french border
LON_MIN = -4.71  # left french border
LAT_MAX = 51.08  # north border
LAT_MIN = 42.467  # south border

# excluding stations not in france(metropolitan)

header = next(reader)
print(header)
all_stations = {}
couner_bef = 0
counter_after = 0

output = open('filtered_stations.csv', mode='w', encoding='utf-8')
writer = csv.writer(output, delimiter=';')
writer.writerow(header)
for raw in reader:
    if len(raw) != 0:
        couner_bef += 1
        if LAT_MIN < float(raw[1]) < LAT_MAX:
            if LON_MIN < float(raw[2]) < LON_MAX:
                counter_after += 1
                writer.writerow(raw)

output.close()
print(couner_bef, counter_after)
