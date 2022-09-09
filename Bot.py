# version 1.1

import discord 
import discord.ext
from discord import File
from discord.ext import commands
from discord.ext.commands import Bot
import time
import asyncio
import os
import json
from discord import utils
from discord import Activity, ActivityType
import datetime
import random
import traceback
import os
import aiohttp
import requests
voprosmembers = []
countervopros = 0
members = []
counter = 0

PREFIX = r'!'

bot = commands.Bot(command_prefix=PREFIX)
    

@bot.command(pass_context=True)
async def test(ctx, title, descript, image, thumb):
    embed = discord.Embed(title=title, description=descript, color = 0x2f3136)
    embed.set_image(url = image)
    embed.set_thumbnail(url = thumb)
    embed.set_footer(text="wezersovvv#9439")
    embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
@commands.has_permissions(view_audit_log=True)
async def clear(ctx, amount: int):
        deleted = await ctx.message.channel.purge(limit=amount + 1)

@bot.event
async def on_voice_state_update(member,before,after):
    if after.channel.id == 833262954022830090:#вставьте свой айди канала
        mainCategory = discord.utils.get(member.guild.categories, id=833262856522301460)#вставьте свой айди группы каналов
        channel2 = await member.guild.create_voice_channel(name = f"Канал {member.display_name}", category = mainCategory)
        await member.move_to(channel2)
        await channel2.set_permissions(member, mute_members=True, move_members=True, manage_channels=True)
        def check(a,b,c):
            return len(channel2.members) == 0
        await bot.wait_for('voice_state_update',check=check)
        await channel2.delete()

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def muteall(ctx,member:discord.Member,time,*,reason=None):
    muterole = discord.utils.get(ctx.guild.roles,id=833262620420603924)
    unit = time[-1]
    if unit == 's':
        duration= int(time[:-1])
        longunit = 'секунд'
    elif unit == 'm':
        duration= int(time[:-1]) * 60
        longunit = 'минут'
    elif unit == 'h':
        duration= int(time[:-1]) * 60 * 60
        longunit = 'часов'
    else:
        await ctx.send('Неправильное время! Используйте `s`, `m` или `h` на конце сообщения.')
    await member.add_roles(muterole)
    await ctx.send(f"Вы замутили {member.mention} во всех каналах на **{time}** причина: **{reason}**")
    await asyncio.sleep(duration )
    await member.remove_roles(muterole)
    await ctx.send(f'{member.mention}, вы были размучены по истечению времени во всех каналах.')

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def mutechannel(ctx, member:discord.Member, channel:discord.TextChannel, time, *, reason):
    await channel.set_permissions(member, send_messages=False)
    unit = time[-1]
    if unit == 's':
        duration= int(time[:-1])
        longunit = 'секунд'
    elif unit == 'm':
        duration= int(time[:-1]) * 60
        longunit = 'минут'
    elif unit == 'h':
        duration= int(time[:-1]) * 60 * 60
        longunit = 'часов'
    else:
        await ctx.send('Неправильное время! Используйте `s`, `m` или `h` на конце сообщения.')
    await ctx.send(f"Вы замутили {member.mention} в канале {channel.mention} на **{time}** причина: **{reason}**")
    await asyncio.sleep(duration)
    await ctx.send(f'{member.mention}, вы были размучены по истечению времени в канале {channel.mention}.')
    await channel.set_permissions(member, overwrite=None)

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} забанен!")

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"{user} разбанен!")
    return

@bot.event
async def on_command_error(ctx, exception):


    channel = bot.get_channel(833263177050488862)#вставьте свой айди канала
    embed = discord.Embed(title=':x: Ошибка Команды(@bot.command)', colour=0xe74c3c)
    embed.add_field(name='Введённая команда', value=ctx.command)
    embed.description = f"```py\n{traceback.format_exception(type(exception), exception, exception.__traceback__)}\n```"
    embed.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embed)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Вы не указали аргументы, {ctx.author.mention}!")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, у вас нет доступа к этой команде!")


        
