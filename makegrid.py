import os
import cv2
import numpy as np
import math
from fuzzywuzzy import fuzz
import fire

def fuzzy_match(filename, keys):
    best_score = -1
    best_match = None
    for key in keys:
        score = fuzz.ratio(filename, key)
        if score > best_score:
            best_score = score
            best_match = key
    return best_match

def overlay_text(image, key, number, position):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.15
    font_thickness = 6
    color = (255, 255, 255)
    key_text = f"{key}"
    number_text = f"{number}"
    text_size, _ = cv2.getTextSize(key_text, font, font_scale, font_thickness)
    key_position = (position[0], position[1] + math.ceil(text_size[1] *1.5))
    # Draw transparent box under the text
    box_color = (0, 0, 0)  # Black color
    h = text_size[1] + 10
    # Create a transparent overlay rectangle
    overlay = image.copy()
    cv2.rectangle(image, (position[0] - 10, position[1] - h), (position[0] + image.shape[1], key_position[1] + h - 20), box_color, -1)
    # Blend the overlay with the original image
    alpha = 0.5  # Transparency level (0.0 - 1.0)
    cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

    cv2.putText(image, key_text, position, font, font_scale, color, font_thickness, cv2.LINE_AA)
    cv2.putText(image, number_text, key_position, font, font_scale, color, font_thickness, cv2.LINE_AA)


def assemble_grid(image_folder, entries_dict, grid_size=(3, 3), output_path='grid.png'):
    # Get list of image files in folder
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('webp')])

    w = math.ceil(math.sqrt(len(image_files)))

    # Initialize empty grid image
    grid_width = grid_size[1] * 256
    grid_height = grid_size[0] * 256
    grid = np.zeros((grid_height, grid_width, 3), dtype=np.uint8)

    # Resize images to fit grid cells and overlay text
    cell_width = grid_width // grid_size[1]
    cell_height = grid_height // grid_size[0]
    data = []
    for i, filename in enumerate(image_files):
        image = cv2.imread(os.path.join(image_folder, filename))
        image = cv2.resize(image, (cell_width, cell_height))

        # Overlay text based on closest match in entries_dict
        best_match = fuzzy_match(filename, entries_dict.keys())
        data += [
            {
                "image": image,
                "key": best_match,
                "number": entries_dict[best_match]
            }
        ]
    for i, info in enumerate(sorted(data, key=lambda v: v["number"])):
        row = i // grid_size[1]
        col = i % grid_size[1]
        overlay_text(info["image"], info["key"], info["number"], (10, 50))
        grid[row*cell_height:(row+1)*cell_height, col*cell_width:(col+1)*cell_width, :] = info["image"]

    # Save assembled grid
    cv2.imwrite(output_path, grid)
    print(f"Grid assembled and saved to {output_path}")


powers = {
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

def run(folder: str):
    assemble_grid(folder, powers, grid_size=(9,17))

if __name__ == "__main__":
    fire.Fire(run)
