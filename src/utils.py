import pandas as pd
import smtplib
from email.mime.text import MIMEText

def get_sensor_data():
    """
    Retrieves sensor data from the manufacturing equipment.
    
    This is a simulated example that generates random sensor data.
    In a real-world scenario, you would replace this with code to retrieve data from your actual equipment or data source.
    
    Returns:
        pd.DataFrame: A pandas DataFrame containing the sensor data.
    """
    import random
    
    # Random sensor data
    temp = random.uniform(60, 90)
    vibration = random.uniform(1, 5)
    pressure = random.uniform(80, 100)
    rpm = random.randint(1000, 1500)
    load = random.uniform(50, 90)
    
    # Create a pandas DataFrame
    new_data = pd.DataFrame({
        'temp': [temp],
        'vibration': [vibration],
        'pressure': [pressure],
        'rpm': [rpm],
        'load': [load]
    })
    
    return new_data

def send_alert():
    """
    Sends an email alert to the maintenance team about a potential equipment failure.
    
    This is a simulated example that sends an email using SMTP.
    In a real-world scenario, you would replace this with code to integrate with your organization's alert or notification system.
    """
    # Email settings
    sender_email = 'your_email@example.com'
    receiver_email = 'equipment_failure_alert@example.com'
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'
    
    # Email content
    subject = 'Potential Equipment Failure Detected'
    body = 'This is an automated alert from the Predictive Maintenance System.\n\nA potential equipment failure has been detected based on the analysis of sensor data. Please investigate and take necessary actions.'
    
    # Create the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.send_message(msg)
        print('Alert email sent successfully.')