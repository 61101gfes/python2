from student import Student
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    
class History:
    def __init__(self):
        self.action=None
        self.link=None
class Back:
    def __init__(self):
        self.node=None
    def pop(self):
        if self.node:
            temp=self.node
            self.node=self.node.link
            return temp.action
        return None
    def push(self,acting):
        temp=History()
        temp.action=acting
        if self.node:
            temp.link=self.node
            self.node=temp
            print('加入已存在歷史紀錄',self.node.action)
        else:
            self.node=temp
        print('加入歷史紀錄',self.node.action)

    def is_empty(self):
        if not self.node:
            print('No history')
            return True
        return False
        
class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if self.items.is_empty():
            return None
        else:
            return self.items.pop(0)
    def is_empty(self):
        return len(self.items)==0
class AVLNode:
    def __init__(self,student):
        self.student=student
        self.height=1
        self.left=None
        self.right=None
class AVLTree:
    def __init__(self):
        self.root=None
    def get_height(self,node):
        return node.height if node else 0
    def balance_factor(self,node):
        return self.get_height(node.left)-self.get_height(node.right) if node else 0
    def ll_rotate(self,node):
        next=node.left
        pivot=next.right
        
        next.right=node
        node.left=pivot
        node.height=1+max(self.get_height(node.left),self.get_height(node.right))
        next.height=1+max(self.get_height(next.left),self.get_height(next.right))
        return next
    def rr_rotate(self,node):
        next=node.right
        pivot=next.left
        
        next.left=node
        node.right=pivot
        node.height=1+max(self.get_height(node.left),self.get_height(node.right))
        next.height=1+max(self.get_height(next.left),self.get_height(next.right))
        return next
    def _insert(self,node,student):
        if not node:
            return AVLNode(student)
        
        if (student.grade<node.student.grade) or (student.grade==node.student.grade and student.name<node.student.name):
            node.left=self._insert(node.left,student)
        elif (student.grade>node.student.grade) or (student.grade==node.student.grade and student.name>node.student.name):
            node.right=self._insert(node.right,student)
        
        node.height=1+max(self.get_height(node.left),self.get_height(node.right))
        balance=self.balance_factor(node)
        if balance>1:
            if self.balance_factor(node.left)<0:
                node.left=self.rr_rotate(node.left)
                return self.ll_rotate(node)
            else:
                return self.ll_rotate(node)
        if balance<-1:
            if self.balance_factor(node.right)>0:
                node.right=self.ll_rotate(node.right)
                return self.rr_rotate(node)
            else:
                return self.rr_rotate(node)
        return node
    def insert(self,student):
        self.root=self._insert(self.root,student)
    
    def _inorder(self,node):
        if node:
            return self._inorder(node.left)+[node.student]+self._inorder(node.right)
        return []
    def inorder(self):
        return self._inorder(self.root)
    def find_min(self,node):
        if not node.left:
            return node
        return self.find_min(node.left)  
    def _delete(self,node,student):
        #print('Current:',node.student,student)
        if not node:
            return 
        if (student.grade<node.student.grade) or (student.grade==node.student.grade and student.name<node.student.name):
            node.left=self._delete(node.left,student)
        elif (student.grade>node.student.grade) or (student.grade==node.student.grade and student.name>node.student.name):
            node.right=self._delete(node.right,student)
        else:
            if node.left==None:
                return node.right
            elif node.right==None:
                return node.left
            else:
                min_point=self.find_min(node.right)
                #print('Find:',node.student)
                node.student=min_point.student
                node.right=self._delete(node.right,min_point.student)
                
        node.height=1+max(self.get_height(node.left),self.get_height(node.right))
        balance=self.balance_factor(node)
        if balance>1:
            if self.balance_factor(node.left)<0:
                node.left=self.rr_rotate(node.left)
                return self.ll_rotate(node)
            else:
                return self.ll_rotate(node)
        if balance<-1:
            if self.balance_factor(node.right)>0:
                node.right=self.ll_rotate(node.right)
                return self.rr_rotate(node)
            else:
                return self.rr_rotate(node)
        return node
    def delete(self,student):
        self.root=self._delete(self.root,student)
        
    def _get_student(self,node,name):
        if not node:
            return None
        if name==node.student.name:
            return node.student
        left=self._get_student(node.left,name)
        if left:
            return left
        if node.right:
            return self._get_student(node.right,name)
        
    def get_student(self,name):
        return self._get_student(self.root,name)
    
    def preorder(self,root,i=0):
        i+=1
        if root:
            print(root.student,self.get_height(root))
            self.preorder(root.left,i)
            self.preorder(root.right,i)
list=[Student('a',60),Student('b',50),Student('d',90),Student('e',65),Student('c',87),Student('q',68)] 
avl=AVLTree()
for l in list:
    #avlnode=AVLNode(l)       
    #print(avlnode.student)
    avl.insert(l)
name=['a','b','d','c','q','e']
for n in name:
    point=avl.get_student(n)
    avl.delete(point)
avl.preorder(avl.root)
#print(point.grade)
#print(point)a,60;b,50;d,90;e,65;c,87;q,68
