import aiohttp
import bs4

from core.services.queries import writing_data
from settings.bd.models import Cards


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

        await writing_data(data, Cards)
