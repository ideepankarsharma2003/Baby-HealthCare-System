import tensorflow as tf

# from keras.preprocessing.image import load_img
# from keras.preprocessing.image import img_to_array
# from keras.preprocessing.image import array_to_img
# load the image
img = tf.keras.utils.load_img('F:\AIML\BabyHealthcareSystem\Emotion-Detection-Classifier\download (1).jpg')
print(type(img))
# convert to numpy array
img_array = tf.keras.utils.img_to_array(img)
print(img_array.dtype)
print(img_array.shape)
# convert back to image
img_pil = tf.keras.utils.array_to_img(img_array)
print(type(img))
