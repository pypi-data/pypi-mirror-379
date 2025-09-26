
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet50_preprocess
from tensorflow.keras.applications.vgg16 import preprocess_input as vgg16_preprocess
from tensorflow.keras.applications.inception_v3 import preprocess_input as inception_v3_preprocess
from tensorflow.keras.applications.mobilenet import preprocess_input as mobilenet_preprocess
from tensorflow.keras.applications.efficientnet import preprocess_input as efficientnet_preprocess
from tensorflow.keras.applications.xception import preprocess_input as xception_preprocess
from PIL import Image
import io

def get_preprocess_function(model):
    print("Determining preprocessing function based on model configuration...")
    preprocess_map = {
        "resnet50": resnet50_preprocess,
        "vgg16": vgg16_preprocess,
        "inception_v3": inception_v3_preprocess,
        "mobilenet": mobilenet_preprocess,
        "efficientnet": efficientnet_preprocess,
        "xception": xception_preprocess,
    }

    model_config = model.get_config()
    if "name" in model_config:
        model_name = model_config["name"].lower()
        # print(f"Model name: {model_name}")
        for key in preprocess_map.keys():
            if key in model_name:
                # print(f"Detected model type: {key}")
                return preprocess_map[key]

    for layer in model.layers:
        layer_name = layer.name.lower()
        print(f"Checking layer: {layer_name}")
        for model_name in preprocess_map.keys():
            if model_name in layer_name:
                # print(f"Detected model type: {model_name}")
                return preprocess_map[model_name]

    print("No supported model type found in the configuration. Falling back to generic normalization.")
    return lambda x: x / 255.0  # Generic normalization to [0, 1]


_cached_preprocess_function = {}

def get_cached_preprocess_function(model):
    """
    Get the cached preprocessing function for the given model.
    If not cached, fetch it and store it in the cache.
    """
    global _cached_preprocess_function
    model_id = id(model)  # Use the model's unique ID as the cache key
    if model_id not in _cached_preprocess_function:
        _cached_preprocess_function[model_id] = get_preprocess_function(model)
    return _cached_preprocess_function[model_id]

def preprocess_loaded_image(model, image):
    expected_shape = model.input_shape
    input_height, input_width = expected_shape[1], expected_shape[2]
    pil_image = Image.open(io.BytesIO(image)).convert("RGB")
    pil_image = pil_image.resize((input_width, input_height))
    preprocess_input = get_cached_preprocess_function(model)
    image_array = preprocess_input(np.array(pil_image))
    image_preprocessed = np.expand_dims(image_array, axis=0)
    return image_preprocessed

def preprocess_image(model, image):
    preprocess_input = get_cached_preprocess_function(model)
    image_array = preprocess_input(np.array(image))
    image_preprocessed = np.expand_dims(image_array, axis=0)
    return image_preprocessed

def preprocess_numpy_image(model, image):
    """
    Preprocess a NumPy array image for the given model.
    """
    # if isinstance(image, list):
    #     image = np.array(image)
    if image.ndim == 3:
        # If the image is 3D, add a batch dimension
        image = np.expand_dims(image, axis=0)

    # Get the appropriate preprocessing function for the model
    preprocess_input = get_cached_preprocess_function(model)

    # Apply the preprocessing function
    image_preprocessed = preprocess_input(image)

    return image_preprocessed