@bot.event
async def on_ready():
    guilds = await bot.fetch_guilds(limit = None).flatten()
    await bot.change_presence(status = discord.Status.online, activity= discord.Activity(name=f'github.com/wezersovvv', type= discord.ActivityType.watching))
    print(f'Бот запущен на {len(guilds)} серверах')
    
    
@bot.command()
@commands.has_permissions(administrator=True)
async def addemoji(ctx,id:int,emoji:discord.Emoji):
    msg = await ctx.channel.fetch_message(id)
    await msg.add_reaction(emoji)



@bot.command()
@commands.has_any_role(885538166596042803, 885538166596042803, 885538166596042803, 885538166596042803)
async def edit(ctx,msg1:int, *, msg: str = None):
    msg12 = await ctx.channel.fetch_message(msg1)
    role = discord.utils.get(ctx.guild.roles,id=885538166596042803)
    role1 = discord.utils.get(ctx.guild.roles,id=885538166596042803)
    role2 = discord.utils.get(ctx.guild.roles,id=885538166596042803)
    role3 = discord.utils.get(ctx.guild.roles,id=885538166596042803)
    roler = [885538166596042803, 885538166596042803, 885538166596042803, 885538166596042803]
    if msg:
        ptext = title = description = image = thumbnail = url = footer = author = color = simple = channel = foothericon = None
        img = thm = ds = t = u = fo = au = colo = smpl = None
        if len(msg12.embeds) > 0:
            old_em = msg12.embeds[0]
        if old_em.description != discord.Embed.Empty:
            ds = old_em.description
        if old_em.title != discord.Embed.Empty:
            t = old_em.title
        if old_em.thumbnail.url != discord.Embed.Empty:
            thm = old_em.thumbnail.url
        if old_em.image.url != discord.Embed.Empty:
            img = old_em.image.url
        if old_em.url != discord.Embed.Empty:
            u = old_em.url
        if old_em.author.name != discord.Embed.Empty:
            a = old_em.author.name
        if old_em.author.icon_url != discord.Embed.Empty:
            ai = old_em.author.icon_url
        if old_em.footer.text != discord.Embed.Empty:
            fo = old_em.footer.text
        if msg12.content is not None:
            smpl = msg12.content
        embed_values = msg.split('$')
        for i in embed_values:
            if i.strip().lower().startswith('msg '):
                ptext = i.strip()[3:].strip()
            elif i.strip().lower().startswith('t '):
                title = i.strip()[2:].strip()
            elif i.strip().lower().startswith('d '):
                description = i.strip()[2:].strip()
            elif i.strip().lower().startswith('image '):
                image = i.strip()[6:].strip()
            elif i.strip().lower().startswith('thumb '):
                thumbnail = i.strip()[6:].strip()
            elif i.strip().lower().startswith('url '):
                url = i.strip()[2:].strip()
            elif i.strip().lower().startswith('f '):
                footer = i.strip()[2:].strip()
            elif i.strip().lower().startswith('a '):
                author = i.strip()[2:].strip()
            elif i.strip().lower().startswith('c '):
                color = i.strip()[2:].strip()
            elif i.strip().lower().startswith('m '):
                simple = i.strip()[3:].strip()
            elif i.strip().lower().startswith('ch '):
                channel = i.strip()[3:].strip()
            elif i.strip().lower().startswith('fu '):
                foothericon = i.strip()[3:].strip()

        if ptext is title is description is image is thumbnail is url is footer is author is color is foothericon is None and 'field=' not in msg:
            if role in ctx.author.roles or role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles:
                return await ctx.send(content=msg)

            else:
                return await ctx.send(content=f'{ctx.author.mention}, у вас нет прав для этой команды!')
        if not ptext:
            if smpl:
                ptext = smpl
        if not title:
                title = t
        if not description:
            description = ds
        if color:
            if "#" in color:
                afa = color[+1] 
                bfa = color[+2]
                cfa = color[+3] 
                dfa = color[+4] 
                efa = color[+5] 
                ffa = color[+6]
                colo = afa+bfa+cfa+dfa+efa+ffa
                color = discord.Color(value=int(colo, 16))
            else:
                color = discord.Color(value=int(color, 16))
        if not color:
            color = old_em.color
        if ptext:
            if role in ctx.author.roles or role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles:
                if ptext == 'here' or ptext == 'everyone' or ptext.startswith('<@'):
                    if ptext == 'here':
                        ptext = '@here'
                    elif ptext == 'everyone':
                        ptext = '@everyone'
                    elif ptext.startswith('<@&'):
                        role = ptext.split()
                        role = role[0]
                        role = role[3:]
                        role = role[:-1]
                        roled = discord.utils.get(ctx.guild.roles, id=int(role))

                        if str(roled.color) != '#000000':
                            color = roled.color
                        if 'color' not in locals():
                            color = 0
                        
                        ptext = f'{ptext}'
            else:
                ptext = None
        if not simple:
            em = discord.Embed(title=title, description=description, color=color)
        if not url:
            if u:
                em = discord.Embed(title=title, description=description, url=u, color=color)
        if url:
            em = discord.Embed(title=title, description=description, url=url, color=color)
        if author:
            if role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles:
                if author == '-':
                    pass
                else:
                    if author.startswith('<@!'):
                        author = author[3:]
                        author = author[:-1]
                    else:
                        author = author[2:]
                        author = author[:-1]
                    fm2 = await bot.fetch_user(int(author))
                    em.set_author(name=f"{fm2}",icon_url=f"{fm2.avatar_url}")
            else:
                em.set_author(name=f"{ctx.author}",icon_url=f"{ctx.message.author.avatar_url}")
        if not author:
            em.set_author(name=a, icon_url=ai)
        if not image:
            if img:
                em.set_image(url=img)
        if image:
            em.set_image(url=image)
        if not thumbnail:
            if thm:
                em.set_thumbnail(url=thm)
        if thumbnail:
            em.set_thumbnail(url=thumbnail)
        if footer:
            if role in ctx.author.roles or role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles:
                if footer == '-':
                    pass
                else:
                    if foothericon:
                        if 'icon=' in footer:
                            text, icon = footer.split('icon=')
                            em.set_footer(text=text.strip()[5:], icon_url=foothericon)
                        else:
                            em.set_footer(text=f"{footer}", icon_url=foothericon)
                    else:
                        if 'icon=' in footer:
                            ext, icon = footer.split('icon=')
                            em.set_footer(text=text.strip()[5:])
                        else:
                            em.set_footer(text=f"{footer}")
            else:
                em.set_footer(text=f"wezersovvv#9439")
        if not footer:
            if foothericon:
                em.set_footer(text=fo, icon_url=foothericon)
            else:
                em.set_footer(text=fo)
        await msg12.edit(content=ptext, embed=em)

    else:
        if len(msg12.embeds) > 0:
            if msg12.content is not None:
                await msg12.edit(content=msg12.content,embed=msg12.embeds[0])
            else:
                await msg12.edit(embed=msg12.embeds[0])
        if len(msg12.embeds) == 0:
            await msg12.edit(content=msg12.content)


