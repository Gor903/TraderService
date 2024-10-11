#!/bin/bash

current_directory=`pwd`
if [ -d $current_directory/venv ]; then
    source $current_directory/venv/bin/activate
else
    python -m venv $current_directory/venv
    source $current_directory/venv/bin/activate
    pip install --upgrade pip
    pip install -r $current_directory/requirements.txt
fi
echo "Start"
python tg_bot.py &
while [[ 1 ]]; do
    python tg_sender.py `./crypto-trader`
    echo "Restart"
done
echo "Finish"
