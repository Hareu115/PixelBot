import discord
from discord.utils import get
from discord.ext import commands
import datetime
import random
import os
import youtube_dl 
import music
bot = commands.Bot(command_prefix='!', description='Este bot es del yocho')
@bot.command()
async def status(ctx, *estado:str):
    estadostring = ""
    for element in estado:
        estadostring += element
        estadostring += ' '
    game = discord.Game(estadostring)
    await bot.change_presence(status=discord.Status.online, activity=game)
    now = datetime.datetime.now()
async def Retroball(context):
    print("Retroball Usada")
    numero_aleatorio = random.randint(0,18)
    if(numero_aleatorio == 0):
        await context.send('Hoy no, mañana si')
    elif(numero_aleatorio == 1):
        await context.send('El huevo kinder contiene la respuesta, yo no!')
    elif(numero_aleatorio == 2):
        await context.send('Si')
    elif(numero_aleatorio == 3):
        await context.send('No')
    elif(numero_aleatorio == 4):
        await context.send('Tal vez')
    elif(numero_aleatorio == 5):
        await context.send('Todos me hacen preguntas, pero nunca como esto :c')
    elif(numero_aleatorio == 6):
        await context.send('Ni lo intentes')
    elif(numero_aleatorio == 7):
        await context.send('Tas loco')
    elif(numero_aleatorio == 8):
        await context.send('Considero este un momento patas')
    elif(numero_aleatorio == 9):
        await context.send('No se, pero la pizza con piña suena mejor que tu pregunta')
    elif(numero_aleatorio == 10):
        await context.send('Hasta la pregunta de si crear la fusion de la menta con chocolate suena mejor pregunta que lo que acabas de preguntar')
    elif(numero_aleatorio == 11):
        await context.send('Posiblemente')
    elif(numero_aleatorio == 12):
        await context.send('Dudoso la verdad')
    elif(numero_aleatorio == 13):
        await context.send('UwU')
    elif(numero_aleatorio == 14):
        await context.send('OwO')
    elif(numero_aleatorio == 15):
        await context.send('**Flan**')
    elif(numero_aleatorio == 16):
        await context.send('No te respondo que tengo que ir a por una lechuga')
    elif(numero_aleatorio == 17):
        await context.send("Negativo {}".format(ctx.message.author.mention))
    elif(numero_aleatorio == 18):
        await context.send("Afirmativo {}".format(context.message.author.mention))
@bot.command()
async def retroball(context):
    print("Retroball Usada")
    numero_aleatorio = random.randint(0,18)
    if(numero_aleatorio == 0):
        await context.send('Hoy no, mañana si')
    elif(numero_aleatorio == 1):
        await context.send('El huevo kinder contiene la respuesta, yo no!')
    elif(numero_aleatorio == 2):
        await context.send('Si')
    elif(numero_aleatorio == 3):
        await context.send('No')
    elif(numero_aleatorio == 4):
        await context.send('Tal vez')
    elif(numero_aleatorio == 5):
        await context.send('Todos me hacen preguntas, pero nunca como esto :c')
    elif(numero_aleatorio == 6):
        await context.send('Ni lo intentes')
    elif(numero_aleatorio == 7):
        await context.send('Tas loco')
    elif(numero_aleatorio == 8):
        await context.send('Considero este un momento patas')
    elif(numero_aleatorio == 9):
        await context.send('No se, pero la pizza con piña suena mejor que tu pregunta')
    elif(numero_aleatorio == 10):
        await context.send('Hasta la pregunta de si crear la fusion de la menta con chocolate suena mejor pregunta que lo que acabas de preguntar')
    elif(numero_aleatorio == 11):
        await context.send('Posiblemente')
    elif(numero_aleatorio == 12):
        await context.send('Dudoso la verdad')
    elif(numero_aleatorio == 13):
        await context.send('UwU')
    elif(numero_aleatorio == 14):
        await context.send('OwO')
    elif(numero_aleatorio == 15):
        await context.send('**Flan**')
    elif(numero_aleatorio == 16):
        await context.send('No te respondo que tengo que ir a por una lechuga')
    elif(numero_aleatorio == 17):
        await context.send("Negativo {}".format(context.message.author.mention))
    elif(numero_aleatorio == 18):
        await context.send("Afirmativo {}".format(context.message.author.mention))
@bot.command()
async def monediwi(context):
    numero_aleatorio = random.randint(0,1)
    print(numero_aleatorio)
    if(numero_aleatorio==1):
        await context.send('Ha salido Cruz')
    else:
        await context.send('Ha salido Cara')



@bot.command()
async def rep(ctx, url : str):
    if(ctx.author.voice and ctx.author.voice.channel):
        cancioncini = os.path.isfile("cancion.mp3")
        try:
            if cancioncini:
                os.remove("cancioncini.mp3")
        except PermissionError:
            await ctx.send("El bot esta ocupado en este momento") 
        voiceChannel = ctx.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected:
            await voice.move_to(voiceChannel)
        else:
            voice = await voiceChannel.connect()
        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "cancioncini.mp3")
    voice.play(discord.FFmpegPCMAudio("cancioncini.mp3"))
#Operaciones matematicas
@bot.command()
async def suma(rsp, n1:int , n2:int):
    await rsp.send(n1 + n2)
@bot.command()
async def resta(rsp, n1:int , n2:int):
    await rsp.send(n1 - n2)
@bot.command()
async def div(rsp, n1:int , n2:int):
    await rsp.send(n1 / n2)
@bot.command()
async def multi(rsp, n1:int , n2:int):
    await rsp.send(n1 * n2)
#Salida de musica
@bot.command()
async def salir (ctx):
  server = ctx.message.guild.voice_client
  await server.disconnect()
#Run Bot
@bot.event
async def on_ready():
    print('Bot en linea')
bot.run('ODMyODExNDAwOTcxNTUwNzQw.YHpODg.6GqCEFL7VkxCH9fj7OzyHLUpA08')