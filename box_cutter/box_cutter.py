import sys
from PIL import Image
from pathlib import Path

import click


def process_folder(folder: Path, output_folder: Path, box: tuple[int]) -> None:
    print(f"Processing folder {folder}")
    for item in folder.iterdir():
        print(item)
        process_file(item, output_folder, box)


def process_file(filename: Path, output_folder: Path, box: tuple[int]) -> None:
    print(f"Processing file {filename}")
    with Image.open(filename) as img:
        product = output_folder.joinpath(filename.name)
        cropped = img.crop(box)
        cropped.save(product)


@click.command()
@click.option(
    "--input",
    "input_path",
    type=click.Path(path_type=Path),
)
@click.option(
    "--output",
    "output_folder",
    type=click.Path(path_type=Path, dir_okay=True),
)
@click.option("--box", type=int, nargs=4, help="left upper right lower")
def main(input_path: Path, output_folder: Path, box: tuple[int]) -> None:
    input_path = input_path.expanduser()
    output_folder = output_folder.expanduser()

    if not input_path.exists():
        print("Input path does not exist")
        sys.exit(5)

    if input_path.is_dir():
        folder = input_path.expanduser()
        process_folder(folder, output_folder, box)
    else:

        filename = input_path.expanduser()
        process_file(filename, output_folder, box)


if __name__ == "__main__":
    main()
