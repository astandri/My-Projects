# Image Classification using keras

## Meet my twin cats, Claudia and Lucy
![Claudia](https://raw.githubusercontent.com/astandri/My-Projects/master/MyCat%20Classification%20with%20Keras/Claudia/Claudia15.jpg)
![Lucy](https://raw.githubusercontent.com/astandri/My-Projects/master/MyCat%20Classification%20with%20Keras/Lucy/Lucy7.jpg)

In this project, I'll try to make a model to classify which one is Claudia, which one is Lucy.

To summarize, here's activities covered in this project:
1. **Data collection**:
	took 100 samples of photos for both of them manually
	
2. **Data Preprocessing**:
	Using OpenCV with the helps from matplotlib and pandas, I preprocess the raw images to become a clean dataset stored in dataframe. 
	I further split this dataset to 80:20 ratio for Testing purpose
	
3. **Model Building**:
	I created a class to automatically build a model with desired number of layers and nodes per layer using keras.
	Defaulted to 1 layer and 10 nodes as base model.
	
4. **Training and Validation**:
	Trained models will be stored in Trained Models folder using .h5 extensions

5. **Experimentation and Optimization**:
	Using my newly created class before, I did some experimentation an optimizations in hyperparameters to build the best model.

6. **Testing**

