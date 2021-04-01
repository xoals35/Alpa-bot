from ssl import Options
import discord
from discord import message
from discord.colour import Color
from discord.enums import _is_descriptor
from discord.ext import commands
import asyncio
import datetime
import random
import time
import sys
from PIL import Image,ImageFont,ImageDraw
from io import BytesIO
import json
from pyrandmeme import *
import os
import discord as d
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
import aiohttp
from captcha.image import ImageCaptcha
from discord.ext.commands import has_permissions, MissingPermissions
from youtube_search import YoutubeSearch
import youtube_dl
import openpyxl
from random import choice
import math
from Tools.var import mainprefix, embedcolor, errorcolor
import aiosqlite
import urllib
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import re # Regex for youtube link
import warnings
import requests
from pafy import new
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from fast_youtube_search import search_youtube
from Tools.var import prefix, embedcolor, mainprefix, version
from Tools.func import warn, errorlog, is_owner
from urllib.request import Request, urlopen
import re
import aiofiles
from bs4 import BeautifulSoup
import lxml
from youtube_dl import YoutubeDL
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import pickle
import pytz
import ast
import configparser
import traceback
import pic
from random import randint
import sqlite3
import smtplib
from email.mime.text import MIMEText
import learn
from discord import utils
from discord import Embed
from urllib import request












db = sqlite3.connect("Money.db")
db_cur = db.cursor()

alarm_time = '23:33'#24hrs
channel_id = '817329494700458015'



con = sqlite3.connect("Test.db", isolation_level = None)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS User_Info(id INTEGER PRIMARY KEY, bank TEXT, account TEXT, money INTEGER, create_date TEXT)")
cur.execute("SELECT * FROM User_Info")
print(cur.fetchall())
cur.execute("SELECT * FROM User_Info")
print(cur.fetchone())
cur.execute("SELECT * FROM User_Info")
print(cur.fetchone())
print(cur.fetchone())
cur.execute("SELECT * FROM User_Info WHERE id = ?", (123456789, ))
print(cur.fetchall())
cur.execute("DELETE FROM User_Info WHERE id = ?", (123456787,))



bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
bot.warnings = {} # guild_id : {member_id: [count, [(admin_id, reason)]]}
client = discord.Client()
bicon = "https://postfiles.pstatic.net/MjAyMDEyMTlfNjUg/MDAxNjA4MzgwMjMwMTk1.vpGaTsHFbFfhvPpt9Hm1NqSDr0DZre02K-usz16qWjgg.bJpkQYomYDzFn9h4kOVuzcs5zw6pPS0JvUTXxtMRH4wg.PNG.kingstonlee/179_20201219070213.png?type=w966"
blankicon = 'https://postfiles.pstatic.net/MjAyMDEyMzBfMjMz/MDAxNjA5MjU3MjI0MjY1.Ywa3JgqklresO2beNqiCyASxDU_CxOIf1DcfL7g0l90g.oJzcdR5bxgQ36qQ8E_NYbPtFOXw7kMYXXPyvRVQL61Ig.PNG.kingstonlee/9HZBYcvaOEnh4tOp5EqgcCr_vKH7cjFJwkvw-45Dfjs.png?type=w966'
bot.multiplier = 1
bot.welcome_channels = {}
bot.goodbye_channels = {}
user = []
musictitle = []
song_queue = []
musicnow = []
userF = []
userFlist = []
allplaylist = []

async def readjson(filename):
    try:
        with open(f'./json/{filename}.json', 'r', encoding="utf-8") as read_file:
            return json.load(read_file)
    except ValueError as e:
        print(f'Json파일 로드실패\n에러 코드: {e}')
        return None

async def writejson(filename, content):
    with open(f'./json/{filename}.json', 'w', encoding="utf-8") as write_file:
        json.dump(content, write_file, ensure_ascii=False, indent=4)



def gmser_check(id) :  # GM 서비스에 가입되어있는지 확인하는 함수 
    alr_exist = []
    con = sqlite3.connect(r'C:\python bot\Test.db', isolation_level = None)
    cur = con.cursor()
    cur.execute("SELECT id FROM UserInfo WHERE id = ?", (id,))
    rows = cur.fetchall()
    for i in rows :
        alr_exist.append(i[0])
    if id not in alr_exist :
        return 0
    elif id in alr_exist :
        return 1
    con.close()

def log_info(channel, user, message):
    Ftime = time.strftime('%Y-%m-%d %p %I:%M:%S', time.localtime(time.time()))
    print("[시간: " + str(Ftime) + ",채널: " + str(channel) + ",유저: " + str(user) + "]: " + str(message))
    log = open("log.txt","a")
    log.close()
    #log_info(message.channel,message.author,message.content)


page1 = discord.Embed(title="유저 명령어", description="`ㅌ밈` `ㅌ시간` `ㅌ서버정보` `ㅌ유저정보` `ㅌ따라해` `ㅌ한일번역` `한영번역` `ㅌ영한번역` `ㅌ일한번역` `ㅌ날씨` `ㅌ실검` `ㅌ노래순위` `ㅌ검색` `ㅌ롤전적` `ㅌ레식전적` `ㅌ프로필2` `ㅌ텍스트 할말` `ㅌ봇초대`", colour=discord.Colour.blue())
page2 = discord.Embed(title="어드민 명령어", description="`ㅌ밴` `ㅌ언밴` `ㅌ뮤트` `ㅌ언뮤트` `ㅌ청소` `ㅌ역할부여` `ㅌ역할제거` `ㅌ입장채널 #채널이름 (들어오면 할말)` `ㅌ퇴장채널 #채널이름 (들어오면 할말)` `ㅌ로그채널 #채널이름`", colour=discord.Colour.blue())
page3 = discord.Embed(title="게임 명령어", description="`ㅌ출석` `ㅌ포인트` `송금` `ㅌ도박 (올인가능)` `ㅌ새총` `ㅌ주사위 (원하는수)` `ㅌ가위, ㅌ보, ㅌ주먹`", colour=discord.Colour.blue())
page4 = discord.Embed(title="뮤직 명령어", description="`ㅌ재생 노래이름` `ㅌ들어와` `ㅌ나가` `ㅌ일시정지` `ㅌ다시재생` `ㅌ노래끄기` `ㅌ지금노래` `ㅌ멜론차트` `ㅌ대기열추가` `대기열삭제` `목록초기화` `목록` `목록재생` `ㅌ즐겨찾기` `ㅌ즐겨찾기추가` `ㅌ즐겨찾기삭제` `ㅌ스킵` `ㅌ볼륨`", colour=discord.Colour.blue())

bot.help_pages = [page1, page2, page3, page4]

def RandomColor():
    return randint(0, 0xFFFFFF)

def title(msg):
    global music

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    chromedriver_dir = r"C:\python bot\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver_dir, options = options)
    driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
    source = driver.page_source
    bs = BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id': 'video-title'})
    entireNum = entire[0]
    music = entireNum.text.strip()
    
    musictitle.append(music)
    musicnow.append(music)
    test1 = entireNum.get('href')
    url = 'https://www.youtube.com'+test1
    with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']

    driver.quit()
    
    return music, URL

