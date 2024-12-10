import re
import os
import urllib
import time
import requests
from pathlib import Path
from functools import partial
import multiprocessing
from tqdm import tqdm
from PIL import Image

# Define the allowed units and other constants in a separate file or within the script
class constants:
    allowed_units = {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard', 'gram', 'kilogram', 'microgram', 'milligram', 'ounce', 'pound', 'ton', 'kilovolt', 'millivolt', 'volt', 'kilowatt', 'watt', 'centilitre', 'cubic foot', 'cubic inch', 'cup', 'decilitre', 'fluid ounce', 'gallon', 'imperial gallon', 'litre', 'microlitre', 'millilitre', 'pint', 'quart'}

def common_mistake(unit):
    if unit in constants.allowed_units:
        return unit
    if unit.replace('ter', 'tre') in constants.allowed_units:
        return unit.replace('ter', 'tre')
    if unit.replace('feet', 'foot') in constants.allowed_units:
        return unit.replace('feet', 'foot')
    return unit

def parse_string(s):
    s_stripped = "" if s is None or str(s) == 'nan' else s.strip()
    if s_stripped == "":
        return None, None
    pattern = re.compile(r'^-?\d+(\.\d+)?\s+[a-zA-Z\s]+$')
    if not pattern.match(s_stripped):
        raise ValueError("Invalid format in {}".format(s))
    parts = s_stripped.split(maxsplit=1)
    number = float(parts[0])
    unit = common_mistake(parts[1])
    if unit not in constants.allowed_units:
        raise ValueError("Invalid unit [{}] found in {}. Allowed units: {}".format(
            unit, s, constants.allowed_units))
    return number, unit

def create_placeholder_image(image_save_path):
    try:
        placeholder_image = Image.new('RGB', (100, 100), color='black')
        placeholder_image.save(image_save_path)
    except Exception as e:
        print(f"Error creating placeholder image: {e}")

def download_image(image_link, save_folder, retries=3, delay=3):
    if not isinstance(image_link, str):
        return

    filename = Path(image_link).name
    image_save_path = os.path.join(save_folder, filename)

    if os.path.exists(image_save_path):
        return

    for _ in range(retries):
        try:
            urllib.request.urlretrieve(image_link, image_save_path)
            return
        except Exception as e:
            print(f"Error downloading image {image_link}: {e}")
            time.sleep(delay)
    
    create_placeholder_image(image_save_path)  # Create a black placeholder image for invalid links/images

def download_images(image_links, download_folder, allow_multiprocessing=True):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    if allow_multiprocessing:
        download_image_partial = partial(
            download_image, save_folder=download_folder, retries=3, delay=3)

        with multiprocessing.Pool(64) as pool:
            list(tqdm(pool.imap(download_image_partial, image_links), total=len(image_links)))
            pool.close()
            pool.join()
    else:
        for image_link in tqdm(image_links, total=len(image_links)):
            download_image(image_link, save_folder=download_folder, retries=3, delay=3)

# Define the path to the folder where images will be saved
download_folder = r'D:\BDA_1_Sem\Amazon ML Hackathon\66e31d6ee96cd_student_resource_3\student_resource 3\images'

# Define the list of image URLs you want to download
image_links = [
    'https://m.media-amazon.com/images/I/21-LmSmehZL.jpg',
    'https://m.media-amazon.com/images/I/213oP6n7jtL.jpg',
    'https://m.media-amazon.com/images/I/213wY3gUsmL.jpg'

]

# Call the function to download images
download_images(image_links, download_folder, allow_multiprocessing=True)
