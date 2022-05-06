# Human Activity Classification from Accelerometer Time-series data
Master's Capstone Project
Sai Surya Nattuva <br />
Advisor: Prof Gokhan Kul <br />
University of Massachusetts Dartmouth <br />
----

#### Abstract
<p>Human activity can be observed and measured by employing different sensors on different parts of the body. An increase in the usage of wearable devices by people has led to increased research in Human Activity monitoring and analysis. This analysis has helped develop many technologies like fall detection, irregular heart rhythms, walking steadiness, posture, etc. This project focuses on classifying the activity performed by a human from time-series data generated from the user's phone's accelerometer. The time-series data is first converted into 2-D images and then fed to a CNN to learn five different activities from 4 features of the data. The project's primary focus is to leverage the predicting power of CNNs on time-series data with a small number of training samples and input channels. </p>
----

# References
> A. Jafari, A. Ganesan, C. S. K. Thalisetty, V. Sivasubramanian, T. Oates and T. Mohsenin, "SensorNet: A Scalable and Low-Power Deep Convolutional Neural Network for Multimodal Data Classification," in IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 66, no. 1, pp. 274-287, Jan. 2019, doi: 10.1109/TCSI.2018.2848647.
> Physics Toolbox Sensor Suite Pro, Vieyra Software
> {Label Studio}: Data labeling software, Heartex Labs
----

# Instructions
The data used in this project is collected by recording the accelerometer sensor in an android smartphone polled at 100Hz. I have used Physics Toolbox Sensor Suite Pro by Vieyra Software to record the accelerometer. The data is generated by recording the movements of a user's dominant arm during a boxing practice session. The user was holding the smartphone in his dominant arm. The data was collected for a session which lasted for about 110 seconds. The raw CSV consists of 5 columns - time(ss.mmmmmmm), gFx(dd.ffff), gFy(dd.ffff), gFz(dd.ffff), TgF(dd.ffff)
<br />

This repo consists of 3 iPython notebooks - *data_cleaner*, *data_labeller*, and *Human Activity Classification from Time Series Data*

- data_cleaner: This notebook helps to clean the input csv time series data by rounding off the timestamps and adding a new column by formatting the time stamps into UTC format. This is required to help with the data labelling process. It is a simple notebook and the process order is as the cells are ordered. The data has 6 columns - time(ss.mmmmmmm), gFx(dd.ffff), gFy(dd.ffff), gFz(dd.ffff), TgF(dd.ffff), TS(%Y-%m-%d %H:%M:%S.%f)
- data_labeller: This notebooks helps with labelling the cleaned CSV data from the annotations JSON file generated by Label-Studio. The notebook uses the cleaned CSV file and the annotations from Label-studio and generated the labelled CSV file. This data will be fed to the machine learning model. The data has 7 columns time(ss.mmmmmmm), gFx(dd.ffff), gFy(dd.ffff), gFz(dd.ffff), TgF(dd.ffff), TS(%Y-%m-%d %H:%M:%S.%f), label(d)
- Human Activity Classification from Time Series Data: This notebook is has the code related to creating windows, splitting the input data into train, validation and test sets, hyperparameter tuning, model training, model learning plots, and model evaluation. This notebook's execution is structured and divided into subsections with brief function descriptions at the start of each function.
<br />

Note: Every notebook in this project is located in the `./code` folder. Every notebook is supposed to be run in the order of the cells to ensure that the code runs seamlessly. 

