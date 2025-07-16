import os
from typing import Callable, TypedDict, List
from pathlib import Path
import inspect


def get_resource_path(*relative_path_parts):
    """
    Membangun path absolut ke resource seperti gambar, ikon, font, dll.
    Bisa dipanggil dari file Python manapun di dalam project.

    Args:
        *relative_path_parts: Bagian path relatif dari folder `assets`.
            Contoh: 'assets', 'font', 'DejaVuSans.ttf'

    Returns:
        str: Path absolut ke file resource tersebut.
    """

    # Lokasi file Python yang MEMANGGIL fungsi ini (bukan lokasi fungsi ini berada)
    caller_file = inspect.stack()[1].filename
    caller_dir = os.path.dirname(os.path.abspath(caller_file))

    # Telusuri naik sampai menemukan folder `assets`
    current = caller_dir
    while True:
        if os.path.isdir(os.path.join(current, "assets")):
            break
        parent = os.path.dirname(current)
        if parent == current:
            raise FileNotFoundError(
                "Folder 'assets' tidak ditemukan dalam struktur direktori atas.")
        current = parent

    # Setelah ditemukan root project, gabungkan dengan relative path
    return os.path.join(current, *relative_path_parts)


# contoh penggunaan
icon_path = get_resource_path("assets", "icon", "send.png")
print("Icon Path:", icon_path)
print("Exists?", os.path.exists(icon_path))


class typeFile(TypedDict):
    pathFile: str
    nameFile: str
# sedikit berantakan nanntik perbaiki lagi


def get_all_files() -> List[typeFile]:
    '''kembalikan dictionary nama file dan path filenya
        @return : [{'pathFile':"...","nameFile":...},...]
    '''
    pathfile = os.path.join(os.path.dirname(__file__), "../assets/file/")
    folder = Path(pathfile)
    if not folder.exists():
        print(f"Folder tidak ditemukan: {folder}")
        return []
    result: List[typeFile] = []

    for file in folder.iterdir():
        if file.is_file():
            print("path", file, "name", file.name)
            result.append(
                {
                    'pathFile': str(file),
                    'nameFile': file.name,
                }
            )
    return result
