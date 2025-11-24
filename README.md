# channel-sync

[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?&logo=discord&logoColor=white)](https://discord.gg/YwC6VpEPfq) [![CodeQL](https://github.com/Uwitz/channel-sync/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/Uwitz/channel-sync/actions/workflows/github-code-scanning/codeql)

A discord bot (with modular code) that allows you to sync channel messages across multiple discord servers.
## Installation
If you don't have `uv` installed:
```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```
```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Install dependencies with `uv`:
```
uv sync
```
## Setup
1. `.env` should contain the `TOKEN` variable.
2. You may drop the files in `cogs` your bot's cog folder. (OPTIONAL)
3. If you are using the cog version ensure you have `motor_asyncio` client in `self.bot.database` attribute as `AsyncIOMotorClient` classtype.

After setup, you can use `uv` to run the bot:
```bash
uv run main.py
```
