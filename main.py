from service import StudentService
import sys
def main():
    service=StudentService()
    service.load_data()
    
    while True:
        print("\n--- 學生成績管理系統 ---")
        print("1. 新增學生")
        print("2. 更新學生成績")
        print("3. 刪除學生")
        print("4. 查詢學生成績")
        print("5. 顯示所有學生")
        print("6. 復原上一步操作")
        print("7. 批次輸入學生資料")
        print("0. 離開系統")
        choice = input("請輸入操作選項：").strip()
        
        if choice=='1':
            name = input("輸入學生姓名：").strip()
            if not name:
                print("姓名不能為空！")
                continue
            try:
                grade = int(input("輸入學生成績（0-100）：").strip())
                if 0 <= grade <= 100:
                    service.add_student(name, grade)
                else:
                    print("成績範圍應在 0 到 100 之間！")
            except ValueError:
                print("成績必須是數字！")
        elif choice == "2":
            name = input("輸入學生姓名：").strip()
            if not name:
                print("姓名不能為空！")
                continue
            try:
                grade = int(input("輸入更新後的成績（0-100）：").strip())
                if 0 <= grade <= 100:
                    service.update_student(name, grade)
                else:
                    print("成績範圍應在 0 到 100 之間！")
            except ValueError:
                print("成績必須是數字！")
        elif choice == "3":
            name = input("輸入學生姓名：").strip()
            if not name:
                print("姓名不能為空！")
                continue
            service.delete_student(name)
        elif choice == "4":
            name = input("輸入學生姓名：").strip()
            if not name:
                print("姓名不能為空！")
                continue
            service.get_studentscore(name)    
        elif choice == "5":
            service.display_student()
        elif choice == "6":
            service.undo()
        elif choice == "7":
            batch = input("輸入批次資料（格式：姓名1,成績1;姓名2,成績2）：").strip()
            if batch:
                service.batch_add(batch)
            else:
                print("批次資料不能為空！")
        elif choice == "0":
            service.save_data()  # 退出前保存資料
            print("系統已退出。")
            sys.exit(1)
            break
        else:
            print("無效的選項，請重新輸入！")
main()