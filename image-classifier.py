import tensorflow
import tensorflow as tf
import numpy as np
import PIL
import PIL.Image
from keras.applications import imagenet_utils

mobilenet = tf.keras.applications.MobileNetV2(weights='imagenet')

def prepare_image(file):
    img_path = ''
    img = tf.keras.utils.load_img(img_path + file, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)


def predict():
    preprocessed_image = prepare_image('/home/salwynm/phone.jpeg')
    predictions = mobilenet.predict(preprocessed_image)
    result = imagenet_utils.decode_predictions(predictions, 3)[0]

    responses = []
    for i, res in enumerate(result):
        responses.append(res[1])
    return responses
