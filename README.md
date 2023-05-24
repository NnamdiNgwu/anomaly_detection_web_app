
#Fraud Detection Web Application

This project is a web application designed for anomaly detection in transactions, specifically targeting fraud detection. The application utilizes advanced machine learning techniques to distinguish between fraudulent and non-fraudulent transactions, providing an efficient solution for identifying potential financial risks. The web application is built using the Flask framework, which allows for seamless development and deployment.

Features

Anomaly Detection: The application incorporates machine learning algorithms to detect anomalies in transaction data, with a specific focus on identifying fraudulent activities.
Web Interface: The user-friendly web interface, powered by Flask, allows users to interact with the application easily and view the results of the anomaly detection process.
Realistic Observation Environment: The framework includes a realistic observation setup to monitor the performance of the machine learning model, with a particular emphasis on evaluating the Receiver Operating Characteristic (ROC) curve.
SMOTE for Data Balancing: The dataset is balanced using the Synthetic Minority Over-sampling Technique (SMOTE) to address any class imbalance issues during model training.
Python Implementation: The application is developed using Python, leveraging its robust libraries and frameworks for machine learning, data analysis, and web development.
Model Performance

The logistic regression model, with the following hyperparameters, achieved impressive performance:

C=0.14121820668347934
penalty='l1'
solver='liblinear'
Accuracy: 0.947
Precision: 0.919
Recall: 0.919
F1-score: 0.946
These scores demonstrate the effectiveness of the logistic regression model in accurately detecting fraudulent transactions.

Usage

Clone the repository: git clone https://github.com/NnamdiNgwu/anomaly-detection-web-app
Install the required dependencies: pip install -r requirements.txt
Prepare the transaction data in a suitable format for model training and evaluation.
Balance the dataset using SMOTE to address any class imbalance issues.
Configure the necessary parameters in the application, such as the model settings, data sources, and web interface customization.
Train the machine learning model using the preprocessed and balanced dataset.
Launch the web application: python app.py
Access the application via the provided URL and use the web interface, powered by Flask, to upload transaction data for anomaly detection.
Monitor the results, including the detected anomalies, model performance metrics, and the ROC curve.
Requirements

Python 3.x
Dependencies listed in requirements.txt
Transaction data for training and testing the model
Contributions

Contributions to this project are welcome! If you have any suggestions, bug fixes, or additional features, feel free to open an issue or submit a pull request.

License

This project is licensed under the MIT License.

Contact

For any inquiries or feedback, please reach out to nnamdingwu@yandex.com.com.

Feel free to customize and modify this README to reflect the performance of your logistic regression model. Provide clear instructions for setup, usage, and contributions to encourage collaboration and engagement from the GitHub community.



