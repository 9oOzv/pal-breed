#!/usr/bin/env python3
import time
import random
import math
import difflib
import fire
import itertools
from dataclasses import dataclass
from typing import Self
import functools
import json

data = json.loads(r'[{"index": 0, "name": "chikipi", "power": 1500, "tiebreak_order": 61, "special": false}, {"index": 1, "name": "teafant", "power": 1490, "tiebreak_order": 13, "special": false}, {"index": 2, "name": "mau", "power": 1480, "tiebreak_order": 3, "special": false}, {"index": 3, "name": "lamball", "power": 1470, "tiebreak_order": 26, "special": false}, {"index": 4, "name": "cattiva", "power": 1460, "tiebreak_order": 45, "special": false}, {"index": 5, "name": "cremis", "power": 1455, "tiebreak_order": 134, "special": false}, {"index": 6, "name": "vixy", "power": 1450, "tiebreak_order": 78, "special": false}, {"index": 7, "name": "mau cryst", "power": 1440, "tiebreak_order": 4, "special": true}, {"index": 8, "name": "lifmunk", "power": 1430, "tiebreak_order": 6, "special": false}, {"index": 9, "name": "hangyu cryst", "power": 1422, "tiebreak_order": 31, "special": true}, {"index": 10, "name": "hangyu", "power": 1420, "tiebreak_order": 30, "special": false}, {"index": 11, "name": "sparkit", "power": 1410, "tiebreak_order": 64, "special": false}, {"index": 12, "name": "flambelle", "power": 1405, "tiebreak_order": 136, "special": false}, {"index": 13, "name": "foxparks", "power": 1400, "tiebreak_order": 19, "special": false}, {"index": 14, "name": "hoocrates", "power": 1390, "tiebreak_order": 81, "special": false}, {"index": 15, "name": "depresso", "power": 1380, "tiebreak_order": 46, "special": false}, {"index": 16, "name": "jolthog", "power": 1370, "tiebreak_order": 16, "special": false}, {"index": 17, "name": "jolthog cryst", "power": 1360, "tiebreak_order": 17, "special": true}, {"index": 18, "name": "pengullet", "power": 1350, "tiebreak_order": 22, "special": false}, {"index": 19, "name": "tocotoco", "power": 1340, "tiebreak_order": 7, "special": false}, {"index": 20, "name": "fuack", "power": 1330, "tiebreak_order": 58, "special": false}, {"index": 21, "name": "bristla", "power": 1320, "tiebreak_order": 20, "special": false}, {"index": 22, "name": "ribunny", "power": 1310, "tiebreak_order": 116, "special": false}, {"index": 23, "name": "swee", "power": 1300, "tiebreak_order": 113, "special": false}, {"index": 24, "name": "killamari", "power": 1290, "tiebreak_order": 84, "special": false}, {"index": 25, "name": "flopie", "power": 1280, "tiebreak_order": 90, "special": false}, {"index": 26, "name": "kelpsea ignis", "power": 1270, "tiebreak_order": 83, "special": false}, {"index": 27, "name": "kelpsea", "power": 1260, "tiebreak_order": 82, "special": false}, {"index": 28, "name": "tanzee", "power": 1250, "tiebreak_order": 106, "special": false}, {"index": 29, "name": "gumoss", "power": 1240, "tiebreak_order": 111, "special": false}, {"index": 30, "name": "gumoss (special)", "power": 1240, "tiebreak_order": 112, "special": false}, {"index": 31, "name": "daedream", "power": 1230, "tiebreak_order": 105, "special": false}, {"index": 32, "name": "fuddler", "power": 1220, "tiebreak_order": 100, "special": false}, {"index": 33, "name": "dazzi", "power": 1210, "tiebreak_order": 23, "special": false}, {"index": 34, "name": "woolipop", "power": 1190, "tiebreak_order": 38, "special": false}, {"index": 35, "name": "nox", "power": 1180, "tiebreak_order": 120, "special": false}, {"index": 36, "name": "wixen", "power": 1160, "tiebreak_order": 79, "special": false}, {"index": 37, "name": "rooby", "power": 1155, "tiebreak_order": 137, "special": false}, {"index": 38, "name": "maraith", "power": 1150, "tiebreak_order": 50, "special": false}, {"index": 39, "name": "leezpunk ignis", "power": 1140, "tiebreak_order": 57, "special": true}, {"index": 40, "name": "rushoar", "power": 1130, "tiebreak_order": 5, "special": false}, {"index": 41, "name": "leezpunk", "power": 1120, "tiebreak_order": 56, "special": false}, {"index": 42, "name": "lunaris", "power": 1110, "tiebreak_order": 21, "special": false}, {"index": 43, "name": "gobfin ignis", "power": 1100, "tiebreak_order": 25, "special": true}, {"index": 44, "name": "gobfin", "power": 1090, "tiebreak_order": 24, "special": false}, {"index": 45, "name": "cawgnito", "power": 1080, "tiebreak_order": 43, "special": false}, {"index": 46, "name": "beegarde", "power": 1070, "tiebreak_order": 94, "special": false}, {"index": 47, "name": "direhowl", "power": 1060, "tiebreak_order": 14, "special": false}, {"index": 48, "name": "vaelet", "power": 1050, "tiebreak_order": 88, "special": false}, {"index": 49, "name": "gorirat", "power": 1040, "tiebreak_order": 15, "special": false}, {"index": 50, "name": "galeclaw", "power": 1030, "tiebreak_order": 11, "special": false}, {"index": 51, "name": "robinquill", "power": 1020, "tiebreak_order": 51, "special": false}, {"index": 52, "name": "felbat", "power": 1010, "tiebreak_order": 69, "special": false}, {"index": 53, "name": "robinquill terra", "power": 1000, "tiebreak_order": 52, "special": true}, {"index": 54, "name": "verdash", "power": 990, "tiebreak_order": 102, "special": false}, {"index": 55, "name": "fenglope", "power": 980, "tiebreak_order": 47, "special": false}, {"index": 56, "name": "loupmoon", "power": 950, "tiebreak_order": 29, "special": false}, {"index": 57, "name": "lovander", "power": 940, "tiebreak_order": 80, "special": false}, {"index": 58, "name": "caprity", "power": 930, "tiebreak_order": 74, "special": false}, {"index": 59, "name": "eikthyrdeer", "power": 920, "tiebreak_order": 8, "special": false}, {"index": 60, "name": "mozzarina", "power": 910, "tiebreak_order": 85, "special": false}, {"index": 61, "name": "eikthyrdeer terra", "power": 900, "tiebreak_order": 9, "special": true}, {"index": 62, "name": "dumud", "power": 895, "tiebreak_order": 135, "special": false}, {"index": 63, "name": "melpaca", "power": 890, "tiebreak_order": 40, "special": false}, {"index": 64, "name": "reindrix", "power": 880, "tiebreak_order": 75, "special": false}, {"index": 65, "name": "celaray", "power": 870, "tiebreak_order": 127, "special": false}, {"index": 66, "name": "broncherry", "power": 860, "tiebreak_order": 70, "special": false}, {"index": 67, "name": "digtoise", "power": 850, "tiebreak_order": 10, "special": false}, {"index": 68, "name": "broncherry aqua", "power": 840, "tiebreak_order": 71, "special": true}, {"index": 69, "name": "kitsun", "power": 830, "tiebreak_order": 55, "special": false}, {"index": 70, "name": "dinossom", "power": 820, "tiebreak_order": 62, "special": false}, {"index": 71, "name": "dinossom lux", "power": 810, "tiebreak_order": 63, "special": true}, {"index": 72, "name": "chillet", "power": 800, "tiebreak_order": 122, "special": false}, {"index": 73, "name": "arsox", "power": 790, "tiebreak_order": 98, "special": false}, {"index": 74, "name": "petallia", "power": 780, "tiebreak_order": 129, "special": false}, {"index": 75, "name": "foxcicle", "power": 760, "tiebreak_order": 103, "special": false}, {"index": 76, "name": "tombat", "power": 750, "tiebreak_order": 95, "special": false}, {"index": 77, "name": "rayhound", "power": 740, "tiebreak_order": 99, "special": false}, {"index": 78, "name": "blazehowl", "power": 710, "tiebreak_order": 107, "special": false}, {"index": 79, "name": "katress", "power": 700, "tiebreak_order": 115, "special": false}, {"index": 80, "name": "univolt", "power": 680, "tiebreak_order": 18, "special": false}, {"index": 81, "name": "blazehowl noct", "power": 670, "tiebreak_order": 108, "special": true}, {"index": 82, "name": "vanwyrm", "power": 660, "tiebreak_order": 59, "special": false}, {"index": 83, "name": "bushi", "power": 640, "tiebreak_order": 126, "special": false}, {"index": 84, "name": "vanwyrm cryst", "power": 620, "tiebreak_order": 60, "special": true}, {"index": 85, "name": "incineram", "power": 590, "tiebreak_order": 1, "special": false}, {"index": 86, "name": "incineram noct", "power": 580, "tiebreak_order": 2, "special": true}, {"index": 87, "name": "anubis", "power": 570, "tiebreak_order": 0, "special": false}, {"index": 88, "name": "surfent", "power": 560, "tiebreak_order": 41, "special": false}, {"index": 89, "name": "surfent terra", "power": 550, "tiebreak_order": 42, "special": true}, {"index": 90, "name": "elphidran", "power": 540, "tiebreak_order": 36, "special": false}, {"index": 91, "name": "elphidran aqua", "power": 530, "tiebreak_order": 37, "special": true}, {"index": 92, "name": "penking", "power": 520, "tiebreak_order": 121, "special": false}, {"index": 93, "name": "grintale", "power": 510, "tiebreak_order": 130, "special": false}, {"index": 94, "name": "azurobe", "power": 500, "tiebreak_order": 44, "special": false}, {"index": 95, "name": "cinnamoth", "power": 490, "tiebreak_order": 131, "special": false}, {"index": 96, "name": "wumpo botan", "power": 480, "tiebreak_order": 87, "special": false}, {"index": 97, "name": "kingpaca", "power": 470, "tiebreak_order": 109, "special": false}, {"index": 98, "name": "wumpo", "power": 460, "tiebreak_order": 86, "special": false}, {"index": 99, "name": "sibelyx", "power": 450, "tiebreak_order": 77, "special": false}, {"index": 100, "name": "ice kingpaca", "power": 440, "tiebreak_order": 110, "special": true}, {"index": 101, "name": "mossanda", "power": 430, "tiebreak_order": 96, "special": false}, {"index": 102, "name": "nitewing", "power": 420, "tiebreak_order": 89, "special": false}, {"index": 103, "name": "sweepa", "power": 410, "tiebreak_order": 114, "special": false}, {"index": 104, "name": "mossanda lux", "power": 390, "tiebreak_order": 97, "special": true}, {"index": 105, "name": "ragnahawk", "power": 380, "tiebreak_order": 125, "special": false}, {"index": 106, "name": "faleris", "power": 370, "tiebreak_order": 72, "special": true}, {"index": 107, "name": "pyrin", "power": 360, "tiebreak_order": 34, "special": false}, {"index": 108, "name": "quivern", "power": 350, "tiebreak_order": 123, "special": false}, {"index": 109, "name": "warsect", "power": 340, "tiebreak_order": 118, "special": false}, {"index": 110, "name": "elizabee", "power": 330, "tiebreak_order": 93, "special": false}, {"index": 111, "name": "reptyro", "power": 320, "tiebreak_order": 48, "special": false}, {"index": 112, "name": "jormuntide ignis", "power": 315, "tiebreak_order": 28, "special": false}, {"index": 113, "name": "jormuntide", "power": 310, "tiebreak_order": 27, "special": false}, {"index": 114, "name": "mammorest", "power": 300, "tiebreak_order": 67, "special": false}, {"index": 115, "name": "mammorest cryst", "power": 290, "tiebreak_order": 68, "special": true}, {"index": 116, "name": "relaxaurus", "power": 280, "tiebreak_order": 53, "special": false}, {"index": 117, "name": "relaxaurus lux", "power": 270, "tiebreak_order": 54, "special": true}, {"index": 118, "name": "menasting", "power": 260, "tiebreak_order": 132, "special": false}, {"index": 119, "name": "lyleen", "power": 250, "tiebreak_order": 91, "special": true}, {"index": 120, "name": "pyrin noct", "power": 240, "tiebreak_order": 35, "special": true}, {"index": 121, "name": "reptyro cryst", "power": 230, "tiebreak_order": 49, "special": true}, {"index": 122, "name": "beakon", "power": 220, "tiebreak_order": 117, "special": false}, {"index": 123, "name": "lyleen noct", "power": 210, "tiebreak_order": 92, "special": true}, {"index": 124, "name": "grizzbolt", "power": 200, "tiebreak_order": 12, "special": true}, {"index": 125, "name": "helzephyr", "power": 190, "tiebreak_order": 124, "special": false}, {"index": 126, "name": "astegon", "power": 150, "tiebreak_order": 101, "special": false}, {"index": 127, "name": "orserk", "power": 140, "tiebreak_order": 133, "special": true}, {"index": 128, "name": "cryolinx", "power": 130, "tiebreak_order": 39, "special": false}, {"index": 129, "name": "frostallion", "power": 120, "tiebreak_order": 65, "special": false}, {"index": 130, "name": "frostallion noct", "power": 100, "tiebreak_order": 66, "special": true}, {"index": 131, "name": "jetragon", "power": 90, "tiebreak_order": 104, "special": false}, {"index": 132, "name": "paladius", "power": 80, "tiebreak_order": 119, "special": false}, {"index": 133, "name": "necromus", "power": 70, "tiebreak_order": 128, "special": false}, {"index": 134, "name": "shadowbeak", "power": 60, "tiebreak_order": 76, "special": true}, {"index": 135, "name": "suzaku", "power": 50, "tiebreak_order": 32, "special": false}, {"index": 136, "name": "suzaku aqua", "power": 30, "tiebreak_order": 33, "special": true}, {"index": 137, "name": "blazamut", "power": 10, "tiebreak_order": 73, "special": false}]')


