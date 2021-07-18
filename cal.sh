#!/bin/bash

if zenity --calendar \
--title="Select a date" \
--text="Click on a date to select that date." \
--calendar-date-format='%d-%m-%y' \
--day=16 --month=7 --year=2021
  then echo $?
  else echo "No date selected"
fi
