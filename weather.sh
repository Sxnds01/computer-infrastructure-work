#! /bin/bash

echo "Fetching weather data..."
wget -O data2/timestamps/weather/`date +"%Y%m%d_%H%M%S.json"` https://prodapi.metweb.ie/observations/athenry/today

echo "Processing data and generating trend graph..."
./combine_and_plot.py