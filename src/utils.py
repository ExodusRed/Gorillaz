import os
import sys

def get_assets_path():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'assets')
    )

def add_assets_to_sys_path():
    assets_path = get_assets_path()
    if assets_path not in sys.path:
        sys.path.insert(0, assets_path)