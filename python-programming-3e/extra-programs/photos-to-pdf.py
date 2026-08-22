# photos-to-pdf.py

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import re


def natural_sort_key(path):
    """
    Sort filenames alphabetically and numerically.

    Examples:
        1.png
        2.png
        10.png
        apple.png
        apple2.png
        apple10.png
        banana.png
    """
    return [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", path.stem)
    ]


def create_pdf(folder_path):
    folder = Path(folder_path)

    if not folder.is_dir():
        print("Error: Folder does not exist.")
        return

    # Find PNG files and sort them naturally
    photos = sorted(
        folder.glob("*.png"),
        key=natural_sort_key
    )

    if not photos:
        print("No PNG files found in the folder.")
        return

    pages = []

    # A4 page size at 150 DPI
    page_width = 1240
    page_height = 1754

    margin = 80
    text_height = 60

    image_max_width = page_width - 2 * margin
    image_max_height = page_height - 2 * margin - text_height

    font = ImageFont.load_default(size=40)

    for number, photo_path in enumerate(photos, start=1):

        # Create white A4 page
        page = Image.new(
            "RGB",
            (page_width, page_height),
            "white"
        )

        draw = ImageDraw.Draw(page)

        # Write photo name
        text = f"Photo {number} : {photo_path.name}"

        draw.text(
            (margin, margin),
            text,
            fill="black",
            font=font
        )

        # Open image
        image = Image.open(photo_path).convert("RGB")

        # Resize while maintaining aspect ratio
        image.thumbnail(
            (image_max_width, image_max_height)
        )

        # Center image horizontally
        x = (page_width - image.width) // 2
        y = margin + text_height

        page.paste(image, (x, y))

        pages.append(page)

    # Create PDF in the same folder
    output_path = folder / "photos.pdf"

    pages[0].save(
        output_path,
        "PDF",
        resolution=150.0,
        save_all=True,
        append_images=pages[1:]
    )

    print(f"\nPDF created successfully:")
    print(output_path)


if __name__ == "__main__":
#    folder = input(
#        "Enter the folder path containing PNG photos: "
#    ).strip()
    fi_path = Path(__file__).parent / "fai-for-ptp"
    folder = fi_path

    create_pdf(folder)
