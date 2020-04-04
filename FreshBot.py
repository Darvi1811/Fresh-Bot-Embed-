import discord
from discord.ext import commands
import os



#префикс 
bot = commands.Bot(command_prefix = "*")



@bot.event

#Подключение
async def on_ready():
	print("[SUCCES] Бот в сети!")


@bot.command()
async def embed(ctx):

	
	
	embed = discord.Embed(
			colour=discord.Colour.red(),
			title="**Counter Strike: Global Offensive**",
			description='**Всем привет! Добавлена категория "Counter Strike: Global Offensive", там можно поиграть в ММ или Напарники.\nЕще добавлены новости по теме CS GO, если вы в <#696055207481573386> получите роль <@&695658082465873920>.\nТо будете получать уведомления при начале  трансляции csgomc_ru!**'
	)

		
	await ctx.send(embed=embed)
	print("[SUCCES] Новости отправлены!")
	

@bot.command()

async def hello(ctx):
	
	await ctx.send("**╔┓┏╦━━╦┓╔┓╔━━╗ @everyone\n║┗┛║┗━╣┃║┃║╯╰║ @everyone\n║┏┓║┏━╣┗╣┗╣╰╯║ @everyone\n╚┛┗╩━━╩━╩━╩━━╝ @everyone**")
	print("[SUCCES] Hello отправлено!")




token = os.environ.get("BOT_TOKEN")
bot.run(str(token))
