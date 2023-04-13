import os
import hikari
import lightbulb
from lightbulb.ext import tasks
import sqlite3
import asyncio
import random
from config import config
from generate import generate_response
from utils.data_utils import clean, search, check

ServerList = config.whitelist["ServerList"]
UserList = config.whitelist["UserList"]
ChannelList={}
for _ in ServerList:
    ChannelList.update(ServerList[_]["Channels"])
ChannelList.update(UserList)
throttle = False
genList = []

EnabledGuilds = ServerList.keys()
with open("./secrets/token") as f:
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

def create_bot() -> lightbulb.BotApp:
    bot = lightbulb.BotApp(
        token=_token,
        intents=hikari.Intents.ALL_UNPRIVILEGED
        | hikari.Intents.MESSAGE_CONTENT,
        default_enabled_guilds=EnabledGuilds, #[XXXXX]  #My private server only, for testing
        owner_ids=[XXXXXX])
    bot.load_extensions_from("./commands")
    tasks.load(bot)
    return bot
bot = create_bot()

def get_response(list): #Results = [ChannelID, Context, Chat History, Username List, server #]
    channel_id, contxt, chat_history, username_list, server_num = list
    response = generate_response(chat_history, context=contxt, temperature=config.temperature, length_penalty=config.length_penalty)
    if check(response, username_list): #Check if response contains a username w/ colon from the prompt. May be too repetitive.
        response = min((response.split(target, 1)[0] for target in username_list if target in response), key=len).strip()
    response = response.split('\n\n', 1)[0] #Nix multi-line responses.
    return clean(response.strip("</s>"))

@bot.listen(hikari.GuildMessageCreateEvent) #Basic listen server. Stores any messages in a local SQL server, indexed by messageID
async def print_message(event):
    if str(event.content) == "None":
        return
    eventMessage = event.message
    reply = eventMessage.referenced_message
    messageContents = [eventMessage.guild_id, eventMessage.id, eventMessage.channel_id, eventMessage.author.username, event.content]
    c.execute("INSERT INTO s"+str(messageContents[0])+" (messageID,channelID,username,content) VALUES (?,?,?,?)", (messageContents[1],messageContents[2],messageContents[3],messageContents[4]))
    conn.commit()
    #Check to see if channel needs a response. Naive reply checker.
    if (search(messageContents[4],["@[Bot]#XXXX", "[Bot]"]) or ChannelList[messageContents[2]]["ResponseChance"] >= random.random() or (reply is not None and reply.author.username == "[Bot]")) and throttle == False:
        ChannelList[messageContents[2]]["Reply"] = True
        print("Reply set to true for "+str(messageContents[2]))

async def replyPacker(chID, ctxWindow): #reply handler for channels, takes channel ID
    if ChannelList[chID]["Reply"] == False: #Checks if channel needs a response
        return
    #Fetch chat history from sql database.
    server = ChannelList[chID]["Server"]
    c.execute("SELECT username, content FROM s"+str(server)+" WHERE channelID = "+str(chID)+" ORDER BY messageID DESC LIMIT "+str(ctxWindow)) #Fetches context from sql server
    conversation = c.fetchall()
    #Puts chats in chronological order
    conversation.reverse() 
    #Generate userList for repetetive text bandaid
    userList = [t[0]+":" for t in conversation]
    #Merge list of tuples into string, and adds index.
    conversation = " ".join(['<{}>{}: {}'.format(len(conversation)-i, t[0], clean(t[1])) for i, t in enumerate(conversation)])
    #Context string for bot
    context = "Platform: Discord, Server: "+ServerList[ChannelList[chID]["Server"]]["Name"]+", Channel: "+ChannelList[chID]["Name"]
    return [chID, context, conversation, userList, server] #All info req'd to gen response & send reply.

@tasks.task(s=15, pass_app=True, auto_start=True)  #Every 10 seconds, check if replies need to be sent
async def launchHandlers(bot):
    global throttle
    if throttle == True:
        print("Throttle on, leaving task")
        return
    throttle = True
    coroPack = [replyPacker(_, config.context_window) for _ in ChannelList]
    results = await asyncio.gather(*coroPack)
    results = [i for i in results if i is not None]
    if not results:
        throttle = False
        print("task found no waiting replies")
        return
    print("Replies found")
    for _ in results:
        channel_id = _[0]
        async with bot.rest.trigger_typing(channel_id): #Results = [ChannelID, Context, Chat History, Username List, server #]
            response = get_response(_)
            if not response:
                throttle = False
                print("response was null, turning throttle off")
            elif ChannelList[channel_id]["Type"] == "Channel":
                await bot.rest.create_message(channel=channel_id, content=response)
            elif ChannelList[channel_id]["Type"] == "DM":
                channel = await bot.rest.create_dm_channel(channel_id)
                await channel.send(response)
            ChannelList[channel_id]["Reply"] = False
    throttle = False
    print("all replies checked. turning throttle off")

bot.run()
conn.close()
