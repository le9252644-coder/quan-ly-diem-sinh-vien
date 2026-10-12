import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 1. Tạo dữ liệu 10 sinh viên
data = {
    "Ho_ten": [
        "An", "Binh", "Chi", "Dung", "Ha",
        "Hung", "Lan", "Minh", "Nam", "Vy"
    ],
    "Chuyen_can": [8, 9, 7, 6, 10, 8, 7, 9, 5, 8],
    "Giua_ky": [7, 8, 6, 7, 9, 8, 6, 7, 5, 9],
    "Cuoi_ky": [9, 8, 7, 5, 9, 7, 8, 9, 4, 8]
}

df = pd.DataFrame(data)

# 2. Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

# 3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 4. Hiển thị bảng điểm
st.subheader("Bảng điểm sinh viên")

bang = df.rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(bang, use_container_width=True)

# 5. Thống kê kết quả
diem_tb = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

st.subheader("Thống kê kết quả")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Điểm trung bình", f"{diem_tb:.2f}")
c2.metric("Số sinh viên đạt", so_sv_dat)
c3.metric("Điểm cao nhất", f"{sv_max['Tong_ket']:.2f}")
c4.metric("Điểm thấp nhất", f"{sv_min['Tong_ket']:.2f}")

st.write("Sinh viên điểm cao nhất:", sv_max["Ho_ten"])
st.write("Sinh viên điểm thấp nhất:", sv_min["Ho_ten"])

# 6. Tra cứu sinh viên
st.subheader("Tra cứu điểm sinh viên")

ten_sv = st.selectbox("Chọn sinh viên", df["Ho_ten"].tolist())
sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write("Họ tên:", sv["Ho_ten"])
st.write("Điểm chuyên cần:", sv["Chuyen_can"])
st.write("Điểm giữa kỳ:", sv["Giua_ky"])
st.write("Điểm cuối kỳ:", sv["Cuoi_ky"])
st.write("Điểm tổng kết:", round(sv["Tong_ket"], 2))
st.write("Xếp loại:", sv["Xep_loai"])

# 7. Vẽ biểu đồ
st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)

st.pyplot(fig)
plt.close(fig)

# 8. Thông tin người tạo
st.caption("Người tạo: Le Van Tan  | MSSV: 038208022568")