@bot.command()
async def say(ctx, *, msg: str = None):
    role = discord.utils.get(ctx.guild.roles,id=885538166596042803)
    role1 = discord.utils.get(ctx.guild.roles,id=885538166596042803)
    role2 = discord.utils.get(ctx.guild.roles,id=885538166596042803)
    role3 = discord.utils.get(ctx.guild.roles,id=885538166596042803)
    roler = [885538166596042803, 885538166596042803, 885538166596042803, 885538166596042803]
    prefix = r'!'
    if msg:
        ptext = title = description = image = thumbnail = url = footer = author = color = simple = channel = foothericon = None
        embed_values = msg.split('$')
        for i in embed_values:
            if i.strip().lower().startswith('msg '):
                ptext = i.strip()[3:].strip()
            elif i.strip().lower().startswith('t'):
                title = i.strip()[2:].strip()
            elif i.strip().lower().startswith('d '):
                description = i.strip()[2:].strip()
            elif i.strip().lower().startswith('image '):
                image = i.strip()[6:].strip()
            elif i.strip().lower().startswith('thumb '):
                thumbnail = i.strip()[6:].strip()
            elif i.strip().lower().startswith('url '):
                url = i.strip()[4:].strip()
            elif i.strip().lower().startswith('f '):
                footer = i.strip()[2:].strip()
            elif i.strip().lower().startswith('a '):
                author = i.strip()[2:].strip()
            elif i.strip().lower().startswith('c '):
                color = i.strip()[2:].strip()
            elif i.strip().lower().startswith('m '):
                simple = i.strip()[3:].strip()
            elif i.strip().lower().startswith('ch '):
                channel = i.strip()[3:].strip()
            elif i.strip().lower().startswith('fu '):
                foothericon = i.strip()[3:].strip()

        if ptext is title is description is image is thumbnail is url is footer is author is color is foothericon is None and 'field=' not in msg:
            if role in ctx.author.roles or role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles:
                return await ctx.send(content=msg)

            else:
                return await ctx.send(content='Неверное использвание команды')
        if color:
            if "#" in color:
                afa = color[+1] 
                bfa = color[+2]
                cfa = color[+3] 
                dfa = color[+4] 
                efa = color[+5] 
                ffa = color[+6]
                colo = afa+bfa+cfa+dfa+efa+ffa
                color = discord.Color(value=int(colo, 16))
            else:
                color = discord.Color(value=int(color, 16))
        if not color:
            color = 0x2f3136
        if ptext:
            if role in ctx.author.roles or role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles:
                if ptext == 'here' or ptext == 'everyone' or ptext.startswith('<@'):
                    if ptext == 'here':
                        ptext = '@here'
                    elif ptext == 'everyone':
                        ptext = '@everyone'
                    elif ptext.startswith('@'):
                        role = ptext.split()
                        role = role[0]
                        role = role[3:]
                        role = role[:-1]
                        roled = discord.utils.get(ctx.guild.roles, id=int(role))

                        if str(roled.color) != '#000000':
                            color = roled.color
                        if 'color' not in locals():
                            color = 0
                        
                        ptext = f'{ptext}'
            else:
                ptext = None
        if not simple:
            em = discord.Embed(title=title, description=description, color=color)
        else:
            await ctx.message.delete()
            if not channel:
                await ctx.send(simple)
            else:
                if role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles:
                    channel = channel[2:]
                    channel = channel[:-1]
                    channel = bot.get_channel(int(channel))
                    await channel.send(simple)
                    return
                else:
                    await ctx.send(content=ptext, embed=em)
        if url:
            em = discord.Embed(title=title, description=description, url=url, color=color)
        if author:
            print(len(author))
            if role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles:
                if author == '-':
                    pass
                else:
                    if author.startswith('<@!'):
                        author = author[3:]
                        author = author[:-1]
                    else:
                        author = author[2:]
                        author = author[:-1]
                    fm2 = await bot.fetch_user(int(author))
                    em.set_author(name=f"{fm2}",icon_url=f"{fm2.avatar_url}")
            else:
                em.set_author(name=f"{ctx.author}",icon_url=f"{ctx.message.author.avatar_url}")
        if not author:
            em.set_author(name=f"{ctx.author}",icon_url=f"{ctx.message.author.avatar_url}")
        if image:
            em.set_image(url=image)
        if thumbnail:
            em.set_thumbnail(url=thumbnail)
        if footer:
            if role in ctx.author.roles or role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles:
                if footer == '-':
                    pass
                else:
                    if foothericon:
                        if 'icon=' in footer:
                            text, icon = footer.split('icon=')
                            em.set_footer(text=text.strip()[5:], icon_url=foothericon)
                        else:
                            em.set_footer(text=f"{footer}", icon_url=foothericon)
                    else:
                        if 'icon=' in footer:
                            ext, icon = footer.split('icon=')
                            em.set_footer(text=text.strip()[5:])
                        else:
                            em.set_footer(text=f"{footer}")
            else:
                em.set_footer(text=f"wezersovvv#9439")
        if not footer:
            if foothericon:
                em.set_footer(text=f"wezersovvv#9439", icon_url=foothericon)
            else:
                em.set_footer(text=f"wezersovvv#9439")
        if not channel:
            await ctx.send(content=ptext, embed=em)
        else:
            if role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles:
                channel = channel[2:]
                channel = channel[:-1]
                channel = bot.get_channel(int(channel))
                await channel.send(content=ptext, embed=em)
            else:
                await ctx.send(content=ptext, embed=em)

    else:
        await ctx.send(f"Не указаны арнументы! {ctx.author.mention}!\nФорма:\n```{prefix}say $a MENTION $c HEX $t TITLE TEXT $d DESC TEXT $f FOOTER TEXT $fu URL $image URL $thumb URL```")

