## requirements
```
pip install diffusers transformers torch
````
## convert .ckpt files
````
python convert_original_stable_diffusion_to_diffusers.py --original_config_file v1-inpainting-inference.yaml --checkpoint_path file.ckpt --dump_path ./my-awesome-model
````

## convert .safetensors files
````
python convert_original_stable_diffusion_to_diffusers.py --original_config_file v1-inpainting-inference.yaml --checkpoint_path file.safetensors --dump_path ./my-awesome-model --from_safetensors
````
