import tensorflow as tf

print('Loading model ...')
model = tf.keras.models.load_model('saved_model')

class_names = ['Dry_skin','Normal_skin','Oil_skin']

def load_and_prep_image(filename, img_shape=224):
  img = tf.io.read_file(filename)
  # Decode it into a tensor
  img = tf.image.decode_jpeg(img)
  # Resize the image
  img = tf.image.resize(img, [img_shape, img_shape])
  # Rescale the image (get all values between 0 and 1)
  img = img/255.
  return img

def predict_class(filename):
  """
  Imports an image located at filename, makes a prediction with model
  and plots the image with the predicted class as the title.
  """
  print('Loading image ...')
  # Import the target image and preprocess it
  img = load_and_prep_image(filename)
  
  print('Predicting class of image ...')

  # Make a prediction
  pred = model.predict(tf.expand_dims(img, axis=0))
  print(pred)

  # Add in logic for multi-class & get pred_class name
  if len(pred[0]) > 1:
    pred_class = class_names[tf.argmax(pred[0])]
  else:
    pred_class = class_names[int(tf.round(pred[0]))]
  print('Predicted class:', pred_class)
  return pred_class

predict_class('test_image.jpg')