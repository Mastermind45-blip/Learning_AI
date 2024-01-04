import numpy as np
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import RMSprop  
from keras.utils import to_categorical

# Load data 
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Preprocess data
X_train = X_train.astype('float32')/255  
X_test = X_test.astype('float32')/255
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Buat model CNN 
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(32, 32, 3)))
model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
model.add(Conv2D(128, kernel_size=(3,3), activation='relu')) # tambah layer
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2)) # kurangi dropout

model.add(Flatten())
model.add(Dense(256, activation='relu')) # tambah filter
model.add(Dropout(0.5))  
model.add(Dense(10, activation='softmax'))

# Compile dan training
opt = RMSprop(learning_rate=0.001) 
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy']) 

model.fit(X_train, y_train, batch_size=64, epochs=50, # epochnya ditambah
          validation_data=(X_test, y_test)) 

# Evaluasi model
score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])