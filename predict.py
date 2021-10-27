import tensorflow as tf
import numpy as np
import os

def print_letter(result):
    letters = "ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return letters[result]

def predicting(path_to_image):

    image = tf.keras.preprocessing.image
    model = tf.keras.models.load_model('model.h5')

    img = image.load_img(path_to_image, target_size=(278, 278))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=1)
    result = int(np.argmax(classes))
    result = print_letter(result)
    print(result)
    return result


def validation():
    count = 0
    for address, dir, files in os.walk("val"):
        for file in files:
            if address.split("/")[1] == predicting(address + "/" + file):
                count +=1
    print(count)

#validation()

predicting("SaveImage/А2.jpeg")