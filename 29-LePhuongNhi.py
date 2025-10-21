student_list = []

def add_student(ho_ten, nam_sinh, dia_chi):
    student = {
        "ho_ten": ho_ten,
        "nam_sinh": nam_sinh,
        "dia_chi": dia_chi
    }
    student_list.append(student)
    print(f"Da them sinh vien {ho_ten} thanh cong.")
def _get(sv, k1, k2):
    return sv.get(k1) if isinstance(sv, dict) else None or sv.get(k2)

def print_student_list():
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
        return

    for sv in student_list:
        ten = sv.get("ho_ten")
        ns  = sv.get("nam_sinh")
        dc  = sv.get("dia_chi")
        print(f" - Ten: {ten}, Nam sinh: {ns}, Dia chi: {dc}")
