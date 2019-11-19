from scripts import utils


def merge_insee(value1, value2):
    """Custom script (x, y) -> x if x is not None else y"""
    if not utils.is_empty(value1):
        insee = value1
    else:
        insee = value2
    return insee.strip()
