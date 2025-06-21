import os
import sys

# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)

def get_assets_path():
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets')))
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'assets')
    )

def add_assets_to_sys_path():
    try:
        assets_path = get_assets_path()
        if assets_path not in sys.path:
            sys.path.insert(0, assets_path)
            print("added to path.")
        return 1
    except:
        return 0
    
def add_root_to_sys_path():
    # project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

    # project_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    # if project_root not in sys.path:
    #     sys.path.insert(0, project_root)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)


if __name__ == "__main__":
    print("This file:", __file__)
    print("Directory:", os.path.dirname(__file__))
    print("Assets path:", get_assets_path())