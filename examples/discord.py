from discord.ext import commands
from google_custom_search import custom_search

google = custom_search(apikey="", engine_id="")

bot = commands.Bot(command_prefix="!")


@bot.command()
async def search(ctx, *, q):
    results = await google.search_async(q)
    await ctx.send(results[0].url)

bot.run("")