names = [v['name'] for v in data]
specials = [v['special'] for v in data]
powers = [v['power'] for v in data]
power_indice = {v: i for i, v in enumerate(powers)}
indice = {v['name']: i for i, v in enumerate(data)}
tiebreaks = [v['tiebreak_order'] for v in data]
sorted_powers = sorted(powers)


def closest(raw):
    lower = None
    higher = None
    diffs = [ 
        (
            abs(raw - powers[i]),
            tiebreaks[i],
            i
        ) for i, v in enumerate(data)
    ]
    return sorted(diffs)[0][2]


power_map = [
    closest(i) for i in range(0, 1501)
]

gender_marks = {
    0: '',
    1: '♀',
    -1: '♂'
}

@dataclass
class Pal:
    index: int
    parent1: Self | None = None
    parent2: Self | None = None
    gender: int = 0

    def __init__(
            self,
            index: int,
            gender: int = 0,
            parent1: int | Self = None,
            parent2: int | Self = None):
        self.parent1 = parent1
        self.parent2 = parent2
        self.index = index
        self.gender = gender

    @property
    def num_breeds(self):
        return (
            (1 + self.parent1.num_breeds if self.parent1 else 0)
            + (self.parent2.num_breeds if self.parent2 else 0)
        )

    @property
    def breed_depth(self):
        return max(
            self.parent1.breed_depth + 1 if self.parent1 else 0,
            self.parent2.breed_depth + 1 if self.parent2 else 0
        )

    def __repr__(self):
        if self.parent1:
            return f'({self.parent1} + {self.parent2}) -> {names[self.index]}{gender_marks[self.gender]}'
        else:
            return f'{names[self.index]}{gender_marks[self.gender]}'


