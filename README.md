# Simple-Classifier-Test
DATA-LEVEL INFORMATION
•	2 Class problems: Benign and Malignant. [B and M : 0 or 1 (Binary)]
•	Structured data
•	No nulls(dataframe.isnull().sum())
•	570 data points.
•	10 to power -4 to 10 to power 4 values. (min to max ; 0 to 1) MinMaxScaler()
•	212 Malignant; 357 Benign
•	Dropout 20% - to prevent overfitting. (works well for upcoming data in future)
•	Data types

![image](https://user-images.githubusercontent.com/40331004/207312346-3167a295-6523-41ca-8873-2ff4b69949c4.png)


MODEL-LEVEL INFORMATION
![image](https://user-images.githubusercontent.com/40331004/207312622-fc7331f9-95be-42cf-b200-b0262ad5ccae.png)
•	X -> all the features; Y -> Output
•	x_train and y_train to train the model, x_test and y_test to test the model
•	75% data to train and 25% to test => about 142 records to test
•	Bottom layer- I/P Layer
•	Dense layer – Rectified Linear Activation Function 
![image](https://user-images.githubusercontent.com/40331004/207312697-25f6fac1-2a96-4d96-8d54-0d0208d22d40.png)
•	Final Layer activation function
![image](https://user-images.githubusercontent.com/40331004/207312734-d5be22e0-2614-4838-86a1-f3ded7a2ef8c.png)
•	I/P Layer – 30 x 16 = 480
•	16 more units in hidden layer 
•	480 + 16 =496 parameters
•	Final layer- 16 weights + 1 bias = 17
•	Get to a saturation points based on epochs
========================================================================================================================================
At 150 epochs  1/7 [===>..........................] - ETA: 0s - loss: 0.1019 - accuracy: 0.9844                                                                                 7/7 [==============================] - 0s 6ms/step - loss: 0.1378 - accuracy: 0.9507 - val_loss: 0.0927 - val_accuracy: 0.9790

At 100 epochs
 1/7 [===>..........................] - ETA: 0s - loss: 0.1431 - accuracy: 0.9844                                                                                 7/7 [==============================] - 0s 6ms/step - loss: 0.1898 - accuracy: 0.9272 - val_loss: 0.1298 - val_accuracy: 0.9580
