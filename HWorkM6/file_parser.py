import sys
from pathlib import Path

MY_IMAGES = []
MY_VIDEOS = []
MY_DOCUMENTS = []
MY_MUSIC = []
MY_ARCHIVES = []
MY_OTHER = []


REGISTER_EXTENSION = {
    'JPEG': MY_IMAGES, 'JPG': MY_IMAGES, 'PNG': MY_IMAGES, 'SVG': MY_IMAGES,
    'AVI': MY_VIDEOS, 'MP4': MY_VIDEOS, 'MOV': MY_VIDEOS,  'MKV': MY_VIDEOS,
    'DOC': MY_DOCUMENTS, 'DOCX': MY_DOCUMENTS,  'TXT': MY_DOCUMENTS,
    'PDF': MY_DOCUMENTS, 'XLSX': MY_DOCUMENTS, 'PPTX': MY_DOCUMENTS,
    'MP3': MY_MUSIC, 'OGG': MY_MUSIC, 'WAV': MY_MUSIC, 'AMR': MY_MUSIC,
    'ZIP': MY_ARCHIVES, 'GZ': MY_ARCHIVES, 'TAR': MY_ARCHIVES,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():

        if item.is_dir():

            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                FOLDERS.append(item)
                scan(item)
            continue


        ext = get_extension(item.name)
        full_name = folder / item.name
        if not ext:
            MY_OTHER.append(full_name)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSIONS.add(ext)
                container.append(full_name)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(full_name)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder: {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f"Images : {MY_IMAGES}")
    print(f"Video: {MY_VIDEOS}")
    print(f"Documents: {MY_DOCUMENTS}")
    print(f"Audio: {MY_MUSIC}")
    print(f"Archives: {MY_ARCHIVES}")
    print('*' * 25)
    print(f'Types of file in folder: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')