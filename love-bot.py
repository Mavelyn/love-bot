import discord
import redis
import random
from discord.ext import commands

r = redis.Redis(charset="utf-8", decode_responses=True)
TOKEN = str(r.get("DISCORD_TOKEN"))

client = discord.Client()

bot = commands.Bot(command_prefix='!', help_command=None)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(name="help")
async def help_command(ctx):
    embed = discord.Embed(
        title="Love-Bot Commands",
        color=discord.Color.green()
    )

    embed.add_field(name="!movies", value="Shows movie list.", inline=False)
    embed.add_field(name="!add_movie", value="Adds movie to movie list.", inline=False)
    embed.add_field(name="!remove_movie", value="Removes movie from movie list.", inline=False)
    embed.add_field(name="!choose_movie", value="Randomly chooses movie from movie list.", inline=False)
    embed.add_field(name="!date_ideas", value="Shows list of date ideas.", inline=False)
    embed.add_field(name="!add_date_idea", value="Adds a date idea to date idea list.", inline=False)
    embed.add_field(name="!remove_date_idea", value="Adds a date idea to date idea list.", inline=False)
    embed.add_field(name="!choose_date_idea", value="Adds a date idea to date idea list.", inline=False)

    await ctx.send(embed=embed)


@bot.command(name="add_movie")
async def add_movie(ctx, *, movie):
    r.rpush("Movies", movie)
    await ctx.send("New movie added.")


@bot.command(name="remove_movie")
async def remove_movie(ctx, *, movie):
    r.lrem("Movies", 0, movie)
    await ctx.send("Movie has been deleted.")


@bot.command(name="choose_movie")
async def choose_movie(ctx):
    movies = r.lrange("Movies", 0, -1)
    random_movie = random.choice(movies)
    await ctx.send(f'{random_movie} has been randomly selected. Enjoy your movie!')


@bot.command(name="movies")
async def list_movies(ctx):
    if r.exists("Movies"):
        movies = r.lrange("Movies", 0, -1)
        embed = discord.Embed(
            title="Our Movie List",
            color=discord.Color.blue()
        )
        for movie in movies:
            embed.add_field(name='\u200b', value=movie, inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("No movies found.")


@bot.command(name="add_date_idea")
async def add_date_idea(ctx, *, date_idea):
    r.rpush("Date Ideas", date_idea)
    await ctx.send("New date idea added.")


@bot.command(name="remove_date_idea")
async def remove_date_idea(ctx, *, date_idea):
    r.lrem("Date Ideas", 0, date_idea)
    await ctx.send("Date idea removed.")


@bot.command(name="choose_date")
async def choose_date(ctx):
    date_ideas = r.lrange("Date Ideas", 0, -1)
    random_date_idea = random.choice(date_ideas)
    await ctx.send(f'{random_date_idea} has been selected. Enjoy your date!')


@bot.command(name="date_ideas")
async def list_date_ideas(ctx):
    if r.exists("Date Ideas"):
        date_ideas = r.lrange("Date Ideas", 0, -1)
        embed = discord.Embed(
            title="Date Ideas",
            color=discord.Color.blue()
        )
        for idea in date_ideas:
            embed.add_field(name='\u200b', value=idea, inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("No date ideas found.")


@bot.command(name="cutestboi")
async def cutie(ctx):
    await ctx.send("Richard Wei uwu")


bot.run(TOKEN)
