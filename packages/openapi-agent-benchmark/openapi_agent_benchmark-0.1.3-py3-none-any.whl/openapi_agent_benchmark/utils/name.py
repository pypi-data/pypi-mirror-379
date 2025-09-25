def sanitize(name: str) -> str:
    return name.replace('-', '').replace('_', '').replace('.', '')
