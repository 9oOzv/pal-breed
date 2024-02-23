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

with open('data.json') as f:
    data = json.loads(f.read())

names = data['names']
n_pals = len(names)
offspring_map = data['offspring_map']

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
    if pal1.gender and pal2.gender and pal1.gender == pal2.gender:
        return None
    return Pal(
        offspring_map[pal1.index*n_pals+pal2.index],
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
        XY_Z = _breed(XY, Z)
        XZ_Y = _breed(XZ, Y)
        YZ_X = _breed(YZ, X)
        if W:
            XW = _breed(X, W)
            YW = _breed(Y, W)
            ZW = _breed(Z, W)
            XY_W = _breed(XY, W)
            XZ_W = _breed(XZ, W)
            YZ_W = _breed(YZ, W)
            YW_X = _breed(YW, X)
            YW_Z = _breed(YW, Z)
            ZW_X = _breed(ZW, X)
            ZW_Y = _breed(ZW, Y)
            XY_Z_W = _breed(XY_Z, W)
            XY_W_Z = _breed(XY_W, Z)
            XZ_Y_W = _breed(XZ_Y, W)
            XZ_W_Y = _breed(XZ_W, Y)
            YZ_X_W = _breed(YZ_X, W)
            YZ_W_X = _breed(YZ_W, X)
            YW_X_Z = _breed(YW_X, Z)
            YW_Z_X = _breed(YW_Z, X)
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
            *XZ_Y,
            *XZ_W,
            *YZ_X,
            *YZ_W,
            *YW_X,
            *YW_Z,
            *ZW_X,
            *ZW_Y,
            *XY_Z_W,
            *XY_W_Z,
            *XZ_Y_W,
            *XZ_W_Y,
            *YZ_X_W,
            *YZ_W_X,
            *YW_X_Z,
            *YW_Z_X,
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
            *XZ_Y,
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
        names.index(fuzzy_name(name)),
        gender = fuzzy_gender(name)
    )


def group_represented(pal: Pal | None, group: list[Pal]):
    if pal is None:
        return False
    if pal.parent1:
        return (
            group_represented(pal.parent1, group)
            or group_represented(pal.parent2, group)
        )
    for p in group:
        if p.index == pal.index:
            if p.gender == 0:
                return True
            if p.gender == pal.gender:
                return True
    return False


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
    print(f'target:\n    {target if target else "<any>"}')
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
        num_any: int = 1,
        print_request_only: bool = False) -> str:
    """
    Calculate breed chains to target from given groups of pals (e.g. with specific traits)

    * Calculate breed chains to given target
    * include pal from each given `--names<n>=pal1[,pal2,pal3...]` group.
    
    List pals with a specific traits in each group to calculate shortest paths to the target with all desired traits.

    Given too many large groups, or too many (additional) pals to inlcude, the script might take long or crash.

    Args:
        num_any: Number of additional pals that can be included in the chain. Chains are calculated
            to maximum of 4 pals.
        print_request_only: only print the given parameters, not calculate anything. Can be used to
            confirm that names get parsed correctly
    Returns:
        List of breed paths to target. Sorted with the shortest/shallowest paths at the bottom.
    """
    print(names3)
    all_pals = list(range(0, n_pals))
    # fuzzy match given pal names/lists
    target = parse_target(target)
    groups = [
        parse_names(names) for names in
            [names1, names2, names3, names4]
                if names is not None
    ]
    filter_groups=[g for g in groups]
    # Include at max <num_any> extra (any) pal in the breed chain
    n = len(groups)
    while len(groups) < min(n + num_any, 4):
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
