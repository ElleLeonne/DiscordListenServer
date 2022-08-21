import hikari
import lightbulb
from lightbulb.ext import tasks


bot = lightbulb.BotApp(
    token="",
    default_enabled_guilds=(744554485350924408)
)
tasks.load(bot)


@tasks.task(m=1, pass_app=True, auto_start=True) #Every 1 minute, run the task
async def create_message(channel):
    print("Reply loop Task called.") #print Task to terminal
    await bot.rest.create_message(channel=744554485350924411, content="Meow") #send message to test server


@bot.listen(hikari.GuildMessageCreateEvent) #Basic listen server. Prints anything that is sent in any channel. 
async def print_message(event):
    print(str(event.guild_id)+" in channel "+str(event.channel_id))
    print(str(event.author).rsplit('#')[0]+": "+str(event.content))


"""
@tasks.task(m=1, ,auto_start=True)
async def replyLoop():

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
    await context.respond('Pong!')

@tasks.task(m=1, pass_app=True, auto_start=True)
async def create_message(channel, content)
    await bot.rest.create_message(channel, content)

await bot.rest.create_message(channel_id, message)

@bot.command
@lightbulb.command('group', 'This is a group')
async def my_group(context):
    pass

@my_group.child
@lightbulb.command('subcommand', 'this is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(context):
    await context.respond('I am a subcommand')


bot = hikari.GatewayBot(token="")

@bot.listen(hikari.StartedEvent) #Activates when bot starts.
async def print_message(event):
    return
"""

bot.run()
