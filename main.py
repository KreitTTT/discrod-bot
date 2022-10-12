import discord
from discord.ext import commands
from config import settings
import random
import json
import requests

bot = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print('BOT подключен')
    await bot.change_presence(status = discord.Status.online, activity= discord.Game('Тут может быть твоя реклама'))

@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.UserInputError):
        await ctx.send(
            f"Правильное использование команды: `{ctx.prefix}{ctx.command.name}` ({ctx.command.brief}): {ctx.prefix}{ctx.command.usage}")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Команда не найдена... Повторите попытку.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Вам не хватает прав")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Вы не указали аргумент")

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int=10):
    author = ctx.message.author
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{author} удалил {amount} сообщений...")

@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Привет {author.mention}! Что бы узнать доступные команды на сервере, необходимо написать /help')

@bot.command()
async def cit(ctx):
    response = requests.get('http://api.forismatic.com/api/1.0/?%20method=getQuote&key=457653&format=json&lang=ru')
    json_data = json.loads(response.text)
    emb = discord.Embed(title=json_data['quoteText'])
    if json_data['quoteAuthor']:
        emb.add_field(name='Автор:', value=json_data['quoteAuthor'])

    await ctx.send(embed = emb)

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = 0xff9900, title = 'Рандомная лиса')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = 0xff9900, title = 'Рандомная собака')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = 0xff9900, title = 'Рандомный кот')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def wink(ctx):
    response = requests.get('https://some-random-api.ml/animu/wink')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = 0xff9900, title = 'Рандомная Wink')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def pat(ctx):
    response = requests.get('https://some-random-api.ml/animu/pat')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = 0xff9900, title = 'Рандомная Pat')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def hug(ctx):
    response = requests.get('https://some-random-api.ml/animu/hug')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = 0xff0099, title = 'Рандомная Hug')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def dev(ctx):
    embed = discord.Embed(
        title="Тык для перехода",
        description="Ссылка для перехода на страничку ВК",
        url='https://vk.com/id540461897',
    )
    await ctx.send(embed=embed)

@bot.command()
async def pong(ctx):
    await ctx.send('ping')

@bot.command()
async def help(ctx):
    emb = discord.Embed( title = 'Навигация по командам' )

    emb.add_field(name='clear', value='Очистка чата от сообщений (можно удалить опр. число сообщений)')
    emb.add_field(name='yt', value='Просмотр видео из ютуба вместе со своими друзьями')
    emb.add_field(name='game', value='Доступыне игры у бота')
    emb.add_field(name='rimage', value='Доступные случайные картинки у бота')
    emb.add_field(name='dev', value='Что бы узнать кто мой создатель и хозяин')
    emb.add_field(name='cit', value='Рандомная цитата')
    emb.add_field(name='roulette', value='Проверь свою удачу в русской рулетке')
    await ctx.send(embed = emb)

@bot.command()
async def rimage(ctx):
    emb = discord.Embed( title = 'Доступные случайные картинки на сервере' )

    emb.add_field(name='dog', value='Рандомная картинка с собакой')
    emb.add_field(name='cat', value='Рандомная картинка с котом')
    emb.add_field(name='fox', value='Рандомная картинка с лисой')
    emb.add_field(name='wink', value='Рандомная анимешная гифка с Wink')
    emb.add_field(name='pat', value='Рандомная анимешная гифка с Pat')
    emb.add_field(name='hug', value='Рандомная анимешная гифка с Hug')

    await ctx.send(embed=emb)

@bot.command()
async def game(ctx):
    emb = discord.Embed( title = 'Доступыне игры на сервере' )

    emb.add_field(name='betrayal', value='текст')
    emb.add_field(name='fishington', value='Игра где можно просто ловить рыбу.')
    emb.add_field(name='doodlecrew', value='текст')
    emb.add_field(name='wordsnacks', value='текст')
    emb.add_field(name='sketchheads', value='текст')

    await ctx.send(embed = emb)

