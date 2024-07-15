from discord import Interaction
from discord.app_commands import command, describe
from discord.ext.commands import Cog

class Setup(Cog):
	def __init__(self, bot):
		self.bot = bot

async def setup(bot):
	await bot.add_cog(Setup(bot))