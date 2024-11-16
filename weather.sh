#! /bin/bash

wget -O data2/timestamps/weather/`date +"%Y%m%d_%H%M%S.json"` https://prodapi.metweb.ie/observations/athenry/today
