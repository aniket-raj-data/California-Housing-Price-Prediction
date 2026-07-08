# 🏡 California Housing Price Prediction
### **Machine Learning Pipeline using Random Forest Regressor**

---

## 📌 Project Overview
This repository contains a complete end-to-end Machine Learning workflow to predict housing prices in California. Using the classic **California Housing Dataset** from `scikit-learn`, we trained a **Random Forest Regressor** capable of handling complex, non-linear feature interactions to estimate median house values.

### 📊 Model Performance Metrics:
* **R² Score (Variance Explained):** 80.51%
* **Mean Absolute Error (MAE):** 0.3275

### 🛠️ Key Technical Steps Covered:
1. **Data Exploration & Ingestion:** Loaded structured spatial and economic data natively into a Pandas DataFrame.
2. **Train-Test Splitting:** Segmented features and target values into an 80/20 train-test split for robust evaluation.
3. **Model Selection & Training:** Deployed a Random Forest Regressor with 100 decision trees to mitigate variance.
4. **Feature Importance Breakdown:** Computed and plotted a seaborn bar chart to isolate `MedInc` (Median Income) as the top economic driver.
5. **Real-time Inference & Serialization:** Resolved pipeline warnings using dynamic DataFrame conversion and exported the optimal state using `joblib` into a production-ready `.pkl` file.

---
*Developed as part of my Applied Data Science & AI portfolio.*
