from pathlib import Path
from watermark_tool.config_loader import load_config
from watermark_tool.error_logger import write_error_log
from watermark_tool.image_io import (
    open_image,
    save_image,
    get_first_image_path,
    get_image_paths,
    copy_file_to_folder,
    open_folder,
)
from watermark_tool.positioning import get_bottom_right_position
from watermark_tool.watermark_service import apply_watermark


def main():
    config = load_config()

    input_folder = config["input_folder"]
    output_folder = config["output_folder"]
    assets_folder = config["assets_folder"]
    temp_folder = config["temp_folder"]
    error_log_path = config["error_log_path"]
    margin_x = config["margin_x"]
    margin_y = config["margin_y"]

    watermark_path = get_first_image_path(assets_folder)
    watermark = open_image(str(watermark_path))

    image_paths = get_image_paths(input_folder)

    success_count = 0
    error_count = 0

    print(f"Found {len(image_paths)} image(s) to process.")
    print(f"Using watermark: {watermark_path}")

    for image_path in image_paths:
        temp_image_path: Path | None = None

        try:
            print(f"Processing: {image_path}")

            # Copy the source image to the temp folder before processing.
            temp_image_path = copy_file_to_folder(image_path, temp_folder)

            # Work on the temp copy, not directly on the original file.
            source_image = open_image(str(temp_image_path))

            position = get_bottom_right_position(
                base_size=source_image.size,
                overlay_size=watermark.size,
                margin_x=margin_x,
                margin_y=margin_y,
            )

            result = apply_watermark(
                source_image=source_image,
                watermark=watermark,
                position=position,
            )

            output_path = (
                f"{output_folder}/{image_path.stem}_watermarked{image_path.suffix}"
            )

            save_image(result, output_path)
            print(f"Saved: {output_path}")

            # Delete the original only after the output file has been saved successfully.
            image_path.unlink()
            print(f"Deleted source file: {image_path}")

            success_count += 1

        except Exception as error:
            error_count += 1
            write_error_log(error_log_path, image_path, error)
            print(f"Error while processing {image_path}: {error}")

        finally:
            # Always remove the temp copy if it exists.
            if temp_image_path is not None and temp_image_path.exists():
                temp_image_path.unlink()
                print(f"Deleted temp file: {temp_image_path}")

    print("Batch processing completed.")
    print(f"Success: {success_count}")
    print(f"Errors: {error_count}")
    print(f"Remaining files in input: {len(get_image_paths(input_folder))}")


if __name__ == "__main__":
    main()
