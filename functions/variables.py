import os
work_income = [
  1, 2, 3, 4, 5, 0, 1, 1, 2, 3,
]


backgrounds = ["rui_fight_bg.png", "beach.png", "bl_forest1.png", "chainsaw_man.png", "chainsaw_man_2.png",
               "crd_forest_1.png", "crd_pink_flowers.png", "franxx.png", "evil_maneken.png", "flowers.png",
               "franks_dinner.png", "franks_house.png", "island.png", "kon.png", "od_house.png", "rui_fight_bg.png",
               "ruins.png", "scene_bl.png", "surface.png", "daki.png", "crd_mount.png", "frost_forest.png",
               "crd_water_tanjiro.png", "arcane_graffity.png", "jinks.png", "jinks_fire.png"]

# for i in backgrounds:
#     print(os.path.exists(f"../backgrounds/{i}"))

common_cards = ["bucky_o_hare_1", "dune2000_1", "metroid_1", "prince_of_persia_1", "tempest_1", "aaron_2", "froggit_2",
                "ice_cap_2", "loox_2", "migosp_2", "moldsmal_2", "snowdrake_2", "tsunderplane_2", "vegetoid_2",
                "vulkin_2", "whimsun_2", "woshua_2", "zhenya_3", "pioner_3", "genda_3", "ikuno_4", "futoshi_4",
                "nana_4", "bim_5", "fox_devil_5", "garugari_5", "katana_man_5", "nyako_5", "reze_5", "tomato_devil_5",
                "ubuyashiki_nichikai_6", "ubuyashiki_kanatai_6", "ubuyashiki_kagaya_6", "ubuyashiki_hinaki_6",
                "ubuyashiki_amane_6", "kanae_kocho_6", "murata_6", "hand_demon_6", "tongue_demon_6", "horned_demon_6",
                "numa_oni_6", "spider_demon_father_6", "spider_demon_mother_6", "spider_demon_son_6",
                "kamado_tanjuro_6", "kamado_kie_6", "kamado_takeo_6", "kamado_hanako_6", "kamado_rokuta_6", "hisa_6",
                "singed_7", "viktor_7"]
#  "loo_loo_8", "burnie_burnz_8", "barbie_wire_8", "agent_two_8", "agent_one_8"

uncommon_cards = ["contra_1", "defender_1", "elite_1", "maniac_mansion_1", "astigmatism_2", "final_froggit_2",
                  "frisk_2", "gyftrot_2", "knight_knight_2", "migospel_2", "moldbygg_2",
                  "moldessa_2", "parsnik_2", "pyrope_2", "whimsalot_2", "yliana_3", "viola_3", "olga_dmitrievna_3",
                  "samanta_3", "mitsuru_4", "goro_4", "kishibe_5", "kwanshi_5", "tendo_michiko_5", "nakime_6",
                  "yushiro_6", "takada_naho_6", "terauchi_kiyo_6", "nakahara_sumi_6", "kyogai_6", "kamanue_6",
                  "mukago_6", "wakuraba_6", "rokuro_6", "ekko_7", "ambessa_medarda_7"]
# "collin_8", "keenie_8",
#               "cletus_8", "deerie_8"

rare_cards = ["pitfall_1", "street_fighter_1", "tekken_1", "dogamy_and_dogaressa_2", "doggo_2", "glyde_2",
              "mad_dummy_2", "dummy_2", "madjick_2", "shyren_2", "so_sorry_2", "shurik_3", "electronik_3",
              "zorome_4", "angel_5", "nayuta_5", "goto_6", "yahaba_6", "susamaru_6", "shinazugawa_genya_6",
              "rengoku_senjuro_6", "jigoro_6", "urokodaki_6", "tamayo_6", "sabito_6", "makomo_6", "makio_6",
              "suma_6", "hinatsuru_6", "gyokko_rare_6", "young_powder_7", "vander_7"
]
#  "paimon_8", "robo_fizz_8

