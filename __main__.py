import os
import hikari
import lightbulb
from lightbulb.ext import tasks
import sqlite3
import json
import asyncio
import random
from __init__ import WHITELIST

ServerList = WHITELIST["ServerList"]
UserList = WHITELIST["UserList"]
ChannelList={}
for _ in ServerList:
    ChannelList.update(ServerList[_]["Channels"])
ChannelList.update(UserList)
throttle = False
genList = []

EnabledGuilds = list(ServerList.keys())
with open("./EmmeDiscord/secrets/token") as f:
    _token = f.read().strip()
conn = sqlite3.connect('./data/ChatDatabase.db')
c = conn.cursor()
for _ in EnabledGuilds:
    c.execute("CREATE TABLE IF NOT EXISTS s"+str(_)+" (messageID INT PRIMARY KEY, channelID INT, username TEXT, content TEXT) WITHOUT ROWID")
    conn.commit()

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()

bot = lightbulb.BotApp(
    token=_token,
    intents=hikari.Intents.ALL_UNPRIVILEGED
    | hikari.Intents.MESSAGE_CONTENT,
    default_enabled_guilds=EnabledGuilds,
    owner_ids=<"Your USERID here!">)
    #task_running = False) attempt at adding a **kwargs to bot, unsuccessful
tasks.load(bot)

@bot.listen(hikari.GuildMessageCreateEvent) #Basic listen server. Stores any messages in a local SQL server, indexed by messageID
async def print_message(event):
    if str(event.content) == "None":
        return
    eventMessage = event.message
    messageContents = [eventMessage.guild_id, eventMessage.id, eventMessage.channel_id, eventMessage.author.username, event.content]
    c.execute("INSERT INTO s"+str(messageContents[0])+" (messageID,channelID,username,content) VALUES (?,?,?,?)", (messageContents[1],messageContents[2],messageContents[3],messageContents[4]))
    conn.commit()

    if "@<"YOUR BOT NAME">" in messageContents[4].lower() or ChannelList[messageContents[2]]["ResponseChance"] >= random.random():
        ChannelList[messageContents[2]]["Reply"] = True
        print("Reply set to true for "+str(messageContents[2]))

async def replyPacker(chID): #reply handler for channels, takes channel ID
    if ChannelList[chID]["Reply"] == False: #Checks if channel needs a response
        return
    c.execute("SELECT username, content FROM s"+str(ChannelList[chID]["Server"])+" WHERE channelID = "+str(chID)+" ORDER BY messageID DESC LIMIT 3") #Fetches context from sql server
    conversation = c.fetchall()
    conversation.reverse()
    print(conversation)
    conn = ""
    for _ in conversation:
        conn = (conn + _[0]+": "+_[1]+"<|endoftext|>")
    return ([chID,ChannelList[chID]["Name"]+" channel in server "+ServerList[ChannelList[chID]["Server"]]["Name"]+" - "+conn+"<YOUR BOT NAME HERE>: "]) #formats context for chatbot

@tasks.task(s=10, pass_app=True, auto_start=True)  #Every 10 seconds, check if replies need to be sent
async def launchHandlers(bot):
    global throttle
    if throttle == True:
        print("Throttle on, leaving task")
        return
    throttle = True
    coroPack = [replyPacker(_) for _ in ChannelList]
    results = await asyncio.gather(*coroPack)
    results = [i for i in results if i is not None]
    if not results:
        throttle = False
        print("task found no waiting replies")
        return
    print("Replies found")
    chans = []
    with open("input.txt", "r+") as f:
        f.truncate(0)
        for _ in results:
            chans.append(_[0])
            f.write(_[1])
            if _ != results[-1]:
                f.write("\n")
    
    #async with bot.rest.trigger_typing(*chans): #Does not accept *args, will need to get clever
    os.system("/home/lily/anaconda3/envs/gpt-neox/bin/python ./deepy.py generate.py -d configs 6bn.yml text_generation.yml")
    responses = []
    with open("output.txt", "r") as f:
        for _ in f:
            responses.append(json.loads(_))
    
    for _ in range(len(chans)):
        if responses[_]["text"] != None:
            if ChannelList[chans[_]]["Type"] == "Channel":
                await bot.rest.create_message(channel=chans[_], content=responses[_]["text"])
            elif ChannelList[chans[_]]["Type"] == "DM":
                channel = await bot.rest.create_dm_channel(chans[_])
                await channel.send(responses[_]["text"])
        ChannelList[chans[_]]["Reply"] = False
    throttle = False
    print("turning throttle off")

bot.run()
conn.close()
