# Import required libraries
import pandas as pd
from sklearn.datasets import load_iris
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
import matplotlib.pyplot as plt

df = pd.read_csv("bfi.csv")
df.columns
# Index(['A1', 'A2', 'A3', 'A4', 'A5', 'C1', 'C2', 'C3', 'C4', 'C5', 'E1', 'E2','E3', 'E4', 'E5', 'N1', 'N2', 'N3', 'N4', 'N5', 'O1', 'O2', 'O3', 'O4','O5', 'gender', 'education', 'age'], dtype = 'object')

# Dropping unnecessary columns
df.drop(['gender', 'education', 'age'], axis=1, inplace=True)
# Dropping missing values rows
df.dropna(inplace=True)

# Evaluate factorability
chi_square_value, p_value = calculate_bartlett_sphericity(df)
print(
    f"Bartlett’s Test: chi_square_value = {chi_square_value}, p_value = {p_value}"
)

kmo_all, kmo_model = calculate_kmo(df)
print(f"Kaiser-Meyer-Olkin Test: KMO Model = {kmo_model}")

# Creating factor analysis object and perform factor analysis
# fa = FactorAnalyzer(n_factors=6, rotation=None)

# request1:Choosing the Number of Factors

# Create factor analysis object and perform factor analysis
# Initialize with maximum possible factors (25 in this case)
fa = FactorAnalyzer(rotation=None, n_factors=25)
fa.fit(df)

# Check Eigenvalues
ev, v = fa.get_eigenvalues()
ev

# You can create scree plot using matplotlib
plt.scatter(range(1, df.shape[1]+1), ev)
plt.plot(range(1, df.shape[1]+1), ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

# request2:Performing Factor Analysis
# Create factor analysis object and perform factor analysis
# Thực hiện Phân tích nhân tố
fa = FactorAnalyzer(n_factors=6, rotation="varimax")
fa.fit(df)
fa.loadings_
# Lấy phương sai của mỗi nhân tố
fa.get_factor_variance()
