import google.cloud.ml as ml

def deploy_models(model_folder, rf, vae):
    ml.upload_model(model_folder, rf)
    ml.upload_model(model_folder, vae)

def monitor_data(rf, vae, scaler, threshold, alert_function):
    while True:
        new_data = get_sensor_data()
        new_data = scaler.transform(new_data)
        anomaly_scores = vae.predict(new_data)
        if np.any(anomaly_scores > threshold):
            failure_prediction = rf.predict(new_data[anomaly_scores > threshold])
            if np.any(failure_prediction):
                alert_function()
        time.sleep(60)  # Check every minute