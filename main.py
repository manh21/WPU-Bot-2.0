import asyncio
import os
import sys
from io import BytesIO
from random import choice

import discord
import DiscordUtils
from discord.ext import commands, tasks
from PIL import Image, ImageDraw, ImageFont

# status         =848750771323404318
# commands       =854593500137652226
# commands-error =855754099840647178
# log-perkenalan =854593552390029322
# warn-log       =856758248416870450

# server minet:
# selamat datang   =850305113554026497
# lobby            =848812370334711848
# perkenalan       =848778311119536128
# log-perkenalan   =855763615093358603

# server WPU
# selamat datang   =745872171825627157
# lobby            =758649904012197908
# perkenalan       =722024507707228160

immune = [
    376337405185097728,  # sandhikagalih
    809244553768861706,  # luminette
    738959539251970048,  # levianthz
    628868756634075167,  # avip syaifulloh
    167174392139350017,  # manh21
    556334409842688023,  # kyo
    613001683030769686,  # r4m∆iЙ
    843803437930119168,  # PG
    351681050713391104,  # alfat
    857795309266796595,  # ramset
]

orange = discord.Colour.blurple()

presence = [
    discord.Activity(
        type=discord.ActivityType.playing, name=("Jangan lupa titik koma")
    ),
    discord.Activity(type=discord.ActivityType.playing, name=("prefix: ';'")),
    discord.Activity(type=discord.ActivityType.watching, name=("Mahasiswa")),
    discord.Activity(type=discord.ActivityType.watching, name=("WPU Members")),
]

PREFIX = ["wpu; ", "wpu;", "; ", ";"]

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(
    command_prefix=PREFIX, case_insensitive=True, help_command=None, intents=intents
)

bot.remove_command("help")


@bot.command()
async def help(ctx):
    embed1 = discord.Embed(
        title="__*WPU bot's commands:*__",
        description=f"Prefix: `{bot.command_prefix}`\n<:WPU:858306984239169566> Develop by: `Luminette#0103`\nWith special helps from: `MANH21#5839`\n<:discordpy:850714601527050251> Using discord.py <:py:858307461244125215>\n‎\n\nFor Moderation commands, please use `;modhelp` ‎ ",
        color=orange,
    )
    embed1.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/831360289274069012/855781549630816287/logo-putih-polos.png"
    )
    embed1.add_field(
        name="__Github:__",
        value="https://github.com/LuminetteBourgeons/wpu-bot-2.0\n",
        inline=False,
    )
    embed1.set_footer(
        text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url
    )
    embed2 = discord.Embed(
        title="<:wpublack:723675025894539294> __Informations:__",
        description="‎ ‎ ‎ ‎ ・*Userinfo:* shows you informations about a user\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; userinfo @user` / `; userinfo`\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ > @user is optional\n‎ ‎ ‎ ‎ ・*Avatar:* shows you informations about a user's avatar\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; avatar @user` / `; avatar`\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ > @user is optional\n‎ ‎ ‎ ‎ ・*Serverinfo:* shows you informations about the server\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; serverinfo`\n‎ ‎ ‎ ‎ ・*Servericon:* shows you the server icon\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; servericon`\n‎ ‎ ‎ ‎ ・*Permissions:* shows you the user's permissions in the server\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; perms` / `; permissions`\n‎ ‎ ‎ ‎ ・*Roleinfo:* shows you the role's informations in the server\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; role <@role>` / `; roleinfo <@role>`\n‎ ‎ ‎ ‎ ・*Channelinfo:* shows you the channel's informations in the server\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; channel <#channel>` / `; channelinfo <#channel>`",
        color=orange,
    )
    embed2.set_footer(
        text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url
    )
    embed3 = discord.Embed(
        title="<:wpublack:723675025894539294> __Miscellaneous:__",
        description="‎ ‎ ‎ ‎ ・*Help:* shows you this message\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; help`\n‎ ‎ ‎ ‎ ・*Calculate:* just a common calculator...\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; calc <operation>` / `; calculate <operation>`\n‎ ‎ ‎ ‎ ・*Picking out some choice:* I'll choose for you\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; choose <opt. 1>|<opt.2>|<opt.3>|<...>` /\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; pick <opt. 1>|<opt.2>|<opt.3>|<...>`\n‎ ‎ ‎ ‎ ~~・*Making regional texts:* simply turn `this` to 🇹 🇭 🇮 🇸~~\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ~~`; regional <text>`~~\n‎ ‎ ‎ ‎ ・*Reminder:* \n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; reminder <time> <text>`\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Example:`; reminder 50m Cookies are ready!`\n‎ ‎ ‎ ‎ ・*Ping:* \n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; ping`\n‎ ‎ ‎ ‎ ・*Poll:* creates a poll where members can vote.\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; poll`",
        color=orange,
    )
    embed3.set_footer(
        text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url
    )
    embed4 = discord.Embed(
        title="🔈 __Voice Activity:__",
        description="‎ ‎ ‎ ‎ ・*Connect to a voice channel:* \n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; join`\n‎ ‎ ‎ ‎ ・*Disconnect from a voice channel:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `; leave`\n‎ ‎ ‎ ‎ ",
        color=orange,
    )
    embed4.set_footer(
        text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url
    )
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction("⏮️", "first")
    paginator.add_reaction("⏪", "back")
    paginator.add_reaction("⏩", "next")
    paginator.add_reaction("⏭️", "last")
    embeds = [embed1, embed2, embed3, embed4]
    await paginator.run(embeds)


