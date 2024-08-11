import random
from redbot.core import commands
import re
from typing import Match
import discord
from discord import Message
from datetime import datetime
import requests
intents = discord.Intents.all()

class authapi(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message) -> None:
        channel = message.channel

    async def checkplayer(ctx, nickname):
        # Замените на URL вашего API
        url = f"https://auth.spacestation14.com/api/query/name?name={nickname}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            player_name = data.get('userName', 'Имя не найдено')
            player_userid = data.get('userId', 'UID не найден')
            player_date = data.get('createdTime', 'Дата создания не найдена')

            date_obj = datetime.fromisoformat(player_date)
            formatted_date = date_obj.strftime('%d.%m.%Y %H:%M:%S')

            message = (f"Никнейм: `{player_name}`\n"
                       f"Userid: `{player_userid}`\n"
                       f"Дата создания аккаунта: `{formatted_date}`")

            await ctx.send(message)

        except requests.exceptions.HTTPError as err:
            await ctx.send(f"Ошибка при запросе API: {err}")
        except requests.exceptions.RequestException as err:
            await ctx.send(f"Ошибка соединения: {err}")
        except ValueError:
            await ctx.send("Ошибка при разборе ответа API (неправильный формат JSON)")
        except Exception as err:
            await ctx.send(f"Произошла ошибка: {err}")
