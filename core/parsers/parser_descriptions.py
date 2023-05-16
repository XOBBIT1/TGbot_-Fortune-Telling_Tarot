import aiohttp
import bs4

from core.services.queries import writing_data
from settings.bd.models import Descriptions


async def descriptions(card_urls: list):
    data = {}
    async with aiohttp.ClientSession() as session:
        for card_taro_url in card_urls:
            response = await session.get(card_taro_url)
            soup = bs4.BeautifulSoup(await response.text(), "lxml")
            love_description = soup.find_all("p")[2]
            work_description = soup.find_all("p")[4]
            issue_description = soup.find_all("p")[6]
            money_description = soup.find_all("p")[8]
            health_description = soup.find_all("p")[10]
            spirit_description = soup.find_all("p")[12]
            data.update(
                love_description=love_description.text.strip(),
                work_description=work_description.text.strip(),
                issue_description=issue_description.text.strip(),
                money_description=money_description.text.strip(),
                health_description=health_description.text.strip(),
                spirit_description=spirit_description.text.strip()
            )

        await writing_data(data, Descriptions)

