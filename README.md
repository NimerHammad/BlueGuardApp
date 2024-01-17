# BlueGuardPersonal

BlueGuardPersonal is an open-source security tool designed for personal use, providing features such as custom actions, personal malware analysis, and real-time monitoring.

## Prerequisites

Before using BlueGuardPersonal, ensure you have the following:

- Python 3.x installed on your machine
- Necessary Python packages installed: PyQt5, requests, scikit-learn, numpy, nmap

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/NimerHammad/BlueGuardPersonal.git


2. Navigate to the project directory:

cd BlueGuardPersonal

3. Install the required Python packages:

pip install -r requirements.txt



Usage

1. Run the BlueGuardPersonal script:

   python BlueGuardPersonal.py

2. The GUI application will appear, providing options for custom actions, personal malware analysis, and real-time monitoring.


Configuration
The script assumes a CSV file located at C:/Users/Your-User-Name/Desktop/personal_security_data.csv for training the machine learning model. Ensure your CSV file follows the specified format.

For personal malware analysis, update the personal_api_key variable in the script with your VirusTotal API key. 


Contributing


If you'd like to contribute to BlueGuardPersonal, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature:
git checkout -b feature-name

3. Commit your changes:
git commit -m "Description of your changes"

4. Push the branch:
git push origin feature-name

5. Open a pull request on GitHub.














