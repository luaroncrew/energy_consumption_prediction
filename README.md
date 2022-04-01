# energy_consumption_prediction

Eliot Veyret, Makarov Kirill

## DATA

to make this predictive model we used open-data sources for year 2018

temperature data taken from METEOFRANCE:
https://meteonet.umr-cnrm.fr/dataset/data/SE/ground_stations/

this data is verified, we compared it with other weather archive data sources, like this one.
https://www.infoclimat.fr/observations-meteo/archives/21/juin/2018/grenoble-le-versoud/07487.html

energy consumption data from:
https://www.rte-france.com/en/eco2mix/download-indicators





What was the working plan?

* find a data for weather conditions and energy consumption
* merge all the data in one csv file (JOIN) 
* make a mathematical model for each hour consumption based on this data
* some frontend development: a very simple interface on R to allow people to interact with model


## ETL
we have 43,3 millions lines of temperature data so there were some steps of transformation:
* make sure this is only french stations. Solution:
    * find borders long and lat values
    * exclude any line when coordinates are not in these ranges
* make a consumption dictionnary like 
   ```Python consumptions = {
      '1h00': [12321,123213,123,12,213213....,213123], # len(consumptions['1h00']) will be = 365 (for each day)
      '2h00': [123213,123213,21312....,123123], # same as for 1h00
      ...
      '23h00' : [123213,123213,21312....,123123] # same as for 1h00
   }
   ```
* make a dictionnary like 
   ```python
   temperatures = {
      '1h00': {
         '2018/01/01': [32, 34, 32, ...., 21, 32], # data from all stations in france.
         '2018/01/02': [34, 35, ...., 36, 35, 12],
         ....
         '2018/12/31': [34, 35, ....,  36, 35, 12]
      },
      '2h00': {
         '2018/01/01': [32, 34, 32, ...., 21, 32], # data from all stations in france.
         '2018/01/02': [34, 35, ...., 36, 35, 12],
         ....
         '2018/12/31': [34, 35, ....,  36, 35, 12]
         },
      ... ,
      '23h00' : {
         '2018/01/01': [32, 34, 32, ...., 21, 32], # data from all stations in france.
         '2018/01/02': [34, 35, ...., 36, 35, 12],
         ....
         '2018/12/31': [34, 35, ....,  36, 35, 12]
         }
      
  }
  ```
* merge these data to get something like
  ```python
       consumption_temperature_per_hour = {
      0: {'cons' = [12,123,213,213,...,213],
         'temp' = [1123,213,21,213,..., 213]
        },
      1: {'cons' = [12,123,213,213,...,213],
         'temp' = [1123,213,21,213,..., 213]
        },
      ...
      23: {'cons' = [12,123,213,213,...,213],
         'temp' = [1123,213,21,213,..., 213]
        }
      }
  ```
* export this data in csv-file

## Analysis
* we decided to make a model for each hour. So using excel for this kind of work would not be fast and interesting. To make all these 24 models on Python we used a       package called sklern and it's class `sklern.linear_model.LinearRegression` which is a very easy thing to use.
* here is the most imortant piece of code:
  ```Python
  model_params = {}
  for hour in consumptions_and_temperatures_per_hour.keys():
      consumptions = np.array(consumptions_and_temperatures_per_hour[hour]['consumptions'])
      temperatures = np.array(consumptions_and_temperatures_per_hour[hour]['temperatures']).reshape((-1, 1))
      model = LinearRegression().fit(temperatures, consumptions) # defining regression with x and y params
      params = {
          'intercept': model.intercept_,
          'slope': model.coef_,
          'R2': model.score(temperatures, consumptions)
      }
      model_params[hour] = params # collecting slope, intercept and R2 for each hour
  ```
* then we export model_params in CSV to make it possible to work in R and Shiny

## Frontend
Our frontend part is powered by R and Shiny package. 

## Useful information
* after filtering all the stations by an altitude and longitude, only 39,58M lines of data out of 43,3M are valid for analysis (these were stations in Corse)

