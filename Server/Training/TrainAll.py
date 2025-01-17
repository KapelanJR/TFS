from keras import layers
from keras import models
from keras.preprocessing import image
import os,shutil
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras import regularizers
from sklearn.metrics import classification_report,confusion_matrix
from keras.models import load_model
import pandas as pd
from keras import regularizers

train_dir = "readyDatasets/cleaned/polish1/train"
validation_dir = "readyDatasets/cleaned/polish1/validation"
test_dir = "readyDatasets/cleaned/polish1/test"

train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

#2 Dense(256,1024) 1 conv(256)
def train1():
    train_generator = train_datagen.flow_from_directory(train_dir,target_size=(20,32),batch_size=90,class_mode='categorical',shuffle=True)
    validation_generator = validation_datagen.flow_from_directory(validation_dir,target_size=(20,32),batch_size=90,class_mode='categorical',shuffle=True)
    test_generator = test_datagen.flow_from_directory(test_dir,target_size=(20,32),batch_size=1,class_mode='categorical',shuffle=True)

    model = models.Sequential()
    model.add(layers.Conv2D(256,(3,3),activation='relu',input_shape=(20,32,3)))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(256,activation='relu'))
    model.add(layers.Dense(1024,activation='relu'))
    model.add(layers.Dense(88,activation='softmax'))

    model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['acc'])

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=train_generator.n//train_generator.batch_size,
        epochs=7,
        validation_data=validation_generator,
        validation_steps=validation_generator.n//validation_generator.batch_size,
    )

    score = model.evaluate_generator(test_generator, test_generator.n)

    model.save("test1_{}.h5".format(score[1]))

#2 Dense(256,1024) 1 conv(256) Dropout(0.3)
def train2():
    train_generator = train_datagen.flow_from_directory(train_dir,target_size=(20,32),batch_size=90,class_mode='categorical',shuffle=True)
    validation_generator = validation_datagen.flow_from_directory(validation_dir,target_size=(20,32),batch_size=90,class_mode='categorical',shuffle=True)
    test_generator = test_datagen.flow_from_directory(test_dir,target_size=(20,32),batch_size=1,class_mode='categorical',shuffle=True)

    model = models.Sequential()
    model.add(layers.Conv2D(256, (3, 3), activation='relu', input_shape=(20, 32, 3)))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.3))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dense(88, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                    optimizer='rmsprop', metrics=['acc'])

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=train_generator.n//train_generator.batch_size,
        epochs=7,
        validation_data=validation_generator,
        validation_steps=validation_generator.n//validation_generator.batch_size,
    )

    score = model.evaluate_generator(test_generator, test_generator.n)

    model.save("test2_{}.h5".format(score[1]))

#2 Dense(128,256) 2 conv(64,128)
def train3():
    train_generator = train_datagen.flow_from_directory(train_dir,target_size=(20,32),batch_size=90,class_mode='categorical',shuffle=True)
    validation_generator = validation_datagen.flow_from_directory(validation_dir,target_size=(20,32),batch_size=90,class_mode='categorical',shuffle=True)
    test_generator = test_datagen.flow_from_directory(test_dir,target_size=(20,32),batch_size=1,class_mode='categorical',shuffle=True)

    model = models.Sequential()
    model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(20, 32, 3)))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(20, 32, 3)))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dropout(0.3))
    model.add(layers.Dense(88, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                    optimizer='rmsprop', metrics=['acc'])

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=train_generator.n//train_generator.batch_size,
        epochs=7,
        validation_data=validation_generator,
        validation_steps=validation_generator.n//validation_generator.batch_size,
    )

    score = model.evaluate_generator(test_generator, test_generator.n)

    model.save("test3_{}.h5".format(score[1]))

#2 Dense(128,256) 2 conv(64,512)
def train4():
    train_generator = train_datagen.flow_from_directory(train_dir,target_size=(20,32),batch_size=90,class_mode='categorical',shuffle=True)
    validation_generator = validation_datagen.flow_from_directory(validation_dir,target_size=(20,32),batch_size=90,class_mode='categorical',shuffle=True)
    test_generator = test_datagen.flow_from_directory(test_dir,target_size=(20,32),batch_size=1,class_mode='categorical',shuffle=True)

    model = models.Sequential()
    model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(20, 32, 3)))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(88, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['acc'])

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=train_generator.n//train_generator.batch_size,
        epochs=7,
        validation_data=validation_generator,
        validation_steps=validation_generator.n//validation_generator.batch_size,
    )

    score = model.evaluate_generator(test_generator, test_generator.n)

    model.save("test4_{}.h5".format(score[1]))