def calculate_offspring(pal1: Pal, pal2: Pal):
    if pal1.gender != 0 and pal2.gender != 0:
        if pal1.gender == pal2.gender:
            return None
    index1 = pal1.index if isinstance(pal1, Pal) else pal1
    index2 = pal2.index if isinstance(pal2, Pal) else pal2
    raw = math.floor((powers[index1] + powers[index2] + 1) / 2)
    return Pal(
        power_map[raw],
        parent1=pal1,
        parent2=pal2
    )


def _breed(X: list[int | Pal], Y: list[int | Pal]):
    Z = [calculate_offspring(x, y) for x in X for y in Y]
    return [z for z in Z if z is not None]


def breed(X: list[Pal], Y: list[Pal], Z: list[Pal] | None = None, W: list[Pal] | None = None):
    XY = _breed(X, Y)
    if Z:
        XZ = _breed(X, Z)
        YZ = _breed(Y, Z)
        if W:
            XW = _breed(X, W)
            YW = _breed(Y, W)
            ZW = _breed(Z, W)
        YZ_X = _breed(YZ, X)
        XY_Z = _breed(XY, Z)
        if W:
            XY_W = _breed(XY, W)
            XZ_W = _breed(XZ, W)
            YZ_W = _breed(YZ, W)
            ZW_X = _breed(ZW, X)
            ZW_Y = _breed(ZW, Y)
            XY_Z_W = _breed(XY_Z, W)
            XY_W_Z = _breed(XY_W, Z)
            XZ_W_Y = _breed(XZ_W, Y)
            YZ_X_W = _breed(YZ_X, W)
            YZ_W_X = _breed(YZ_W, X)
            ZW_X_Y = _breed(ZW_X, Y)
            ZW_Y_X = _breed(ZW_Y, X)
            XY_ZW = _breed(XY, ZW)
            XZ_YW = _breed(XZ, YW)
            XW_YZ = _breed(XW, YZ)
    if W:
        breeds = [
            *XY,
            *XZ,
            *XW,
            *YZ,
            *YW,
            *ZW,
            *XY_Z,
            *XY_W,
            *XZ_W,
            *YZ_X,
            *YZ_W,
            *ZW_X,
            *ZW_Y,
            *XY_Z_W,
            *XY_W_Z,
            *XZ_W_Y,
            *YZ_X_W,
            *YZ_W_X,
            *ZW_X_Y,
            *ZW_Y_X,
            *XY_ZW,
            *XZ_YW,
            *XW_YZ,
        ]
    elif Z:
        breeds = [
            *XY,
            *XZ,
            *YZ,
            *XY_Z,
            *YZ_X,
        ]
    else:
        breeds = [
            *XY,
        ]
    return breeds


