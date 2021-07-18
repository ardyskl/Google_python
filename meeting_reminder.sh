#!/bin/bash

meeting_info=$(zenity --forms \
    --title="Meeting" --text 'Reminder information' \
    --add-calendar 'Date' --add-entry 'Title' \
    --add-entry 'Emails' \
    --forms-date-format='%d-%m-%y' \
    2>/dev/null)
    
echo $meeting_info

if [[ -n "$meeting_info" ]]; then
    python3 areas.py "$meeting_info"
fi
