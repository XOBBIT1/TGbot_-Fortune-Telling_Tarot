import asyncio
import aiohttp
import bs4

from core.parsers.parser_descriptions import descriptions
from core.parsers.parser_harness import card_harnes
from core.parsers.parser_img import card_images
from settings.bd.session_to_postgres import create_dbsession

db_session = create_dbsession()


async def get_card_data(url):
    async with aiohttp.ClientSession() as session:
        res = {}
        cards_urls = []
        response = await session.get(url)
        soup = bs4.BeautifulSoup(await response.text(), "lxml")
        taro_cards = soup.find_all("div", class_="col-lg-2 col-md-3 col-sm-3 col-6")
        for card in taro_cards:
            taro_url = "https://astrometa.ru/" + card.find("a").get("href").strip()
            taro_name = card.find("a").get("title").strip()
            res.update(card_name=taro_name,
                       card_url=taro_url)
            cards_urls.append(taro_url)

            # await card_harnes(cards_urls, res)
            # await descriptions(cards_urls)
            await card_images(cards_urls)
            print("Done")


async def gather_data():
    await asyncio.gather(asyncio.create_task(get_card_data(
        "https://astrometa.ru/znachenie-taro/")))


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(gather_data())
