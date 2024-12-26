'''
Cực đại hàm:

Z = 3x + 2y

với các ràng buộc:

x + 2y <= 4
3x + y <= 5
x >= 0
y >= 0
''' 

import numpy as np
from scipy.optimize import minimize

# Hàm mục tiêu
def objective(x):
    """
    Tính giá trị của hàm mục tiêu cần tối thiểu hóa.

    Args:
      x: Một danh sách hoặc mảng chứa các giá trị của các biến quyết định (x, y).

    Returns:
      Giá trị của hàm mục tiêu.
    """
    return -3*x[0] - 2*x[1]  # -3x - 2y

# Các ràng buộc
constraints = [
    {'type': 'ineq', 'fun': lambda x:  4 - (x[0] + 2*x[1])},  # x + 2y <= 4
    {'type': 'ineq', 'fun': lambda x:  5 - (3*x[0] + x[1])},  # 3x + y <= 5
    {'type': 'ineq', 'fun': lambda x:  x[0]},                # x >= 0
    {'type': 'ineq', 'fun': lambda x:  x[1]}                 # y >= 0
]
# Mỗi ràng buộc là một từ điển với các khóa 'type' và 'fun'.
# 'type': 'ineq' cho biết ràng buộc bất đẳng thức.
# 'fun': Một hàm lambda xác định ràng buộc. Nó sẽ trả về một giá trị không âm nếu ràng buộc được thỏa mãn.

# Giá trị ban đầu
x0 = [0, 0]  # Điểm bắt đầu cho thuật toán tối ưu hóa

# Giải quyết bài toán
result = minimize(objective, x0, constraints=constraints, bounds=[(0, None), (0, None)])
# minimize: Hàm từ scipy.optimize để tìm giá trị tối thiểu của hàm mục tiêu.
# objective: Hàm mục tiêu cần tối thiểu hóa.
# x0: Giá trị ban đầu.
# constraints: Danh sách các ràng buộc.
# bounds: Xác định giới hạn cho mỗi biến quyết định. (0, None) có nghĩa là biến phải lớn hơn hoặc bằng 0.

# In kết quả
if result.success:
    print(f"Giá trị tối ưu (Z): {-result.fun}")  # In giá trị tối ưu của hàm mục tiêu (đảo dấu vì chúng ta đang tối đa hóa)
    print(f"Nghiệm tối ưu: x = {result.x[0]}, y = {result.x[1]}")  # In các giá trị tối ưu của x và y
else:
    print("Không tìm thấy nghiệm")  # In thông báo nếu không tìm thấy nghiệm