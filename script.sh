#!/bin/bash

current_directory=`pwd`
trades_configuration="TradesConfiguration.txt"
trades_history="TradesHistory.txt"
last_trades="LastTrades.txt"
if [ -d $current_directory/venv ]; then
    source $current_directory/venv/bin/activate
else
    python -m venv $current_directory/venv
    source $current_directory/venv/bin/activate
    pip install --upgrade pip
    pip install -r $current_directory/requirements.txt
fi
echo "Start"
if [[ ! -e $trades_configuration ]] ;then
    echo "{\"Trades\" : [], \"count\": 0}" > $trades_configuration
fi
if [[ ! -e $trades_history ]] ;then
    touch $trades_history
fi
if [[ ! -e $last_trades ]] ;then
    echo {} > $last_trades
fi
python tg_bot.py &
while [[ 1 ]]; do
    python tg_sender.py `./crypto-trader`
    echo "Restart"
done
echo "Finish"
