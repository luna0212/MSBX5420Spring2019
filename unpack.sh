#!/usr/bin/env bash

for i in structured-2018-01-14-neworleans.tar.gz structured-2018-03-11-atlanta.tar.gz structured-2018-04-01-birmingham.tar.gz structured-2018-04-08-proleague1.tar.gz structured-2018-04-19-relegation.tar.gz structured-2018-04-22-seattle.tar.gz structured-2018-06-17-anaheim.tar.gz structured-2018-07-29-proleague2.tar.gz structured-2018-08-19-champs.tar.gz
do
    tar zxvf $i -C ~/work/week7
done

echo All done
