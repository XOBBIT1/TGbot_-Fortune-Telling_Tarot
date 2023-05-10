import asyncio
import aiohttp
import bs4
from my_settings.bd.session_to_postgres import create_dbsession
from my_settings.bd.models import Cards

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
                       card_url=taro_url, )
            cards_urls.append(taro_url)

            await card_harnes(cards_urls, res)


async def card_harnes(card_urls: list, data: dict):
    async with aiohttp.ClientSession() as session:
        for card_taro_url in card_urls:
            response = await session.get(card_taro_url)
            soup = bs4.BeautifulSoup(await response.text(), "lxml")
            descriptions = soup.find_all("p")[0]
            cards = soup.find_all("div", class_="taro-cat")
            for cards_data in cards:
                harnes = cards_data.find("a")
                data.update(harness=harnes.text)
            data.update(card_description=descriptions.text.strip())

        await writing_data(data)


async def writing_data(data: dict):
    db_session.add(Cards(**data))
    db_session.commit()
    db_session.close()

    print("Done")


async def gather_data():
    await asyncio.gather(asyncio.create_task(get_card_data(
        "https://astrometa.ru/znachenie-taro/")))


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(gather_data())
