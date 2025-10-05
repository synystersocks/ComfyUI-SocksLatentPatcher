import numpy as np
import torch


class I2VLatentPatcher:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "NewSamples": ("LATENT",),
                "PreviousSamples": ("LATENT",),
                "FramesLength": ("INT", {"default": 65, "min": 1, "max": 257, "step": 4}),
                             }}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "I2VLatentPatcher"

    CATEGORY = "latent/video"

    EXPERIMENTAL = True

    def I2VLatentPatcher(self, PreviousSamples, NewSamples, FramesLength):
         
         samples_out = NewSamples.copy()
         s2 = PreviousSamples["samples"]
         
         Axislength = ((FramesLength - 1) // 4)
         
         samples_out[0,0,0,0] = s2[0,0,Axislength,3]
         samples_out[0,0,0,1] = s2[0,0,Axislength,3]
         samples_out[0,0,0,2] = s2[0,0,Axislength,3]
         samples_out[0,0,0,3] = s2[0,0,Axislength,3]
        
         return (samples_out,)
 
class VaceExt4fLatentPatcher:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "NewSamples": ("LATENT",),
                "PreviousSamples": ("LATENT",),
                "PrevGenFramesLength": ("INT", {"default": 65, "min": 1, "max": 257, "step": 4}),
                             }}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "VaceExt4fLatentPatcher"

    CATEGORY = "latent/video"

    EXPERIMENTAL = True

    def VaceExt4fLatentPatcher(self, PreviousSamples, NewSamples, PrevGenFramesLength):
         
         samples_out = NewSamples.copy()
         s2 = PreviousSamples["samples"]
         Axislength = ((PrevGenFramesLength - 1) // 4)
         
         samples_out[0,0,0,0] = s2[0,0,Axislength,3]
         samples_out[0,0,0,1] = s2[0,0,Axislength,3]
         samples_out[0,0,0,2] = s2[0,0,Axislength,3]
         samples_out[0,0,0,3] = s2[0,0,Axislength,3]
         samples_out[0,0,1,0] = s2[0,0,Axislength,0]
         samples_out[0,0,1,1] = s2[0,0,Axislength,1]
         samples_out[0,0,1,2] = s2[0,0,Axislength,2]
         samples_out[0,0,1,3] = s2[0,0,Axislength,3]
        
         return (samples_out,)

class VaceExt6fLatentPatcher:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "NewSamples": ("LATENT",),
                "PreviousSamples": ("LATENT",),
                "PrevGenFramesLength": ("INT", {"default": 65, "min": 1, "max": 257, "step": 4}),
                             }}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "VaceExt6fLatentPatcher"

    CATEGORY = "latent/video"

    EXPERIMENTAL = True

    def VaceExt6fLatentPatcher(self, PreviousSamples, NewSamples, PrevGenFramesLength):
         
         samples_out = NewSamples.copy()
         s2 = PreviousSamples["samples"]
         Axislength = ((PrevGenFramesLength - 1) // 4)
         AxislenghtNegOne = (Axislength - 1)
         
         samples_out[0,0,0,0] = s2[0,0,Axislength,3]
         samples_out[0,0,0,1] = s2[0,0,Axislength,3]
         samples_out[0,0,0,2] = s2[0,0,Axislength,3]
         samples_out[0,0,0,3] = s2[0,0,Axislength,3]
         samples_out[0,0,1,0] = s2[0,0,AxislenghtNegOne,2]
         samples_out[0,0,1,1] = s2[0,0,AxislenghtNegOne,3]
         samples_out[0,0,1,2] = s2[0,0,Axislength,0]
         samples_out[0,0,1,3] = s2[0,0,Axislength,1]
         samples_out[0,0,2,0] = s2[0,0,Axislength,2]
         samples_out[0,0,2,1] = s2[0,0,Axislength,3]
        
         return (samples_out,)

class VaceExt8fLatentPatcher:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "NewSamples": ("LATENT",),
                "PreviousSamples": ("LATENT",),
                "PrevGenFramesLength": ("INT", {"default": 65, "min": 1, "max": 257, "step": 4}),
                             }}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "VaceExt8fLatentPatcher"

    CATEGORY = "latent/video"

    EXPERIMENTAL = True

    def VaceExt8fLatentPatcher(self, PreviousSamples, NewSamples, PrevGenFramesLength):
         
         samples_out = NewSamples.copy()
         s2 = PreviousSamples["samples"]
         Axislength = ((PrevGenFramesLength - 1) // 4)
         AxislenghtNegOne = (Axislength - 1)
         
         samples_out[0,0,0,0] = s2[0,0,Axislength,3]
         samples_out[0,0,0,1] = s2[0,0,Axislength,3]
         samples_out[0,0,0,2] = s2[0,0,Axislength,3]
         samples_out[0,0,0,3] = s2[0,0,Axislength,3]
         samples_out[0,0,1,0] = s2[0,0,AxislenghtNegOne,0]
         samples_out[0,0,1,1] = s2[0,0,AxislenghtNegOne,1]
         samples_out[0,0,1,2] = s2[0,0,AxislenghtNegOne,2]
         samples_out[0,0,1,3] = s2[0,0,AxislenghtNegOne,3]
         samples_out[0,0,2,0] = s2[0,0,Axislength,0]
         samples_out[0,0,2,1] = s2[0,0,Axislength,1]
         samples_out[0,0,2,2] = s2[0,0,Axislength,2]
         samples_out[0,0,2,3] = s2[0,0,Axislength,3]
        
         return (samples_out,)