def fuzzy_name(name):
    ranking = [difflib.SequenceMatcher(None, n, name.lower()).ratio() for n in names]
    i = ranking.index(max(ranking))
    return names[i]


def fuzzy_gender(name):
    if 'F' in name:
        return 1
    if 'M' in name:
        return -1
    else:
        return 0

def fuzzy_pal(name):
    return Pal(
        indice[fuzzy_name(name)],
        gender = fuzzy_gender(name)
    )


def group_represented(pal: Pal | None, group: list[Pal]):
    if pal is None:
        return False
    g_indice = [p.index for p in group]
    if pal.parent1:
        return (
            group_represented(pal.parent1, group)
            or group_represented(pal.parent2, group)
        )
    for p in group:
        if p.index == pal.index:
            if p.gender == 0:
                return True
            if pal.gender == 0:
                return True
            if p.gender == pal.gender:
                return True


def cmp_names(p1: Pal, p2: Pal):
    n1 = str(p1)
    n2 = str(p2)
    if n1 < n2:
        return -1
    if n2 < n1:
        return 1
    return 0


def cmp_numbreeds(p1: Pal, p2: Pal):
    if p1.num_breeds < p2.num_breeds:
        return -1
    elif p2.num_breeds < p1.num_breeds:
        return 1
    return 0


