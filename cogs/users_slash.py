import datetime
import random
import requests
from PIL import Image
import io
import disnake
import os
from random import choice

from datetime import timedelta
from disnake.ext import commands

from functions import data_base_functions as db, variables as v, buttons, system_functions as sf


class SlashUsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = db.connection
        self.cursor = self.connection.cursor()

    @commands.slash_command(name="sell", description="Продать названную карточку/карточки")
    async def sell_card(self, ctx, name=None, number=1):
        rarity_and_cost = sf.cost_genre_rarity(name)
        rarity = rarity_and_cost[0]
        cost = rarity_and_cost[1]
        button = buttons.SellCard(name, ctx.author.id, number, cost, rarity)
        await ctx.send(f"{ctx.author.mention}, вы желаете продать карточку **{name}** "
                       f"**{rarity} редкости** **{number}** раз за {cost} :coin: ?", view=button)

    @commands.slash_command(name="upgrade", description="Получить из двух одинаковых карточек "
                                                        "карточку выше по редкости того же поколения")
    async def upgrade(self, ctx, name=None):
        crafting = sf.crafting_cards(name)
        if crafting[0] == "wrong card":
            await ctx.send(f"{ctx.author.mention}, вы ввели неправильное название карты.")
        elif crafting[0] == "wrong rarity":
            await ctx.send(f"{ctx.author.mention}, из карт редкости **{crafting[1]}** нельзя ничего скрафтить.")
        else:
            craft_or_no = buttons.AfterCraftButtons(crafting[0], crafting[1], crafting[2], crafting[3], ctx.author.id)
            await ctx.send(
                f"{ctx.author.mention}, вы хотите получить карточку редкости **{crafting[3]}**"
                f" того же поколения, что и ваша карточка? \n"
                f"Это будет стоить **{crafting[2]}** :coin: и потратится 2 карточки **{crafting[0]} .**",
                view=craft_or_no
            )

    @commands.slash_command(name='see', description="Просмотреть карточку из вашего инвентаря")
    async def see(self, ctx, name=None):
        a = db.see_card(self, name, ctx.author.id)
        if a == "no":
            await ctx.send(f"В инвентаре карточка с таким названием отсутствует",
                           ephemeral=True)
        else:
            await ctx.send(f"{ctx.author.mention}", file=disnake.File(a))

    @commands.slash_command(name='drop', description="Получить случайную карточку бесплатно.")
    async def drop(self, ctx):
        if f"{ctx.author}" in v.time_limits_per_drop:
            time_left = v.time_limits_per_drop.get(f"{ctx.author}").replace(microsecond=0)
            time_left -= datetime.datetime.now().replace(microsecond=0)
            if time_left < timedelta(0):
                del v.time_limits_per_drop[f"{ctx.author}"]
        if f"{ctx.author}" not in v.time_limits_per_drop:
            weights = list(map(lambda val: val['drop_chance'], v.drop_info.values()))
            rarity = random.choices(
                list(v.drop_info.keys()),
                weights=weights,
                k=1)[0]
            rarity2 = random.choices(
                list(v.drop_info.keys()),
                weights=weights,
                k=1)[0]
            drop = sf.choose_card_for_drop(rarity)
            drop2 = sf.choose_card_for_drop(rarity2)
            if rarity == 'coins':
                await ctx.send(f"{ctx.author.mention}, **поздравляем**, вы получили **{drop}** :coin: монет!")
                db.give_take_money(self, drop, ctx.author.id, '+')
                return
            elif rarity2 == 'coins':
                await ctx.send(f"{ctx.author.mention}, **поздравляем**, вы получили **{drop2}** :coin: монет!")
                db.give_take_money(self, drop2, ctx.author.id, '+')
                return

            else:
                cost = drop[1]
                cost2 = drop2[1]
                name = drop[2]
                name2 = drop[2]
                background = Image.open(f"./backgrounds/{choice(v.backgrounds)}")\
                    .convert(mode="RGBA").resize((1080, 680))
                img2 = Image.open(f"./cards/{rarity2}/{drop2[0]}").convert("RGBA")
                img1 = Image.open(f"./cards/{rarity}/{drop[0]}").convert("RGBA")
                background.alpha_composite(img1, (50, 50))
                background.alpha_composite(img2, (635, 50))

                with io.BytesIO() as image_binary:
                    background.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    first_or_second_card = buttons.ChoiceOneOfTwoCardsForDrop(cost, cost2, name, name2, rarity,
                                                                              rarity2, ctx.author.id)
                    await ctx.send(f"{ctx.author.mention}, Вам выпали **{rarity}** и **{rarity2}** карточки,"
                                   f" поздравляем! Выберите из них лишь одну.",
                                   view=first_or_second_card,
                                   file=disnake.File(fp=image_binary, filename='image.png'))
            v.time_limits_per_drop[f"{ctx.author}"] = datetime.datetime.now() + timedelta(minutes=5)
        else:
            time_left = v.time_limits_per_drop.get(f"{ctx.author}").replace(microsecond=0)
            time_left -= datetime.datetime.now().replace(microsecond=0)
            if time_left < timedelta(0):
                del v.time_limits_per_drop[f"{ctx.author}"]
            else:
                await ctx.send(
                    f"{ctx.author.mention}, вы сможете использовать дроп только через {time_left}",
                )

    @commands.slash_command(name="work", description="Получить 0-5 монеток")
    async def work(self, ctx):
        income = random.choice([1, 2, 3, 4, 5, 0, 1, 1, 2, 3])
        db.give_take_money(self, income, ctx.author.id, '+')
        self.connection.commit()
        await ctx.send(f"**{ctx.author}**, вы заработали {income} **монеток** :coin:")
        db.give_take_money(self, income, ctx.author.id, '+')

    @commands.slash_command()
    async def buy_box(self, ctx):
        pass

    @commands.slash_command(name="chances", description="Шансы дропа")
    async def check_drop_chances(self, ctx):
        await ctx.send(embed=disnake.Embed(
            description=f"**Дроп** ничего не стоит, активируется по команде */drop* раз в несколько минут."
                        f"\n *Шанс на обычную карту* - **50%**. \n *Шанс на необычную карту* - **21.75%**. \n "
                        f"*Шанс на редкую карту* - **13%** \n *Шанс на эпическую карту* - **6.3%**."
                        f"\n *Шанс на мифическую карту* - **2.8%**. \n *Шанс на легендарную карту* - **0.8%**"
                        f"\n *Шанс на секретную карту* - **0.25%**. \n *Шанс на разное кол-во мемокоинов* - **5%**"))

    @commands.slash_command(name="inventory", description="Просмотреть свой инвентарь карт")
    async def inventory(self, ctx):
        data = self.cursor.execute(f"""SELECT * from users WHERE id = {ctx.author.id}""").fetchall()[0][12:]
        cards_data = []
        count = 1
        for el in zip(v.all_cards, data):
            if el[1] != 0:
                cards_data.append(f'{count}) {el[0]}\t\t\t\t{el[1]}шт.\n')
                count += 1
        cards = ''.join(cards_data)
        await ctx.send(embed=disnake.Embed(
            description=f" **--ИНВЕНТАРЬ--** \n"
                        f"{cards}"), ephemeral=True)

    @commands.slash_command(name="profile", description="Твоя статистика в целом")
    async def profile(self, ctx):
        opened = self.cursor.execute(f'SELECT cards_opened FROM users WHERE id = {ctx.author.id}').fetchone()[0]
        cash = self.cursor.execute(f'SELECT cash FROM users WHERE id = {ctx.author.id}').fetchone()[0]
        commons = self.cursor.execute(f"SELECT common FROM users WHERE id = {ctx.author.id}").fetchone()[0]
        uncommons = self.cursor.execute(f"SELECT uncommon FROM users WHERE id = {ctx.author.id}").fetchone()[0]
        rares = self.cursor.execute(f"SELECT rare FROM users WHERE id = {ctx.author.id}").fetchone()[0]
        epics = self.cursor.execute(f"SELECT epic FROM users WHERE id = {ctx.author.id}").fetchone()[0]
        mythics = self.cursor.execute(f"SELECT mythic FROM users WHERE id = {ctx.author.id}").fetchone()[0]
        secrets = self.cursor.execute(f"SELECT secret FROM users WHERE id = {ctx.author.id}").fetchone()[0]
        legendarys = self.cursor.execute(f"SELECT legendary FROM users WHERE id = {ctx.author.id}").fetchone()[0]
        craftable = self.cursor.execute(f"SELECT craftable FROM users WHERE id = {ctx.author.id}").fetchone()[0]
        await ctx.send(embed=disnake.Embed(
            description=f" **--ПРОФИЛЬ--**"
                        f"\n"
                        f"Ваш баланс составляет  **{cash} монеток :coin:  ** \n"
                        f"Получено карт: **{opened}**."
                        f"\n Взято обычных карт: **{commons}**"
                        f"\n Взято необычных карт: **{uncommons}**"
                        f"\n Взято редких карт: **{rares}**"
                        f"\n Взято эпических карт: **{epics}**"
                        f"\n Взято мифических карт: **{mythics}**"
                        f"\n Взято легендарных карт: **{legendarys}**"
                        f"\n Взято секретных карт: **{secrets}**"
                        f"\n Скрафчено карт: **{craftable}**"))

    @commands.slash_command(name="economy", description="Краткая сводка о ценах в игре и от чего они зависят")
    async def economy(self, ctx):
        await ctx.send(embed=disnake.Embed(
            description=
            f"Цена **Обычной** карты 1 поколения: *{v.drop_info['common']['cost'] - 1}* :coin: , с каждым поколением цена понижается на 1 :coin: \n "
            f"Цена **Необычной** карты 1 поколения: *{v.drop_info['uncommon']['cost'] - 1}* :coin: , с каждым поколением цена понижается на 1 :coin: \n"
            f"Цена **Редкой карты** 1 поколения: *{v.drop_info['rare']['cost'] - 2}* :coin: , с каждым поколением цена понижается на 2 :coin: \n"
            f"Цена **Эпической карты** 1 поколения: *{v.drop_info['epic']['cost'] - 5}* :coin: , с каждым поколением цена понижается на 5 :coin: \n"
            f"Цена **Мифической** карты 1 поколения: *{v.drop_info['mythic']['cost'] - 5}* :coin: , с каждым поколением цена понижается на 5 :coin: \n"
            f"Цена **Легендарной** карты 1 поколения: *{v.drop_info['legendary']['cost'] - 15}* :coin: , с каждым поколением цена понижается на 15 :coin: \n"
            f"Цена __**secret**__ карты 1 поколения: *{v.drop_info['secret']['cost'] - 15}* :coin: , с каждым поколением цена понижается на 15 :coin:\n"
            "\n Цена улучшения **обычных** карт: *50* :coin: \n"
            "Цена улучшения **необычных** карт: *150* :coin: \n"
            "Цена улучшения **редких** карт: *250* :coin: \n"
            "Цена улучшения **эпических** карт: *600* :coin: \n"
            "Цена улучшения **мифических** карт: *1300* :coin: \n"))

    @commands.slash_command(name="help", description="Просмотреть комманды и что они делают.")
    async def help_commands(self, ctx):
        await ctx.send(embed=disnake.Embed(
            description=f"*Команды:* \n **!!(дропинфо/шансы)** - шансы из дропа, \n "
                        f"**!!(профиль/баланс/меню)** - краткая информация о вашем аккаунте, \n "
                        f"**!!(работать/work)** - получить 0-5 монеток, \n "
                        f" **!!(дроп/drop)** - получить опр карточку раз в пару минут(зависит от настроения админа),"
                        f" \n **!!(карты/инвентарь)** - просмотреть карты, которые у тебя есть, \n"
                        f" **!!(see/посмотреть)** **(название карточки)** - посмотреть на карточку "
                        f"(только если она в инвентаре), \n**!!(улучшить/upgrade/upg)** **(название карточки)**"
                        f" - крафтится карточка"
                        f" следуюшей редкости того же поколения, но нужно иметь 2 изначальной карточки и опр. кол-во "
                        f"монет. \n"
                        f"**!!(магазин/shop)** - открывает магазин с бустерами \n"
                        f"**!!(открыть/open) (название бустера)** - позволяет открыть выбранный бустер (если он у вас есть) \n"
                        f"**!!(экономика/цены)** - показывает сводку о ценах в игре и от чего они зависят. \n"
                        f"**!!(продать/sell) (название карточки) (кол-во(по умолчанию = 1))** - "
                        f"продать выбранную карточку"))


def setup(bot):
    bot.add_cog(SlashUsers(bot))
