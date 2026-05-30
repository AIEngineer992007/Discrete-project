# Giải Quyết Bài Toán Người Đi Giao Hàng (TSP) với Dữ Liệu `kroB100.tsp`

Kho lưu trữ này chứa các thuật toán tối ưu hóa bằng Python nhằm giải quyết bài toán **Traveling Salesperson Problem (TSP)** sử dụng tập dữ liệu mẫu chuẩn TSPLIB mang tên `kroB100.tsp` (gồm 100 thành phố). 

Dự án triển khai và so sánh 3 phương pháp tiếp cận khác nhau từ cơ bản đến nâng cao: thuật toán tham lam (Greedy), tìm kiếm cục bộ (2-Opt Local Search), và tối ưu hóa bầy đàn (Ant Colony Optimization).

## 📌 Các Thuật Toán Triển Khai

### 1. Thuật toán Tham lam (Greedy / Nearest Neighbor)
* **File:** `TSP Solve_Greedy_alg.py`
* **Cách hoạt động:** Xuất phát từ thành phố số `0`, thuật toán luôn chọn đi đến thành phố gần nhất chưa được ghé thăm trong mỗi bước cho đến khi đi qua hết tất cả các điểm, cuối cùng quay trở lại điểm xuất phát.
* **Đặc điểm:** Tốc độ thực thi cực nhanh nhưng dễ bị rơi vào bẫy tối ưu cục bộ và cho ra kết quả chưa phải tốt nhất.

### 2. Tìm kiếm Cục bộ 2-Opt (Local Search)
* **File:** `TSP Solve_Local_search_alg_otp_2.py`
* **Cách hoạt động:** Lấy hành trình của thuật toán Greedy làm lời giải ban đầu. Sau đó, thuật toán liên tục duyệt qua các cặp cạnh $(A, B)$ và $(C, D)$ để kiểm tra xem việc cắt và hoán đổi thành $(A, C)$ và $(B, D)$ có làm giảm tổng chiều dài quãng đường hay không. Quá trình lặp lại cho đến khi không tìm thấy cải tiến nào thêm.
* **Đặc điểm:** Cải thiện đáng kể chất lượng hành trình của Greedy với chi phí thời gian thêm vào rất ít.

### 3. Tối ưu hóa Thuật toán Đàn kiến (Ant Colony Optimization - ACO)
* **File:** `ACO.py`
* **Cách hoạt động:** Thuật toán phỏng sinh học dựa trên hành vi tìm đường của đàn kiến. Tập hợp các con kiến ảo di chuyển qua các thành phố dựa trên xác suất kết hợp giữa **vết mùi (Pheromone)** và **khoảng cách vật lý (Heuristic)**. Sau mỗi thế hệ, vết mùi trên các tuyến đường ngắn sẽ được tăng cường, trong khi các tuyến đường dài sẽ bị bay hơi dần.
* **Đặc điểm:** Thuật toán metaheuristic mạnh mẽ, có khả năng tìm ra lời giải tiệm cận tối ưu toàn cục rất tốt cho các bài toán phức tạp.

---

## 🛠️ Yêu cầu Hệ thống & Cấu hình

Dự án chỉ sử dụng các thư viện chuẩn (built-in) của Python nên bạn không cần cài đặt thêm các thư viện bên ngoài.

* **Ngôn ngữ:** Python 3.x
* **Thư viện sử dụng:** `math`, `time`, `random`
* **Dữ liệu đầu vào:** File `kroB100.tsp` đặt cùng cấp thư mục với các file mã nguồn.

---

## 🚀 Hướng dẫn Chạy Chương trình

Đảm bảo bạn đã tải file dữ liệu `kroB100.tsp` về máy, sau đó mở Terminal/Command Prompt tại thư mục dự án và chạy các lệnh sau:

### Chạy thuật toán Tham lam (Greedy):
```bash
python "TSP Solve_Greedy_alg.py"