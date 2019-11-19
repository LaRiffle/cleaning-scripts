import re


def clean_phone(raw_input):
    """Clean phone number to 0x xx xx xx xx"""
    pattern = re.compile("(\d{2})" + "[\.\-\s]*(\d{2})" * 4)
    occurrences = pattern.findall(raw_input)
    if len(occurrences) > 0:
        phone = " ".join(occurrences[0])
        return phone
    return ""
