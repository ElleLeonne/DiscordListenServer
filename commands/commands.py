import lightbulb
from lightbulb import commands
from config import config

@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option("value", "The new temperature value.", float, default=0.7, required=True)
@lightbulb.command('temperature', 'Adjusts the volatility of response weights', hidden=True, guilds=[744554485350924408])
@lightbulb.implements(lightbulb.SlashCommand)
async def temp(ctx: lightbulb.context.Context):
    new = ctx.options.value
    config.change_temp(new)
    await ctx.respond("Temperature is now ", new)

@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option("value", "The new length penalty value.", float, default=0.7, required=True)
@lightbulb.command('length_penalty', 'Adjusts the penalty value for long sequences', hidden=True, guilds=[744554485350924408])
@lightbulb.implements(lightbulb.SlashCommand)
async def length_penalty(ctx: lightbulb.context.Context):
    new = ctx.options.value
    config.change_length_penalty(new)
    await ctx.respond("Length penalty is now ", new)

@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option("value", "How many messages back [bot] can see.", int, default=3, required=True)
@lightbulb.command('context_window', 'Adjusts the context window for replies', hidden=True, guilds=[744554485350924408])
@lightbulb.implements(lightbulb.SlashCommand)
async def context_window(ctx: lightbulb.context.Context):
    new = ctx.options.value
    config.change_ctx_win(new)
    await ctx.respond("Context window is now ", new)

@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command('forcequit', 'Remotely terminates the bot session', hidden=True, guilds=[744554485350924408])
@lightbulb.implements(lightbulb.SlashCommand)
async def forcequit(ctx: lightbulb.context.Context):
    await ctx.bot.close()

@lightbulb.command('flag', 'Flags a time when [bot2] should have responded')
@lightbulb.implements(lightbulb.SlashCommand)
async def flag(ctx: lightbulb.context.Context):
    await ctx.respond("Position flagged for training.")

def load(bot: lightbulb.BotApp) -> None:
    bot.command(forcequit)
    bot.command(context_window)
    bot.command(length_penalty)
    bot.command(temp)
    bot.command(flag)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_command(bot.get_slash_command("forcequit"))
    bot.remove_command(bot.get_slash_command("context window"))
    bot.remove_command(bot.get_slash_command("temperature"))
    bot.remove_command(bot.get_slash_command("length penalty"))
    bot.remove_command(bot.get_slash_command("flag"))
