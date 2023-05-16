import random
from bs4 import BeautifulSoup
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import parser
bot = Bot(token="6287055552:AAGf6FM3-z3prT0NWwHFLF7VgEEH-8hEBF4")
dp = Dispatcher(bot)
@dp.message_handler(commands=["start"])
async def cmd_start(msg: types.Message) -> None:
    await msg.answer("Добрый день, для поиска лекарств введите комманду /search")

    @dp.message_handler(commands=["search"])
    async def cmd_search(msg: types.Message) -> None:
        await msg.answer("Введите названия лекарства")

        @dp.message_handler()
        async def cmd_search(msg: types.Message) -> None:
            strmsg= str(msg.text)
            d = dict()
            k = int()
            text = str()
            d = str()
            d = strmsg
            url = 'https://omsk.vapteke.ru/search?s=' + (d)
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            soup.get_text(strip=True)
            mydivs = soup.find_all("a", {"class": "media-heading init-loader"})
            mydivs2 = soup.find_all("div", {"class": "m-result-price flex-wide"})
            result = str()
            for data in mydivs:
                item_url = str(data.get("href"))
                text = data.text.strip()
                text = text.replace("\n", " ")
                text = text.replace("\r", " ")
                result+= ("\n" + "🟢 " + text + "\n" +"Ссылка на страницу с аптеками где есть данный товар" + " " + item_url + "\n" )
            await msg.answer(result)


if __name__ == "__main__":
    executor.start_polling(dp)