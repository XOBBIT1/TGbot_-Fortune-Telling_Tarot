import aiohttp
import bs4

from core.services.queries import writing_data
from settings.bd.models import Images


async def card_images(card_urls: list):
    data = {}
    async with aiohttp.ClientSession() as session:
        for card_taro_url in card_urls:
            response = await session.get(card_taro_url)
            soup = bs4.BeautifulSoup(await response.text(), "lxml")
            images = soup.find_all("div", class_="zodiac-pic text-center mb-3")
            for img in images:
                card_img = img.find("img").get("src")
                data.update(img_url="https://astrometa.ru"+card_img)

        await writing_data(data, Images)
