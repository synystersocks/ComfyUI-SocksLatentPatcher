# ComfyUI-SocksLatentPatcher
This node circumnavigates the loss of detail, saturation/desaturation for infinite length video generation, the node bypasses the vae decode and directly patches the latent tensor. experimental covering i2v and vace extend (should work on all models apart from ti2v5b "wan2.1&amp;2.2Hs/Ls, hunyuan, ltxv skyreel")

Below is an example of the vace8frame patcher, patching from the i2v into vace, using the original ref and last 8 pixel-space frames "for the encode process" for the vace conditionals, then overwriting the vace reference dim with the last frame from the previous generation while patching the last 8 frames in latent space - 


https://github.com/user-attachments/assets/2f9cee88-d9ce-4693-8a74-6f891b1f5bc4

the issue is not the quality loss of the vae, yet the decompression and recompression of the last frames, like with downsampling, a division of 2 equates to 4 pixels becoming 1 pixel the condensed combination of all 4, this changes the colour overtime, degrading recursivly.
