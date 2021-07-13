#Bot Name : Shahed-Chan
#Bot Author : Shahed
#Bot Has Made With <3
#یام یام یام یام یام


#Imports

from asyncio import events
import discord
import random
from discord import embeds
from discord import activity
from discord.client import Client
from discord.ext import commands
from discord.ext.commands.core import Command, command
from discord.ext.commands import Bot
from discord.flags import alias_flag_value
from discord.message import Message
from discord.user import User
import asyncio

#Client Events

client = commands.Bot(command_prefix = 's!' , help_command=None)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="100 Subscribers :D"))
    print('╔═.✵.══════════════════════════╗\n    Bot  Has  Been  Started\n╚══════════════════════════.✵.═╝')


#Client Command (Ping)

@client.command()
async def ping(ctx):
    await ctx.send(f'`{round(client.latency * 1000)}ms`') 


#Client Command (8Ball)

@client.command(aliases=['8ball' , 'soal'])
async def _8ball(ctx, *, question):
    responses = ['Are',
     'Na','Nemidonam',
      'Shayad...','100 Darsad' ,
       'Fekr Nakonam','Only God Know...',
        'Be Shoma Marbot Nist :)',
         'Kheyli Dost Daram Begam Are Vali Na :))',
          'Be Ejaze Bozorg Tar Ha Baleee :))',
           'Nope','He He He Nemigam >:3',
            'Khodet Midoni Az Man Miporsi? :3','Chi Migi??? :|',
            'Malome Ke Are','Malome Ke Na Azize Man','Mage Khari? :|','Ba Khodete Nemidonam Valla']

    await ctx.reply(f'`Javab` : {random.choice(responses)}')



#Client Command (Help)

@client.command()
async def help(ctx):
    embed=discord.Embed(title="📖 **Shahed-Chan** Commands Help 📖", description="―――――――――――――――――――\n⬜️ `s!soal [Soal]`\nSoal Beporsid Be Sorat Random Be Shoma Javab Mide\n\n⬜️ `s!ping`\nPing Bot Ro Be Shoma Mide\n\n⬜️ `s!kar`\nShoghl Ayande Shoma Ro Mige\n\n⬜️`s!dama [Shahr]`\nDama Shahr Mored Nazar Shoma Ro Pishgoei Mikone :D\n\n⬜️ `s!gay`\nDarsad Gay Bodane Shoma Ro Behetun Mige\n\n⬜️ `s!simp`\nCheghr Simpi? 🤔\n\n⬜️ `s!eshgh [@user]`\nEshgh Shoma Nesbat Be Kesi Ke Mention Kardin Ro Mige\n\n⬜️ `s!help`\nTamamie CMD Haye Bot Ro Beheton Mige (Hamin Payam)\n", color=0x00ff00)
    embed.add_field(name="―――――――――――――――――――" , value="Bot Was Designed By `Shahed`", inline=False)
    await ctx.send(embed=embed)

#Client Command (Kar)    

@client.command()
async def kar(ctx):
    kar = ['خلبان' 
    , 'مهماندار هواپیما' , 'بازیگر' 
    , 'معمار', 'بازاریاب' 
    , 'حسابدار' , 'منشی' , 'وکیل'
    , 'پلیس' , 'ناشر کتاب' , 'نویسنده'
    , 'پرستار' , 'دامپزشک' , 'کارمند' 
    , 'پیش خدمت' , 'معلم' , 'حمال', 'مهندس عمران'
    , 'برنامه نویس' , 'طراح وب' , 'روانشناس'
    , 'تحویل دار بانک', 'دزد' ]
    embed=discord.Embed(title="🔎 Kare Shoma Dar Ayande 🔎", description=f"~ ~ ~\nInshalla Shoma Gharare **~~{random.choice(kar)}~~** Beshi 😃\n~ ~ ~", color=0xfff000)
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTk8vvb1UnfU-x90PpyVaXvoD4D8M7IWIK0kw&usqp=CAU")
    await ctx.reply(embed=embed)


#Client Command (Dama)

@client.command(aliases=['dama'])
async def _dama(ctx , * , shahr):
    embed=discord.Embed(title="⛅️ ~ ⛅️ ~ ⛅️", description=f"👩‍🏫 Damaye Shahr `{shahr}` , Farda `{random.randint(-5,60)}` Daraje Khahad Bood 👩‍🏫", color=0x33DFFF)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/zXuxmCMcJ6xAVeoc4ltHOUkxKcjB2Uab4HM5i2BjfIl7bMG0oik2SHoImvEwOU_xo9I-txTnptfiuaDQOXeQANrig4aQYQg")
    await ctx.reply(embed=embed)


#Client Command (Gay)

@client.command()
async def gay(ctx):
    embed=discord.Embed(title="Are You Gay? 🌈", description=f"🌈 Shoma `%{random.randint(0,100)}` Gay Hastid 🌈", color=0xFF00EE)
    embed.set_thumbnail(url="https://www.memecreator.org/static/images/memes/5153999.jpg")
    await ctx.reply(embed=embed)


#Client Command (Simp)

@client.command(aliases=['simp'])
async def _simp(ctx):
    embed=discord.Embed(title="Are You Simp? 🤔", description=f"Shoma `%{random.randint(0,100)}` Simp Hastid 😸", color=0xFF8B00)
    embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-000724058395-t0ne5p-t500x500.jpg")
    await ctx.reply(embed=embed)

#Client Command (Eshgh)

@client.command()
async def eshgh(ctx , * , esm):
    embed=discord.Embed(title="Eshgh Beyneton Cheghdr Ziade? 🥰", description=f"|\n😍 Mizan Eshgh Beyn Shoma Va {esm} `%{random.randint(0,100)}` Mibashad.\n|", color=0xff0000)
    embed.set_thumbnail(url="https://i.pinimg.com/736x/60/c7/56/60c7563ecec85141343c95c73c8c977c.jpg")
    await ctx.reply(embed=embed)


#Client Join & Leave

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send ('[+] **Bot Joine Channel Shod**')
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    embed=discord.Embed(title="title", description="description", color=0xff0000)
    await ctx.send (embed=embed)

#――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

client.run('Enter The Token Here')

#――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――



# ~  Embed Codes  ~ #

#  ~   embed=discord.Embed(title="title", description="description", color=0xff0000)
#  ~   embed.set_author(name="name", url="url", icon_url="icon")
#  ~   embed.set_thumbnail(url="thumbnail")
#  ~   embed.add_field(name="field", value="value", inline=False)
#  ~   embed.set_footer(text="footer")
#  ~   await ctx.send(embed=embed)
