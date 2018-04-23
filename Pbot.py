from discord import Game
import discord
import random
import asyncio

TOKEN = ('replace this with your bots token')

bot = commands.Bot(command_prefix='+')

@bot.command()
async def kms():
                await bot.say('NO') 

@bot.group()
async def ping():
        await bot.say('Sorry demon was just too lazy to implement this.')
        await bot.say('pong :ping_pong:')

@bot.group(pass_context=True)
async def lewd(ctx):
        await bot.say('Why you gotta be so lewd {0.subcommand_passed}'.format(ctx))

@bot.group(pass_context=True)
async def kill(ctx):
        await bot.say('{0.subcommand_passed} got killed'.format(ctx))

@bot.group(pass_context=True)
async def bitchslap(ctx):
        await bot.say('{0.subcommand_passed} got bitch slapped'.format(ctx))
        await bot.say('{0.subcommand_passed} got bitch slapped'.format(ctx))
        await bot.say('{0.subcommand_passed} got bitch slapped'.format(ctx))
        await bot.say('{0.subcommand_passed} got bitch slapped'.format(ctx))
        await bot.say('{0.subcommand_passed} got bitch slapped'.format(ctx))
        await bot.say('{0.subcommand_passed} got bitch slapped'.format(ctx))
        await bot.say('https://imgur.com/bTGigCv')

@bot.group(pass_context=True)
async def cage(ctx):
      await bot.say('{0.subcommand_passed} got caged'.format(ctx))

@bot.group()
async def bitcoin():
        await bot.say('Have a bitcoin')

@bot.group(pass_context=True)
async def k(ctx):
        await bot.say('KKY'.format(ctx))
                      
#random resonces

@bot.command()
async def coinflip():
        possible_responces = [
                'Heads',
                'Tails'
                ]
        await bot.say(random.choice(possible_responces))

@bot.command()
async def dice():
        possible_responces = [
                '1',
                '2',
                '3',
                '4',
                '5',
                '6',
                'No dice'
                ]
        await bot.say(random.choice(possible_responces))

@bot.command()
async def eightball( name = '8ball' ):
        possible_responces = [
                'Yes',
                'Maybe',
                'No',
                'Proubably',
                'Nah',
                'No way',
                'Nope'
                ]
        await bot.say(random.choice(possible_responces))

@bot.command()
async def Russianroulette():
        possible_responces = [
                'Dead',
                'Alive',
                'Alive',
                'Alive',
                'Alive'
                ]
        await bot.say(random.choice(possible_responces))

@bot.group(pass_context=True)
async def kiss(ctx):
        await bot.say('{0.subcommand_passed} got kissed'.format(ctx))
        possible_responces = [
                'https://i.imgur.com/nqyZPn9.jpg',
                'https://imgur.com/EtaXopA',
                'https://imgur.com/1Suhkjm'
                ]
        await bot.say(random.choice(possible_responces))

@bot.group(pass_context=True)
async def slap(ctx):
        await bot.say('{0.subcommand_passed} got slapped'.format(ctx))
        possible_responces = [
                'https://imgur.com/DfRsmUY',
                'https://imgur.com/yTTzzKv'
                ]
        await bot.say(random.choice(possible_responces))

@bot.group(pass_context=True)
async def poke(ctx):
        await bot.say('{0.subcommand_passed} got poked'.format(ctx))
        possible_responces = [
                'https://imgur.com/bIcjhXJ',
                'https://imgur.com/h6ddy0V',
                'https://imgur.com/7C5jWYq'
                ]
        await bot.say(random.choice(possible_responces))

@bot.group(pass_context=True)
async def pat(ctx):
        await bot.say('{0.subcommand_passed} got patted'.format(ctx))
        possible_responces = [
                'https://imgur.com/pUeah8O',
                'https://imgur.com/OtW9yBs',
                'https://imgur.com/7C5jWYq',
                'https://imgur.com/T6Y2L3u'
                ]
        await bot.say(random.choice(possible_responces))

@bot.group(pass_context=True)
async def punch(ctx):
        await bot.say('{0.subcommand_passed} got punched'.format(ctx))
        possible_responces = [
                'https://imgur.com/xw9CG0q',
                'https://imgur.com/sgXNkUd',
                'https://imgur.com/eWQQGja'
                ]
        await bot.say(random.choice(possible_responces))

@bot.group(pass_context=True)
async def hug(ctx):
        await bot.say('{0.subcommand_passed} got hugged'.format(ctx))
        possible_responces = [
                'https://imgur.com/wiAW9r6',
                'https://imgur.com/wjJvhId',
                'https://imgur.com/kCe5Bcl',
                'https://imgur.com/BcabNdw',
                'https://imgur.com/I6dF7Jk',
                'https://imgur.com/75k34aJ'
                ]
        await bot.say(random.choice(possible_responces))

@bot.group(pass_context=True)
async def cuddle(ctx):
        await bot.say('{0.subcommand_passed} got cuddled'.format(ctx))
        possible_responces = [
                'https://imgur.com/7zdANGl',
                'https://imgur.com/IFeaAkR',
                'https://imgur.com/AtEvIWI'
                ]
        await bot.say(random.choice(possible_responces))

@bot.group(pass_context=True)
async def bkiss(ctx):
        await bot.say('{0.subcommand_passed} got kissed'.format(ctx))

@bot.group()
async def info():
        await bot.say('')

#online confirmation
@bot.event
async def on_ready():
   await bot.change_presence(game=Game(name="+help"))
   print(bot.user.name)
   print('online')

bot.run(TOKEN)
