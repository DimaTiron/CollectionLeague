import disnake
from disnake.ext import commands

from functions import data_base_functions as db, variables as v, buttons, system_functions as sf, \
    dropdowns as dd


class Dropdown(disnake.ui.StringSelect):
    def __init__(self, author_mention, author_id):
        self.connection = db.connection
        self.cursor = self.connection.cursor()
        self.author_mention = author_mention
        self.author = author_id
        options = [
            disnake.SelectOption(label="Бустер необычный. Цена: 100", description="Слегка повышены шансы на все "
                                                                       "карты.", emoji="📗"),

            disnake.SelectOption(label="Бустер редкий. Цена: 350", description="Немного повышены шансы на все "
                                                                       "карты", emoji="📘"),

            disnake.SelectOption(label="Бустер эпический. Цена: 600", description="Неплохо повышены шансы на все "
                                                                       "карты.", emoji="🔮"),

            disnake.SelectOption(label="Бустер мифический. Цена: 1000", description="Хорошо повышены шансы на все "
                                                                       "карты всех сетов.", emoji="📕"),

            disnake.SelectOption(label="Бустер легендарный. Цена: 2000", description="Сильно повышены шансы на все "
                                                                       "карты.", emoji="📙"),

            disnake.SelectOption(label="Бустер секретный. Цена: 4000", description="Божественно повышены шансы на все "
                                                                       "карты.", emoji="📓")
        ]
        super().__init__(placeholder="🎴МАГАЗИН🎴",
                         min_values=1,
                         max_values=1,
                         options=options)

    async def callback(self, inter: disnake.MessageInteraction):
        if inter.author.id != self.author:
            await inter.response.send_message("Это меню не для вас!", ephemeral=True)
            return
        player_money = db.member_money(self)
        name = v.boosters_true_names_dict[self.values[0]]
        cost = v.boosters_costs_dict[self.values[0]]
        if cost < player_money:
            db.buy_booster(self, name, cost)
            await inter.response.send_message(f"{self.author_mention} Вы купили **{name}** за **{cost}** монет :coin:.")
        else:
            await inter.response.send_message(f"{self.author_mention}  У вас не хватает **{cost - player_money}**"
                                              f" монет на **{name}**.:tired_face: ")


class DropdownView(disnake.ui.View):
    def __init__(self, author_mention, author_id):
        super().__init__()
        self.author_mention = author_mention
        self.author_id = author_id  # Исправлено на author_id для ясности
        self.add_item(Dropdown(self.author_mention, self.author_id))

    async def interaction_check(self, inter: disnake.Interaction) -> bool:
        if inter.author.id != self.author_id:
            await inter.response.send_message(
                "❌ Это меню доступно только автору команды!",
                ephemeral=True
            )
            return False
        return True

