# COWIN_SLOT_ALERTS
This repository contains jupyter notebook which can send alerts whenever the slot's are available in provided center id

Dependecies:
pandas
pip -install pandas


Once you get your district id, cell no 3 and 4 can be commented out with hardcoding district id in next cell

The above notebook can be edited and scheduled with a cron job or can be run inside a ksh script

nohup ./schedule_notebook.ksh &


To get sms alerts, create an account on sinch and get key and password fron the dashboard

This is just a template sript I used to get alerts for my nearest center 

Reference: https://apisetu.gov.in/public/marketplace/api/cowin
