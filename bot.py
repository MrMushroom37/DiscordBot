import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Meme Bot", description="A very large noob.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="MrMushroom37")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value="A lot")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discordapp.com/oauth2/authorize?&client_id=484898978417344513&scope=bot&permissions=8")

    await ctx.send(embed=embed)

@bot.command()
async def quit(ctx):
    dead="yeet"

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('token')

while True:
    if dead=="yeet":
        quit()
