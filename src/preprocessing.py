from sklearn.preprocessing import StandardScaler


def scale_data(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(x_train)
    X_test_scaled = scaler.transform(x_test)
    return x_train_scaled, x_test_scaled, scaler