async def subtitle_song(ctx, suburl):
    TEXT = suburl
    rink = TEXT[-11:]
    target = request.urlopen("http://video.google.com/timedtext?type=list&v="+rink)

    soup = BeautifulSoup(target, "html.parser")
    sub = 0
    kor = 0
    for track in soup.select("track"):
        if sub == 0:
            firstsub = track['lang_code']
        if track['lang_code'] == 'ko':
            kor += 1
        sub += 1

    if sub == 0: #자막이 없음
        await ctx.send("""
        ```
        유튜브 자막이 포함되지 않은 영상입니다!
        ```
        """)
        return 0

    elif kor == 0 and sub != 0: #한글이 아닌 자막 재생
        target = request.urlopen("http://video.google.com/timedtext?lang="+firstsub+"&v="+rink)
        
    elif kor == 1 and sub != 0:  #한글 자막 재생
        target = request.urlopen("http://video.google.com/timedtext?lang=ko&v="+rink)

    soup = BeautifulSoup(target, "html.parser")
    subtimedur = []
    subtimelast = []
    last_time = 0
    subtext = []

    for text in soup.select("text"):
        subtimedur.append(text['start'])
        subtimelast.append(text['dur'])
        subtext.append(text.string)
    
    for i in range(len(subtext)):
        last_time += 1
        embed = discord.Embed(description=subtext[i], color=0x00ff00)
        if i == 0:
            time.sleep(float(subtimedur[i]))
            sub_message = await ctx.send(embed = embed)
        else:
            time.sleep(float(subtimedur[i]) - float(subtimedur[i-1]) - float(0.1))
            await sub_message.edit(embed = embed)
        
    time.sleep(subtimelast[last_time])

    await sub_message.delete()
    del subtimedur [:]
    del subtext [:]

def play(ctx):
    global vc
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    URL = song_queue[0]
    del user[0]
    del musictitle[0]
    del song_queue[0]
    vc = get(bot.voice_clients, guild=ctx.guild)
    if not vc.is_playing():
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx)) 
        client.loop.create_task(subtitle_song(ctx, URL))

def play_next(ctx):
    if len(musicnow) - len(user) >= 2:
        for i in range(len(musicnow) - len(user) - 1):
            del musicnow[0]
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if len(user) >= 1:
        if not vc.is_playing():
            del musicnow[0]
            URL = song_queue[0]
            del user[0]
            del musictitle[0]
            del song_queue[0]
            vc.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after=lambda e: play_next(ctx))
            client.loop.create_task(subtitle_song(ctx, URL))
    
    else:
            if not vc.is_playing():
                client.loop.create_task(vc.disconnect())







url = "https://discord.com/api/webhooks/817329524889878558/bWmeDAR0ugmy9k1NvVpxnxkenuwuyycdKlJjUmLvtgM7J-NwwyGDSl1yL9gadozTJa8q" #webhook url, from here: https://i.imgur.com/f9XnAew.png


data = {
    "image" : "https://ibb.co/9nGRJFJ",
    "username" : "작동로그"
}

data["embeds"] = [
    {
        "description" : "봇이 작동되었습니다.",
        "title" : "작동로그",
    }
]

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'downloads': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {'options': '-vn'}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')
        self.id = data.get('id')
        self.uploader = data.get('uploader')
        self.uploaderid = data.get('uploader_id')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)







