from PIL import Image


def apply_watermark(
    source_image: Image.Image,
    watermark: Image.Image,
    position: tuple[int, int],
) -> Image.Image:
    # Convert the source image to RGBA so it can handle transparency.
    result = source_image.convert("RGBA")

    # Convert the watermark to RGBA to preserve its alpha channel.
    watermark_rgba = watermark.convert("RGBA")

    # Paste the watermark using itself as a transparency mask.
    result.paste(watermark_rgba, position, watermark_rgba)

    return result