import telebot
from telebot import types
bot = telebot.TeleBot('5872934194:AAEyDaOZRypC3BuPiuc5KbxTOxRyU_9NNZg')

heroes = {
    "huskar": "Ancient Apparition, Viper, Necrophos",
    "riki": "Bounty Hunter, Bloodseeker, Bristleback",
    "bristleback": "Viper, Legion Commander, Slark Silencer",
    "viper": "Phantom Lancer, Chaos Knight, Naga Siren",
    "phantom lancer": "Beastmaster, Ember Spirit, Sven",
    "ember spirit": "Huskar, Slark, Troll Warlord",
    "void spirit": "Meepo, Naga Siren, Ember Spirit, Troll Warlord",
    "naga siren": "Underlord, Axe, Leshrac",
    "axe": "Timbersaw, 	Leshrac, Viper",
    "pudge": "Ursa, Slark, Timbersaw, Viper",
    "timbersaw": "Outworld Destroyer, Silencer, Death Prophet, Medusa",
    "outworld destroyer": "Huskar, Visage, Phantom Lancer, Templar Assassin",
    "skywrath mage": "Chaos Knight, Lycan, Templar Assassin, Tidehunter",
    "Chaos Knight": "Naga Siren, Phantom Lancer, Axe",
    "phoenix": "Marci, 	Lina, Juggernaut",
    "juggernaut": "Anti-Mage, Night Stalker, Phantom Assassin, Faceless Void",
    "faceless void": "Meepo, Naga Siren, 	Huskar, Chaos Knight",
    "lone druid": "Windranger, Bristleback, Winter Wyvern",
    "windranger": "Centaur Warrunner, Spectre, Axe",
    "spectre": "Viper, Necrophos, Undying, 	Anti-Mage",
    "anti-mage": "Meepo, Troll Warlord, Phantom Assassin, Slardar",
    "meepo": "Elder Titan, Leshrac, Sven, Winter Wyvern",
    "troll warlord": "Axe, Muerta, Slark",
    "muerta": "Spectre, Wraith King, Enchantress",
    "broodmother": "Legion Commander, Earthshaker, Phantom Lancer, Spirit Breaker",
    "marci": "Troll Warlord, Axe, Muerta",
    "earth spirit": "Marci, Enigma, Troll Warlor",
    "arc warden": "	Meepo, Lycan, Phantom Lancer, Lone Druid, Broodmother",
    "doom": "Arc Warden, Broodmother, Meepo, Lone Druid, Batrider",
    "tinker": "	Visage, Batrider, Nyx Assassin, Pugna, Anti-Mage	",
    "drow ranger": "Mars, Phantom Lancer, Spectre, Lycan, Zeus	",
    "zeus": "Mars, Anti-Mage, Storm Spirit, Bristleback, Visage,Void Spirit",
    "shadow demon": "Anti-Mage ,Meepo, Troll Warlord, Riki, Huskar,",
    "abaddon": "Dark Seer, Slark, Shadow Demon, Ancient Apparition, Lycan",
    "bane": "Naga Siren, Chaos Knight, Abaddon, Meepo, Phantom Lancer",
    "hoodwink": "Timbersaw, Tinker, Bane, Primal Beast, Puck",
    "puck": "Night Stalker,Riki, Templar Assassin, Lone Druid, Huskar,",
    "monkey king": "Batrider,Muerta, Phoenix, Ancient Apparition, Viper",
    "io": "Ancient Apparition, Troll Warlord, Monkey King, Elder Titan, Sven",
    "oracle	": "Shadow Demon, Lycan, Riki, Razor, Templar Assassin",
    "storm spirit": "Anti-Mage, Meepo, Troll Warlord, Riki, Huskar",
    "queen of pain": "Legion Commander, Puck, Anti-Mage, Huskar, Enigma",
    "legion commanderS": "Monkey King, Winter Wyvern, Troll Warlord, Pudge, Shadow Demon",
    "enigma": "Spectre, Rubick, Wraith King, Bristleback, Medusa",
    "lifestealer": "Troll Warlord, Broodmother, Enigma, Morphling, Slardar",
    "kunkka": "Lifestealer, Winter Wyvern, Juggernaut, Ember Spirit, Slardar",
    "slardar": "Terrorblade	, Naga Siren, Phantom Lancer, Troll Warlord, Medusa",
    "nyx assassin": "Templar Assassin, Lifestealer, Sven, Naga Siren, Kunkka",
    "morphling": "Nyx Assassin, Axe, Anti-Mage, Ancient Apparition, Outworld Destroyer",
    "nature's prophet": "Spectre, Phantom Assassin, Primal Beast, Naga Siren, Morphling",
    "primal beast": "Underlord, Faceless Void, Clockwerk, Leshrac, Venomancer",
    "venomancer	": "Phantom Lancer, Nature's Prophet, Dark Seer, Arc Warden, Storm Spirit",
    "dark seer": "Lone Druid, Oracle, Weaver, Ursa, Clinkz",
    "bloodseeker": "Medusa, Nature's Prophet, Juggernaut, Faceless Void, Arc Warden",
    "pangolier": "Bloodseeker, Razor, Clinkz, Queen of Pain, Mars",
    "mars": "Phantom Lancer, Lone Druid, Riki, Meepo, Void Spirit",
    "sniper": "Spectre, Mars, Morphling, Storm Spirit, Nature's Prophet",
    "silencer": "Lycan, Nature's Prophet, Legion Commander, Abaddon, Phantom Lancer",
    "leshrac": "Medusa, Ancient Apparition, Silencer, Anti-Mage, Clinkz",
    "clinkz": "Phantom Lancer, Bristleback, Naga Siren, Chaos Knight, Bounty Hunter",
    "bounty hunter": "Huskar, Naga Siren, Slark, Meepo, Omniknight",
    "underlord": "Rubick, Ursa, Timbersaw, Batrider, Juggernaut",
    "wraith king": "Phantom Lancer, Underlord, Naga Siren, Alchemist, Bristleback",
    "night stalker": "Naga Siren, Terrorblade, Wraith King, Troll Warlord, Huskar",
    "terrorblade": "Dark Seer, Axe, Naga Siren, Phantom Lancer, Sand King",
    "templar assassin": "Phantom Lancer, Batrider, Terrorblade, Spectre, Sand King",
    "sand king": "Zeus, Bristleback, Juggernaut, Sniper, Void Spirit",
    "grimstroke": "Lone Druid, Razor, Visage, Shadow Fiend, Lycan",
    "ancient apparition": "Broodmother, Anti-Mage, Lycan, Arc Warden, Phantom Lancer",
    "crystal maiden": "Rubick, Enigma, Pudge, Juggernaut, Pangolier",
    "death prophet": "Medusa, Terrorblade, Lone Druid, Broodmother, Drow Ranger",
    "disruptor": "Lone Druid, Huskar, Phantom Assassin, Terrorblade, Clinkz",
    "enchantress": "Naga Siren, Phantom Assassin, Batrider, Medusa, Tinker",
    "invoker": "Void Spirit, Broodmother, Lycan, Phantom Assassin, Phantom Lancer",
    "jakiro	": "Rubick, Clinkz, Juggernaut, Morphling, Weaver",
    "keeper of the light": "Faceless Void, Phantom Assassin, Batrider, Clinkz, Huskar",
    "lich": "Anti-Mage, Enigma, Shadow Demon, Bristleback, Bane",
    "lina": "Axe, Spectre, Clockwerk, Spirit Breaker, Phantom Assassin",
    "lion": "Beastmaster, Razor, Doom, Dragon Knight, Nature's Prophet",
    "necrophos": "Muerta, Ancient Apparition, Leshrac, Viper, Skywrath Mage",
    "oracle": "Phantom Lancer, Lone Druid, Riki, Meepo, Void Spirit",
    "pugna": "Pudge, Anti-Mage, Nature's Prophet, Medusa, Chaos Knight",
    "silencer	": "Lycan, Nature's Prophet, Legion Commander, Abaddon, Phantom Lancer",
    "rubick": "Broodmother, Primal Beast, Razor, Earth Spirit, Huskar",
    "shadow shaman": "Phantom Lancer, Meepo, Naga Siren, Chaos Knight, Terrorblade",
    "warlock": "Bristleback, Broodmother, Lycan, Weaver, Phantom Assassin",
    "witch doctor": "Broodmother, Morphling, Nature's Prophet, Bristleback, Mars",
    "gyrocopter": "Phantom Lancer, Anti-Mage, Lifestealer, Meepo, Juggernaut",
    "luna": "Spectre, Medusa, Bristleback, Phantom Lancer, Chen",
    "phantom assassin": "Omniknight, Morphling, Axe, Templar Assassin, Primal Beast",
    "razor": "Phantom Lancer, Anti-Mage, Bristleback, Weaver, Terrorblade",
    "shadow fiend": "Terrorblade, Broodmother, Zeus, Batrider, Templar Assassin",
    "ursa": "Bristleback, Phantom Lancer, Venomancer, Templar Assassin, Windranger",
    "weaver": "Faceless Void, Naga Siren, Drow Ranger, Muerta, Axe",
    "batrider": "Abaddon, Queen of Pain, Faceless Void,Brewmaster, Slark",
    "beastmaster": "Medusa, Keeper of the Light, Chen, Kunkka, Ember Spirit",
    "chen": "Lina, Weaver, Keeper of the Light, Batrider, Naga Siren",
    "clockwerk": "Phantom Lancer, Broodmother, Anti-Mage, Meepo, Lycan",
    "dark willow": "Naga Siren, Axe, Phantom Lancer, Spectre, Broodmother",
    "dazzle": "Omniknight, Slark, Riki, Ancient Apparition , Axe",
    "lycan": "Naga Siren, Troll Warlord, Axe, Underlord	, Sven",
    "magnus": "Leshrac, Huskar, Winter Wyvern, Enigma  , Puck",
    "mirana": "Naga Siren, Meepo, Broodmother, Puck, Terrorblade",
    "snapfire": "Dark Seer, Axe, Naga Siren, Phantom Lancer, Sand King",
    "techies": "Templar Assassin, Bristleback, Juggernaut, Leshrac, Enigma",
    "vengeful spirit": "Phantom Lancer, Naga Siren, Marci, Ember Spirit  , Chaos Knight",
    "venomancer": "Phantom Lancer, Nature's Prophet, Dark Seer, Arc Warden, Storm Spirit",
    "visage": "Winter Wyvern, Axe, Naga Siren, Lycan, Broodmother",
    "winter wyvern": "Anti-Mage, Timbersaw, Spectre, Necrophos, Sand King",
    "alchemist": "Ancient Apparition, Terrorblade, Batrider, Clinkz, Huskar",
    "centaur warranner": "Bristleback, Alchemist, Witch Doctor, Lifestealer, Monkey King",
    "chaos knight": "Naga Siren, Phantom Lancer, Sand King, Axe, Phoenix",
    "dawnbreaker": "Bristleback, Broodmother, Weaver, Winter Wyvern, Phoenix",
    "dragon knight": "Dark Seer, Terrorblade, Chen, Phantom Lancer, Meepo",
    "earthshaker": "Templar Assassin, Clockwerk, Viper, Enchantress, Night Stalker",
    "elder titan": "Troll Warlord, Lycan, Nature's Prophet, Lone Druid , Broodmother",
    "ogre magi": "Phantom Lancer, Naga Siren, Chaos Knight, Anti-Mage, Meepo",
    "omniknigh": "Shadow Demon, Outworld Destroyer, Leshrac, Ancient Apparition, Necrophos",
    "spirit breaker": "Underlord, Necrophos, Timbersaw, Clockwerk, Morphling",
    "sven": "Troll Warlord, Templar Assassin, Winter Wyvern, Venomancer, Terrorblade",
    "tidehunter": "Slark, Timbersaw, Razor, Ursa, Io",
    "tiny": "Necrophos, Lifestealer, Terrorblade, Venomancer, Huskar",
    "treant protector": "Leshrac, Phoenix, Slark, Timbersaw, Necrophos",
    "tusk": "Templar Assassin, Meepo, Naga Siren, Ember Spirit, Phantom Lancer",
    "undying": "Medusa, Broodmother, Elder Titan, Luna, Clinkz",

}