def cmp_breed_depth(p1: Pal, p2: Pal):
    if p1.breed_depth < p2.breed_depth:
        return -1
    elif p2.breed_depth < p1.breed_depth:
        return 1
    return 0


def cmp_breeds(b1: Pal, b2: Pal):
    if (cmp := cmp_numbreeds(b1, b2)) != 0:
        return cmp
    if (cmp := cmp_breed_depth(b1, b2)) != 0:
        return cmp
    if (cmp := cmp_names(b1, b2)) != 0:
        return cmp
    return 0


def parse_names(names: str | list[str]):
    if isinstance(names, str):
        return [ fuzzy_pal(names) ]
    return [ fuzzy_pal(n) for n in names ]


def print_request(target: Pal, groups: list[list[Pal]]):
    print(f'target:\n    {target} if target else "<any>"')
    for i, g in enumerate(groups):
        if len(g) > 16:
                print(
                    f'group {i}:\n    '
                    + ", ".join([str(p) for p in g])
                )
        else:
            print(
                f'group {i}:\n    '
                + "\n    ".join([str(p) for p in g])
            )


def parse_target(target):
    return fuzzy_pal(target) if target else None


def filter_sort_breeds(breeds:list[Pal], groups:list[list[Pal]], target:Pal):
    if target:
        breeds = [b for b in breeds if b.index == target.index]
    for g in groups:
        breeds = [b for b in breeds if group_represented(b, g)]
    return sorted(
        breeds,
        key=functools.cmp_to_key(cmp_breeds),
        reverse=True
    )


def run(
        target: str | None = 'anubis',
        names1: str | list[str] | None = None,
        names2: str | list[str] | None = None,
        names3: str | list[str] | None = None,
        names4: str | list[str] | None = None,
        print_request_only: bool = False):
    print(names3)
    all_pals = list(range(0, len(data)))
    # fuzzy match given pal names/lists
    target = parse_target(target)
    groups = [
        parse_names(names) for names in
            [names1, names2, names3, names4]
                if names is not None
    ]
    filter_groups=[g for g in groups]
    # Include at max 1 extra (any) pal in the breed chain
    n = len(groups)
    while len(groups) < min(n + 1, 4):
        groups.append([Pal(index) for index in all_pals])
    # Print the requested target and pal groups
    print_request(target, groups)
    if print_request_only:
        return
    # Calculate
    breeds = breed(*groups)
    breeds = filter_sort_breeds(
        breeds,
        filter_groups,
        target
    )
    for b in breeds:
        print(b)


if __name__ == "__main__":
    fire.Fire(run)
