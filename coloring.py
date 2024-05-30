import setting

def coloring(txt: str, mode:str):
    return f"\x1b[{setting.get_setting("color")[mode]}m{txt}\x1b[0m"