universal_heroes = ['/Назад', 'Abaddon', 'Bane', 'Batrider', 'Beastmaster', 'Broodmother', 'Chen',
             'Clockwerk', 'Dark Seer', 'Dark Willow', 'Dazzle', 'Enigma', 'Io', 'Lone Druid ', 'Lycan'
            'Marci', 'Magnus', 'Mirana', 'Nyx Assassin', 'Pangolier', 'Phoenix', 'Sand King', 'Snapfire', 'Techies', 'Timbersaw'
            'Vengeful Spirit', 'Venomancer', 'Visage', 'Void Spirit', 'Windranger', 'Winter Wyvern']

forces_heroes = ['/Назад', 'Mars', 'Alchemist', 'Axe', 'Bristleback', 'Centaur Warranner', 'Chaos Knight', 'Dawnbreaker', 'Doom', 'Dragon Knight',
                   'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Huskar', 'Legion Commander', 'Lifestealer', 'Night Stalker','Ogre Magi',
                   'Omniknight', 'Primal Beast', 'Pudge', 'Slardar', 'Spirit Breaker', 'Sven', 'Tidehunter', 'Tiny', 'Treant Protector',
                   'Tusk', 'Underlord', 'Undying', 'Wraith King']

agility_heroes = ['/Назад', 'Anti-Mage', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', ' Clinkz', 'Drow Ranger', 'Ember Spirit',
                  'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Luna', 'Medusa', 'Meepo', 'Monkey King',
                  'Morphling', 'Naga Siren', 'Phantom Assassin', 'Phantom Lancer', 'Razor', 'Riki', 'Shadow Fiend', 'Slark',
                  'Sniper', 'Spectre', 'Templar Assassin', 'Terrorblade', 'Troll Warlord', 'Ursa', 'Viper', 'Weaver']

