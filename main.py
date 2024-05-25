import discord
import random,time
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
#il prefisso
bot = commands.Bot(command_prefix='$', intents=intents)


#il punteggio
punteggio = 0
#la connferma(se è pronto invia un messaggio nel terminale)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
#it.aggiunge un punto
@bot.command()
async def fatto(ctx):
    global punteggio
    await ctx.send(f'bravo hai preso un punto ')
    punteggio += 1
#en.aggiunge un punto 
@bot.command()
async def done(ctx):
    global punteggio
    await ctx.send(f'good you make a point ')
    punteggio += 1

@bot.command()
async def list(ctx):
    await ctx.send(f"SaveBot è stato creato per far si che le persone facciano l'indifferenziata  --- SaveBot is created to make people make the waste collection")
    await ctx.send(f"gli admin hanno bisogno del ruolo salvatore del pianeta --- the admin require the role savior of the planet")    
    await ctx.send(f"scrivi $ prima di ongni comando  --- write $ before any command")
    await ctx.send(f"segreto:?!?!?! --- secret:?!?!?!")
    await ctx.send(f"perche:spiega perche è importante fare la raccolta indifferenziata --- why:explain why is it important to do the waste collection")
    await ctx.send(f"hey:saluto --- HEY:greeting")
    await ctx.send(f"numero:il numero dei punti --- number:the number of the point")
    await ctx.send(f"indietro:fa tornare in dietro il punteggio --- back:brings the score back")
    await ctx.send(f"fatto:aggiunge un punto USARE SOLO SE SI è APPENA FATTA L'INDIFFERENZIATA --- done:adds a point USE ONLY IF YOU HAVE JUST MADE THE WASTE COLLECTION")
    await ctx.send(f"SaveBot è stato fato da @enrystrange  --- SaveBot is made by @enrystrange")
@bot.command()
async def lista(ctx):
    await ctx.send(f"SaveBot è stato creato per far si che le persone facciano l'indifferenziata  --- SaveBot is created to make people make the waste collection")
    await ctx.send(f"gli admin hanno bisogno del ruolo salvatore del pianeta --- the admin require the role savior of the planet")    
    await ctx.send(f"scrivi $ prima di ongni comando  --- write $ before any command")
    await ctx.send(f"segreto:?!?!?! --- secret:?!?!?!")
    await ctx.send(f"perche:spiega perche è importante fare la raccolta indifferenziata --- why:explain why is it important to do the waste collection")
    await ctx.send(f"hey:saluto --- HEY:greeting")
    await ctx.send(f"numero:il numero dei punti --- number:the number of the point")
    await ctx.send(f"indietro:fa tornare in dietro il punteggio --- back:brings the score back")
    await ctx.send(f"fatto:aggiunge un punto USARE SOLO SE SI è APPENA FATTA L'INDIFFERENZIATA --- done:adds a point USE ONLY IF YOU HAVE JUST MADE THE WASTE COLLECTION")
    await ctx.send(f"SaveBot è stato fato da @enrystrange  --- SaveBot is made by @enrystrange")
     
@bot.command()
async def why(ctx):
    await ctx.send(f"doing the waste collection not only ensures that there is less toxic waste in the environment but also reduces the need to cultivate, collect or extract new raw materials from the Earth")   
@bot.command()
async def perche(ctx):
    await ctx.send(f"fare la raccolta indifferenziata,non solo fa sì che vi siano meno rifiuti tossici nell ambiente ma riduce anche la necessità di coltivare, raccogliere o estrarre nuove materie prime dalla Terra")     
@bot.command()
async def hey(ctx):
    await ctx.send(f"hey fai l'indifferenziata")   
@bot.command()
async def HEY(ctx):
    await ctx.send(f"hey do de waste collection")   
@bot.command()
async def secret(ctx):
    await ctx.send(f"workinprogres")   
@bot.command()
async def segreto(ctx):
    await ctx.send(f"workinprogres")    
@bot.command()
async def workinprogres(ctx):
    await ctx.send(f"-.-- --- ..- ..-. --- ..- -. -.. -- . στα ολλανδικά χωρίς κενά")
@bot.command()
async def JEHEBTMEGEVONDEN (ctx):
    await ctx.send(f"I didn't expect anyone to find me....")  

@bot.command()
async def numero(ctx):
    await ctx.send(punteggio)
@bot.command()
async def number(ctx):
    await ctx.send(punteggio)
@bot.command()
async def set(ctx,nuovopunteggio:int):
    global punteggio
    user_roles = [role.name for role in ctx.author.roles]
    required_role = 'youWillnEvErgueSSthisrolE'  
    if required_role in user_roles:
        punteggio += nuovopunteggio
        await ctx.send(f'subito !')
    else:
        await ctx.send(f'Non puoi!')

@bot.command()
async def indietro(ctx):
    global punteggio
    user_roles = [role.name for role in ctx.author.roles]
    required_role = 'salvatore del pianeta'  
    if required_role in user_roles:
        await ctx.send(f'subito {required_role}!')
        punteggio -= 1
    else:
        await ctx.send(f'Non hai il ruolo {required_role}!')
@bot.command()
async def back(ctx):
    global punteggio
    user_roles = [role.name for role in ctx.author.roles]
    required_role = 'savior of the planet'  
    if required_role in user_roles:
        await ctx.send(f'immediately {required_role}!')
        punteggio -= 1
    else:
        await ctx.send (f'you dont have the role {required_role}!')
bot.run("")
