def get_bottom_right_position(
    base_size: tuple[int, int],
    overlay_size: tuple[int, int],
    margin_x: int = 40,
    margin_y: int = 40,
) -> tuple[int, int]:
    # base_size contains the width and height of the source image.
    base_width, base_height = base_size

    # overlay_size contains the width and height of the watermark.
    overlay_width, overlay_height = overlay_size

    # Bottom-right position means:
    # x = source width - watermark width - horizontal margin
    # y = source height - watermark height - vertical margin
    x = base_width - overlay_width - margin_x
    y = base_height - overlay_height - margin_y

    return x, y