@bot.command()
@commands.has_any_role(885538166596042803, 885538166596042803, 885538166596042803, 885538166596042803)
async def content(ctx,msg:int):
    msg = await ctx.channel.fetch_message(msg)
    prefix = r'!'
    if len(msg.embeds) > 0:
        ds = t = f = c = a =img = thm = None
        embed = msg.embeds[0]
        if embed.description != discord.Embed.Empty:
            ds = f'&d {embed.description}'
        else:
            ds = ''
        if embed.title != discord.Embed.Empty:
            t = f'&t {embed.title}'
        else:
            t = ''
        if embed.thumbnail.url != discord.Embed.Empty:
            thm = f'&thumb {embed.thumbnail.url}'
        else: 
            thm = ''
        if embed.image.url != discord.Embed.Empty:
            img = f'&image {embed.image.url}'
        else:
            img = ''
        if embed.footer.text != discord.Embed.Empty:
            f = f'&f {embed.footer.text}'
        else:
            f = '&f -'
        if embed.author.name != discord.Embed.Empty:
            a = f'&a @{embed.author.name}'
        else:
            a = f'&a -'
        if embed.colour != discord.Embed.Empty:
            c = f'&c {embed.colour}'
        else:
            c = f''
        if embed.footer.icon_url != discord.Embed.Empty:
            fu = f'&fu {embed.footer.icon_url}'
        else:
            fu = ''
        
        await ctx.send(f'```md\n{prefix}say {a} {c} {t} {ds} {f} {fu} {img} {thm}```')