#2 Dense(256,1024) 2 Conv(128,256)
def train5():
    train_generator = train_datagen.flow_from_directory(train_dir, target_size=(
        20, 32), batch_size=90, class_mode='categorical', shuffle=True)
    validation_generator = validation_datagen.flow_from_directory(
        validation_dir, target_size=(20, 32), batch_size=90, class_mode='categorical', shuffle=True)
    test_generator = test_datagen.flow_from_directory(test_dir, target_size=(
        20, 32), batch_size=1, class_mode='categorical', shuffle=True)

    model = models.Sequential()
    model.add(layers.Conv2D(
        128, (3, 3), activation='relu', input_shape=(20, 32, 3)))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Conv2D(
        256, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dense(88, activation='softmax'))


    model.compile(loss='categorical_crossentropy',
                optimizer='rmsprop', metrics=['acc'])

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=train_generator.n//train_generator.batch_size,
        epochs=7,
        validation_data=validation_generator,
        validation_steps=validation_generator.n//validation_generator.batch_size,
    )

    score = model.evaluate_generator(test_generator, test_generator.n)

    model.save("test5_{}.h5".format(score[1]))

#2 Dense(256,1024) 2 Conv(64,128)
def train6():
    train_generator = train_datagen.flow_from_directory(train_dir, target_size=(
        20, 32), batch_size=90, class_mode='categorical', shuffle=True)
    validation_generator = validation_datagen.flow_from_directory(
        validation_dir, target_size=(20, 32), batch_size=90, class_mode='categorical', shuffle=True)
    test_generator = test_datagen.flow_from_directory(test_dir, target_size=(
        20, 32), batch_size=1, class_mode='categorical', shuffle=True)

    model = models.Sequential()
    model.add(layers.Conv2D(
        64, (3, 3), activation='relu', input_shape=(20, 32, 3)))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Conv2D(
        128, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dense(88, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop', metrics=['acc'])

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=train_generator.n//train_generator.batch_size,
        epochs=7,
        validation_data=validation_generator,
        validation_steps=validation_generator.n//validation_generator.batch_size,
    )

    score = model.evaluate_generator(test_generator, test_generator.n)

    model.save("test6_{}.h5".format(score[1]))

#2 Dense(256,1024) 1 conv(256) Augmentation
def train7():

    train_datagen = ImageDataGenerator(rescale=1./255,
    rotation_range=15,
    zoom_range=0.1,
    width_shift_range=0.15,
    height_shift_range=0.15)

    train_generator = train_datagen.flow_from_directory(train_dir, target_size=(
        20, 32), batch_size=90, class_mode='categorical', shuffle=True)
    validation_generator = validation_datagen.flow_from_directory(
        validation_dir, target_size=(20, 32), batch_size=90, class_mode='categorical', shuffle=True)
    test_generator = test_datagen.flow_from_directory(test_dir, target_size=(
        20, 32), batch_size=1, class_mode='categorical', shuffle=True)

    model = models.Sequential()
    model.add(layers.Conv2D(256, (3, 3), activation='relu', input_shape=(20, 32, 3)))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dense(88, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop', metrics=['acc'])

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=train_generator.n//train_generator.batch_size,
        epochs=7,
        validation_data=validation_generator,
        validation_steps=validation_generator.n//validation_generator.batch_size,
    )

    score = model.evaluate_generator(test_generator, test_generator.n)

    model.save("test7_{}.h5".format(score[1]))


#2 Dense(256,1024) 1 conv(256) regularizers
def train8():
    train_generator = train_datagen.flow_from_directory(train_dir, target_size=(
        20, 32), batch_size=90, class_mode='categorical', shuffle=True)
    validation_generator = validation_datagen.flow_from_directory(
        validation_dir, target_size=(20, 32), batch_size=90, class_mode='categorical', shuffle=True)
    test_generator = test_datagen.flow_from_directory(test_dir, target_size=(
        20, 32), batch_size=1, class_mode='categorical', shuffle=True)

    model = models.Sequential()
    model.add(layers.Conv2D(
        256, (3, 3), activation='relu', input_shape=(20, 32, 3)))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.001)))
    model.add(layers.Dense(1024, activation='relu', kernel_regularizer=regularizers.l2(0.001)))
    model.add(layers.Dense(88, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop', metrics=['acc'])

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=train_generator.n//train_generator.batch_size,
        epochs=7,
        validation_data=validation_generator,
        validation_steps=validation_generator.n//validation_generator.batch_size,
    )

    score = model.evaluate_generator(test_generator, test_generator.n)

    model.save("test8_{}.h5".format(score[1]))

def main():
    '''
    print("******************** Model 1 ********************")
    train1()
    print("******************** Model 2 ********************")
    train2()
    print("******************** Model 3 ********************")
    train3()
    print("******************** Model 4 ********************")
    train4()
    print("******************** Model 2 ********************")
    train2()
    print("******************** Model 5 ********************")
    train5()
    print("******************** Model 6 ********************")
    train6()
    print("******************** Model 7 ********************")
    train7()
    '''
    print("******************** Model 8 ********************")
    train8()

if __name__ == "__main__":
    main()
