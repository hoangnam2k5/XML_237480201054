import xml.etree.ElementTree as ET

def sua_sinhvien(file_path, ma_sv, ten_moi, lop_moi, diem_moi):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    for sv in root.findall('sinhvien'):
        if sv.find('masv').text == ma_sv:
            sv.find('hoten').text = ten_moi
            sv.find('lop').text = lop_moi
            sv.find('diem').text = str(diem_moi)
            
            tree.write(file_path, encoding='utf-8', xml_declaration=True)
            print("Đã cập nhật thành công!")
            return
            
    print(f"Không tìm thấy mã: {ma_sv}")

if __name__ == "__main__":
    file_path = "Sinhvien.xml"
    ma_sv = input("Mã SV cần sửa: ")
    ten_moi = input("Tên mới: ")
    lop_moi = input("Lớp mới: ")
    diem_moi = input("Điểm mới: ")
    
    sua_sinhvien(file_path, ma_sv, ten_moi, lop_moi, diem_moi)