epic_cards = ["donkey_kong_1", "mega_man2_1", "zero_tolerance_1", "greater_dog_2", "jerry_2", "lesser_dog_2",
              "mettaton_2", "muffet_2", "napstablook_2", "toriel_2", "undyne_2", "slavya_3", "lena_3", "kokoro_4",
              "miku_4", "himeno_5", "kobeni_5", "pochita_5", "enmu_6", "yoriichi_6", "gyomei_6", "kanzaki_aoi_6",
              "kanao_6", "hantengu_6", "sanemi_6", "kokushibo_6", "nezuko_6", "jayce_7", "heimerdinger_7"
]

mythic_cards = ["pac_man_1", "the_legend_of_zelda_1", "alphys_2", "asgore_2", "flowey_2", "mad_mew_mew_2",
                "mettaton_ex_2", "papyrus_2", "sans_2", "temmie_2", "undine_the_undying_2", "miku_3", "ulia_3",
                "zero_zero_one_4", "ichigo_4", "denji_5", "hayakawa_aki_5", "power_5", "muichiro_6", "obanai_6",
                "giyu_6", "gyokko_6", "mitsuri_6", "tengen_6", "daki_6", "gyutaro_6", "inosuke_6", "kamado_tanjiro_6",
                "caitlyn_7", "vi_7"]

legendary_cards = ["mortal_kombat_1", "super_mario_bros_1", "asriel_dreemurr_2", "bad_time_sans_2", "alice_3",
                   "zero_two_4", "hero_4", "makima_5", "chainsaw_man_5", "zenitsu_6", "rengoku_6", "shinobu_6", "akaza_6",
                   "douma_6", "mel_medarda_7", "jinx_7"]

secret_cards = ["battle_city_1", "gaster_2", "mudzan_6", "silko_7"]

craftable_cards = ["chara_dreemurr", "frisk", "mad_mew_mew", "mettaton_neo", "kamado_tanjiro_fire", "muzan_6"]


all_cards = sorted(list(set(common_cards + uncommon_cards + rare_cards + epic_cards + mythic_cards +
                            legendary_cards + secret_cards + craftable_cards)))

bd_params = ['cards_opened', 'common', 'uncommon', 'rare', 'epic', 'mythic', 'legendary', 'secret', 'craftable']


time_limits_per_drop = {}

all_rarities = bd_params[1:]

boosters_true_names = ["uncommon_booster", "rare_booster", "epic_booster", "mythic_booster", "legendary_booster", \
                      "secret_booster"]

boosters_true_names_dict = {
    "Бустер необычный. Цена: 100": "uncommon_booster",
    "Бустер редкий. Цена: 350": "rare_booster",
    "Бустер эпический. Цена: 600": "epic_booster",
    "Бустер мифический. Цена: 1000": "mythic_booster",
    "Бустер легендарный. Цена: 2000": "legendary_booster",
    "Бустер секретный. Цена: 4000": "secret_booster"
}

boosters_costs_dict = {
    "Бустер необычный. Цена: 100": 200,
    "Бустер редкий. Цена: 350": 350,
    "Бустер эпический. Цена: 600": 600,
    "Бустер мифический. Цена: 1000": 1000,
    "Бустер легендарный. Цена: 2000": 2000,
    "Бустер секретный. Цена: 4000": 4000
}

bd_table_create = f'''CREATE TABLE IF NOT EXISTS users (
                    name TEXT,
                    id INT,
                    cash BIGINT, {" INT, ".join(bd_params + boosters_true_names + all_cards)} INT);'''

db_len_before_cards = len(bd_params + boosters_true_names)


drop_info = {
    "craftable": {
        'drop_chance': 0,
        'cost': 500,
        'cards': craftable_cards},
    'common': {
        'drop_chance': 50,
        'cost': 56,
        'cards': common_cards},
    'uncommon': {
        'drop_chance': 22.75,
        'cost': 66,
        'cards': uncommon_cards},
    'rare': {
        'drop_chance': 13,
        'cost': 122,
        'cards': rare_cards},
    'epic': {
        'drop_chance': 6.3,
        'cost': 245,
        'cards': epic_cards},
    'mythic': {
        'drop_chance': 2.8,
        'cost': 355,
        'cards': mythic_cards},
    'legendary': {
        'drop_chance': 0.8,
        'cost': 1015,
        'cards': legendary_cards},
    'secret': {
        'drop_chance': 0.25,
        'cost': 2115,
        'cards': secret_cards},
    'coins': {
        'drop_chance': 4,
        'coins': {
            80: 0.316,
            125: 0.242,
            200: 0.179,
            260: 0.158,
            404: 0.105
        }
    }
}

