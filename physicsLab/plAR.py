import os
import json
import platform

from getpass import getuser
from typing import Optional

if platform.system() != "Windows":
    raise RuntimeError("plAR.py only support Windows")

def get_plAR_version():
    ''' 获取物实版本 '''
    if platform.system() == "Windows":
        dir_l = tuple(os.walk(f"C:/Users/{getuser()}/AppData/LocalLow/CIVITAS/Quantum Physics/Unity/"))[0][1]
        if len(dir_l) == 1:
            version_file = f"C:/Users/{getuser()}/AppData/LocalLow/CIVITAS/" \
                           f"Quantum Physics/Unity/{dir_l[0]}/Analytics/values"

            with open(version_file) as f:
                version = json.load(f)["app_ver"]
                return version
    return None

def get_plAR_path() -> Optional[str]:
    ''' 获取物实路径 '''
    with open(f"C:/Users/{getuser()}/AppData/LocalLow/CIVITAS/Quantum Physics/Player-prev.log") as f:
        f.readline()
        f.readline()
        res = os.path.dirname(os.path.dirname(f.readline()[25:-2]))

    if res == "":
        return None
    return res