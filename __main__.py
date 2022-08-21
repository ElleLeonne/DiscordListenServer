import os
import hikari
import lightbulb
from lightbulb.ext import tasks
from . import ELLE_GUILD_ID, ELLE_GENERAL_CHANNEL

with open("./EmmeDiscord/secrets/token") as f:
    _token = f.read().strip()

bot = lightbulb.BotApp(
    token=_token,
    default_enabled_guilds=ELLE_GUILD_ID
)
tasks.load(bot)

#bot.load_extensions_from("./EmmeDiscord/extensions")

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()

"""
@tasks.task(m=1, pass_app=True, auto_start=True) #Every minute, send Meow to test channel
async def create_message():
    channel = await bot.rest.fetch_channel(ELLE_GENERAL_CHANNEL)
    await channel.send("Meow")
"""
@tasks.task(m=1, pass_app=True, auto_start=True) #Every minute, send Meow to test channel
async def create_message(channel):
    print("Reply loop Task called.")
    await bot.rest.create_message(channel=ELLE_GENERAL_CHANNEL, content="Meow")

@bot.listen(hikari.GuildMessageCreateEvent) #Basic listen server. Prints anything that is sent in any channel. 
async def print_message(event):
    print(str(event.guild_id)+" in channel "+str(event.channel_id))
    print(str(event.author).rsplit('#')[0]+": "+str(event.content))


bot.run()