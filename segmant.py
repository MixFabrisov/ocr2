import cv2
import numpy as np
import tensorflow as tf

emnist_labels = "ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def print_letter(result):
    letters = "ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return letters[result]

def predicting(model, img):

    image = tf.keras.preprocessing.image
    model = tf.keras.models.load_model('model.h5')
#################
    #img = image.load_img(path_to_image, target_size=(278, 278))
####################
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=1)
    result = int(np.argmax(classes))
    result = print_letter(result)
    print(result)
    return result
###############################################
def img_to_str(model, image_file: str):

    letters = letters_extract(image_file)
    s_out = ""
    for i in range(len(letters)):
        dn = letters[i+1][0] - letters[i][0] - letters[i][1] if i < len(letters) - 1 else 0
        s_out += predicting(model, letters[i][2])
        if (dn > letters[i][1]/4):
            s_out += ' '
    return s_out

#model = tf.keras.models.load_model('model.h5')
#s_out = img_to_str(model, "1.jpeg")
#print(s_out)