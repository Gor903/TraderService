import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
from dotenv import load_dotenv
import os, subprocess, signal, json

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# utils.py
def message_reader(message: str) -> list:
    keys = [
        "coin",
        "value_to_change",
        "value",
    ]
    return {a[0]: a[1] for a in zip(keys, message.split()[1:])}


def get_trades():
    with open("TradesConfiguration.txt", "r") as file:
        return json.load(file)


def save_trades(data):
    with open("TradesConfiguration.txt", "w") as file:
        json.dump(data, file)


def stop_bot():
    pid = subprocess.run(["pgrep", "crypto-trader"], stdout=subprocess.PIPE, text=True).stdout[
        :-1
    ]
    os.kill(int(pid), signal.SIGTERM)


@dp.message(Command(commands=["new"]))
async def new(message: types.Message):
    new_data = {
        "coin": message.text.split()[1],
        "shortBuy": 0,
        "shortSell": 0,
        "longBuy": 0,
        "longSell": 0,
        "qty": "0"
    }
    data = get_trades()
    data["Trades"] += [new_data]
    data["count"] += 1
    save_trades(data)
    stop_bot()
    await message.answer("Done")


@dp.message(Command(commands=["change"]))
async def change(message: types.Message):
    args = message_reader(message.text)
    data = get_trades()
    index = -1
    for i, v in enumerate(data["Trades"]):
        if v["coin"] == args["coin"]:
            index = i
            break
    data["Trades"][index][args["value_to_change"]] = float(args["value"]) if args["value_to_change"] != "qty" else args["value"]
    save_trades(data)
    stop_bot()
    await message.answer("Done")


@dp.message(Command(commands=["delete"]))
async def delete(message: types.Message):
    data = get_trades()
    coin = message.text.split()[1]
    data_to_delete = None
    for i, v in enumerate(data["Trades"]):
        if v["coin"] == coin:
            data_to_delete = v
            break
    data["Trades"].remove(data_to_delete)
    data["count"] -= 1
    save_trades(data)
    stop_bot()
    await message.answer("Done")


@dp.message(Command(commands=["restart"]))
async def stop_tradeing(message: types.Message):
    stop_bot()
    await message.answer("Done")


@dp.message(Command(commands=["forcestop"]))
async def force_stop_tradeing(message: types.Message):
    data = get_trades()
    data["Trades"] = []
    data["count"] = 0
    save_trades(data)
    stop_bot()
    await message.answer("Done")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
