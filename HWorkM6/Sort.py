from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize
# import os
# import tarfile
# import zipfile
# import gzip


def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_arhive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path) -> None:
    try:
        folder.rmdir()
    except OSError:
        print(f'Sorry, we can not delete the folder: {folder}')


def main(folder: Path) -> None:
    parser.scan(folder)
    for file in parser.MY_IMAGES:
        handle_media(file, folder / 'images')

    for file in parser.MY_VIDEOS:
        handle_media(file, folder / 'videos')

    for file in parser.MY_DOCUMENTS:
        handle_media(file, folder / 'documents')

    for file in parser.MY_MUSIC:
        handle_media(file, folder / 'audio')

    for file in parser.MY_OTHER:
        handle_media(file, folder / 'MY_OTHER')

    for file in parser.MY_ARCHIVES:
        handle_media(file, folder / 'archives')

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)





if __name__ == '__main__':
    folder_for_scan = Path(sys.argv[1])
    main(folder_for_scan.resolve())

