# Project Name

## Description
CryptoTrader is an automated trading bot that allows you to trade cryptocurrencies effortlessly. Using a Telegram bot interface, you can set your trading options and preferences, and the CryptoTrader bot will execute buy and sell orders based on your specified settings.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Gor903/TraderService.git
   cd TraderService

## Usage
1. **Environment file**

    Before running the application, you need to set up your environment variables. Create a `.env` file in the root of your project directory with the following format:

    **Example .env**

        BOT_TOKEN="your telegram bot token here"
        USER_ID="your telegram user id"

2. **Running the application**:

    You just have to activate script.sh file.
    ```bash
    bash script.sh

3. **Configuration**:

    After running the application, open your telegram bot and use the following commands.

    - **/new [Coin name]** 
    - **/delete [Coin name]**
    - **/change [Coin name] [Key] [Value]**
    - **/restart**
    - **/forcestop**

    Using this command you will change Trades.txt file.
    **Important:** Dont change file in other way!!!

    **Example Trades.txt**
        
        {
            "Trades": [
                    {
                        "coin": BTC,
                        "shortBuy": 53000,
                        "shortSell": 53100,
                        "longBuy": 51000,
                        "longSell": 55000,
                        "qty": "100"
                    }
                ],  
            "count": 1
        }
        



## Important Note
**crypto-trader** is not the original file. Please contact me to get the correct version.

## Contact
- **Email:** gorbeglaryan07@gmail.com
- **Telegram:** Gor903
