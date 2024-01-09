# -*- coding: utf-8 -*-
"""Module for cropping picture into sections."""
from PIL import Image
import logging

MODULE_LOGGER = logging.getLogger("__name__")
logging.basicConfig(level=logging.ERROR)


def crop(input_image: str, sections: int, name: str) -> None:
    try:
        with Image.open(input_image) as img:
            width, height = img.size

            if not width == height:
                MODULE_LOGGER.error("The image is not square.")
                raise ValueError("The image is not square.")

            section_size = width // int(sections**0.5)

            for i in range(int(sections ** 0.5)):
                for j in range(int(sections ** 0.5)):
                    box = (j * section_size, i * section_size, (j + 1) * section_size, (i + 1) * section_size)
                    cropped_image = img.crop(box)

                    cropped_image_path = f"{name}_{i}_{j}.png"
                    cropped_image.save(cropped_image_path)

    except FileExistsError:
        MODULE_LOGGER.error("The file does not exist.")


if __name__ == '__main__':
    crop(input_image="st_emmeram/wall.png", sections=8, name="wall")
