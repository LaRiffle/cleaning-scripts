from enum import Enum
import logging


class FamilySituation(Enum):
    MARRIED = "Marié(e)"
    SINGLE = "Célibataire"
    WIDOWED = "Veuvage"
    DIVORCED = "Divorcé(e)"
    PACSED = "Pacsé(e)"


def family_situation(code):
    """Map family situation codes M/C/V/D/O"""
    status = FamilySituation
    mapping = {
        "M": status.MARRIED.value,
        "C": status.SINGLE.value,
        "V": status.WIDOWED.value,
        "D": status.DIVORCED.value,
        "O": status.PACSED.value,
    }
    if code in mapping.keys():
        return mapping[code]
    else:
        logging.warning(
            "In {}, args {} not recognised".format("family_situation", code)
        )
        return code
