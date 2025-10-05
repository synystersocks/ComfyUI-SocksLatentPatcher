from .nodes.nodes import *

NODE_CLASS_MAPPINGS = { 
    "I2VLatentPatcher": I2VLatentPatcher,
    "VaceExt4fLatentPatcher": VaceExt4fLatentPatcher,
    "VaceExt6fLatentPatcher": VaceExt6fLatentPatcher,
    "VaceExt8fLatentPatcher": VaceExt8fLatentPatcher,
    }
    
print("\033[34mComfyUI SocksLatentPatcher Node: \033[92mLoaded\033[0m")