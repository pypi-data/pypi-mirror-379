from pathlib import Path


def get_home():
    return str(Path.home())


def get_documents():
    return str(Path.home() / "Documents")


def get_desktop():
    return str(Path.home() / "Desktop")


def get_downloads():
    return str(Path.home() / "Downloads")
def all_paths():
    return {
        "home": get_home(),
        "documents": get_documents(),
        "desktop": get_desktop(),
        "downloads": get_downloads(),

    }