@bot.command()
async def betrayal(ctx):
    data = {
        "max_age": 0,
        "max_uses": 0,
        "target_application_id": 773336526917861400,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot OTQ0MzE3MTEzNDQxNjE1OTAy.Yg_12A.30yk5v2JV6ocs-i9gT5I9y7Fz5M",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send("Зайдите в канал")
    else:
        await ctx.send("Зайдите в канал")

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def yt(ctx):
    data = {
        "max_age": 0,
        "max_uses": 0,
        "target_application_id": 880218394199220334,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot OTQ0MzE3MTEzNDQxNjE1OTAy.Yg_12A.30yk5v2JV6ocs-i9gT5I9y7Fz5M",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send("Зайдите в канал")
    else:
        await ctx.send("Зайдите в канал")

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def fishington(ctx):
    data = {
        "max_age": 0,
        "max_uses": 0,
        "target_application_id": 814288819477020702,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot OTQ0MzE3MTEzNDQxNjE1OTAy.Yg_12A.30yk5v2JV6ocs-i9gT5I9y7Fz5M",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send("Зайдите в канал")
    else:
        await ctx.send("Зайдите в канал")

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def doodlecrew(ctx):
    data = {
        "max_age": 0,
        "max_uses": 0,
        "target_application_id": 878067389634314250,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot OTQ0MzE3MTEzNDQxNjE1OTAy.Yg_12A.30yk5v2JV6ocs-i9gT5I9y7Fz5M",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send("Зайдите в канал")
    else:
        await ctx.send("Зайдите в канал")

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def wordsnacks(ctx):
    data = {
        "max_age": 0,
        "max_uses": 0,
        "target_application_id": 879863976006127627,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot OTQ0MzE3MTEzNDQxNjE1OTAy.Yg_12A.30yk5v2JV6ocs-i9gT5I9y7Fz5M",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send("Зайдите в канал")
    else:
        await ctx.send("Зайдите в канал")

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def sketchheads(ctx):
    data = {
        "max_age": 0,
        "max_uses": 0,
        "target_application_id": 902271654783242291,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot OTQ0MzE3MTEzNDQxNjE1OTAy.Yg_12A.30yk5v2JV6ocs-i9gT5I9y7Fz5M",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send("Зайдите в канал")
    else:
        await ctx.send("Зайдите в канал")

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def roulette(ctx):
    await ctx.send("Делаю выстрел :gun: ")
    author = ctx.message.author
    if random.randint(0, 6) == 4:
        await ctx.send(f'{author.mention} погиб :skull_crossbones: ')
    else:
        await ctx.send(f'{author.mention} выжил, тебе сегодня везет!')

@bot.command()
async def vsy(ctx):
    await ctx.send('https://youtu.be/7FjjnWfcJ-k')

@bot.command()
async def minesweeper(ctx, columns=None, rows=None, bombs=None):
        if columns is None or rows is None and bombs is None:
            if columns is not None or rows is not None or bombs is not None:
                await ctx.send("error")
                return
            else:
                columns = random.randint(3, 11)
                rows = random.randint(3, 11)
                bombs = columns * rows - 1
                bombs = bombs / 2.5
                bombs = round(random.randint(5, round(bombs)))
        try:
            columns = int(columns)
            rows = int(rows)
            bombs = int(bombs)
        except ValueError:
            await ctx.send("error")
            return
        if columns > 13 or rows > 13:
            await ctx.send('Ограничение для столбцов и строк составляет 13 из-за дискорда..')
            return
        if columns < 1 or rows < 1 or bombs < 1:
            await ctx.send('Введеные числа не могут быть нулевыми или отрицательными...')
            return
        if bombs + 1 > columns * rows:
            await ctx.send(
                ':boom:**BOOM**, у вас больше бомб, чем ячеек в сетке, или вы попытались сделать все ячейки бомбами!')
            return

        grid = [[0 for num in range(columns)] for num in range(rows)]

        loop_count = 0
        while loop_count < bombs:
            x = random.randint(0, columns - 1)
            y = random.randint(0, rows - 1)
            if grid[y][x] == 0:
                grid[y][x] = 'B'
                loop_count = loop_count + 1
            if grid[y][x] == 'B':
                pass

        pos_x = 0
        pos_y = 0
        while pos_x * pos_y < columns * rows and pos_y < rows:
            adj_sum = 0
            for (adj_y, adj_x) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                try:
                    if grid[adj_y + pos_y][adj_x + pos_x] == 'B' and adj_y + pos_y > -1 and adj_x + pos_x > -1:
                        adj_sum = adj_sum + 1
                except Exception as error:
                    pass
            if grid[pos_y][pos_x] != 'B':
                grid[pos_y][pos_x] = adj_sum
            if pos_x == columns - 1:
                pos_x = 0
                pos_y = pos_y + 1
            else:
                pos_x = pos_x + 1

        string_builder = []
        for the_rows in grid:
            string_builder.append(''.join(map(str, the_rows)))
        string_builder = '\n'.join(string_builder)
        # Replaces the numbers and B for the respective emotes and spoiler tags
        string_builder = string_builder.replace('0', '||:zero:||')
        string_builder = string_builder.replace('1', '||:one:||')
        string_builder = string_builder.replace('2', '||:two:||')
        string_builder = string_builder.replace('3', '||:three:||')
        string_builder = string_builder.replace('4', '||:four:||')
        string_builder = string_builder.replace('5', '||:five:||')
        string_builder = string_builder.replace('6', '||:six:||')
        string_builder = string_builder.replace('7', '||:seven:||')
        string_builder = string_builder.replace('8', '||:eight:||')
        final = string_builder.replace('B', '||:bomb:||')

        percentage = columns * rows
        percentage = bombs / percentage
        percentage = 100 * percentage
        percentage = round(percentage, 2)

        embed = discord.Embed(title='\U0001F642 Сапер \U0001F635', color=0xC0C0C0)
        embed.add_field(name='Столбцы:', value=columns, inline=True)
        embed.add_field(name='Ряды:', value=rows, inline=True)
        embed.add_field(name='Всего ячеек:', value=columns * rows, inline=True)
        embed.add_field(name='\U0001F4A3 Счет:', value=bombs, inline=True)
        embed.add_field(name='\U0001F4A3 Доля:', value=f'{percentage}%', inline=True)
        embed.add_field(name='Запрос от:', value=ctx.author.display_name, inline=True)
        await ctx.send(content=f'\U0000FEFF\n{final}', embed=embed)

@bot.command()
async def d6(ctx):
    await ctx.send(f':game_die: У тебе выпало {random.randint(1,6)}')
@bot.command()
async def d12(ctx):
    await ctx.send(f':game_die: У тебе выпало {random.randint(1,12)}')
@bot.command()
async def d100(ctx):
    await ctx.send(f':game_die: У тебе выпало {random.randint(1,100)}')

bot.run(settings['token'])