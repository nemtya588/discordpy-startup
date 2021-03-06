from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def しね(ctx):
    await ctx.send('おまえがしね')

    
@bot.command()
async def うんこ(ctx):
    await ctx.send('それはエンド')
    
    
@bot.command()
async def でぐ(ctx):
    await ctx.send('神')   
 

@bot.command()
async def くさい(ctx):
    await ctx.send('みんたのこと？')
    
    
@client.event
async def on_message(message):
    if client.user in message.mentions:
        
        reply = f`{message.author.mention}なんだクソガキ‘
        
        await message.channel.send(reply)
    
bot.run(token)

