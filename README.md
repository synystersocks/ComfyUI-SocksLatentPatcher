# ComfyUI-SocksLatentPatcher
This node circumnavigates the loss of detail, saturation/desaturation for infinite length video generation, the node bypasses the vae decode and directly patches the latent tensor. experimental covering i2v and vace extend (should work on all models apart from ti2v5b "wan2.1&amp;2.2Hs/Ls, hunyuan, ltxv skyreel")

Below is an example of the vace8frame patcher, patching from the i2v into vace, using the original ref and last 8 pixel-space frames "for the encode process" for the vace conditionals, then overwriting the vace reference dim with the last frame from the previous generation while patching the last 8 frames in latent space - 


https://github.com/user-attachments/assets/2f9cee88-d9ce-4693-8a74-6f891b1f5bc4

the issue is not the quality loss of the vae, yet the decompression and recompression of the last frames, like with downsampling, a division of 2 equates to 4 pixels becoming 1 pixel the condensed combination of all 4, this changes the colour overtime, degrading recursivly.

This is an Experimental node and is still a wip, currently runs on 8gb vram using gguf models.
the above video took 2 hours and 30 mins on an rtx 3060 ti 8gb.

the workflow allows for multiple conditionals, and has a bool at the end of each generation allowing testing before continuing to generate the next segment

<img width="1897" height="609" alt="Screenshot 2025-10-05 035357" src="https://github.com/user-attachments/assets/318320a4-ce41-4bc9-988d-ea86ebd2088b" />
