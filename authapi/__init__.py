from .authapi import authapi


async def setup(bot) -> None:
    await bot.add_cog(authapi(bot))
