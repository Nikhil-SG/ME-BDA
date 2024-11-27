import requests
from PIL import Image
import pytesseract
import re

def fetch_and_preprocess_image(image_url):
    """Fetches and preprocesses a single image from a URL.

    Args:
        image_url: The URL of the image.

    Returns:
        A preprocessed Image object.
    """

    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        img = Image.open(response.raw)
        # Preprocessing (e.g., resize, convert to grayscale)
        img = img.resize((800, 800))  # Adjust size as needed
        img = img.convert('RGB')
        return img
    else:
        print(f"Error fetching image from {image_url}")
        return None

def extract_measurements(image):
    """Extracts measurements (width, depth, height, item_weight) from an image.

    Args:
        image: A preprocessed Image object.

    Returns:
        A dictionary containing extracted measurements.
    """

    measurements = {}
    text = pytesseract.image_to_string(image, config='--psm 6')

    # Regular expressions for matching measurements
    width_pattern = r"width: (\d+(\.\d+)?)\s*(centimetre|foot|inch|metre|millimetre|yard)"
    depth_pattern = r"depth: (\d+(\.\d+)?)\s*(centimetre|foot|inch|metre|millimetre|yard)"
    height_pattern = r"height: (\d+(\.\d+)?)\s*(centimetre|foot|inch|metre|millimetre|yard)"
    item_weight_pattern = r"item_weight: (\d+(\.\d+)?)\s*(gram|kilogram|microgram|milligram|ounce|pound|ton)"

    # Find matches and extract values
    for pattern, key in [(width_pattern, 'width'), (depth_pattern, 'depth'), (height_pattern, 'height'), (item_weight_pattern, 'item_weight')]:
        match = re.search(pattern, text)
        if match:
            value, unit = match.groups()
            measurements[key] = {'value': float(value), 'unit': unit}

    return measurements

# Example usage
image_url = "https://m.media-amazon.com/images/I/71d+dz7ogkL.jpg"

image = fetch_and_preprocess_image(image_url)
if image:
    measurements = extract_measurements(image)
    print(measurements)
else:
    print("Error fetching image.")