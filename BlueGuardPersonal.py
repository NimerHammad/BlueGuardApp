import sys
import threading
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit
from PyQt5.QtGui import QTextCursor
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import nmap
import csv

# Function to load data from CSV file
def load_data(file_path="C:/Users/Developer Security/Desktop/personal_security_data.csv"):
    try:
        data = np.genfromtxt(file_path, delimiter=',', skip_header=1)
        features = data[:, :-1]
        labels = data[:, -1]
        return features, labels
    except Exception as e:
        log_activity(f"Error loading data: {str(e)}", "Data Loading Error")
        return None, None

# Function to save data to CSV file
def save_data(file_path, features, labels):
    try:
        data = np.column_stack((features, labels))
        np.savetxt(file_path, data, delimiter=',', header='Feature1,Feature2,Label', comments='')
        log_activity("Data saved to CSV file.", "Data Save")
    except Exception as e:
        log_activity(f"Error saving data: {str(e)}", "Data Save Error")

# Function to perform network scan
def perform_network_scan():
    network_scanner = nmap.PortScanner()
    network_scanner.scan('192.168.1.0/24', '1-1024')
    return network_scanner.all_hosts()

# Function to extract features from network scan result
def extract_features(network_scan_result):
    return [len(host) for host in network_scan_result]

# Class for Personal Security Application
class PersonalSecurityApp(QWidget):
    def __init__(self):
        super().__init__()

        # Train the machine learning model
        self.random_forest_model = self.train_model()

        # Initialize the user interface
        self.setup_ui()

    # Initialize the user interface
    def setup_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Personal Security Tool")
        layout.addWidget(label)

        custom_action_button = QPushButton("Execute Custom Action")
        custom_action_button.clicked.connect(self.execute_custom_action)
        layout.addWidget(custom_action_button)

        personal_malware_scan_button = QPushButton("Perform Personal Malware Analysis")
        personal_malware_scan_button.clicked.connect(self.analyze_personal_malware)
        layout.addWidget(personal_malware_scan_button)

        real_time_monitoring_button = QPushButton("Initiate Personal Real-time Monitoring")
        real_time_monitoring_button.clicked.connect(self.initiate_personal_real_time_monitoring)
        layout.addWidget(real_time_monitoring_button)

        # Add other personal-specific buttons and functionalities

        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        layout.addWidget(self.log_display)

        self.setLayout(layout)

    # Train the machine learning model
    def train_model(self):
        # Load data from the CSV file
        features, labels = load_data()
        if features is not None and labels is not None:
            # Further processing and model training...
            X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            test_predictions = model.predict(X_test)
            accuracy = accuracy_score(y_test, test_predictions)
            print(f"Random Forest Model Accuracy: {accuracy:.4f}")

            # Save the trained model back to the CSV file
            save_data("C:/Users/Developer Security/Desktop/personal_security_data.csv", X_train, y_train)

            return model
        else:
            # Handle the case where data loading failed
            print("Error loading data. Model not trained.")
            return None

    # Function to execute custom action
    def execute_custom_action(self):
        self.log_activity("Custom action executed.", "Custom Action")

    # Function for personal malware analysis
    def analyze_personal_malware(self):
        try:
            analysis_result = "Performing Personal Malware Analysis..."
            personal_api_key = "8f55a1ef0230f47efc444d1055a233df793aa23757559e779003dec201b6cb50"
            disk_path = "C:/"
            
            # Iterate through files in the disk for analysis
            for root, dirs, files in os.walk(disk_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Call your malware analysis function here with 'file_path'

            self.log_activity(analysis_result, "Personal Malware Analysis Result")
        except Exception as e:
            self.log_activity(f"Error: {str(e)}", "Error")

    # Function to initiate personal real-time monitoring
    def initiate_personal_real_time_monitoring(self):
        self.log_activity("Personal Real-time monitoring initiated.", "Personal Real-time Monitoring")

    # Function to log messages
    def log_activity(self, message, category):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} [{category}]: {message}"
        self.log_display.append(log_entry)
        cursor = self.log_display.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.log_display.setTextCursor(cursor)

# Entry point for the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    personal_app = PersonalSecurityApp()
    sys.exit(app.exec_())


