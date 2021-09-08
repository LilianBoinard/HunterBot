import discord
from discord.ext import commands

botTicketChannel = 883018618584055950
# tickets = [["Creation", "Ceci est un test", ":keyboard:"], ["Voila", "Marche stp", ":stopwatch:"], ["Creazrg", "Ca serait sympa", ":white_check_mark:"]]
tickets = []

def isChannelBOT(ctx):
    return ctx.message.channel.id == botTicketChannel


class CogHunterBOT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(isChannelBOT)
    async def work(self, ctx):
        """ Vérifier qu'HunterBOT est allumé """
        client = ctx.author
        contextAuthor = str(client)
        await ctx.send("I'm working " + contextAuthor + " Senpai ❤")

    @commands.command()
    @commands.check(isChannelBOT)
    async def hunter(self, ctx):
        """ Embed d'HunterBOT """
        embed = discord.Embed(title="**HunterBOT**", description="created with ❤", colour=8860319)
        embed.set_author(name="Pyro#0239",
                         icon_url="https://cdn.discordapp.com/avatars/494220268076662795/34105985236f76d533bc0766b0fe85b4.webp?size=128")
        embed.set_footer(
            icon_url="https://cdn.discordapp.com/avatars/883026564818812978/1a220b40bcee76b6c86eb26b782dbd54.webp?size=128",
            text="2021")
        await ctx.send(embed=embed)


    @commands.command()
    async def clear(self, ctx):
        await ctx.channel.purge()

    @commands.command()
    @commands.check(isChannelBOT)
    async def tickets(self, ctx):
        """ Show active tickets """
        embed = discord.Embed(title="**Tickets**", description="Liste des tickets actifs:", colour=8860319)
        embed.set_author(name="HunterBOT",icon_url="https://cdn.discordapp.com/avatars/883026564818812978/1a220b40bcee76b6c86eb26b782dbd54.webp?size=128")
        if len(tickets) == 0:
            embed.add_field(name="Rien..", value="Il n'y a aucun ticket pour le moment", inline=True)
        else:
            for item in tickets:
                embed.add_field(name="*" + item[0] + "*", value=item[1] + "\n State: " + item[2], inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.check(isChannelBOT)
    async def createTicket(self, ctx, name, *, description):
        tickets.append([name, description, " :stopwatch:"])
        await ctx.send("Ticket successfully created")

    @commands.command()
    @commands.check(isChannelBOT)
    async def deleteTicket(self, ctx, name):
        for item in tickets:
            if item[0] == name:
                tickets.remove(item)
        await ctx.send("Ticket successfully removed")

    @commands.command()
    @commands.check(isChannelBOT)
    async def takeTicket(self, ctx, name):
        for item in tickets:
            if item[0] == name:
                item[2] = f" take by {ctx.author}"
        await ctx.send("Ticket successfully taked")

    @commands.command()
    @commands.check(isChannelBOT)
    async def closeTicket(self, ctx, name):
        for item in tickets:
            if item[0] == name:
                item[2] = f" :white_check_mark: by {ctx.author}"
        await ctx.send("Ticket successfully closed")