@bot.event
async def on_ready():
    user = len(bot.users)
    server = len(bot.guilds)
    message = ["ㅌ도움",  str(user) + "유저와 함께해요!", str(server) + "개의 서버에 알파가 같이운영해요!"]
    while True:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(message[0]))
            message.append(message.pop(0))
            await asyncio.sleep(4)

    for file in ["welcome_channels.txt", "goodbye_channels.txt"]:
        async with aiofiles.open(file, mode="a") as temp:
            pass
        
    async with aiofiles.open("welcome_channels.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            bot.welcome_channels[int(data[0])] = (int(data[1]), " ".join(data[2:]).strip("\n"))

    async with aiofiles.open("goodbye_channels.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            bot.goodbye_channels[int(data[0])] = (int(data[1]), " ".join(data[2:]).strip("\n"))


async def update_totals(member):
    invites = await member.guild.invites()

    c = datetime.today().strftime("%Y-%m-%d").split("-")
    c_y = int(c[0])
    c_m = int(c[1])
    c_d = int(c[2])

    async with bot.db.execute("SELECT id, uses FROM invites WHERE guild_id = ?", (member.guild.id,)) as cursor: # this gets the old invite counts
        async for invite_id, old_uses in cursor:
            for invite in invites:
                if invite.id == invite_id and invite.uses - old_uses > 0: # the count has been updated, invite is the invite that member joined by
                    if not (c_y == member.created_at.year and c_m == member.created_at.month and c_d - member.created_at.day < 7): # year can only be less or equal, month can only be less or equal, then check days
                        print(invite.id)
                        await bot.db.execute("UPDATE invites SET uses = uses + 1 WHERE guild_id = ? AND id = ?", (invite.guild.id, invite.id))
                        await bot.db.execute("INSERT OR IGNORE INTO joined (guild_id, inviter_id, joiner_id) VALUES (?,?,?)", (invite.guild.id, invite.inviter.id, member.id))
                        await bot.db.execute("UPDATE totals SET normal = normal + 1 WHERE guild_id = ? AND inviter_id = ?", (invite.guild.id, invite.inviter.id))

                    else:
                        await bot.db.execute("UPDATE totals SET normal = normal + 1, fake = fake + 1 WHERE guild_id = ? and inviter_id = ?", (invite.guild.id, invite.inviter.id))

                    return
    

@bot.event
async def on_member_join(member):
    for guild_id in bot.welcome_channels:
        if guild_id == member.guild.id:
            channel_id, message = bot.welcome_channels[guild_id]
            await bot.get_guild(guild_id).get_channel(channel_id).send(f"{member.mention}{message}")
            return

@bot.event
async def on_member_remove(member):
    for guild_id in bot.goodbye_channels:
        if guild_id == member.guild.id:
            channel_id, message = bot.goodbye_channels[guild_id]
            await bot.get_guild(guild_id).get_channel(channel_id).send(f"{member.mention}{message}")
            return

@bot.command()
async def 입장채널(ctx, new_channel: discord.TextChannel=None, *, message=None):
    if new_channel != None and message != None:
        for channel in ctx.guild.channels:
            if channel == new_channel:
                bot.welcome_channels[ctx.guild.id] = (channel.id, message)
                await ctx.channel.send(f"환영 메세지를 {channel.name}에 보내고 {message}라고 보낼게요!")
                await channel.send("새로운 환영 채널입니다!")
                
                async with aiofiles.open("welcome_channels.txt", mode="a") as file:
                    await file.write(f"{ctx.guild.id} {new_channel.id} {message}\n")

                return

        await ctx.channel.send("주어진 채널을 찾을 수 없습니다.")

    else:
        await ctx.channel.send("환영 채널의 이름이나 환영 메시지를 포함하지 않았습니다.")


@bot.command()
async def 퇴장채널(ctx, new_channel: discord.TextChannel=None, *, message=None):
    if new_channel != None and message != None:
        for channel in ctx.guild.channels:
            if channel == new_channel:
                bot.goodbye_channels[ctx.guild.id] = (channel.id, message)
                await ctx.channel.send(f"퇴장 메세지를 {channel.name}에 보내고 {message}라고 보낼게요!")
                await channel.send("새로운 퇴장 채널입니다!")
                
                async with aiofiles.open("goodbye_channels.txt", mode="a") as file:
                    await file.write(f"{ctx.guild.id} {new_channel.id} {message}\n")

                return

        await ctx.channel.send("주어진 채널을 찾을 수 없습니다.")

    else:
        await ctx.channel.send("작별 채널의 이름이나 작별 메시지를 포함하지 않았습니다.")



@bot.command() 
async def 안녕(ctx):
	await ctx.send("그래 안녕!")



@bot.command(aliases=['청소'])
@commands.has_permissions(administrator=True)
async def clear(ctx, l: int = 50):
   c = await ctx.channel.purge(limit=l)
   await ctx.send(f"`{len(c)}` 개의 메세지를 삭제했습니다.", delete_after=3)
   












@bot.command(name="뮤트")
@commands.has_permissions(manage_messages=True)
async def mute(ctx , member: discord.Member, *, reason=None):
	guild = ctx.guild
	mutedRole = discord.utils.get(guild.roles, name="Muted")

	if not mutedRole:
		mutedRole = await guild.create_role(name="Muted")

		for channel in guild.channels:
			await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

	await member.add_roles(mutedRole, reason=reason)
	await ctx.send(f"뮤트 {member.mention} 사유: {reason}으로 뮤트를 먹으셨습니다.")
	await member.send(f"뮤트 {member.mention} 사유: {reason}으로 뮤트를 먹으셨습니다.")


@bot.command(name="언뮤트")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
	mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

	
			

	await member.remove_roles(mutedRole)
	await ctx.send(f"언뮤트 {member.mention}님이 언뮤트를 당하셨습니다.")
	await member.send(f"언뮤트 {member.mention}님이  언뮤트를 당하셨습니다.")






 
@bot.command(aliases = ['세이','메세지'])
async def say(ctx,*,message):
    await ctx.message.delete()
    emb=discord.Embed(description=f"{message}")
    msg=await ctx.channel.send(embed=emb)
    

                 
@bot.command()
async def 경품(ctx, mins : int, * , prize: str):
	embed = discord.Embed(title = "상품!", description = f"{prize}", color = ctx.author.color)

	end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

	embed.add_field(name = "종료 시간:", value = f"{end} UTC")
	embed.set_footer(text = f"지금부터 {mins}분 후 Emds")

	my_msg = await ctx.send(embed = embed)

	await my_msg.add_reaction("🎉")

@bot.command(name="로드")
async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: {extension}을(를) 로드했습니다!")


@bot.command(name="언로드")
async def unload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: {extension}을(를) 언로드했습니다!")


@bot.command(name="리로드")
async def reload_commands(ctx, extension=None):
        if extension is None:  # extension이 None이면 (그냥 !리로드 라고 썼을 때)
            for filename in os.listdir("cogs"):
                if filename.endswith(".py"):
                    bot.unload_extension(f"cogs.{filename[:-3]}")
                    bot.load_extension(f"cogs.{filename[:-3]}")
                    await ctx.send(":white_check_mark: 모든 명령어를 다시 불러왔습니다!")
        else:
            bot.unload_extension(f"cogs.{extension}")
            bot.load_extension(f"cogs.{extension}")
            await ctx.send(f":white_check_mark: {extension}을(를) 다시 불러왔습니다!")


for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.command(aliases = ['ㅊㄴㅈㄱ'])
async def 채널제거(ctx, channel: d.TextChannel):
	mbed = d.Embed(
		title = '완료!',
		description = f'{channel}이라는 채널을 삭제했습니다.',
	)
	if ctx.author.guild_permissions.manage_channels:
		await ctx.send(embed=mbed)
		await channel.delete()


@bot.command(aliases = ['ㅊㄴㅅㅅ'])
async def 채널생성(ctx, channelName):
	guild = ctx.guild

	mbed = d.Embed(
		title = '완료!',
		description = "{}이라는 채널을 성공적으로 생성되었습니다.".format(channelName)
	)
	if ctx.author.guild_permissions.manage_channels:
		await guild.create_text_channel(name='{}'.format(channelName))
		await ctx.send(embed=mbed)
		
		
@bot.command(aliases = ['ㄸㄹㅎ'])
async def 따라해(ctx, *, text):
    await ctx.send(text)



@bot.command(pass_context=True)
async def 역할부여(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"{user.name}님한테 **{role.name}**역할을 추가했어요!")

@bot.command(pass_context=True)
async def 역할제거(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    await ctx.send(f"{user.name}님한테 **{role.name}**역할을 제거했어요!")

@bot.command()
async def 유튜브(ctx):
    embed = discord.Embed(colour=0x95efcc, title=f"알파캡틴유튜브")
    await ctx.send(embed=embed)
    await ctx.send('https://www.youtube.com/user/cho090501')
    
@bot.command()
async def 레일건사기템존(ctx):
    embed=discord.Embed(title='이거 눌러보셈 ㅋㅋㅋㅋㅋㅋㅋ', description = "레일건 사기템존님은?\n잼민티 내고 이상하고 병신임 이거 이욕해도됌 제목눌러보셈", color = 0xff0000, url = "https://www.youtube.com/watch?v=K51gdMm3wWM")
    embed.set_footer(text = "와 니애미 욕은 해도됌 이사람한테는 (?)")
#출처: https://tercomgame.tistory.com/138 [단순한.]
    await ctx.send(embed=embed)


@bot.command()
async def 마크서버(ctx, arg):
    r = requests.get('https://api.minehut.com/server/' + arg + '?byName=true')
    json_data = r.json()

    description = json_data["server"]["motd"]
    online = str(json_data["server"]["online"])
    playerCount = str(json_data["server"]["playerCount"])

    embed = discord.Embed(
        title=arg + " Server Info",
        description='서술: ' + description + '\온라인: ' + online + '\n플레이어: ' + playerCount,
        color=discord.Color.dark_green()
    )
    embed.set_thumbnail(url="https://i1.wp.com/www.craftycreations.net/wp-content/uploads/2019/08/Grass-Block-e1566147655539.png?fit=500%2C500&ssl=1")

    await ctx.send(embed=embed)





   
@bot.command()
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)

            await ctx.channel.send("'" + args + "' dm전송이 완료되었습니다.: " + target.name)

        except:
            await ctx.channel.send("지정된 사용자한테 dm을(를)할 수 없습니다.")
        

    else:
        await ctx.channel.send("사용자 ID 및 / 또는 메시지를 제공하지 않았습니다.")
 




@bot.command()
async def 시간(ctx):
    await ctx.send(embed=discord.Embed(title="현재시간", timestamp=datetime.datetime.utcnow()))



    





@bot.command(name="검색")
async def s(ctx, *, search_query):
    temp = 0
    url_base = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="
    url = url_base + urllib.parse.quote(search_query)
    title = ["", "", "", ""]
    link = ["", "", "", ""]
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    result = soup.find_all('a', "api_txt_lines total_tit") #수정됨
    embed = discord.Embed(title="검색 결과", description=" ", color=0xf3bb76)
    for n in result:
        if temp == 4:
            break
        title[temp] = n.text #수정됨
        link[temp] = n.get("href")
        embed.add_field(name=title[temp], value=link[temp], inline=False)
        temp+=1
    embed.set_footer(text="네이버 블로그만 검색됩니다.")
    await ctx.send(embed=embed)




@bot.command()
async def 뽑기(ctx):
        await ctx.trigger_typing()
        randomNum = random.randrange(1, 3)
        if randomNum == 1:
            await ctx.send('당첨')
        if randomNum == 2:
            await ctx.send('꽝')



@bot.command()
async def 출근(ctx):
    시간 = datetime.datetime.utcnow()
    await ctx.send(f"{ctx.author.mention}님이 출근합니다.\n> 출근시간 {시간}")


@bot.command()
async def 퇴근(ctx):
    시간 = datetime.datetime.utcnow()
    await ctx.send(f"{ctx.author.mention}님이 퇴근합니다.\n> 퇴근시간 {시간}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):
        await warn(ctx=ctx, content=f"쿨타임이 발생했어요 `{round(error.retry_after, 2)}`초 후에 다시시도해 주세요")
    elif isinstance(error, commands.CheckFailure):
        await warn(ctx=ctx, content='실행하실 조건이 충족 되지않음')
    elif isinstance(error, commands.BadArgument):
        await warn(ctx=ctx, content='올바른 값을 넣어 주세요.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await warn(ctx=ctx, content='값이 필요합니다...')
    elif isinstance(error, commands.MissingPermissions):
        await warn(ctx=ctx, content='권한이 없습니다...')
    elif isinstance(error, commands.CommandNotFound):
        pass
    elif '403 Forbidden' in str(error):
        await warn(ctx=ctx, content='봇한테 권한을 제데로 주세요 ㅠㅠ')
    else:
        await errorlog(ctx=ctx, error=error, bot=bot)

@bot.command()
async def 검바(ctx):
    await ctx.send(f'{ctx.author.mention}, ㅁㅗㅅㅅㅐㅇㄱㅣㄴ 검바')
    time.sleep(2)
    await ctx.send(f'{ctx.author.mention} 니얼굴 검바')




@bot.command()
async def 들어와(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
        await ctx.send(f'{ctx.author.mention}님 채널에 저 {ctx.bot.name}이 접속했어요!')
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send('음성 채널에 유저가 없습니다.')

@bot.command()
async def 나가(ctx):
        await vc.disconnect()
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send('음성 채널에 유저가 없습니다.')

   

@bot.command()
async def 재생(ctx, *, msg):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
        embed = discord.Embed(description=f"{ctx.author.mention}님 `{ctx.message.author.voice.channel}`채널에 저 알파가 접속했어요!")
        await ctx.send(embed=embed)
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send('음성 채널에 유저가 없습니다.')

    if not vc.is_playing():
        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = "C:\python bot\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir)
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        musicnow.insert(0, entireText)
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx))
        await subtitle_song(ctx, url)
        
    else:
        user.append(msg)
        result, URLTEST = title(msg)
        song_queue.append(URLTEST)
        await ctx.send("다른노래가 재생되고있으므로" + result + "이라는 곡을 자동으로 대기열에 추가되었습니다.")
        
        

@bot.command()
async def 일시정지(ctx):
    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(description = entireText + "노래가 일시정지 되었습니다.", color = 0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되지 않네요.")

@bot.command()
async def 다시재생(ctx):
    try:
        vc.resume()
    except:
         await ctx.send("지금 노래가 재생되지 않네요.")
    else:
         await ctx.send(embed = discord.Embed(description = entireText  + "노래을(를) 다시 재생했습니다.", color = 0x00ff00))

@bot.command()
async def 노래끄기(ctx):
    if vc.is_playing():
        vc.stop()
        await ctx.send(embed = discord.Embed(description = entireText  + "노래을(를) 껐습니다.", color = 0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되지 않네요.")

@bot.command()
async def 지금노래(ctx):
    if not vc.is_playing():
        await ctx.send("지금은 노래가 재생되지 않네요..")
    else:
        await ctx.send(embed = discord.Embed(title = "지금노래", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))

@bot.command()
async def 멜론차트(ctx):

    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send('음성 채널에 유저가 없습니다.')


    if not vc.is_playing():
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = r"C:\python bot\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir, options = options)
        driver.get("https://www.youtube.com/results?search_query=멜론차트")
        source = driver.page_source
        bs = BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        musicnow.insert(0, entireText)
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after = lambda e: play_next(ctx))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

@bot.command()
async def 즐겨찾기(ctx):
    global Ftext
    Ftext = ""
    correct = 0
    global Flist
    for i in range(len(userF)):
        if userF[i] == str(ctx.message.author.name): #userF에 유저정보가 있는지 확인
            correct = 1 #있으면 넘김
    if correct == 0:
        userF.append(str(ctx.message.author.name)) #userF에다가 유저정보를 저장
        userFlist.append([]) #유저 노래 정보 첫번째에 유저이름을 저장하는 리스트를 만듬.
        userFlist[len(userFlist)-1].append(str(ctx.message.author.name))
        
    for i in range(len(userFlist)):
        if userFlist[i][0] == str(ctx.message.author.name):
            if len(userFlist[i]) >= 2: # 노래가 있다면
                for j in range(1, len(userFlist[i])):
                    Ftext = Ftext + "\n" + str(j) + ". " + str(userFlist[i][j])
                titlename = str(ctx.message.author.name) + "님의 즐겨찾기"
                embed = discord.Embed(title = titlename, description = Ftext.strip(), color = 0x00ff00)
                embed.add_field(name = "목록에 추가\U0001F4E5", value = "즐겨찾기에 모든 곡들을 목록에 추가합니다.", inline = False)
                embed.add_field(name = "플레이리스트로 추가\U0001F4DD", value = "즐겨찾기에 모든 곡들을 새로운 플레이리스트로 저장합니다.", inline = False)
                Flist = await ctx.send(embed = embed)
                await Flist.add_reaction("\U0001F4E5")
                await Flist.add_reaction("\U0001F4DD")
            else:
                await ctx.send("아직 등록하신 즐겨찾기가 없어요.")



@bot.command()
async def 즐겨찾기추가(ctx, *, msg):
    correct = 0
    for i in range(len(userF)):
        if userF[i] == str(ctx.message.author.name): #userF에 유저정보가 있는지 확인
            correct = 1 #있으면 넘김
    if correct == 0:
        userF.append(str(ctx.message.author.name)) #userF에다가 유저정보를 저장
        userFlist.append([]) #유저 노래 정보 첫번째에 유저이름을 저장하는 리스트를 만듦.
        userFlist[len(userFlist)-1].append(str(ctx.message.author.name))

    for i in range(len(userFlist)):
        if userFlist[i][0] == str(ctx.message.author.name):
            
            options = webdriver.ChromeOptions()
            options.add_argument("headless")

            chromedriver_dir = r"C:\python bot\chromedriver.exe"
            driver = webdriver.Chrome(chromedriver_dir, options = options)
            driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
            source = driver.page_source
            bs = BeautifulSoup(source, 'lxml')
            entire = bs.find_all('a', {'id': 'video-title'})
            entireNum = entire[0]
            music = entireNum.text.strip()

            driver.quit()

            userFlist[i].append(music)
            await ctx.send(music + "(이)가 정상적으로 등록되었어요!")



@bot.command()
async def 즐겨찾기삭제(ctx, *, number):
    correct = 0
    for i in range(len(userF)):
        if userF[i] == str(ctx.message.author.name): #userF에 유저정보가 있는지 확인
            correct = 1 #있으면 넘김
    if correct == 0:
        userF.append(str(ctx.message.author.name)) #userF에다가 유저정보를 저장
        userFlist.append([]) #유저 노래 정보 첫번째에 유저이름을 저장하는 리스트를 만듦.
        userFlist[len(userFlist)-1].append(str(ctx.message.author.name))

    for i in range(len(userFlist)):
        if userFlist[i][0] == str(ctx.message.author.name):
            if len(userFlist[i]) >= 2: # 노래가 있다면
                try:
                    del userFlist[i][int(number)]
                    await ctx.send("정상적으로 삭제되었습니다.")
                except:
                     await ctx.send("입력한 숫자가 잘못되었거나 즐겨찾기의 범위를 초과하였습니다.")
            else:
                await ctx.send("즐겨찾기에 노래가 없어서 지울 수 없어요!")

@bot.command()
async def 대기열추가(ctx, *, msg):
    user.append(msg)
    result, URLTEST = title(msg)
    song_queue.append(URLTEST)
    await ctx.send(result + "를 재생목록에 추가했어요!")

@bot.command()
async def 대기열삭제(ctx, *, number):
    try:
        ex = len(musicnow) - len(user)
        del user[int(number) - 1]
        del musictitle[int(number) - 1]
        del song_queue[int(number)-1]
        del musicnow[int(number)-1+ex]
            
        await ctx.send("대기열이 정상적으로 삭제되었습니다.")
    except:
        if len(list) == 0:
            await ctx.send("대기열에 노래가 없어 삭제할 수 없어요!")
        else:
            if len(list) < int(number):
                await ctx.send("숫자의 범위가 목록개수를 벗어났습니다!")
            else:
                await ctx.send("숫자를 입력해주세요!")

@bot.command()
async def 목록(ctx):
    if len(musictitle) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")
    else:
        global Text
        Text = ""
        for i in range(len(musictitle)):
            Text = Text + "\n" + str(i + 1) + ". " + str(musictitle[i])
            
        await ctx.send(embed = discord.Embed(title= "노래목록", description = Text.strip(), color = 0x00ff00))

@bot.command()
async def 목록초기화(ctx):
    try:
        ex = len(musicnow) - len(user)
        del user[:]
        del musictitle[:]
        del song_queue[:]
        while True:
            try:
                del musicnow[ex]
            except:
                break
        await ctx.send(embed = discord.Embed(title= "목록초기화", description = """목록이 정상적으로 초기화되었습니다. 이제 노래를 등록해볼까요?""", color = 0x00ff00))
    except:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")

@bot.command()
async def 목록재생(ctx):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if len(user) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")
    else:
        if len(musicnow) - len(user) >= 1:
            for i in range(len(musicnow) - len(user)):
                del musicnow[0]
        if not vc.is_playing():
            play(ctx)
        else:
            await ctx.send("노래가 이미 재생되고 있어요!")

@bot.command()  # 다음곡 재생하기
async def 스킵(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Playing next")
        voice.stop()
        await ctx.send(embed = discord.Embed(title= "노래 스킵", description = "스킵으로 현재 " + musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        print("No music playing failed to playing next song")
        await ctx.send("재생할 곡이 없어요.")

@bot.command()
async def 도움(ctx):
   buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
   current = 0
   msg = await ctx.send(embed=bot.help_pages[current])

   for button in buttons:
       await msg.add_reaction(button)

   while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
                    embed = bot.help_pages[current]
                    embed.set_footer(text="Timed Out.")
                    await msg.clear_reactions()

        else:
            previous_page = current

            if reaction.emoji == u"\u23EA":
                current = 0
                    
            elif reaction.emoji == u"\u25C0":
                if current > 0:
                    current -= 1

            elif reaction.emoji ==u"\u25B6":
                if current < len(bot.help_pages)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(bot.help_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=bot.help_pages[current])



@bot.command()
async def 밴(ctx, user: discord.User, *,reason=None):
    guild = ctx.guild
    reason=reason
    mbed = discord.Embed(
        title = "밴 명령어 작동",
        description = f"{user}님을 밴 했습니다 사유:{reason}",
        colour=discord.Colour.red()
        
    )
    if ctx.author.guild_permissions.ban_members:
        await ctx.send(embed=mbed)
        await guild.ban(user=user)

@bot.command()
async def 언밴(ctx, user: discord.User, *,reason=None):
        guild = ctx.guild
        reason=reason
        mbed = discord.Embed(
            title = '언밴 작동',
            description = f"{user}님을 언밴 했어요! 사유:{reason}",
            colour=discord.Colour.red()
        )
        if ctx.author.guild_permissions.ban_members:
            await ctx.send(embed=mbed)
            await guild.unban(user=user)

@bot.event
async def on_message(message):
    list_message = message.content.split(' ')
    if message.author.bot:
        return
    if not message.guild:
        return
 
  
    if message.content.startswith ("ㅌ공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(813964369167253504)
            embed = discord.Embed(title="**공지사항**", description="\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="담당 관리자 : {}".format(message.author), icon_url="https://ifh.cc/v-AZqzkm")
            embed.set_thumbnail(url="https://ifh.cc/v-AZqzkm")
            await message.channel.send(embed=embed)
            await message.author.send("*[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))
    

    if message.content.startswith('ㅌ재난문자'):
        log_info(message.channel,message.author,message.content)
        try:
            try:
                data_false = list_message[1]
            except: #목록갯수
                list_search = 10
            else:
                list_search = int(list_message[1])
            try:
                data_false = list_message[2]
            except: #지역설정
                locate_search = '전국'
            else:
                locate_search = list_message[2]
            data = "https://m.search.naver.com/search.naver?query=" + locate_search + " 재난문자"
            html = requests.get(data).text
            max_search = len(html.split('<em class="area_name">'))-1
            if max_search < list_search:
                list_search = max_search
            embed = discord.Embed(title=locate_search + ' 재난문자 발령 현황', color=0x00aaaa)
            for i in range(list_search):
                city_name = html.split('<em class="area_name">')[i+1].split('</em>')[0]
                date_time = html.split('<time datetime="">')[i+1].split('</time>')[0]
                text = html.split('<span class="dsc _text">')[i+1].split('</span>')[0]
                embed.add_field(name=city_name, value='[' + date_time + ']:' + text, inline=False)
            await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(title='에러', description='알수없는 오류가 발생하였습니다.', color=0x00aaaa)
            await message.channel.send(embed=embed)
        return

    if message.content.startswith(f'ㅌeval'):
    
        def insert_returns(body): # [1]
            # insert return stmt if the last expression is a expression statement
            if isinstance(body[-1], ast.Expr):
                body[-1] = ast.Return(body[-1].value)
                ast.fix_missing_locations(body[-1])

            # for if statements, we insert returns into the body and the orelse
            if isinstance(body[-1], ast.If):
                insert_returns(body[-1].body)
                insert_returns(body[-1].orelse)

            # for with blocks, again we insert returns into the body
            if isinstance(body[-1], ast.With):
                insert_returns(body[-1].body)

        cmd = message.content.split(" ")[1:]
        _cmd = cmd
        print(cmd)
        msg = await message.channel.send(embed = discord.Embed(title='<a:loading1:754264610420424725> Code Compiling').add_field(
            name='📥 Input',
            value=f'```py\n{cmd}```',
            inline=False
        ))
        await asyncio.sleep(1.5)

        #banword checking
        banword = ['token', 'file=', 'file ='] 
        # 본인이 원하는걸 넣으심 됩니다  # banword에 있는 단어가 있으면 return None으로 처리됩니다.
        
        if cmd in banword: # [2]
            embed = discord.Embed(title='<a:loading1:754264610420424725> Code Compiling')
            embed.add_field(name='📥 Input', value=f'```py\n{_cmd}```', inline=False)
            embed.add_field(name = '📤 Output', value = f'`{cmd}`에는 eval에서 사용 금지된 단어가 포함되어 있습니다.')
            await msg.edit(embed=embed)
            await message.channel.send(f'{message.content}는 사용 금지된 단어가 포함되어 있습니다.')
            return None # [3]
        else:
            try:
                code = message.content[6:]
                cmd = code
                fn_name = "_eval_expr"
                cmd = cmd.strip("` ")
                # add a layer of indentation
                cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
                # wrap in async def body
                body = f"async def {fn_name}():\n{cmd}"
                parsed = ast.parse(body)
                body = parsed.body[0].body
                insert_returns(body)
                env = {
                    'client': client,
                    'discord': discord,
                    'message': message,
                    '__import__': __import__
                } # [4]
                exec(compile(parsed, filename="<ast>", mode="exec"), env)
                result = (await eval(f"{fn_name}()", env)) # [5]
                embed=discord.Embed(title="실행 성공", colour=discord.Colour.green(), timestamp=message.created_at)
                embed.add_field(name="`📥 Input (들어가는 내용) 📥`", value=f"```py\n{code}```", inline=False)
                embed.add_field(name="`📤 Output (나오는 내용) 📤`", value=f"```py\n{result}```", inline=False)
                embed.add_field(name="`🔧 Type (타입) 🔧`",value=f"```py\n{type(result)}```", inline=False)
                embed.add_field(name="`🏓 Latency (지연시간) 🏓`",value=f"```py\n{str((datetime.datetime.now()-message.created_at)*1000).split(':')[2]}```", inline=False)
                embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                await msg.edit(embed = embed) # [6]
            except Exception as e: # [7]
                await message.channel.send(f"{message.author.mention}, 실행 중 오류가 발생하였습니다.\n\n```py\n{e}```")

   
    if message.content == 'ㅌ줌실검' or message.content == 'ㅌ줌실시간검색어':
            url = 'http://issue.zum.com/'
            req = Request(url)
            html = urllib.request.urlopen(req)
            soup = BeautifulSoup(html, "html.parser")

            s = soup.find_all('div', {'class': 'cont'})

            rank = 1
            data = []
            for title in s:
                tt = title.find('span', {'class': 'word'}).text
                data.append(f'**{rank}**. {tt}')
                rank += 1
                if rank > 10:
                    break

            dat = str(data)
            dat = dat.replace("'", "")
            dat = dat.replace(", ", "\n")
            dat = dat[1:-1]
            embed = discord.Embed(title='줌 실시간 검색어 순위', description=dat, colour=0x19CE60)
            await message.channel.send(embed=embed)

    if message.content.startswith("ㅌ골라"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await message.channel.send("저는 "  + choiceresult +  " 을 고르겠습니다.")


   



    await bot.process_commands(message)

@bot.command(name='주사위')
async def roll(ctx, number: int):
    await ctx.send(f'주사위를 굴려 {random.randint(1,number)}이(가) 나왔습니다. (1-{number})')


@roll.error
async def roll_error(ctx, error):
    await ctx.send(f"2 이상의 정수를 넣어주세요")

@bot.command()
async def 봇초대(ctx):
    embed = discord.Embed(title="봇초대링크", description="[관리자권한으로 초대](https://discord.com/oauth2/authorize?client_id=807987021863583744&permissions=8&scope=bot)\n[일반으로 초대](https://discord.com/api/oauth2/authorize?client_id=807987021863583744&permissions=0&scope=bot)\n[공식디스코드](https://discord.gg/z6k3AEzDW2)", colour=discord.Colour.blue())
    await ctx.send(embed=embed)

@bot.event
async def on_guild_join(guild):
    try:
        c = 806409549258686504
        invite = await guild.invites()
        embed = discord.Embed(
                title="알파봇이 새로운 서버에 초대되었어요!",
                description=f"알파봇이 {guild.name}({guild.id})에 초대되었습니다!",
                color=RandomColor()
            )
        embed.set_thumbnail(url=f"{guild.icon_url}")
        embed.add_field(name="초대 링크", value=f"{invite}", inline=False)
    except:
        c = 806409549258686504
        embed = discord.Embed(
                title="알파봇이 새로운 서버에 초대되었어요!",
                description=f"알파봇이 {guild.name}({guild.id})에 초대되었습니다!",
                color=RandomColor()
            )
        embed.set_thumbnail(url=f"{guild.icon_url}")
    await bot.get_channel(int(c)).send(embed=embed)


@bot.event
async def on_guild_remove(guild):
    try:
        c = 806409549258686504
        invite = await guild.invites()
        embed = discord.Embed(
                title="알파봇",
                description=f"알파봇이 {guild.name}서버에서 강퇴 아니면 밴을 당한거 같습니다.",
                color=RandomColor()
            )
        embed.set_thumbnail(url=f"{guild.icon_url}")
    except:
        c = 806409549258686504
        embed = discord.Embed(
                title="알파프리베이트봇",
                description=f"알파프리베이트봇이 {guild.name}서버에서 강퇴 아니면 밴을 당한거 같습니다.",
                color=RandomColor()
            )
        embed.set_thumbnail(url=f"{guild.icon_url}")
    await bot.get_channel(int(c)).send(embed=embed)


@bot.command(name="타이머", help="타이머를 맟춰줘요!", usage="[m/s] [숫자 Number] (내용 Content)", aliases=['timer'])
async def timer(ctx, mors, num, *, desc="없음"):
    if mors == "m":
        embed = discord.Embed(
            title=f"{num}분동안 타이머를 시작합니다!\n\n{ctx.author.mention}님의 타이머입니다!",
            description=f"{desc}",
            color=RandomColor()
        )
        await ctx.send(embed=embed)
        await asyncio.sleep(int(num) * 60)
        await ctx.send(f"{ctx.author.mention}님! {num}분의 타이머가 끝났어요!\n내용: {desc}")
    if mors == "s":
        embed = discord.Embed(
            title=f"{num}초동안 타이머를 시작합니다!",
            description=f"{desc}\n\n{ctx.author.mention}님의 타이머입니다!",
            color=RandomColor()
        )
        await ctx.send(embed=embed)
        await asyncio.sleep(int(num))
        await ctx.send(f"{ctx.author.mention}님! {num}초의 타이머가 끝났어요!\n내용: {desc}")
    else:
        await ctx.send(f"{ctx.author.mention}, 으에? 그런 단위는 없는것같은데...\n사용 가능한 시간의 단위는 분(m) 그리고 초(s)에요!")


with open("config.json", "r") as configjsonFile:
    configData = json.load(configjsonFile)
    TOKEN = configData["DISCORD_TOKEN"]

@bot.event
async def on_member_join(member):
    await update_totals(member)
    await bot.db.commit()
        
@bot.event
async def on_member_remove(member):
    cur = await bot.db.execute("SELECT inviter_id FROM joined WHERE guild_id = ? and joiner_id = ?", (member.guild.id, member.id))
    res = await cur.fetchone()
    if res is None:
        return
    
    inviter = res[0]
    
    await bot.db.execute("DELETE FROM joined WHERE guild_id = ? AND joiner_id = ?", (member.guild.id, member.id))
    await bot.db.execute("DELETE FROM totals WHERE guild_id = ? AND inviter_id = ?", (member.guild.id, member.id))
    await bot.db.execute("UPDATE totals SET left = left + 1 WHERE guild_id = ? AND inviter_id = ?", (member.guild.id, inviter))
    await bot.db.commit()

@bot.event
async def on_invite_create(invite):
    await bot.db.execute("INSERT OR IGNORE INTO totals (guild_id, inviter_id, normal, left, fake) VALUES (?,?,?,?,?)", (invite.guild.id, invite.inviter.id, invite.uses, 0, 0))
    await bot.db.execute("INSERT OR IGNORE INTO invites (guild_id, id, uses) VALUES (?,?,?)", (invite.guild.id, invite.id, invite.uses))
    await bot.db.commit()
    
@bot.event
async def on_invite_delete(invite):
    await bot.db.execute("DELETE FROM invites WHERE guild_id = ? AND id = ?", (invite.guild.id, invite.id))
    await bot.db.commit()

@bot.event
async def on_guild_join(guild): # add new invites to monitor
    for invite in await guild.invites():
        await bot.db.execute("INSERT OR IGNORE INTO invites (guild_id, id, uses), VAlUES (?,?,?)", (guild.id, invite.id, invite.uses))
        
    await bot.db.commit()
    
@bot.event
async def on_guild_remove(guild): # remove all instances of the given guild_id
    await bot.db.execute("DELETE FROM totals WHERE guild_id = ?", (guild.id,))
    await bot.db.execute("DELETE FROM invites WHERE guild_id = ?", (guild.id,))
    await bot.db.execute("DELETE FROM joined WHERE guild_id = ?", (guild.id,))

    await bot.db.commit()
    
# commands
@bot.command()
async def 초대(ctx, member: discord.Member=None):
    if member is None: member = ctx.author

    # get counts
    cur = await bot.db.execute("SELECT normal, left, fake FROM totals WHERE guild_id = ? AND inviter_id = ?", (ctx.guild.id, member.id))
    res = await cur.fetchone()
    if res is None:
        normal, left, fake = 0, 0, 0

    else:
        normal, left, fake = res

    total = normal - (left + fake)
    
    em = discord.Embed(
        title=f"{member.name}#{member.discriminator}님의 초대정보입니다.",
        description=f"{member.mention} 현재 **{total}** 명 초대했습니다. (**{normal}** 표준, **{left}** 왼쪽, **{fake}** 모조품).",
        colour=discord.Colour.orange())

    await ctx.send(embed=em)
    
async def setup():
    await bot.wait_until_ready()
    bot.db = await aiosqlite.connect("inviteData.db")
    await bot.db.execute("CREATE TABLE IF NOT EXISTS totals (guild_id int, inviter_id int, normal int, left int, fake int, PRIMARY KEY (guild_id, inviter_id))")
    await bot.db.execute("CREATE TABLE IF NOT EXISTS invites (guild_id int, id string, uses int, PRIMARY KEY (guild_id, id))")
    await bot.db.execute("CREATE TABLE IF NOT EXISTS joined (guild_id int, inviter_id int, joiner_id int, PRIMARY KEY (guild_id, inviter_id, joiner_id))")
    
    # fill invites if not there
    for guild in bot.guilds:
        for invite in await guild.invites(): # invites before bot was added won't be recorded, invitemanager/tracker don't do this
            await bot.db.execute("INSERT OR IGNORE INTO invites (guild_id, id, uses) VALUES (?,?,?)", (invite.guild.id, invite.id, invite.uses))
            await bot.db.execute("INSERT OR IGNORE INTO totals (guild_id, inviter_id, normal, left, fake) VALUES (?,?,?,?,?)", (guild.id, invite.inviter.id, 0, 0, 0))

        await bot.db.commit()
          
@bot.command()
async def 프로필2(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    wanted = Image.open("wanted.jpg")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((177,177))

    wanted.paste(pfp, (120,212))

    wanted.save("profile.jpg")

    await ctx.send(file = discord.File("profile.jpg"))
    await ctx.send(f'{ctx.author.name}님에 프로필을 사진에 옮겼습니다.')

@bot.command()
async def 텍스트(ctx, *, text = "No text entered"):

    img = Image.open("white.png")
    
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("NanumGothicBold.ttf", 50)

    draw.text((10,150), text, (1, 0, 1), font=font)

    img.save("text.png")

    await ctx.send(file = discord.File("text.png"))


@bot.command()
async def 밈(ctx):
    await ctx.send(embed=await pyrandmeme())

@bot.command(aliases = ['유저정보', "ui"])
async def information(ctx, user:discord.Member=None):
        if user == None:
            user = ctx.author
        status = str(user.status)
        if status == "online":
            status = "온라인🟢"
        elif status == "dnd":
            status = "다른용무중⛔"
        elif status == "idle":
            status = "자리비움🟡"
        else:
            status = "오프라인⚪"
        if user.bot == False:
            bot = "유저"
        else:
            bot = "봇"
        try:
            game = str(ctx.author.activities[0].name)
            act = str(ctx.author.activity)
        except:
            game = "없음"
            act = "없음"
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=f'{user.name}의 정보', color=embedcolor)
        embed.add_field(name="이름", value=user.name, inline=False)
        embed.add_field(name="별명", value=user.display_name)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=user.id)
        embed.add_field(name="상태", value=f"{status}", inline=False)
        embed.add_field(name="사용자 지정 상태", value=f"{act}", inline=False)
        embed.add_field(name="게임 활동", value=game)
        embed.add_field(name="최상위 역할", value=user.top_role.mention, inline=False)
        embed.add_field(name="봇", value=bot)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

@bot.event
async def on_message_delete(message):
    json = await readjson('anno')
    try:
        channel = bot.get_channel(json[str(message.guild.id)])
        dem = discord.Embed(title='메세지 삭제됨', description=f'{message.channel.mention}에서 메세지 **{message.id}** 삭제됨\n**메세지 내용**: {message.content}', timestamp=datetime.datetime.utcnow(), colour=0xFF0000)
        dem.set_author(name=f'메세지 작성자 - {message.author} ({message.author.id})', icon_url=f'{message.author.avatar_url}')
        return await channel.send(embed=dem)
    except AttributeError:
        pass

@bot.event
async def on_member_join(member):
    json = await readjson('anno')
    try:
        channel = bot.get_channel(json[str(member.guild.id)])
        if member.bot:
            jem = discord.Embed(title='입장로그', description=f'**{member}** 님이 서버에 입장하셨습니다.', timestamp=datetime.datetime.utcnow(), colour=0x00ff2a)
            jem.set_thumbnail(url=member.avatar_url)
            jem.add_field(name='🤖봇 입니다.', value=f'닉네임: **{member}**\n아이디: **{member.id}**\n멘션: {member.mention}')
            return await channel.send(embed=jem)
        else:
            jem = discord.Embed(title='입장로그', description=f'**{member}** 님이 서버에 입장하셨습니다.', timestamp=datetime.datetime.utcnow(), colour=0x00ff2a)
            jem.set_thumbnail(url=member.avatar_url)
            jem.add_field(name='👤유저 입니다.', value=f'닉네임: **{member}**\n아이디: **{member.id}**\n멘션: {member.mention}')
            return await channel.send(embed=jem)
    except AttributeError:
        pass

@bot.event
async def on_member_remove(member):
    json = await readjson('anno')
    try:
        channel = bot.get_channel(json[str(member.guild.id)])
        if member.bot:
            jem = discord.Embed(title='퇴장로그', description=f'**{member}** 님이 서버에서 퇴장하셨습니다', timestamp=datetime.datetime.utcnow(), colour=0xff0000)
            jem.set_thumbnail(url=member.avatar_url)
            jem.add_field(name='🤖봇 입니다.', value=f'닉네임: **{member}**\n아이디: **{member.id}**\n멘션: {member.mention}')
            return await channel.send(embed=jem)
        else:
            jem = discord.Embed(title='퇴장로그', description=f'**{member}** 님 서버에서 퇴장하셨습니다', timestamp=datetime.datetime.utcnow(), colour=0xff0000)
            jem.set_thumbnail(url=member.avatar_url)
            jem.add_field(name='👤유저 입니다.', value=f'닉네임: **{member}**\n아이디: **{member.id}**\n멘션: {member.mention}')
            return await channel.send(embed=jem)
    except AttributeError:
        pass

@bot.event
async def on_member_update(before, after):
    json = await readjson('anno')
    try:
        if before.nick==None and after.nick==None:
            pass
        else:
            channel = bot.get_channel(json[str(before.guild.id)])
            upem = discord.Embed(title="닉네임변경 로그", description=f'{before.mention}님 닉네임 변경\n`{before.nick}` -> `{after.nick}`', timestamp=datetime.datetime.utcnow(), colour=0xebcb00)
            upem.set_author(name=f'{before}', icon_url=before.avatar_url)
            return await channel.send(embed=upem)
    except AttributeError:
        pass

@bot.event
async def on_guild_channel_create(channel):
    json = await readjson('anno')
    try:
        logchannel = bot.get_channel(json[str(channel.guild.id)])
        chcem = discord.Embed(title='채널생성 로그', description=f'{channel.mention} 채널 생성됨', timestamp=datetime.datetime.utcnow(), colour=0x00ff2a)
        return await logchannel.send(embed=chcem)
    except AttributeError:
        pass

@bot.event
async def on_guild_channel_delete(channel):
    json = await readjson('anno')
    try:
        logchannel = bot.get_channel(json[str(channel.guild.id)])
        chcem = discord.Embed(title='채널삭제 로그', description=f'**{channel}** 채널 삭제됨', timestamp=datetime.datetime.utcnow(), colour=0xff0000)
        return await logchannel.send(embed=chcem)
    except AttributeError:
        pass

@bot.event
async def on_webhooks_update(channel):
    json = await readjson('anno')
    try:
        logchannel = bot.get_channel(json[str(channel.guild.id)])
        em = discord.Embed(title='웹훅업데이트 로그', description=f'{channel.mention} 채널에 웹훅 업데이트됨', timestamp=datetime.datetime.utcnow(), colour=0xebcb00)
        return await logchannel.send(embed=em)
    except AttributeError:
        pass

@bot.event
async def on_guild_role_create(role):
    json = await readjson('anno')
    try:
        logchannel = bot.get_channel(json[str(role.guild.id)])
        em = discord.Embed(title='역할생성 로그', description=f'{role.mention} 역할 생성됨', timestamp=datetime.datetime.utcnow(), colour=0x00ff2a)
        return await logchannel.send(embed=em)
    except AttributeError:
        pass

@bot.event
async def on_guild_role_delete(role):
    json = await readjson('anno')
    try:
        logchannel = bot.get_channel(json[str(role.guild.id)])
        em = discord.Embed(title='역할삭제 로그', description=f'**{role}** 역할 삭제됨', timestamp=datetime.datetime.utcnow(), colour=0xff0000)
        return await logchannel.send(embed=em)
    except AttributeError:
        pass

@bot.event
async def on_member_ban(guild, member):
    json = await readjson('anno')
    try:
        logchannel = bot.get_channel(json[str(guild.id)])
        em = discord.Embed(title='유저 밴 로그', description=f'{member.mention}님이 관리자에 의해 **차단** 됨', timestamp=datetime.datetime.utcnow(), colour=0xebcb00)
        return await logchannel.send(embed=em)
    except AttributeError:
        pass

@bot.event
async def on_member_unban(guild, member):
    json = await readjson('anno')
    try:
        logchannel = bot.get_channel(json[str(guild.id)])
        em = discord.Embed(title='유저 언밴 로그', description=f'**{member}**님이 관리자에 의해 **차단해제** 됨', timestamp=datetime.datetime.utcnow(), colour=0x1f80ff)
        return await logchannel.send(embed=em)
    except AttributeError:
        pass

@bot.event
async def on_invite_create(invite):
    json = await readjson('anno')
    try:
        logchannel = bot.get_channel(json[str(invite.guild.id)])
        em = discord.Embed(title='초대링크 생성 로그', description=f'`{invite}` 초대링크 생성됨', timestamp=datetime.datetime.utcnow(), colour=0x00ff2a)
        return await logchannel.send(embed=em)
    except AttributeError:
        pass



@bot.command()
async def 로그채널(ctx, channel: discord.TextChannel):
    if ctx.message.author.guild_permissions.administrator:
        json = await readjson('anno')
        json[str(ctx.guild.id)] = int(channel.id)
        await writejson('anno', json)
        embed = discord.Embed(title=f'채널을 로그채널로 등록하였습니다.', description=f"등록된 채널 : <#{channel.id}>", timestamp=datetime.datetime.utcnow(), colour=0x00FFB7)
        embed.set_footer(text=ctx.author,icon_url=ctx.author.avatar_url)
        return await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="명령어 실행중 오류가 발생했습니다.\n", description=f"**해당 명령어는 서버관리자만 사용할 수 있습니다.**", timestamp=datetime.datetime.utcnow(), colour=0x00FFB7)
        embed.set_footer(text=ctx.author,icon_url=ctx.author.avatar_url)
        return await ctx.send(embed=embed)



bot.loop.create_task(setup())
bot.run(TOKEN)
bot.remove_command("help")
asyncio.run(bot.db.close())
