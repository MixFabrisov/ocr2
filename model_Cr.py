import os
import cv2
import numpy as np
from skimage.transform import AffineTransform, warp, rotate

list_charchest = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", 
                    "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

def make_background(image, name, count):

    im = image
    im = cv2.imdecode(np.fromfile(im, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

    trans_mask = im[:, :, 3] == 0
    im[trans_mask] = [255, 255, 255, 255]

    new_img = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)

    cv2.imwrite("Cyrillic_jpeg/" + name + "/" + name + count + '.jpeg', new_img)

def shift(image, name, count):

    img = cv2.imread(image) 

    arr_translation = [[15, -15], [-15, 15], [-15, -15],[15, 15]]
    arr_caption=['15-15','-1515','-15-15','1515']

    for i in range(4):

        transform = AffineTransform(translation = tuple(arr_translation[i]))
        warp_image = warp(img, transform, mode = "wrap")

        img_convert = cv2.convertScaleAbs(warp_image,alpha = (255.0))

        cv2.imwrite("Cyrillic_jpeg_shift/" + name + "/" + name + arr_caption[i] + count + '.jpeg', img_convert)

def rotate_shift(image, name, count):

    img = cv2.imread(image)
    
    angles = np.ndarray((2,), buffer=np.array([-13, 13]), dtype=int)
    
    for angle in angles:

        transformed_image = rotate(np.array(img), angle, cval = 255, preserve_range = True).astype(np.uint8)
        cv2.imwrite("Cyrillic_jpeg_shift_rotate/" + name + "/" + name + str(angle) + count + '.jpeg', transformed_image)

def balancing():

    arr_len_files = []

    for address, dir, files in os.walk("Cyrillic_jpeg_shift_rotate"): 
        lenFil=os.listdir(address)
        arr_len_files.append(len(lenFil)) ## получаем количество файло из каждого класса

    min_value=min(arr_len_files[1:]) #минимальное значения под которое надо подстроить дата сет
  
    for address, dir, files in os.walk("Cyrillic_jpeg_shift_rotate"): #проходим все классы

        k =len(os.listdir(address)) #количество файлов в классе
        d = 0
        
        for i in files:
            if d == k - min_value:
                break
            os.remove(address + "/" + i)
            d += 1


def image_list():
    count = 0

    for address, dir, files in os.walk("Cyrillic"):
        for file in files:
            make_background(address + "/" + file, address.split("/")[1], str(count))
            count += 1
        count = 0

def image_shift():
    count = 0

    for address, dir, files in os.walk("Cyrillic_jpeg"):
        for file in files:
            shift(address + "/" + file, address.split("/")[1], str(count))
            count += 1
        count = 0

def image_rotate():
    count = 0

    for address, dir, files in os.walk("Cyrillic_jpeg_shift"):
        for file in files:
            rotate_shift(address + "/" + file, address.split("/")[1], str(count))
            count += 1
        count = 0

def delete():
    for address, dir, files in os.walk("Cyrillic_jpeg_shift"):
        for file in files:
            os.remove(address + "/" + file)

def delete1():
    for l in list_charchest:
        for i in range(2750):
            os.remove(l+str(i))

def rename():
    count = 0
    for address, dir, files in os.walk("Cyrillic_jpeg_shift_rotate"):
        for file in files:
            os.rename(address + "/" + file, address + "/" + address.split("/")[1] + str(count) + ".jpeg")
            count += 1
        count = 0
#image_list()
#image_shift()
#image_rotate()
#balancing()
#rename()
