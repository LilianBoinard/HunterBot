import discord
from discord.ext import commands
import hunterbot
import asyncio

from colorama import init, Fore
def logo():
    print(Fore.GREEN + "\n")
    print(",--.  ,--.                  ,--.")
    print("|  '--'  |,--.,--.,--,--, ,-'  '-. ,---. ,--.--.")
    print("|  .--.  ||  ||  ||      \'-.  .-'| .-. :|  .--'")
    print("|  |  |  |'  ''  '|  ||  |  |  |  \   --.|  |")
    print("`--'  `--' `----' `--''--'  `--'   `----'`--'   ")
    print('discord.py v.{0}'.format(discord.__version__))
    print(Fore.WHITE + "\n")
    print("--------------------------------------")
logo()

botToken = "ODgzMDI2NTY0ODE4ODEyOTc4.YTD8kg.k_afsYkNEhkBO0wKM9GBEiaP0NM" # exemple token
botDefaultChannel = 882998867828813869
botErrorChannel = 883026122755936267
botWelcomeChannel = 882998867828813866

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description="Hey, je suis HunterBOT", intents=intents)

#----------Events-----------#
@bot.event
async def on_ready():
    print(Fore.LIGHTGREEN_EX + "Bot ready !\n" + Fore.WHITE)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('HunterGame'))
    await bot.get_channel(botDefaultChannel).send("I cuming ❤")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un/des argument(s).")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Baka, cette commande n'existe pas.")
    elif isinstance(error, commands.NotOwner):
        await ctx.send("Tu dois être mon maitre pour utiliser cette commande.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Tu ne peux pas utiliser cette commande, tu n'as peut-être pas les droits ou ne l'utilise pas au bon endroit.")
    elif isinstance(error, commands.MessageNotFound):
        await ctx.send("Désolé, le message n'a pas été trouvé.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("Désolé, le membre n'a pas été trouvé.")
    elif isinstance(error, commands.UserNotFound):
        await ctx.send("Désolé, l'utilisateur n'a pas été trouvé.")
    elif isinstance(error, commands.ChannelNotFound):
        await ctx.send("Désolé, le membre n'a pas été trouvé.")
    elif isinstance(error, commands.ChannelNotReadable):
        await ctx.send("Je n'ai pas la permission de lire des messages dans ce canal.")
    elif isinstance(error, commands.RoleNotFound):
        await ctx.send("Désolé, je n'ai pas trouvé ce role.")
    else:
        await bot.get_channel(botErrorChannel).send(error)


@bot.event
async def on_member_join(member):
    embed = discord.Embed(title="**Arrivage**", description="Un membre nous a rejoint.", color=8860319)
    embed.set_author(name=member.name, icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Membre en question:", value=member.name, inline=True)
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/avatars/883026564818812978/1a220b40bcee76b6c86eb26b782dbd54.webp?size=128",
        text="HunterGame")

    await member.guild.get_channel(botWelcomeChannel).send(embed=embed)

print("Load hunter cog...")
bot.add_cog(hunterbot.CogHunterBOT(bot))
print("Run...\n")
bot.run(botToken)
