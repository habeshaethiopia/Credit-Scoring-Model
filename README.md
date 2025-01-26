
# Credit Scoring Model for Bati Bank  
**Predicting Default Risk for Buy-Now-Pay-Later Customers**  

---

## 📌 Project Overview  
Bati Bank has partnered with an eCommerce platform to launch a buy-now-pay-later (BNPL) service. This project aims to build a **credit scoring model** to classify users as high-risk (likely to default) or low-risk using transactional data. The solution includes:  
- **Proxy variable** for default risk (RFMS framework).  
- **Feature engineering** and Weight of Evidence (WoE) binning.  
- **ML models** (Logistic Regression, Random Forest) to predict risk probability.  
- **REST API** for real-time predictions and MLOps pipelines (CML/MLFlow).  

---

## 🎯 Objectives  
1. Define a default proxy variable using RFMS analysis.  
2. Perform exploratory data analysis (EDA) and feature engineering.  
3. Train and tune ML models to predict credit risk.  
4. Deploy the model via API and implement CI/CD pipelines.  

---

## 📊 Data Description  
**Dataset**: [Xente Challenge Dataset (Kaggle)](https://www.kaggle.com/datasets/atwine/xente-challenge)  
**Key Features**:  
- `TransactionId`, `CustomerId`, `Amount`, `FraudResult`  
- `ProductCategory`, `ChannelId`, `TransactionStartTime`  
- **Target Variable**: Custom proxy for default risk (under development).  

---

## 📂 Project Structure  
```
bati-bank-credit-scoring/  
├── data/                   # Raw and processed datasets  
├── notebooks/              # Jupyter notebooks for EDA and analysis  
│   ├── Task2_EDA.ipynb  
│   └── Task3_Feature_Engineering.ipynb  
├── src/  
│   ├── features/           # Feature engineering scripts  
│   ├── models/             # Model training and evaluation  
│   └── api/                # FastAPI deployment code  
├── docs/                   # Reports and references  
├── requirements.txt        # Python dependencies  
└── README.md  
```

---

## ⚙️ Installation  
1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/yourusername/bati-bank-credit-scoring.git  
   ```  
2. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

**Key Libraries**:  
- `pandas`, `scikit-learn`, `matplotlib`, `seaborn`  
- `FastAPI`, `uvicorn` (for API deployment)  
- `mlflow`, `cml` (for MLOps)  

---

## 🚀 Usage  
### 1. Data Preprocessing  
```python  
# Example: Aggregate customer-level features  
df_agg = df.groupby('CustomerId').agg(
    Total_Amount=('Amount', 'sum'),
    Avg_Amount=('Amount', 'mean')
)
```  

### 2. Model Training  
```bash  
# Train logistic regression model  
python src/models/train_model.py --model lr  
```  

### 3. Serve Model via API  
```bash  
uvicorn src.api.main:app --reload  
```  
**API Endpoint**:  
```bash  
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"customer_id": 123}'
```  

---

## 📈 Results  
### Key Insights from EDA  
- Fraudulent transactions represent **3%** of the data (class imbalance).  
- `Amount` and `Value` are highly correlated (ρ = 0.92).  
- Transactions peak on weekends.  

### Feature Importance (Preliminary)  
| Feature               | Importance |  
|-----------------------|------------|  
| Total_Amount          | 0.45       |  
| Transaction_Count     | 0.32       |  
| FraudResult           | 0.18       |  

---
