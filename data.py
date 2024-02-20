#!/usr/bin/env python3
import json
import sys
from dataclasses import dataclass
import math


@dataclass
class Pal:
    index: int
    name: str
    power: int
    tiebreak: int
    unique: bool
    only_same: bool


breed_powers = {
    'chikipi': 1500,
    'teafant': 1490,
    'mau': 1480,
    'lamball': 1470,
    'cattiva': 1460,
    'cremis': 1455,
    'vixy': 1450,
    'mau cryst': 1440,
    'lifmunk': 1430,
    'hangyu cryst': 1422,
    'hangyu': 1420,
    'sparkit': 1410,
    'flambelle': 1405,
    'foxparks': 1400,
    'hoocrates': 1390,
    'depresso': 1380,
    'jolthog': 1370,
    'jolthog cryst': 1360,
    'pengullet': 1350,
    'tocotoco': 1340,
    'fuack': 1330,
    'bristla': 1320,
    'ribunny': 1310,
    'swee': 1300,
    'killamari': 1290,
    'flopie': 1280,
    'kelpsea ignis': 1270,
    'kelpsea': 1260,
    'tanzee': 1250,
    'gumoss': 1240,
    'gumoss (special)': 1240,
    'daedream': 1230,
    'fuddler': 1220,
    'dazzi': 1210,
    'woolipop': 1190,
    'nox': 1180,
    'wixen': 1160,
    'rooby': 1155,
    'maraith': 1150,
    'leezpunk ignis': 1140,
    'rushoar': 1130,
    'leezpunk': 1120,
    'lunaris': 1110,
    'gobfin ignis': 1100,
    'gobfin': 1090,
    'cawgnito': 1080,
    'beegarde': 1070,
    'direhowl': 1060,
    'vaelet': 1050,
    'gorirat': 1040,
    'galeclaw': 1030,
    'robinquill': 1020,
    'felbat': 1010,
    'robinquill terra': 1000,
    'verdash': 990,
    'fenglope': 980,
    'loupmoon': 950,
    'lovander': 940,
    'caprity': 930,
    'eikthyrdeer': 920,
    'mozzarina': 910,
    'eikthyrdeer terra': 900,
    'dumud': 895,
    'melpaca': 890,
    'reindrix': 880,
    'celaray': 870,
    'broncherry': 860,
    'digtoise': 850,
    'broncherry aqua': 840,
    'kitsun': 830,
    'dinossom': 820,
    'dinossom lux': 810,
    'chillet': 800,
    'arsox': 790,
    'petallia': 780,
    'foxcicle': 760,
    'tombat': 750,
    'rayhound': 740,
    'blazehowl': 710,
    'katress': 700,
    'univolt': 680,
    'blazehowl noct': 670,
    'vanwyrm': 660,
    'bushi': 640,
    'vanwyrm cryst': 620,
    'incineram': 590,
    'incineram noct': 580,
    'anubis': 570,
    'surfent': 560,
    'surfent terra': 550,
    'elphidran': 540,
    'elphidran aqua': 530,
    'penking': 520,
    'grintale': 510,
    'azurobe': 500,
    'cinnamoth': 490,
    'wumpo botan': 480,
    'kingpaca': 470,
    'wumpo': 460,
    'sibelyx': 450,
    'kingpaca cryst': 440,
    'mossanda': 430,
    'nitewing': 420,
    'sweepa': 410,
    'mossanda lux': 390,
    'ragnahawk': 380,
    'faleris': 370,
    'pyrin': 360,
    'quivern': 350,
    'warsect': 340,
    'elizabee': 330,
    'reptyro': 320,
    'jormuntide ignis': 315,
    'jormuntide': 310,
    'mammorest': 300,
    'mammorest cryst': 290,
    'relaxaurus': 280,
    'relaxaurus lux': 270,
    'menasting': 260,
    'lyleen': 250,
    'pyrin noct': 240,
    'reptyro cryst': 230,
    'beakon': 220,
    'lyleen noct': 210,
    'grizzbolt': 200,
    'helzephyr': 190,
    'astegon': 150,
    'orserk': 140,
    'cryolinx': 130,
    'frostallion': 120,
    'frostallion noct': 100,
    'jetragon': 90,
    'paladius': 80,
    'necromus': 70,
    'shadowbeak': 60,
    'suzaku': 50,
    'suzaku aqua': 30,
    'blazamut': 10
}