admin_drop_info = {
    "craftable": {
        'drop_chance': 0,
        'cost': 500,
        'cards': craftable_cards},
    'common': {
        'drop_chance': 2,
        'cost': 36,
        'cards': common_cards},
    'uncommon': {
        'drop_chance': 21,
        'cost': 56,
        'cards': uncommon_cards},
    'rare': {
        'drop_chance': 24.5,
        'cost': 82,
        'cards': rare_cards},
    'epic': {
        'drop_chance': 17,
        'cost': 175,
        'cards': epic_cards},
    'mythic': {
        'drop_chance': 13.5,
        'cost': 305,
        'cards': mythic_cards},
    'legendary': {
        'drop_chance': 8.85,
        'cost': 810,
        'cards': legendary_cards},
    'secret': {
        'drop_chance': 5.3,
        'cost': 2050,
        'cards': secret_cards},
    'coins': {
        'drop_chance': 7.85,
        'coins': {
            100: 0.316,
            150: 0.242,
            250: 0.179,
            300: 0.158,
            404: 0.105
        }
    }
}

booster_chances_names = {                            # чтобы при попытке пользователя открыть бустер он сразу по названию
    # находил ключ того словаря, откуда должен брать шансы
    "uncommon_booster": "uncommon_booster_chances"
}

uncommon_booster_chances = {
    "craftable": {
        'drop_chance': 0,
        'cost': 500,
        'cards': craftable_cards},
    'common': {
        'drop_chance': 36,
        'cost': drop_info['common']['cost'],
        'cards': common_cards},
    'uncommon': {
        'drop_chance': 33.5,
        'cost': drop_info['uncommon']['cost'],
        'cards': uncommon_cards},
    'rare': {
        'drop_chance': 17,
        'cost': drop_info['rare']['cost'],
        'cards': rare_cards},
    'epic': {
        'drop_chance': 9,
        'cost': drop_info['epic']['cost'],
        'cards': epic_cards},
    'mythic': {
        'drop_chance': 3.1,
        'cost': drop_info['mythic']['cost'],
        'cards': mythic_cards},
    'legendary': {
        'drop_chance': 1.1,
        'cost': drop_info['legendary']['cost'],
        'cards': legendary_cards},
    'secret': {
        'drop_chance': 0.3,
        'cost': drop_info['secret']['cost'],
        'cards': secret_cards},
    }

rare_booster_chances = {
    "craftable": {
        'drop_chance': 0,
        'cost': 500,
        'cards': craftable_cards},
    'common': {
        'drop_chance': 25,
        'cost': drop_info['common']['cost'],
        'cards': common_cards},
    'uncommon': {
        'drop_chance': 32,
        'cost': drop_info['uncommon']['cost'],
        'cards': uncommon_cards},
    'rare': {
        'drop_chance': 25,
        'cost': drop_info['rare']['cost'],
        'cards': rare_cards},
    'epic': {
        'drop_chance': 12,
        'cost': drop_info['epic']['cost'],
        'cards': epic_cards},
    'mythic': {
        'drop_chance': 4.2,
        'cost': drop_info['mythic']['cost'],
        'cards': mythic_cards},
    'legendary': {
        'drop_chance': 1.45,
        'cost': drop_info['legendary']['cost'],
        'cards': legendary_cards},
    'secret': {
        'drop_chance': 0.35,
        'cost': drop_info['secret']['cost'],
        'cards': secret_cards},
    }

