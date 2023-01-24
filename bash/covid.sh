#!/bin/bash
#Covid Information

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSP=$(echo $DATA | jq '.[0].hospitalized')
TODAY=$(date)

echo "On $TODAY, There were $POSITIVE positive COVID cases, $NEGATIVE negative COVID cases, $DEATHS deaths and $HOSP hospitalized."

