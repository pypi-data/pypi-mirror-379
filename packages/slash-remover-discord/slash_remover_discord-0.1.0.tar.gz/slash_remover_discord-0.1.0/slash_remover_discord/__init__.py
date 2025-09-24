import discord

class SlashRemover(discord.Client):
    def __init__(self, token: str):
        intents = discord.Intents.default()
        intents.guilds = True
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)
        self.token = token

    async def on_ready(self):
        print(f"SlashRemover > Logged in as {self.user}")

        # Clear all global commands
        await self.tree.sync()
        for command in await self.http.get_global_commands(self.user.id):
            await self.http.delete_global_command(self.user.id, command["id"])
            print(f"SlashRemover > Deleted global command: {command['name']}")

        # Clear all guild commands
        for guild in self.guilds:
            for command in await self.http.get_guild_commands(self.user.id, guild.id):
                await self.http.delete_guild_command(self.user.id, guild.id, command["id"])
                print(f"SlashRemover > Deleted guild command: {command['name']}")

        print("SlashRemover > All commands cleared")

    def run_remover(self):
        self.run(self.token)


def main():
    token = input("Enter your Discord bot token: ").strip()
    bot = SlashRemover(token)
    bot.run_remover()