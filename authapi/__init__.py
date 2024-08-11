from redbot.core.bot import Red
from .authapi import AuthApi
import discord
from discord.ext import commands
from datetime import datetime
import requests

async def setup(bot: Red) -> None:
    await bot.add_cog(authapi(bot))
