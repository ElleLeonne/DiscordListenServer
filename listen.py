import hikari
import lightbulb

bot = lightbulb.BotApp(
    token="",
    default_enabled_guilds=(744554485350924408)
)

@bot.listen(hikari.GuildMessageCreateEvent) #Basic listen server. Prints anything that is sent in any channel. 
async def print_message(event):
    #print(str(event.guild_id)+" in channel "+str(event.channel_id))
    print(str(event.author).rsplit('#')[0]+": "+str(event.content))


"""
@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
    await context.respond('Pong!')

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
x = x + 1
print(X)

bot.run()
