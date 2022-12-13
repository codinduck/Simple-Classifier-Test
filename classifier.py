import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from matplotlib import pyplot as plt


#fetching the data

dataframe = pd.read_csv(r'C:\Users\Rajat Malhotra\Documents\Cancer detection\data\data.csv')
y=dataframe["diagnosis"].values
print("Binary classifiers are", np.unique(y))

#preprocessing the data

le=preprocessing.LabelEncoder()
mms=preprocessing.MinMaxScaler()
ny=le.fit_transform(y)
print("Encoded classifiers are", np.unique(ny))

#y represents output values
#x represents input set

x=dataframe.drop(labels = ["diagnosis","id"], axis=1)
x=x.loc[:, ~x.columns.str.contains('^Unnamed')]
mms.fit(x)
x=mms.transform(x)
print(x)

#train and test datasets
x_train, x_test, y_train, y_test=train_test_split(x, ny, test_size=0.25, random_state=42)
print("dimensions of training data set", x_train.shape)
print("dimensions of test data set", x_test.shape)

#Deep Learning model (adding layers)
model = Sequential()
model.add(Dense(16, input_dim=30, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
history = model.fit(x_train, y_train, verbose=1, epochs=100, batch_size=64, validation_data=(x_test, y_test))

#prediction
yp = model.predict(x_test)
yp = (yp > 0.5)
c = confusion_matrix(y_test,yp)
print(c)


