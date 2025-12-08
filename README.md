# Data Cleaning and Preprocessing with Scikit-learn

A growing collection of Python scripts demonstrating essential data cleaning and preprocessing techniques using scikit-learn. This repository is actively being developed with new examples and techniques.

## 📋 Table of Contents

- [Overview](#overview)
- [Current Files](#current-files)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Topics Covered](#topics-covered)
- [Usage Examples](#usage-examples)
- [Datasets](#datasets)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

## 🎯 Overview

Data cleaning and preprocessing are critical steps in any machine learning pipeline. This repository provides practical, hands-on examples of handling common data quality issues and preparing datasets for model training using scikit-learn's preprocessing utilities.

> **Note:** This repository is under active development. More preprocessing techniques and examples will be added regularly.

## 📁 Current Files

### Python Scripts (So Far)

1. **1.simple_impute.py**
   - Handling missing values using SimpleImputer
   - Different imputation strategies (mean, median, most_frequent, constant)

2. **2.onehotcoding_and_dummyvariable.py**
   - One-hot encoding for categorical variables
   - Difference between one-hot encoding and dummy variables

3. **3.Label_encoding.py**
   - Label encoding for categorical variables
   - When to use label encoding vs one-hot encoding

4. **4.Ordinal_encoding.py**
   - Ordinal encoding for ordered categorical variables
   - Preserving natural order of categories

5. **5.removing_outlier_with_IQR.py**
   - Outlier detection using Interquartile Range (IQR)
   - Identifying and removing outliers from datasets

6. **6.Feature_scaling_Standarization.py**
   - Feature scaling using StandardScaler
   - Standardization (z-score normalization)

### Data Files

- **Bankloan.csv** - Banking dataset for demonstrations
- **loan.csv** - Loan data for practical examples

## 🔧 Prerequisites

```
Python 3.7+
pandas
numpy
scikit-learn
matplotlib (optional, for visualization)
```

## 💻 Installation

1. Clone this repository:
```bash
git clone https://github.com/iankitsubedi/scikit-learn-learning.git
cd scikit-learn-learning/data\ cleaning\ and\ preprocessing
```

2. Install required packages:
```bash
pip install pandas numpy scikit-learn matplotlib
```

3. Run any script:
```bash
python 1.simple_impute.py
```

## 📚 Topics Covered

### Currently Implemented:

- ✅ Handling Missing Values (SimpleImputer)
- ✅ Categorical Encoding (One-Hot, Label, Ordinal)
- ✅ Outlier Detection & Removal (IQR method)
- ✅ Feature Scaling (Standardization)

### Coming Soon:

- 🔄 More feature scaling techniques (Normalization, MinMaxScaler, RobustScaler)
- 🔄 Advanced imputation methods
- 🔄 Feature engineering techniques
- 🔄 Additional outlier detection methods
- 🔄 Data transformation techniques
- 🔄 More real-world datasets

## 🚀 Usage Examples

### Handling Missing Values

```python
from sklearn.impute import SimpleImputer
import pandas as pd

df = pd.read_csv('Bankloan.csv')
imputer = SimpleImputer(strategy='mean')
df_imputed = imputer.fit_transform(df[['Age', 'Income']])
```

### One-Hot Encoding

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse=False, drop='first')
encoded_features = encoder.fit_transform(df[['Category']])
```

### Feature Scaling

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['Age', 'Income']])
```

## 📊 Datasets

**Bankloan.csv** - Banking customer data with features like Age, Income, Education Level, Loan Status, Credit Score

**loan.csv** - Loan application data with various features for preprocessing demonstrations

*More datasets will be added as the repository grows.*

## 🗺️ Roadmap

This repository is actively expanding. Here's what's planned:

- [ ] Add normalization techniques (MinMaxScaler, RobustScaler)
- [ ] Implement advanced imputation (KNN, Iterative)
- [ ] Add feature engineering examples
- [ ] Include text preprocessing techniques
- [ ] Add time series preprocessing
- [ ] Create comprehensive Jupyter notebooks
- [ ] Add visualization examples for each technique
- [ ] Include pipeline examples combining multiple techniques

## 💡 Key Concepts

**Simple Imputation** - For handling missing values based on strategy (mean, median, mode)

**One-Hot Encoding** - For nominal categorical variables with no inherent order

**Label Encoding** - For binary variables or creating target variables

**Ordinal Encoding** - For ordered categorical variables (low, medium, high)

**Outlier Removal** - Using IQR method for robust outlier detection

**Feature Scaling** - Essential for distance-based algorithms (KNN, SVM, Neural Networks)

## 🤝 Contributing

Contributions and suggestions are welcome! This is a learning repository, so feel free to:

- Add new preprocessing techniques
- Improve existing examples
- Add more datasets
- Suggest new topics to cover
- Report issues or bugs

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-technique`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new technique'`)
5. Push to the branch (`git push origin feature/new-technique`)
6. Create a Pull Request

## 📝 Best Practices

1. Always split your data before preprocessing to avoid data leakage
2. Fit transformers on training data only, then apply to test data
3. Save your preprocessing objects (scalers, encoders) for production use
4. Document your preprocessing choices for reproducibility

## 🔍 Additional Resources

- [Scikit-learn Preprocessing Documentation](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

**Status:** 🚧 Active Development | Last Updated: December 2025

This is an educational repository that's continuously evolving. Check back regularly for new content!