@bot.command()
async def modhelp(ctx):
    embed = discord.Embed(
        title="__Admins commands:__",
        description=" ***Presence Changing:***\n・set<status>\n‎ ‎ ‎ ‎ `ex: setidle`\n・act<activity> <activity name>\n‎ ‎ ‎ ‎ `ex: actlistening music`\n\n‎ ‎ ‎ ‎ ***Moderations:***\n・warn @user\n・kick @user\n・ban @user\n・mute @user\n・unmute @user\n・nick @user <new nickname>\n\n‎ ‎ ‎ ‎ ***Making Embed:***\n・embed\n‎ ‎ ‎ ‎ `uses JSON`\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <https://discohook.org/> \n\n‎ ‎ ‎ ‎ ***DM***\n・dm @user <value>\n\n‎ ‎ ‎ ‎ ***Delete Messages***\n・delete <# of messages>\n・delete <# of messages> @user\n‎ ‎ ‎ ‎ has a limit of 500 messages",
        color=orange,
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/831360289274069012/855781549630816287/logo-putih-polos.png"
    )
    await ctx.send(embed=embed)


@bot.command()
async def invite(ctx):
    # ga ada
    pass


@bot.event
async def on_ready():
    # channel status
    channel = bot.get_channel(848750771323404318)
    await channel.send("Rebooting")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.competing, name=("booting...")
        )
    )
    await asyncio.sleep(5)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.competing, name=("development")
        )
    )
    print("WPU is online.")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Error!",
            description="You are missing the permission `"
            + ", ".join(error.missing_perms)
            + "` to execute this command!",
            color=discord.Colour.red(),
        )
        await ctx.send(embed=embed, delete_after=7)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Error!",
            description=str(error).capitalize(),
            color=discord.Colour.red(),
        )
        await ctx.send(embed=embed, delete_after=7)

    if isinstance(
        error,
        (
            commands.MissingPermissions,
            commands.MissingRequiredArgument,
            commands.ChannelNotFound,
            commands.MemberNotFound,
        ),
    ):
        channel = bot.get_channel(855754099840647178)
        embed = discord.Embed(
            title=f"ERROR -- {error.__class__.__qualname__}",
            description=f"{ctx.message.content}",
            colour=discord.Color.red(),
        )
        embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
        await channel.send(
            "––––––––––––––––––––––––––––––––––––––––––––––––", embed=embed
        )

    # Don't re-raise converter errors
    if isinstance(error, (commands.ChannelNotFound, commands.MemberNotFound)):
        return

    raise error


@bot.event
async def on_member_join(member):
    if member.guild.id != 722002048643497994:
        return

    def wrapper():
        img = Image.open("Welcome.png")
        font = ImageFont.truetype("BebasNeue-Regular.ttf", 100)
        nama = member.name
        lebar, *_ = font.getsize(nama)
        if lebar > 500:
            dot, *_ = font.getsize("...")

            while lebar + dot > 500:
                nama = nama[:-1]
                lebar, *_ = font.getsize(nama)

            nama += "..."

        draw = ImageDraw.Draw(img)
        text = f"Welcome,\n {nama}\n Enjoy your stay!"
        fill_color = (255, 255, 255)
        stroke_color = (35, 150, 200)
        draw.text(
            (75, 175),
            text,
            fill=fill_color,
            stroke_width=1,
            stroke_fill=stroke_color,
            font=font,
        )
        buffer = BytesIO()
        img.save(buffer, "PNG")
        buffer.seek(0)
        return buffer

    fp = await bot.loop.run_in_executor(None, wrapper)
    filename = f"{member.name}.png"
    embed = (
        discord.Embed(
            title=f"Halo, {member.name}",
            description="<:wpublack:723675025894539294> Selamat datang di server discord\nWeb Programming UNPAS\n\nSebelum itu, silakan membuka <#745872171825627157> untuk membaca **Peraturan** server kami!\n\nDilanjutkan ke <#722024507707228160> untuk berkenalan **sesuai format**\n\nJika ada pertanyaan, jangan malu untuk bertanya kepada __Ketua Kelas__",
            colour=orange,
        )
        .set_thumbnail(url=member.avatar_url)
        .set_image(url=f"attachment://{filename.replace(' ', '_')}")
    )
    channel = bot.get_channel(758649904012197908)
    await channel.send(
        f"{member.mention} Selamat datang!",
        embed=embed,
        file=discord.File(fp, filename),
    )


