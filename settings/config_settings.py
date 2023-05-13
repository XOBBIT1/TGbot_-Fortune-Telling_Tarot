import os
import dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

token = os.environ['TOKEN']

# bd_settings
host = os.environ['HOST']
user = os.environ['USER']
password = os.environ['PASSWORD']
db_name = os.environ['DB_NAME']
port = os.environ["PORT"]

common_phrases = [
    '<b>Подбираем правельную формулировку</b> {}',
    '<b>Обдумываем ваше будущее</b>{}',
    '<b>Подбираем правильную формулировку</b> {}',
    '<b>Хм.....</b> {}',
    '<b>Всё не так однозначно. Обдумываем...</b> {}',
    '<b>Чувствую интересную ауру...</b> {}'
]

emojis = ["🔮", "꒰ঌ🕯໒꒱", "🎴", "🀥", "🪬", "☪️"]