epic_booster_chances = {
    "craftable": {
        'drop_chance': 0,
        'cost': 500,
        'cards': craftable_cards},
    'common': {
        'drop_chance': 10,
        'cost': drop_info['common']['cost'],
        'cards': common_cards},
    'uncommon': {
        'drop_chance': 30,
        'cost': drop_info['uncommon']['cost'],
        'cards': uncommon_cards},
    'rare': {
        'drop_chance': 30,
        'cost': drop_info['rare']['cost'],
        'cards': rare_cards},
    'epic': {
        'drop_chance': 21.1,
        'cost': drop_info['epic']['cost'],
        'cards': epic_cards},
    'mythic': {
        'drop_chance': 6.5,
        'cost': drop_info['mythic']['cost'],
        'cards': mythic_cards},
    'legendary': {
        'drop_chance': 1.95,
        'cost': drop_info['legendary']['cost'],
        'cards': legendary_cards},
    'secret': {
        'drop_chance': 0.45,
        'cost': drop_info['secret']['cost'],
        'cards': secret_cards},
    }

mythic_booster_chances = {
    "craftable": {
        'drop_chance': 0,
        'cost': 500,
        'cards': craftable_cards},
    'common': {
        'drop_chance': 0,
        'cost': drop_info['common']['cost'],
        'cards': common_cards},
    'uncommon': {
        'drop_chance': 20,
        'cost': drop_info['uncommon']['cost'],
        'cards': uncommon_cards},
    'rare': {
        'drop_chance': 30,
        'cost': drop_info['rare']['cost'],
        'cards': rare_cards},
    'epic': {
        'drop_chance': 35,
        'cost': drop_info['epic']['cost'],
        'cards': epic_cards},
    'mythic': {
        'drop_chance': 10,
        'cost': drop_info['mythic']['cost'],
        'cards': mythic_cards},
    'legendary': {
        'drop_chance': 4,
        'cost': drop_info['legendary']['cost'],
        'cards': legendary_cards},
    'secret': {
        'drop_chance': 1,
        'cost': drop_info['secret']['cost'],
        'cards': secret_cards},
    }

legendary_booster_chances = {
    "craftable": {
        'drop_chance': 0,
        'cost': 500,
        'cards': craftable_cards},
    'common': {
        'drop_chance': 0,
        'cost': drop_info['common']['cost'],
        'cards': common_cards},
    'uncommon': {
        'drop_chance': 5,
        'cost': drop_info['uncommon']['cost'],
        'cards': uncommon_cards},
    'rare': {
        'drop_chance': 25,
        'cost': drop_info['rare']['cost'],
        'cards': rare_cards},
    'epic': {
        'drop_chance': 40,
        'cost': drop_info['epic']['cost'],
        'cards': epic_cards},
    'mythic': {
        'drop_chance': 20,
        'cost': drop_info['mythic']['cost'],
        'cards': mythic_cards},
    'legendary': {
        'drop_chance': 8,
        'cost': drop_info['legendary']['cost'],
        'cards': legendary_cards},
    'secret': {
        'drop_chance': 2,
        'cost': drop_info['secret']['cost'],
        'cards': secret_cards},
    }

secret_booster_chances = {
    "craftable": {
        'drop_chance': 0,
        'cost': 500,
        'cards': craftable_cards},
    'common': {
        'drop_chance': 0,
        'cost': drop_info['common']['cost'],
        'cards': common_cards},
    'uncommon': {
        'drop_chance': 0,
        'cost': drop_info['uncommon']['cost'],
        'cards': uncommon_cards},
    'rare': {
        'drop_chance': 0,
        'cost': drop_info['rare']['cost'],
        'cards': rare_cards},
    'epic': {
        'drop_chance': 33,
        'cost': drop_info['epic']['cost'],
        'cards': epic_cards},
    'mythic': {
        'drop_chance': 40,
        'cost': drop_info['mythic']['cost'],
        'cards': mythic_cards},
    'legendary': {
        'drop_chance': 18,
        'cost': drop_info['legendary']['cost'],
        'cards': legendary_cards},
    'secret': {
        'drop_chance': 9,
        'cost': drop_info['secret']['cost'],
        'cards': secret_cards},
    }
