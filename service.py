from student import Student
from data_structure import Stack,Queue,AVLTree,AVLNode
import os

DATA_FILE='student.txt'

class StudentService:
    def __init__(self):
        self.student_list=[]
        self.tree=AVLTree()
        self.queue=Queue()
        self.history=Stack()
        self.hst=Back()
        
    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE,'r') as file:
            for line in file:
                name,grade=line.strip().split(',')
                grade=int(grade)
                student=Student(name,grade)
                self.student_list.append(student)
                self.tree.insert(student)
        print('資料載入完畢')
    def save_data(self):
        with open(DATA_FILE,'w') as file:
            for student in self.student_list:
                file.write(f"{student.name},{student.grade}\n")
        print('資料保存完畢')
    
    def add_student(self,name,grade):
        for student in self.student_list:
            if student.name==name:
                print(f'此學生{name}已存在!')
                return 
        student=Student(name,grade)
        self.student_list.append(student)
        self.tree.insert(student)
        self.history.push(('add',student))
        self.hst.push(('add',student))
        print(f"已新增學生：{student}")
        
    def update_student(self,name,grade):
        student=self.tree.get_student(name)
        if not student:
            print("學生不存在！")
            return
        old_grade=student.grade
        self.tree.delete(student)
        student.grade=grade
        self.tree.insert(student)
        self.history.push(('update',student,old_grade))
        self.hst.push(('update',student,old_grade))
        print(f"已更新學生 {name} 的成績為 {grade}") 
        
    def delete_student(self,name):
        for student in self.student_list:
            if student.name==name:
                self.student_list.remove(student)
                self.tree.delete(student)
                self.history.push(('delete',student))
                self.hst.push(('delete',student))
                print(f"已刪除學生：{student}")
                return
        print("學生不存在！")
    
    def get_studentscore(self,name):
        student=self.tree.get_student(name)
        if student:
            print(f'學生{student}')
        else:
            print("學生不存在！")
            
    def display_student(self):
        print("所有學生（按成績排序）:")
        for student in self.tree.inorder():
            print(student)
        
    def undo(self):
        if self.history.is_empty():
            print("無操作可復原！")
            return 
        last_action=self.history.pop()
        if last_action[0]=='add':
            student=last_action[1]
            self.student_list.remove(student)
            self.tree.delete(student)
            print(f"已復原新增操作：刪除學生 {student}")
        elif last_action[0]=='update':
            student=last_action[1]
            old_grade=last_action[2]
            self.tree.delete(student)
            student.grade=old_grade
            self.tree.insert(student)
            print(f"已復原更新操作：恢復學生 {student.name} 的成績為 {old_grade}")
        elif last_action[0]=='delete':
            student=last_action[1]
            self.student_list.append(student)
            self.tree.insert(student)
            print(f"已復原刪除操作：恢復學生 {student}")
            
    def batch_add(self,batch_data):
        datas=batch_data.split(';')
        for data in datas:
            try:
                name,grade=data.split(',')
                grade=int(grade)
                if 0<=grade<=100:
                    self.queue.enqueue(Student(name.strip(),grade))
                else:
                    print(f"成績 {grade} 超出範圍，略過 {name.strip()}！")
            except ValueError:
                print(f"格式錯誤，略過資料：{data}")
        while not self.queue.is_empty():
            student=self.queue.dequeue()
            self.add_student(student.name,student.grade)

    def backdo(self):
        if self.hst.is_empty():
            print("無操作可復原！")
            return 
        last_action=self.hst.pop()
        if last_action[0]=='add':
            student=last_action[1]
            self.student_list.remove(student)
            self.tree.delete(student)
            print(f"已復原新增操作：刪除學生 {student}")
        elif last_action[0]=='update':
            student=last_action[1]
            old_grade=last_action[2]
            self.tree.delete(student)
            student.grade=old_grade
            self.tree.insert(student)
            print(f"已復原更新操作：恢復學生 {student.name} 的成績為 {old_grade}")
        elif last_action[0]=='delete':
            student=last_action[1]
            self.student_list.append(student)
            self.tree.insert(student)
            print(f"已復原刪除操作：恢復學生 {student}")
            
