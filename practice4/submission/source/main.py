import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv("bfi.csv")
# Loại bỏ các cột không cần thiết
df.drop(['gender', 'education', 'age'], axis=1, inplace=True)
# Loại bỏ các dòng có giá trị thiếu
df.dropna(inplace=True)

# 1. Đánh giá khả năng phân tích nhân tố
chi_square_value, p_value = calculate_bartlett_sphericity(df)
print(
    f"Kiểm định Bartlett: chi_square = {chi_square_value:.4f}, p_value = {p_value:.4f}")

kmo_all, kmo_model = calculate_kmo(df)
print(f"Kiểm định KMO: KMO Model = {kmo_model:.4f}")

# 2. Xác định số lượng nhân tố tối ưu
fa_explore = FactorAnalyzer(rotation=None, n_factors=min(25, df.shape[1]))
fa_explore.fit(df)

# Lấy eigenvalues
ev, v = fa_explore.get_eigenvalues()
print("\nEigenvalues:")
for i, value in enumerate(ev, 1):
    print(f"Nhân tố {i}: {value:.4f}")

# Vẽ biểu đồ Scree Plot
plt.figure(figsize=(10, 6))
plt.scatter(range(1, len(ev)+1), ev)
plt.plot(range(1, len(ev)+1), ev)
plt.axhline(y=1, color='r', linestyle='--')
plt.title('Biểu đồ Scree Plot')
plt.xlabel('Số lượng nhân tố')
plt.ylabel('Giá trị riêng (Eigenvalue)')
plt.grid()
plt.savefig('scree_plot.png')
plt.show()

# 3. Thực hiện phân tích nhân tố với số lượng nhân tố tối ưu (dựa vào eigenvalues > 1)
n_factors = sum(ev > 1)
print(f"\nSố lượng nhân tố có eigenvalue > 1: {n_factors}")

fa = FactorAnalyzer(n_factors=n_factors, rotation="varimax")
fa.fit(df)

# 4. Hiển thị và phân tích kết quả
# Lấy hệ số tải
loadings = fa.loadings_
# Tạo DataFrame để hiển thị hệ số tải
loadings_df = pd.DataFrame(loadings, index=df.columns)
loadings_df.columns = [f'Nhân tố {i+1}' for i in range(n_factors)]

# Chỉ hiển thị hệ số tải có giá trị tuyệt đối >= 0.4


def highlight_loadings(val):
    if abs(val) >= 0.4:
        return f"{val:.4f}"
    return ""


pd.set_option('display.max_rows', None)
print("\nBảng hệ số tải (Loadings):")
print(loadings_df.applymap(highlight_loadings))

# Lấy phương sai của mỗi nhân tố
variance = fa.get_factor_variance()
var_df = pd.DataFrame(variance,
                      index=['SS Loadings', 'Proportion Var', 'Cumulative Var'],
                      columns=[f'Nhân tố {i+1}' for i in range(n_factors)])
print("\nBảng phương sai nhân tố:")
print(var_df)

# 5. Trực quan hóa hệ số tải bằng heatmap
plt.figure(figsize=(12, 10))
mask = np.abs(loadings) < 0.4  # Ẩn các giá trị dưới 0.4
sns.heatmap(loadings_df, annot=True, cmap='coolwarm',
            mask=mask, fmt=".2f", linewidths=.5)
plt.title('Bản đồ nhiệt hệ số tải (Chỉ hiển thị giá trị >= 0.4)')
plt.tight_layout()
plt.savefig('factor_loadings_heatmap.png')
plt.show()

# 6. Lưu kết quả vào file
result = pd.concat([loadings_df, var_df.T], axis=0)
result.to_csv('factor_analysis_results.csv')