intelligence_heroes = ['/Назад', 'Grimstroke', 'Ancient Apparition', 'Crystal Maiden', 'Death Prophet', 'Disruptor',
                        'Enchantress', 'Invoker', 'Jakiro', 'Keeper of the Light', 'Leshrac', 'Lich', 'Lina',
                        'Lion', 'Muerta', 'Nature Prophet', 'Necrophos', 'Oracle', 'Outworld Destroyer',
                        'Puck', 'Pugna', 'Queen of Pain', 'Rubick', 'Shadow Shaman', 'Silencer', 'Skywrath Mage',
                        'Storm Spirit', 'Tinker', 'Warlock', 'Witch Doctor', 'Zeus']

@bot.message_handler(commands=['Назад'])
@bot.message_handler(commands=['start'])
def cmd_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    forces = types.KeyboardButton('🏋️ Сила')
    agility = types.KeyboardButton('🤸 Ловкость')
    intelligence = types.KeyboardButton('🎓 Интелект')
    universal = types.KeyboardButton('🤖 Универсалы')
    markup.add(forces, agility, intelligence, universal)
    bot.send_message(message.chat.id, 'Выберите атрибут', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() in heroes:
        bot.send_message(text=heroes[message.text.lower()], chat_id=message.from_user.id)
    elif message.text == "🏋️ Сила":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for hero in forces_heroes:
            markup.add(types.KeyboardButton(hero))
        bot.send_message(message.from_user.id, "Герои силы", reply_markup=markup)
    elif message.text == "🤖 Универсалы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for hero in universal_heroes:
            markup.add(types.KeyboardButton(hero))
        bot.send_message(message.from_user.id, "Герои универсаллы", reply_markup=markup)
    elif message.text == "🤸 Ловкость":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for hero in agility_heroes:
            markup.add(types.KeyboardButton(hero))
        bot.send_message(message.from_user.id, "Герои ловкости", reply_markup=markup)
    elif message.text == "🎓 Интелект":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for hero in intelligence_heroes:
            markup.add(types.KeyboardButton(hero))
        bot.send_message(message.from_user.id, "Герои интелекта", reply_markup=markup)



bot.polling(none_stop=True, interval=0)