tiebreak_order = [
    'anubis',
    'incineram',
    'incineram noct',
    'mau',
    'mau cryst',
    'rushoar',
    'lifmunk',
    'tocotoco',
    'eikthyrdeer',
    'eikthyrdeer terra',
    'digtoise',
    'galeclaw',
    'grizzbolt',
    'teafant',
    'direhowl',
    'gorirat',
    'jolthog',
    'jolthog cryst',
    'univolt',
    'foxparks',
    'bristla',
    'lunaris',
    'pengullet',
    'dazzi',
    'gobfin',
    'gobfin ignis',
    'lamball',
    'jormuntide',
    'jormuntide ignis',
    'loupmoon',
    'hangyu',
    'hangyu cryst',
    'suzaku',
    'suzaku aqua',
    'pyrin',
    'pyrin noct',
    'elphidran',
    'elphidran aqua',
    'woolipop',
    'cryolinx',
    'melpaca',
    'surfent',
    'surfent terra',
    'cawgnito',
    'azurobe',
    'cattiva',
    'depresso',
    'fenglope',
    'reptyro',
    'reptyro cryst',
    'maraith',
    'robinquill',
    'robinquill terra',
    'relaxaurus',
    'relaxaurus lux',
    'kitsun',
    'leezpunk',
    'leezpunk ignis',
    'fuack',
    'vanwyrm',
    'vanwyrm cryst',
    'chikipi',
    'dinossom',
    'dinossom lux',
    'sparkit',
    'frostallion',
    'frostallion noct',
    'mammorest',
    'mammorest cryst',
    'felbat',
    'broncherry',
    'broncherry aqua',
    'faleris',
    'blazamut',
    'caprity',
    'reindrix',
    'shadowbeak',
    'sibelyx',
    'vixy',
    'wixen',
    'lovander',
    'hoocrates',
    'kelpsea',
    'kelpsea ignis',
    'killamari',
    'mozzarina',
    'wumpo',
    'wumpo botan',
    'vaelet',
    'nitewing',
    'flopie',
    'lyleen',
    'lyleen noct',
    'elizabee',
    'beegarde',
    'tombat',
    'mossanda',
    'mossanda lux',
    'arsox',
    'rayhound',
    'fuddler',
    'astegon',
    'verdash',
    'foxcicle',
    'jetragon',
    'daedream',
    'tanzee',
    'blazehowl',
    'blazehowl noct',
    'kingpaca',
    'kingpaca cryst',
    'gumoss',
    'gumoss (special)',
    'swee',
    'sweepa',
    'katress',
    'ribunny',
    'beakon',
    'warsect',
    'paladius',
    'nox',
    'penking',
    'chillet',
    'quivern',
    'helzephyr',
    'ragnahawk',
    'bushi',
    'celaray',
    'necromus',
    'petallia',
    'grintale',
    'cinnamoth',
    'menasting',
    'orserk',
    'cremis',
    'dumud',
    'flambelle',
    'rooby'
]

uniques = set([
    'relaxaurus lux',
    'incineram noct',
    'mau cryst',
    'vanwyrm cryst',
    'eikthyrdeer terra',
    'elphidran aqua',
    'pyrin noct',
    'mammorest cryst',
    'mossanda lux',
    'dinossom lux',
    'jolthog cryst',
    'frostallion noct',
    'kingpaca cryst',
    'lyleen noct',
    'leezpunk ignis',
    'blazehowl noct',
    'robinquill terra',
    'broncherry aqua',
    'surfent terra',
    'gobfin ignis',
    'suzaku aqua',
    'reptyro cryst',
    'hangyu cryst',
    'lyleen',
    'faleris',
    'grizzbolt',
    'orserk',
    'shadowbeak',
])

