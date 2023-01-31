from discord import Intents, Status, Activity, ActivityType
from discord.ext.bridge import Bot
from utils import Utils
data = Utils.get_data()
intents = Intents(guilds=True, guild_messages=True)
#intents.message_content = True #Uncomment this if you use prefixed command that are not mentions
bot = Bot(intents=intents, command_prefix=data['Prefix'], status=Status.dnd, activity=Activity(type=ActivityType.playing, name="you (prefix: @mention)"), debug_guilds=[773950337303314518])
bot.load_extensions("cogs") #Loads all cogs in the cogs folder
@bot.listen()
async def on_connect():
    print('Connected to Discord!')

@bot.listen()
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('------')
    #await bot.sync_commands()

bot.run(data['Token'])