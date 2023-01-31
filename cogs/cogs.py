from os import listdir
from discord.ext.commands import slash_command
from discord.ext import commands
from discord import Option
#from discord.errors import ExtensionAlreadyLoaded
from utils import Utils
class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.info = Utils.get_data()

    def getcogs(self, ctx):
        if ctx.interaction.user.id not in self.info['Owners']:
            return ["You are not an owner of the bot!"]
        cogs = []
        for fn in listdir("./cogs"):
            if fn.endswith(".py"):
                cogs.append(fn[:-3])
        return cogs

    @slash_command(description='Only the owners of the bot can run this command', guild_ids=[773950337303314518])
    async def cogs(self, ctx, action: Option(choices=["Load", "Unload", "Reload"]), cog: Option(autocomplete=getcogs)):
        if ctx.author.id not in self.info['Owners']:
            return
        if cog.lower() not in [f"{fn[:-3]}" for fn in listdir("./cogs")]:
            await ctx.respond("That cog doesn't exist!", ephemeral=True)
            return
        if action.lower() not in ["load", "unload", "reload"]:
            await ctx.respond("That action doesn't exist!", ephemeral=True)
            return
        try:
            if action == "Load":
                self.bot.load_extension(f"cogs.{cog}")
            elif action == "Unload":
                self.bot.unload_extension(f"cogs.{cog}")
            elif action == "Reload":
                self.bot.reload_extension(f"cogs.{cog}")
        except Exception as e:
            await ctx.respond(f"An error has occured!\n{e}")
            raise e
        await ctx.respond(f"{action}ed {cog}")

def setup(bot):
    bot.add_cog(Cogs(bot))