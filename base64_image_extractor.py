#!/usr/bin/env python3

import base64
import argparse
import sys
from bs4 import BeautifulSoup

def save_base64_images_and_update_html(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    images = soup.find_all('img')
    image_counter = 1

    for img in images:
        img_src = img.get('src', '')
        if img_src.startswith('data:image/jpeg;base64,'):
            base64_data = img_src.replace('data:image/jpeg;base64,', '').strip()
            img_data = base64.b64decode(base64_data)
            filename = f"{image_counter:03}.jpeg"
            with open(filename, 'wb') as img_file:
                img_file.write(img_data)

            # Update the src attribute to the filename of the saved image
            img['src'] = filename
            image_counter += 1

    # Output the modified HTML to standard output
    print(soup.prettify())

def main():
    parser = argparse.ArgumentParser(description="Extracts and saves 'data:image/jpeg' images encoded in base64 format from an HTML file into JPEG files, and outputs the modified HTML with image paths replaced.")
    parser.add_argument('html_file', type=str, nargs='?', help='The path to the HTML file containing base64 encoded images.')

    args = parser.parse_args()

    # Check if no arguments were provided or the html_file is None
    if args.html_file is None:
        parser.print_help()
        sys.exit(1)

    save_base64_images_and_update_html(args.html_file)

if __name__ == "__main__":
    main()
