import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model,Sequential
from tensorflow.keras.layers import Input,GlobalAveragePooling2D,Dense,Dropout,Flatten
from tensorflow.keras.layers import Conv2D,MaxPooling2D,BatchNormalization
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop,Adam
#from tensorflow.keras import initializers
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True)

training_set = train_datagen.flow_from_directory(r'C:/Users/pranj/OneDrive/Desktop/ges_dataset/archive (2)/train/train',
                                                 target_size = (50, 50),
                                                 batch_size = 64,
                                                 class_mode = 'sparse')


test_datagen = ImageDataGenerator(rescale = 1./255)
test_set = test_datagen.flow_from_directory(r'C:/Users/pranj/OneDrive/Desktop/ges_dataset/archive (2)/test/test',
                                            target_size = (50, 50),
                                            batch_size = 64,
                                            class_mode = 'sparse')

cnn = tf.keras.models.Sequential()

cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[50, 50, 3],padding='same'))
cnn.add(tf.keras.layers.BatchNormalization())
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2))
cnn.add(tf.keras.layers.Dropout(0.25))

cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu',padding='same'))
cnn.add(tf.keras.layers.BatchNormalization())
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2))
cnn.add(tf.keras.layers.Dropout(0.25))

cnn.add(tf.keras.layers.Flatten())

# Step 4 - Full Connection
cnn.add(tf.keras.layers.Dense(units=1024, activation='relu'))

# Step 5 - Output Layer
cnn.add(tf.keras.layers.Dense(units=20, activation='softmax'))

# Part 3 - Training the CNN

# Compiling the CNN


#constructing callback to save best model to disk and reducing LR
from tensorflow.keras.callbacks import ModelCheckpoint,ReduceLROnPlateau
filepath=r'C:/Users/pranj/OneDrive/Desktop/gesture_recognition/weights.h5'
checkpoint = ModelCheckpoint(filepath,monitor='val_accuracy',mode='max',save_best_only=True,verbose=1)
lrp = ReduceLROnPlateau(monitor='val_loss', factor=0.99, patience=3)
callbacks=[checkpoint,lrp]

cnn.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])



#cnn.fit(x = training_set, validation_data = test_set, epochs=25)

train_steps=training_set.samples//64
validation_steps=test_set.samples//64


history=cnn.fit_generator(
    training_set,
    steps_per_epoch=train_steps,
    epochs=25,
    validation_data=test_set,
    validation_steps=validation_steps,
    callbacks=callbacks


)

cnn.save(r'C:/Users/pranj/OneDrive/Desktop/gesture_recognition')

