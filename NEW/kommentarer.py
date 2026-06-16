from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# train test split
# fit model etc
# predict on test data:
y_pred = model.predict(X_test_sm)

# calc stats on test predictions
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2_test = r2_score(y_test, y_pred)

# Från

import statsmodels.api as sm
model = sm.OLS(y_train, X_train_sm).fit()
print(model.summary())  