@bot.command()
@commands.has_permissions(administrator=True)
async def give(ctx,member:discord.Member,role: discord.Role):
    await ctx.send('{}, {} была выдана роль `{}`'.format(ctx.author.mention, member, role))
    try:
        await member.add_roles(role)
    except:
        roled = discord.utils.get(ctx.guild.roles, name=role)
        await member.add_roles(roled)


@muteall.error
async def muteall_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('У вас нет прав для выполнение этой команды.')   
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention}, у вас нет прав для этой команды!')    

@mutechannel.error
async def mutechannel_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('У вас нет прав для выполнение этой команды.')

    if isinstance(error, commands.MissingRole):
        await ctx.send('У вас нет прав для выполнение этой команды.')        

@edit.error
async def edit_error(ctx, error):
    prefix = r"!"
    if isinstance(error, commands.MissingRole):
        await ctx.send(f'{ctx.author.mention}, у вас нет прав для этой команды!') 

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention}, у вас нет прав для этой команды!') 

    if isinstance(error, commands.MissingRequiredArgument ):
        await ctx.send(f'Вы не указали аргументы, {ctx.author.mention}\nВозможный способ использование:\n```{prefix}edit <optional $ch ChannelID> messageID <&t | &d | &url | &c | &thumb | &image | &f | &a>\n$t для заглавы. Пример: $t Test Title\n$d для описания. Пример: $d Test Desc\n$url ссылка. Пример: $url Url\n$c цвет Hex. Пример: $c #111111\n$thumb Thumbnail. Пример: $thumb Url\nПример: {prefix}edit 620317365921513485 $t A gay title!```') 


#Paste token from discord.com
bot.run('token') 