@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.id in immune:
        return

    # ngasi prefix kalo ditag
    if bot.user.mentioned_in(message):
        await message.channel.send(f"My Prefix is `{bot.command_prefix}`")

    # verifikasi form
    if message.channel.id != 722024507707228160:
        return

    raw = message.content.split("\n")
    pertanyaan = [
        "siapa nama kamu",
        "asal dari mana",
        "sekolah / kuliah di mana",
        "bekerja di mana",
        "dari mana tau wpu",
        "bahasa pemrograman favorit",
        "hobby / interest",
    ]
    for data in raw:
        split = data.split("?")
        tanya = split.pop(0).lower()
        if not split or not split.pop(0).strip():
            # Jawaban tidak valid
            break

        try:
            pertanyaan.remove(tanya)
        except ValueError:
            continue

    if pertanyaan:
        await message.add_reaction("\U0000274c")
        salah = await message.channel.send(
            f"{message.author.mention}, tolong masukkan data sesuai format!"
        )
        await asyncio.sleep(5)
        await message.delete()
        await salah.delete()
        return

    await message.add_reaction("\U00002705")
    role = message.guild.get_role(730328477160439878)
    await message.author.add_roles(role)
    await message.channel.send(
        f"Terimakasih {message.author.mention}, sudah perkenalan sesuai format. Salam kenal!"
    )
    channel1 = bot.get_channel(854593552390029322)
    channel2 = bot.get_channel(855763615093358603)
    embed = discord.Embed(
        color=orange, title="Perkenalan", description=f"```{message.content}```"
    )
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await channel1.send(embed=embed)
    await channel2.send(embed=embed)


# ini buat ngeremind format formnya
@tasks.loop(minutes=20)
async def perkenalan():
    channel = bot.get_channel(722024507707228160)
    embed = discord.Embed(
        title="Halo! Untuk perkenalan, bisa copy format dibawah ini ya!",
        description="```Siapa nama kamu?\nAsal dari mana?\nSekolah / Kuliah di mana?\nBekerja di mana?\nDari mana tau WPU?\nBahasa pemrograman favorit?\nHobby / Interest?```",
        colour=discord.Color.orange(),
    )
    await channel.send(embed=embed)


@perkenalan.before_loop
async def perkenalan_before():
    await bot.wait_until_ready()


@bot.command()
async def introstart(ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
        perkenalan.start()
        await ctx.send("Auto introduction reminder has started.")
    else:
        await ctx.send("You are not allowed to use this command!")


@bot.command()
async def introstop(ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
        perkenalan.cancel()
        await ctx.send("Auto introduction reminder has stopped.")
    else:
        await ctx.send("You are not allowed to use this command!")


@bot.event
async def on_command(ctx):
    channel = bot.get_channel(854593500137652226)
    embed = discord.Embed(
        title=f"{ctx.author.name} used a command!",
        description=ctx.message.content,
        colour=discord.Color.orange(),
    )
    await channel.send("––––––––––––––––––––––––––––––––––––––––––––––––", embed=embed)


@bot.event
async def on_command_completion(ctx):
    channel = bot.get_channel(854593500137652226)
    embed = discord.Embed(
        title=f"Completed {ctx.author.name}'s command!",
        description=ctx.message.content,
        colour=discord.Color.gold(),
    )
    await channel.send(embed=embed)


@bot.command(aliases=["echo"])
async def say(ctx, *, msg):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
        await ctx.message.delete()
        await ctx.send(msg)


@bot.command()
async def servers(ctx):
    # ga ada
    pass


@tasks.loop(minutes=5)
async def presence_change():
    await asyncio.sleep(10)
    await bot.change_presence(activity=choice(presence))
    channel = bot.get_channel(848750771323404318)
    await channel.send("Changing Presence")
    print("Changing Presence")


@presence_change.before_loop
async def presence_change_before():
    await bot.wait_until_ready()


@bot.command()
async def pstart(ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
        presence_change.start()
        await ctx.send("Auto presence-changing started.")
    else:
        await ctx.send("You are not allowed to use this command!")


@bot.command()
async def pstop(ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
        presence_change.cancel()
        await ctx.send("Auto presence-changing has stopped.")
    else:
        await ctx.send("You are not allowed to use this command!")


@bot.command()
async def shutdown(ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
        await ctx.send("shutting down... good night...")
        await bot.close()


extensions = [
    "cogs.miscellaneous",
    "cogs.mod",
    "cogs.reminder",
    "cogs.voice",
    "cogs.info",
]

if __name__ == '__main__':
  for ext in extensions:
    bot.load_extension(ext)

token = ""
if sys.argv[1]: 
  token = sys.argv[1]

if os.getenv('TOKEN'):
  token = os.getenv('TOKEN')

bot.run(token)
