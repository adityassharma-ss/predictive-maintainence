import numpy as np

def detect_anomalies(vae, X_test, threshold=0.95):
    generated_data = vae.decoder.predict(tf.random.normal(shape=(1000, 8)))
    anomaly_scores = np.mean(np.abs(generated_data - X_test), axis=1)
    threshold_value = np.percentile(anomaly_scores, threshold * 100)
    anomalies = X_test[anomaly_scores > threshold_value]
    return anomalies, anomaly_scores