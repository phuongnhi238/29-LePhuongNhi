student_list = []

def add_student(ho_ten, nam_sinh, dia_chi):
    student = {
        "ho_ten": ho_ten,
        "nam_sinh": nam_sinh,
        "dia_chi": dia_chi
    }
    student_list.append(student)
    print(f"Da them sinh vien {ho_ten} thanh cong.")
