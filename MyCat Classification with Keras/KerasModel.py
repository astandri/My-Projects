#Supporting Libraries
import numpy as np
import pandas as pd

#Keras
from keras.layers import Dense
from keras.utils import to_categorical
from keras.models import Sequential
from keras.callbacks import EarlyStopping

#Model
class Model():
    def __init__(self, file):
        self.file = file
        self.model = Sequential()
        self.model_name = ''
        
        self.df = pd.read_csv(self.file)
        self.y = to_categorical(self.df['label'])
        self.X = self.df.drop('label',axis=1).as_matrix()
        self.X = np.multiply(self.X, 1/255)
        
    def build_model(self, layers = 1, nodes = 10):          
        #layers
        for layer in range(layers):
            if layer==0:
                self.model.add(Dense(nodes, activation='relu', input_shape=(self.X.shape[1],)))
            else:
                self.model.add(Dense(nodes, activation='relu'))
            
        #Output Layer
        self.model.add(Dense(self.y.shape[1], activation='softmax'))
        
        self.model_name = 'model {}layers and {}nodes.h5'.format(layers, nodes)
        print('Model has been created, ready for training!')
        
    def train_model(self, patience = 1, split = 0.2, epochs = 10):        
        #Compile
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        #Training
        early_stopping_monitor = EarlyStopping(patience=patience)

        self.model.fit(self.X, self.y, validation_split=split, epochs=epochs, callbacks=[early_stopping_monitor])
        
        print(self.model.summary())
        print('Model has been trained, validated, and saved!')
        
        self.model.save('Trained Models/{}'.format(self.model_name))
        

