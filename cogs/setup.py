from discord import Argument, Choice, Interaction
from discord.app_commands import command, describe
from discord.ext.commands import Bot, Cog

class Setup(Cog):
	def __init__(self, bot: Bot):
		self.bot = bot

	@command(name = "link", description = "Link global chat to a channel.")
	@Argument(
		name = "filter",
		description = "Enable or Disable profanity filter.",
		choices = [
			Choice(
				name = "Enable",
				value = True
			),
			Choice(
				name = "Disable",
				value = False
			)
		]
	)
	async def link(self, interaction: Interaction, filter: bool):
		if len(self.bot.database["config"].find({"_id": interaction.guild.id})) == 0:
			webhook_url = await interaction.channel.create_webhook(
				name = self.bot.user.name,
				avatar = self.bot.user.avatar,
				reason = "Linking channel to global chat."
			).
			await self.bot.database["config"].insert_one(
				{
					"_id": interaction.guild.id,
					"sync_channel": interaction.channel.id
				}
			)

async def setup(bot: Bot):
	await bot.add_cog(Setup(bot))