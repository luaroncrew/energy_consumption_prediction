# energy_consumption_prediction

Eliot Veyret, Makarov Kirill

to make this predictive model we used open-data sources for 2018 year

temperature data taken from: 
https://meteonet.umr-cnrm.fr/dataset/data/SE/ground_stations/

this data is verified, we compared it with other archive data sources, like this one.
https://www.infoclimat.fr/observations-meteo/archives/21/juin/2018/grenoble-le-versoud/07487.html

energy consumption data from:
https://www.rte-france.com/en/eco2mix/download-indicators





What was the working plan?

* find a data for weather conditions and energy consumption
* merge all the data in one csv file (JOIN) 
* make a mathematical model for consumption based on this data
* some frontend development: a very simple interface on R to allow people to interact with model


## ETL
we have 43,3 millions lines of temperature data so there were some steps of transformation:
* make sure this is only french stations. Solution:
    * find borders long and lat values
    * exclude any line when coordinates are not in these ranges
* filter by 15-minutes step ranges to then join with RTE (company name) data
* find average temperatures from all the stations for every 15 minute step
* create a new csv file containing on each line average consumption and average temperature in France


## Analysis

## Useful information
* after filtering all the stations by an altitude and longitude, only 39,58M out of 43,3M are valid for analysis

