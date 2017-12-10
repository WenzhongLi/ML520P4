# coding : utf-8
#author : Heng-Shao Chen

# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop, SGD, Adam, Adamax
from keras.utils import to_categorical
#from keras import initializations

import scipy.io as sio
#import pydot


batch_size = 10
nb_epoch = 300

# 從Mat檔案讀取訓練/測試 參數
mat_contents = sio.loadmat('gray.mat')
X_train = mat_contents['gray']

mat_contents = sio.loadmat('rgb60.mat')
Y_train = mat_contents['rgb60']

#mat_contents = sio.loadmat('meter_4class_testing.mat')
#X_test = mat_contents['accentCoeffTesting']

#mat_contents = sio.loadmat('meter_4class_testing_answer.mat')
#Y_test = mat_contents['DeepLearning_correctMeterTesting']

print('X_train shape:', X_train.shape)
#print('X_test shape:', X_test.shape)


# 建立模型
model = Sequential([
Dense(60, input_dim = 60),
#Dropout(0.25),
Activation('relu'),

Dense(60),
Activation('relu'),

Dense(60),
Activation('relu'),

Dense(60),
Activation('relu'),

Dense(60),
Activation('softmax'),
])


# Optimizers
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.001)
sgd = SGD(lr=0.01, decay=0, momentum=0, nesterov=False)
adam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.005)
adamMax = Adamax(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

model.compile(
    optimizer=adam,
    loss='categorical_crossentropy',
    metrics=['categorical_accuracy'],
    )


print('Training ------')
model.fit(to_categorical(X_train), to_categorical(Y_train), epochs=nb_epoch, batch_size=batch_size, validation_split =0.2 )
#print(model.history)         , validation_split =0.1

#print('\n Testing ------')
#loss, accuracy = model.evaluate(X_test, Y_test,batch_size=batch_size)

#print('\n Predict ------')
#predictMatrix = model.predict(X_test, batch_size=batch_size, verbose=0)


#print('test loss:', loss)
#print('test accuracy', accuracy)
#print('predictMatrix', predictMatrix)
#sio.savemat('classification_results_from_DNN.mat', {'predictMatrix_DNN': predictMatrix, 'accuracy_DNN': accuracy})
#plot(model, to_file='model.png',show_shapes='True')
