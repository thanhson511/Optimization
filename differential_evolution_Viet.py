'''
Mục tiêu:

Tìm giá trị nhỏ nhất của hàm số:

f(a, b, c, d) = a * d * (a + b + c) + c^2 - b

Với các ràng buộc:

a * b * c * d >= 25
a^2 + b^2 + c^2 + d^2 <= 40
Giới hạn:

Trong đó các giá trị của a, b, c, và d nằm trong khoảng:

1 <= a, b, c, d <= 5
Về cơ bản, đoạn mã tìm kiếm các giá trị của a, b, c, và d để hàm mục tiêu f(a, b, c, d) đạt giá trị nhỏ nhất 
trong khi vẫn thỏa mãn các ràng buộc đã cho. 
Đoạn mã sử dụng thuật toán differential evolution từ thư viện SciPy để giải quyết bài toán.
'''


import numpy as np
from scipy.optimize import differential_evolution  # Nhập hàm differential_evolution từ SciPy

def objective(x):  # Định nghĩa hàm mục tiêu cần giảm thiểu
    a, b, c, d = x  # phân rã mảng đầu vào x thành các biến riêng lẻ
    return a*d*(a+b+c) + c**2 - b  # Tính toán và trả về giá trị hàm mục tiêu

def constraint1(x):  # Định nghĩa hàm ràng buộc thứ nhất
    return x[0]*x[1]*x[2]*x[3] - 25.0  # Tính toán và trả về giá trị của ràng buộc thứ nhất

def constraint2(x):  # Định nghĩa hàm ràng buộc thứ hai
    return 40 - sum(xi**2 for xi in x)  # Tính toán và trả về giá trị của ràng buộc thứ hai

bounds = [(1.0, 5.0)] * 4  # Xác định giới hạn cho mỗi biến (1.0 <= a, b, c, d <= 5.0)

constraint_1 = {'type': 'ineq', 'fun': constraint1}  # Định nghĩa ràng buộc thứ nhất là ràng buộc bất đẳng thức
constraint_2 = {'type': 'eq', 'fun': constraint2}  # Định nghĩa ràng buộc thứ hai là ràng buộc đẳng thức

constraints = (constraint_1, constraint_2)  # Tạo một tuple các ràng buộc

result = differential_evolution(  # Gọi hàm differential_evolution để thực hiện tối ưu hóa
    func=objective,  # Truyền hàm mục tiêu
    bounds=bounds,  # Truyền giới hạn cho các biến
    strategy='best1bin',  # Chỉ định chiến lược differential evolution
    maxiter=1000,  # Đặt số lần lặp tối đa
    popsize=15,  # Đặt kích thước quần thể
    tol=1e-7,  # Đặt dung sai cho hội tụ
    mutation=(0.5, 1),  # Đặt tỷ lệ đột biến
    recombination=0.7,  # Đặt tỷ lệ tái hợp
    seed=None,  # Đặt hạt giống ngẫu nhiên (None cho không có hạt giống)
    callback=None,  # Đặt hàm gọi lại (None cho không có hàm gọi lại)
    disp=True,  # Cho phép hiển thị tiến trình tối ưu hóa
    polish=True,  # Cho phép tinh chỉnh giải pháp cuối cùng bằng cách sử dụng bộ tối ưu hóa cục bộ
    init='latinhypercube'  # Chỉ định phương pháp khởi tạo cho quần thể
)

print(result)  # In đối tượng kết quả tối ưu hóa
print("Optimal solution:", result.x)  # In giải pháp tối ưu
print("Objective function value:", result.fun)  # In giá trị hàm mục tiêu tại giải pháp tối ưu
print("Success:", result.success)  # In ra cho biết quá trình tối ưu hóa có thành công hay không
print("Message:", result.message)  # In thông báo kết thúc từ bộ tối ưu hóa
print("Number of iterations:", result.nit)  # In số lần lặp được thực hiện
print("Number of function evaluations:", result.nfev)  # In số lần đánh giá hàm