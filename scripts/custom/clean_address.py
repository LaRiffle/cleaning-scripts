def process_address(raw_input):
    """Clean your addresses"""
    if raw_input is None:
        return None
    # TODO: Process: add coma, R->RUE, etc.
    return raw_input.title().strip()
