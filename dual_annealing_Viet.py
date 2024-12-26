import numpy as np  # Nhập thư viện NumPy cho các phép toán số học, đặc biệt là hàm sin
from scipy.optimize import dual_annealing  # Nhập hàm dual_annealing từ SciPy để tối ưu hóa

def objective(x):  # Định nghĩa hàm mục tiêu cần giảm thiểu
    a, b, c, d = x  # Giải nén mảng đầu vào x thành các biến riêng lẻ a, b, c, và d
    return a*d*(a+b+c) + c**2 - b*d + np.sin(a*b)  # Tính toán và trả về giá trị hàm mục tiêu

def constraint1(x):  # Định nghĩa hàm ràng buộc thứ nhất
    return x[0]*x[1]*x[2]*x[3] - 25.0  # Tính toán và trả về giá trị của ràng buộc thứ nhất (a*b*c*d >= 25)

def constraint2(x):  # Định nghĩa hàm ràng buộc thứ hai
    return 40 - sum(xi**2 for xi in x)  # Tính toán và trả về giá trị của ràng buộc thứ hai (a^2 + b^2 + c^2 + d^2 = 40)

bounds = [(1.0, 5.0)] * 4  # Xác định giới hạn cho mỗi biến (1.0 <= a, b, c, d <= 5.0)

def combined_constraints(x):  # Định nghĩa hàm để kết hợp cả hai ràng buộc
    return [constraint1(x), abs(constraint2(x))]  # Trả về một danh sách chứa giá trị của cả hai ràng buộc, với giá trị tuyệt đối của ràng buộc thứ hai được lấy để đảm bảo nó được coi là một bất đẳng thức

result = dual_annealing(  # Gọi hàm dual_annealing để thực hiện tối ưu hóa
    func=objective,  # Truyền hàm mục tiêu cần giảm thiểu
    bounds=bounds,  # Truyền giới hạn cho các biến
    x0=None,  # Điểm bắt đầu cho tối ưu hóa (None có nghĩa là điểm bắt đầu ngẫu nhiên)
    maxiter=1000,  # Đặt số lần lặp tối đa
    initial_temp=5230.0,  # Đặt nhiệt độ ban đầu cho quá trình ủ
    restart_temp_ratio=2e-5,  # Đặt tỷ lệ để khởi động lại quá trình ủ nếu nó bị kẹt
    visit=2.62,  # Tham số điều khiển để truy cập các vùng khác nhau của không gian tìm kiếm
    accept=-5.0,  # Tham số điều khiển để chấp nhận các giải pháp mới
    maxfun=10000000.0,  # Đặt số lần đánh giá hàm tối đa
    seed=None,  # Đặt hạt giống ngẫu nhiên (None cho không có hạt giống)
    no_local_search=False,  # Kích hoạt tìm kiếm cục bộ để tinh chỉnh giải pháp
    callback=None,  # Đặt hàm gọi lại (None cho không có hàm gọi lại)
    minimizer_kwargs={'method': 'COBYLA', 'constraints': {'type': 'ineq', 'fun': combined_constraints}}  # Sử dụng phương pháp COBYLA cho tìm kiếm cục bộ với các ràng buộc kết hợp là ràng buộc bất đẳng thức
)

print(result)  # In đối tượng kết quả tối ưu hóa
print("Optimal solution:", result.x)  # In giải pháp tối ưu được tìm thấy
print("Objective function value:", result.fun)  # In giá trị hàm mục tiêu tại giải pháp tối ưu
print("Success:", result.success)  # In ra cho biết quá trình tối ưu hóa có thành công hay không
print("Message:", result.message)  # In thông báo kết thúc từ bộ tối ưu hóa
print("Number of function evaluations:", result.nfev)  # In số lần hàm mục tiêu được đánh giá
print("Number of iterations:", result.nit)  # In số lần lặp được thực hiện