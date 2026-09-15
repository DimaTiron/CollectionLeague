import disnake
import os
from functions import data_base_functions as db, variables as v


class SellCard(disnake.ui.View):
    def __init__(self, name, author, number, cost, rarity):
        super().__init__(timeout=60.0)
        self.name = name
        self.author = author
        self.connection = db.connection
        self.cursor = self.connection.cursor()
        self.cost = cost
        self.rarity = rarity
        self.number = number

    @disnake.ui.button(label="🎴Оставить🎴", style=disnake.ButtonStyle.green)
    async def take(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author.id:
            return
        else:
            await inter.response.send_message(f"Вы решили не продавать эту карточку.")
            self.stop()

    @disnake.ui.button(label="💸Продать💸", style=disnake.ButtonStyle.red)
    async def sell(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author.id:
            return
        else:
            if db.number_of_cards_in_inv(self, self.name, self.author) >= self.number:
                await inter.response.send_message(f"Вы продали карточку *{self.name}* за **{self.cost}** :coin:")
                db.sell_card(self)
            else:
                await inter.response.send_message(f"У вас {self.number} этой карты.")
            self.stop()


class ChoiceOneOfTwoCardsForDrop(disnake.ui.View):
    def __init__(self, cost, cost2, name, name2, rarity, rarity2, author):
        super().__init__(timeout=60.0)
        self.cost = cost
        self.cost2 = cost2
        self.name = name
        self.name2 = name2
        self.author = author
        self.rarity = rarity
        self.rarity2 = rarity2
        self.connection = db.connection
        self.cursor = self.connection.cursor()

    @disnake.ui.button(label="Первая", style=disnake.ButtonStyle.blurple)
    async def first(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author.id:
            return
        else:
            sell_or_take = SellTakeButtons(self.cost, self.name, self.rarity, self.author)
            await inter.response.send_message(f"Вы выбрали карточку "
                                              f"**{self.name}** редкости *{self.rarity}*, вы можете её продать"
                                              f" за **{self.cost}** :coin:",
                                              view=sell_or_take)
            self.stop()

    @disnake.ui.button(label="Вторая", style=disnake.ButtonStyle.blurple)
    async def second(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author.id:
            return
        else:
            sell_or_take = SellTakeButtons(self.cost2, self.name2, self.rarity2, self.author)
            await inter.response.send_message(f"Вы выбрали карточку "
                                              f"**{self.name2}** редкости *{self.rarity2}*, вы можете её продать"
                                              f" за **{self.cost2}** :coin:",
                                              view=sell_or_take)
            self.stop()


class SellTakeButtons(disnake.ui.View):
    def __init__(self, cost, name, rarity, author):
        super().__init__(timeout=60.0)
        self.cost = cost
        self.name = name
        self.author = author
        self.rarity = rarity
        self.connection = db.connection
        self.cursor = self.connection.cursor()

    @disnake.ui.button(label="🎴Взять🎴", style=disnake.ButtonStyle.green)
    async def take(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author.id:
            return
        else:
            await inter.response.send_message(f"Карточка *{self.name}* добавлена в ваш инвентарь.")
            db.take_card(self)
            db.increase_rarity(self, self.rarity)
            self.stop()

    @disnake.ui.button(label="💸Продать💸", style=disnake.ButtonStyle.blurple)
    async def sell(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author.id:
            return
        else:
            await inter.response.send_message(f"Вы продали карточку *{self.name}* за **{self.cost}** :coin:")
            db.sell_card_from_drop(self)
            self.stop()


class AfterCraftButtons(disnake.ui.View):
    def __init__(self, card_name, end_card_name, cost, rarity, author):
        super().__init__(timeout=60.0)
        self.cost = cost
        self.name_before = card_name
        self.name = end_card_name
        self.author = author
        self.rarity = rarity
        self.connection = db.connection
        self.cursor = self.connection.cursor()
        self.num_cards = db.number_of_cards_in_inv(self, self.name_before, self.author)
        self.persone_money = db.member_money(self)

    @disnake.ui.button(label="🔨Да🔨", style=disnake.ButtonStyle.green)
    async def sell(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author.id:
            return
        else:
            if self.num_cards >= 2 and self.persone_money >= self.cost:
                db.give_take_money(self, self.cost, self.author, "-")
                await inter.response.send_message(f"Вы получили карточку **{self.name}**",
                                                  file=disnake.File(f"./cards/{self.rarity}/{self.name}.png"))
                db.take_away_card(self, self.author, self.name_before, 2)
                db.take_card(self)
            else:
                await inter.response.send_message(f"У вас не хватает монет или самих карточек ("
                                                  f"нужно **{self.cost}** :coin: и *2* карточки"
                                                  f" **{self.name_before}**)",
                                                  ephemeral=True)
        self.stop()

    @disnake.ui.button(label="❌Нет❌", style=disnake.ButtonStyle.red)
    async def take(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author.id:
            return
        else:
            await inter.response.send_message(f"Вы решили не крафтить карточку.")
            self.stop()
