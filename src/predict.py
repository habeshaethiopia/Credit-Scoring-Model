import joblib
import pandas as pd
import numpy as np
import sklearn
def predict_fraud(new_data):
    """
    Preprocesses new data and makes predictions using the trained model.
    
    Args:
        new_data (pd.DataFrame): New transaction data with the same features as the training data.
    
    Returns:
        predictions (np.array): Predicted fraud results (1 for fraud, 0 for no fraud).
    """
    # Load the model, scaler, and encoder
    model = joblib.load('model/credit_scoring_model.pkl')
    scaler = joblib.load('model/scaler.pkl')
    label_encoder = joblib.load('model/label_encoder.pkl')
    
    # Preprocess the new data (same steps as during training)
    new_data['TransactionStartTime'] = pd.to_datetime(new_data['TransactionStartTime'])
    new_data['TransactionHour'] = new_data['TransactionStartTime'].dt.hour
    new_data['TransactionDay'] = new_data['TransactionStartTime'].dt.day
    new_data['TransactionMonth'] = new_data['TransactionStartTime'].dt.month
    new_data['TransactionDayOfWeek'] = new_data['TransactionStartTime'].dt.dayofweek
    
    # Feature engineering
    new_data['TransactionCount'] = new_data.groupby('AccountId')['TransactionId'].transform('count')
    new_data['AvgTransactionAmount'] = new_data.groupby('AccountId')['Amount'].transform('mean')
    new_data['TimeSinceLastTransaction'] = new_data.groupby('AccountId')['TransactionStartTime'].diff().dt.total_seconds() / 3600
    new_data['TimeSinceLastTransaction'].fillna(0, inplace=True)
    new_data['UniqueProductCount'] = new_data.groupby('AccountId')['ProductId'].transform('nunique')
    new_data['UniqueCategoryCount'] = new_data.groupby('AccountId')['ProductCategory'].transform('nunique')
    new_data['PastFraudCount'] = new_data.groupby('AccountId')['FraudResult'].transform('cumsum') - new_data['FraudResult']
    
    # Encode categorical variables
    new_data['ChannelId'] = label_encoder.transform(new_data['ChannelId'])
    new_data = pd.get_dummies(new_data, columns=['CurrencyCode', 'CountryCode', 'ProductCategory'], drop_first=True)
    
    # Scale numerical features
    numerical_features = ['Amount', 'Value', 'TransactionCount', 'AvgTransactionAmount', 
                          'TimeSinceLastTransaction', 'UniqueProductCount', 'UniqueCategoryCount', 'PastFraudCount']
    new_data[numerical_features] = scaler.transform(new_data[numerical_features])
    
    # Drop unnecessary columns
    new_data = new_data.drop(['TransactionId', 'BatchId', 'SubscriptionId', 'CustomerId', 'TransactionStartTime'], axis=1)
    
    # Make predictions
    predictions = model.predict(new_data)
    
    return predictions
import pandas as pd

# Sample data
data = {
    "TransactionId": ["TransactionId_76871"],
    "BatchId": ["BatchId_36123"],
    "AccountId": ["AccountId_3957"],
    "SubscriptionId": ["SubscriptionId_887"],
    "CustomerId": ["CustomerId_4406"],
    "CurrencyCode": ["UGX"],
    "CountryCode": ["256"],
    "ProviderId": ["ProviderId_6"],
    "ProductId": ["ProductId_10"],
    "ProductCategory": ["airtime"],
    "ChannelId": ["ChannelId_3"],
    "Amount": [1000],
    "Value": [1000],
    "TransactionStartTime": ["2018-11-15T02:18:49Z"],
    "PricingStrategy": ["2"],
    "FraudResult": [0]
}
if __name__=="__main__":
    # Convert to DataFrame
    new_data = pd.DataFrame(data)

    # Display the sample data
    print(new_data)
    predictions = predict_fraud(new_data)
    print("Predictions:", predictions)