from pathlib import Path
from PIL import Image
import shutil
import os


def open_image(image_path: str) -> Image.Image:
    # Convert the string path to a Path object for cleaner file handling.
    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    # Open the image with Pillow.
    return Image.open(path)

def save_image(image: Image.Image, output_path: str) -> None:
    # Convert the string path to a Path object for cleaner file handling.
    path = Path(output_path)

    # Create the parent folder if it does not already exist.
    path.parent.mkdir(parents=True, exist_ok=True)

    # JPEG does not support alpha transparency.
    # If the output file is a JPEG and the image is RGBA, convert it to RGB before saving.
    if path.suffix.lower() in {".jpg", ".jpeg"} and image.mode == "RGBA":
        image = image.convert("RGB")

    # Save the image to the requested path.
    image.save(path)

def get_first_image_path(folder_path: str) -> Path:
    # Convert the string path to a Path object for cleaner folder handling.
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Path is not a folder: {folder}")

    # Define the image extensions accepted by the tool.
    allowed_extensions = {".png", ".jpg", ".jpeg", ".webp"}

    # Keep only files with an allowed image extension, then sort them by name.
    image_paths = sorted(
        path for path in folder.iterdir()
        if path.is_file() and path.suffix.lower() in allowed_extensions
    )

    if not image_paths:
        raise FileNotFoundError(f"No image found in folder: {folder}")

    # Return the first image path in alphabetical order.
    return image_paths[0]

def get_image_paths(folder_path: str) -> list[Path]:
    # Convert the string path to a Path object for cleaner folder handling.
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Path is not a folder: {folder}")

    # Define the image extensions accepted by the tool.
    allowed_extensions = {".png", ".jpg", ".jpeg", ".webp"}

    # Keep only files with an allowed image extension, then sort them by name.
    image_paths = sorted(
        path for path in folder.iterdir()
        if path.is_file() and path.suffix.lower() in allowed_extensions
    )

    return image_paths

def copy_file_to_folder(source_path: Path, target_folder_path: str) -> Path:
    # Convert the target folder path to a Path object.
    target_folder = Path(target_folder_path)

    # Create the target folder if it does not already exist.
    target_folder.mkdir(parents=True, exist_ok=True)

    # Build the full target path using the original file name.
    target_path = target_folder / source_path.name

    # Copy the source file to the target path.
    shutil.copy2(source_path, target_path)

    return target_path

def open_folder(folder_path: str) -> None:
    # Open the folder in the operating system file explorer.
    os.startfile(folder_path)