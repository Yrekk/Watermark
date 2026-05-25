from datetime import datetime
from pathlib import Path


def write_error_log(error_log_path: str, file_path: Path, error: Exception) -> None:
    # Convert the error log path to a Path object.
    path = Path(error_log_path)

    # Create the log folder if it does not already exist.
    path.parent.mkdir(parents=True, exist_ok=True)

    # Build a simple timestamped error message.
    timestamp = datetime.now().isoformat(timespec="seconds")
    message = f"[{timestamp}] File: {file_path} | Error: {type(error).__name__}: {error}\n"

    # Append the error message to the log file.
    with path.open("a", encoding="utf-8") as log_file:
        log_file.write(message)