import re

from discord import Message
from discord import SyncWebhook
from discord.ext.commands import Cog

from typing import List

def _clean_message(message: str) -> str:
    return re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', message)

class Sync(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener("on_message")
    async def message_sync(self, message: Message):
        if message.author.bot: return
        current_guild_config = await self.bot.database["config"].find_one(
            {
                "_id": message.guild.id
            }
        )
        if current_guild_config.get("linked") and message.channel.id == current_guild_config.get("sync_channel"):
            guild_config_list: List[dict] = self.bot.database["config"].find(
                {
                    "linked": True
                }
            )
            message_content = _clean_message(message.content)
            message_data = {
                "_id": message.id,
                "message_author": {
                    "id": message.author.id,
                    "username": message.author.display_name,
                    "name": message.author.name,
                    "avatar_icon": message.author.display_avatar.url
                },
                "content": message.content,
                "guild_messages": {
                    f"{message.guild.id}": message.id
                },
                "attachments": message.attachments
            }
            for guild in guild_config_list:
                webhook = SyncWebhook.from_url(guild.get("sync_webhook"))
                message = webhook.send(
                    username = message.author.name,
                    avatar_url = message.author.display_avatar.url,
                    content = message_content,
                    files = message.attachments,
                    allowed_mentions = False
                )
                message_data["guild_messages"][f"{guild.id}"] = message.id

            await self.bot.database["messages"].insert_one(message_data)

async def setup(bot):
    await bot.add_cog(Sync(bot))