unique_combos = {
    ('relaxaurus'  ,'sparkit'   ): 'relaxaurus lux',
    ('incineram'   ,'maraith'   ): 'incineram noct',
    ('mau'         ,'pengullet' ): 'mau cryst',
    ('vanwyrm'     ,'foxcicle'  ): 'vanwyrm cryst',
    ('eikthyrdeer' ,'hangyu'    ): 'eikthyrdeer terra',
    ('elphidran'   ,'surfent'   ): 'elphidran aqua',
    ('pyrin'       ,'katress'   ): 'pyrin noct',
    ('mammorest'   ,'wumpo'     ): 'mammorest cryst',
    ('mossanda'    ,'grizzbolt' ): 'mossanda lux',
    ('dinossom'    ,'rayhound'  ): 'dinossom lux',
    ('jolthog'     ,'pengullet' ): 'jolthog cryst',
    ('frostallion' ,'helzephyr' ): 'frostallion noct',
    ('kingpaca'    ,'reindrix'  ): 'kingpaca cryst',
    ('lyleen'      ,'menasting' ): 'lyleen noct',
    ('leezpunk'    ,'flambelle' ): 'leezpunk ignis',
    ('blazehowl'   ,'felbat'    ): 'blazehowl noct',
    ('robinquill'  ,'fuddler'   ): 'robinquill terra',
    ('broncherry'  ,'fuack'     ): 'broncherry aqua',
    ('surfent'     ,'dumud'     ): 'surfent terra',
    ('gobfin'      ,'rooby'     ): 'gobfin ignis',
    ('suzaku'      ,'jormuntide'): 'suzaku aqua',
    ('reptyro'     ,'foxcicle'  ): 'reptyro cryst',
    ('hangyu'      ,'swee'      ): 'hangyu cryst',
    ('mossanda'    ,'petallia'  ): 'lyleen',
    ('vanwyrm'     ,'anubis'    ): 'faleris',
    ('mossanda'    ,'rayhound'  ): 'grizzbolt',
    ('grizzbolt'   ,'relaxaurus'): 'orserk',
    ('kitsun'      ,'astegon'   ): 'shadowbeak'
}

only_same_breeds = [
    'frostallion',
    'jetragon',
    'paladius',
    'necromus',
    'jormuntide ignis'
]

pals = [
    Pal(
        index=i,
        name=name,
        power=power,
        tiebreak=tiebreak_order.index(name),
        unique=(name in uniques),
        only_same=(name in only_same_breeds)
    ) for i, (name, power) in enumerate(breed_powers.items())
]

by_index = {
    p.index: p for p in pals
}

by_name = {
    p.name: p for p in pals
}

regular_pals = [
    p for p in pals if not p.unique and not p.only_same
]


def closest(power: int) -> Pal:
    diffs = []
    for pal in regular_pals:
        diff = abs(power - pal.power)
        tiebreak = pal.tiebreak
        diffs.append((diff, tiebreak, pal))
    return sorted(diffs)[0][2]


power_to_offspring = [
    closest(i) for i in range(0, 1501)
]



def breed_power(pal1, pal2):
    return math.floor((pal1.power + pal2.power + 1) / 2)


def unique_offspring(pal1: Pal, pal2: Pal):
    if (pal1.name, pal2.name) in unique_combos:
        offspring_name = unique_combos[(pal1.name, pal2.name)]
        return by_name[offspring_name]
    if (pal2.name, pal1.name) in unique_combos:
        offspring_name = unique_combos[(pal2.name, pal1.name)]
        return by_name[offspring_name]
    return None


def same_offspring(pal1: Pal, pal2: Pal):
    if pal1 == pal2:
        return pal1


def regular_offspring(pal1: Pal, pal2: Pal):
    power = breed_power(pal1, pal2)
    return power_to_offspring(power)


def offspring(pal1: Pal, pal2: Pal):
    return (
        unique_offspring(pal1, pal2)
        or same_offspring(pal1, pal2)
        or regular_offspring(pal1, pal2)
    )


n = len(pals)
names = n * [ '' ]
for i in range(0, n):
    names[i] = by_index[i].name

offspring_map = n**2 * [ 0 ]
for i in range(0, n):
    for j in range(0, n):
        pal1 = by_index[i]
        pal2 = by_index[j]
        offspring_map[i * n + j] = offspring(pal1, pal2).index

data = {
    'names': names,
    'offspring_map': offspring_map
}

json.dump(data, sys.stdout)
