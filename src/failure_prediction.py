from sklearn.ensemble import RandomForestClassifier

def train_failure_prediction_model(X_train_anomalies, y_train_anomalies):
    rf = RandomForestClassifier()
    rf.fit(X_train_anomalies, y_train_anomalies)
    return rf

def evaluate_model(rf, X_test, y_test):
    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    return accuracy, precision, recall, f1