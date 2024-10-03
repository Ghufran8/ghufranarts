import os
import random
import string

PAGES = {
    "ads": {
        "IMAGE_DIR": "./gallery/img/ads/new_images",
        "HTML_FILE": "./gallery/adsCmction.html",
        "PLACEHOLDER": "<!--Please add images next line-->",
        "IMG_PATH": "img/ads/new_images/"
    },
    "arts": {
        "IMAGE_DIR": "./gallery/img/arts/new_images",
        "HTML_FILE": "./gallery/arts.html",
        "PLACEHOLDER": "<!-- Image Portfolio Section -->",
        "IMG_PATH": "img/arts/new_images/"
    },
    "corp_logo": {
        "IMAGE_DIR": "./gallery/img/corp/logo/new_images",
        "HTML_FILE": "./gallery/corporateIdentity.html",
        "PLACEHOLDER": "<!--Please add logo images next line-->",
        "IMG_PATH": "img/corp/logo/new_images/"
    },
    "corp_packaging": {
        "IMAGE_DIR": "./gallery/img/corp/pack/new_images",
        "HTML_FILE": "./gallery/corporateIdentity.html",
        "PLACEHOLDER": "<!--Please add packaging images next line-->",
        "IMG_PATH": "img/corp/pack/new_images/"
    },
    "calligraphic_adults": {
        "IMAGE_DIR": "./gallery/img/GA/caAdlt/new_images",
        "HTML_FILE": "./gallery/calligraphic.html",
        "PLACEHOLDER": "<!--Please add Adults images next line-->",
        "IMG_PATH": "img/GA/caAdlt/new_images/",
        "SECTION": "Adults"
    },
    "calligraphic_bags": {
        "IMAGE_DIR": "./gallery/img/GA/cabags/new_images",
        "HTML_FILE": "./gallery/calligraphic.html",
        "PLACEHOLDER": "<!--Please add BAGS images next line-->",
        "IMG_PATH": "img/GA/cabags/new_images/",
        "SECTION": "Bags"
    },
    "calligraphic_kids": {
        "IMAGE_DIR": "./gallery/img/GA/cakids/new_images",
        "HTML_FILE": "./gallery/calligraphic.html",
        "PLACEHOLDER": "<!--Please add KIDS images next line-->",
        "IMG_PATH": "img/GA/cakids/new_images/",
        "SECTION": "Kids"
    },
    "calligraphic_mugs": {
        "IMAGE_DIR": "./gallery/img/GA/mugs/new_images",
        "HTML_FILE": "./gallery/calligraphic.html",
        "PLACEHOLDER": "<!--Please add Mugs images next line-->",
        "IMG_PATH": "img/GA/mugs/new_images/",
        "SECTION": "Mugs"
    },
    "calligraphic_pillows": {
        "IMAGE_DIR": "./gallery/img/GA/pillows/new_images",
        "HTML_FILE": "./gallery/calligraphic.html",
        "PLACEHOLDER": "<!--Please add Pillows images next line-->",
        "IMG_PATH": "img/GA/pillows/new_images/",
        "SECTION": "Pillows"
    },
    "photography_evday": {
        "IMAGE_DIR": "./gallery/img/photo/evday/new_images",
        "HTML_FILE": "./gallery/photography.html",
        "PLACEHOLDER": "<!--Please add evday images next line-->",
        "IMG_PATH": "img/photo/evday/new_images/",
        "SECTION": "birthdays"
    },
    "photography_nature": {
        "IMAGE_DIR": "./gallery/img/photo/ntre/new_images",
        "HTML_FILE": "./gallery/photography.html",
        "PLACEHOLDER": "<!--Please add Nature images next line-->",
        "IMG_PATH": "img/photo/ntre/new_images/",
        "SECTION": "nature"
    },
    "photography_landscape": {
        "IMAGE_DIR": "./gallery/img/photo/lnds/new_images",
        "HTML_FILE": "./gallery/photography.html",
        "PLACEHOLDER": "<!--Please add landscape images next line-->",
        "IMG_PATH": "img/photo/lnds/new_images/",
        "SECTION": "landscape"
    },
    "photography_figures": {
        "IMAGE_DIR": "./gallery/img/photo/fgrs/new_images",
        "HTML_FILE": "./gallery/photography.html",
        "PLACEHOLDER": "<!--Please add FIGURES images next line-->",
        "IMG_PATH": "img/photo/fgrs/new_images/",
        "SECTION": "figures"
    }
}


def generate_random_name(length=7):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def rename_images_in_directory(directory):
    try:
        for filename in os.listdir(directory):
            if filename.endswith((".jpg", ".png", ".jpeg")):
                
                new_name = generate_random_name() + os.path.splitext(filename)[1]
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_name)
                
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} to {new_name}")
    except FileNotFoundError:
        print(f"Directory {directory} not found.")


def is_image_in_html(html_content, image_name):
    return image_name in html_content


def generate_html(image_name, img_path, section):
    return f'''
    <div class="col-12 col-sm-6 col-lg-3 single_gallery_item {section} mb-30 wow fadeInUp" data-wow-delay="100ms">
        <div class="single-portfolio-content">
            <img src="{img_path}{image_name}" alt="">
            <div class="hover-content">
                <a href="{img_path}{image_name}" class="portfolio-img">+</a>
            </div>
        </div>
    </div>
    '''

def append_new_images_to_html(image_dir, html_file, placeholder, img_path, section):
    try:
        images = [img for img in os.listdir(image_dir) if img.endswith((".jpg", ".png", ".jpeg", ".JPG"))]
    except FileNotFoundError:
        print(f"Directory {image_dir} not found.")
        return

    
    try:
        with open(html_file, "r") as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"HTML file {html_file} not found.")
        return

    
    if placeholder not in html_content:
        print(f"Placeholder '{placeholder}' not found in {html_file}.")
        return
    new_images_html = ""
    for image in images:
        if not is_image_in_html(html_content, image):
            image_html = generate_html(image, img_path, section)
            new_images_html += image_html

    
    if new_images_html:
        new_html_content = html_content.replace(placeholder, f"{placeholder}\n{new_images_html}")
        with open(html_file, "w") as file:
            file.write(new_html_content)
        print(f"Updated {html_file} with new images.")
    else:
        print("No new images to add.")


for page, details in PAGES.items():
    section = details.get("SECTION", "gallery")
    rename_images_in_directory(details["IMAGE_DIR"])
    append_new_images_to_html(details["IMAGE_DIR"], details["HTML_FILE"], details["PLACEHOLDER"], details["IMG_PATH"], section)