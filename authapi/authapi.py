import discord
from discord.ext import commands
from datetime import datetime
import requests

log = logging.getLogger("red.wizard-cogs.authapi")

class AuthApi(commands.Cog):
    def __init__(self, bot: bot.Red) -> None:
        self.config = Config.get_conf(self, identifier=5645456348)

# Выше копипаст с кога оффов. Кроме импорта.
    async def checkplayer(ctx, nickname):

        url = f"https://auth.spacestation14.com/api/query/name?name={nickname}" #API оффов на проверку никнейма

        try:
            response = requests.get(url) # url
            response.raise_for_status()  # Проверяем на ошибки HTTP
            data = response.json()  # Парсим JSON-ответ

            player_name = data.get('userName', 'Имя не найдено')
            player_userid = data.get('userId', 'UID не найден')
            player_date = data.get('createdTime', 'Дата создания не найдена')

            date_obj = datetime.fromisoformat(player_date) # Форматируем в читаемый пользователем формат
            formatted_date = date_obj.strftime('%d.%m.%Y %H:%M:%S')

            message = (f"Никнейм: `{player_name}`\n"
                       f"Userid: `{player_userid}`\n"
                       f"Дата создания аккаунта: `{formatted_date}`")

            await ctx.send(message)

        except requests.exceptions.HTTPError as err: #Ошибки.
            await ctx.send(f"Ошибка при запросе API: {err}")
        except requests.exceptions.RequestException as err:
            await ctx.send(f"Ошибка соединения: {err}")
        except ValueError:
            await ctx.send("Ошибка при разборе ответа API (неправильный формат JSON)")
        except Exception as err:
            await ctx.send(f"Произошла ошибка: {err}")

# Копипаст продолжается

class StatusException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

        self.message = message

T = TypeVar("T")

def remove_list_elems(l: List[T], pred: Callable[[T], bool]) -> None:
    for i in list(filter(pred, l)):
        l.remove(i)
