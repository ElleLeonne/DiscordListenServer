import os
import hikari
import lightbulb
from lightbulb.ext import tasks
import sqlite3
from . import ELLE_GUILD_ID, WHITELIST

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

conn = sqlite3.connect('./EmmeDiscord/ChatDatabase.db')
c = conn.cursor()

@tasks.task(m=1, pass_app=True, auto_start=True) #Every minute, send Meow to test channel
async def create_message(channel):
    print("Reply loop Task called.")
    #await bot.rest.create_message(channel=ELLE_GENERAL_CHANNEL, content="Meow")

@bot.listen(hikari.GuildMessageCreateEvent) #Basic listen server. Prints anything that is sent in any channel. 
async def print_message(event):
    if str(event.content) != "None":
        for srvr in WHITELIST:
            if srvr[0] == event.guild_id:
                srvrname = srvr[1]
                for chnl in srvr[3]:
                    if chnl[0] == event.channel_id:
                        sqline = "INSERT INTO '"+srvrname+"' (MessageID,Channel,User,Content) VALUES (?,?,?,?)"
                        c.execute(sqline, (int(event.message_id),chnl[1],str(event.author),str(event.content)))
                        conn.commit()
  
bot.run()

conn.close()
