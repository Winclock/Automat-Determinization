import pandas as pd

class QSP():
    def __init__(self, name, path:list) -> None:
        self.name = name
        self.path = path

    def __repr__(self):
        return f"{self.name}_"
    
    def get_path(self):
        return list(self.path)
    
    def get_name(self):
        return str(self.name)
    
    def check_epsilon(self):
        for i in self.path:
            if i[1] == "e":
                return self.path.index(i)
            else:
                return None
            
    # не реальзована ситуация с несколькими эпсилон-переходами
    def delete_path(self, index):
        self.path.remove(self.path[index])



class Automat():
    def __init__(self) -> None:
        self.arr = list()
        self.peak = None
        self.conditions = None
        self.res_of_S = []  # двумерный массив где каждый вложенный массив соответствует вершине и состоянию которое туда входит из .name
        self.Tab_of_S = []  # 

        self.add_automat()
        self.fill_arr()
        self.make_set_with_S()
        print(self.res_of_S)
        self.make_tab()
        print(self.Tab_of_S)



    def add_automat(self):
        self.conditions = input("введите состояния автомата >> ").split()
        print("Введенные состояния : ", self.conditions)
        self.peak = input("Введите вершины >> ").split()
        print("Введенные вершины : ", self.peak)

    def fill_arr(self):
        for name in self.peak:
            path = list()
            inp_pathh = input(f"Введите пути из {name} >> ").split(" ")
            for i in inp_pathh:
                path.append(i.split(","))
            self.arr.append(QSP(name, path))
        print("self.arr: ", self.arr)

    #Работает только с проверкой 1 пути
    #возвращает массив с вершинами учитывая эпсилон-переходы
    def forward(self, elem: QSP):
        elem_res = []
        elem_res.append(elem.get_name())  # Засовывает изначальную вершину.
        for path in elem.get_path():
            if path[1] == 'e':
                elem_res.append(path[0]) #Засовывает имя пути куда идет эпсилон.
        return elem_res

    
    def make_set_with_S(self):
        for peak in self.arr:
            self.res_of_S.append(self.forward(peak))


    def forward1(self, elem: QSP, condition: str, flag):
        elem_res = []
        for path in elem.get_path():
            if path[1] == condition:
                flag = False
                elem_res.append(path[0])
            if path[1] == 'e':
                elem_res.append(path[0])

        if flag:  # если нужное состояние не найдено и мы прошли все пути, рекурсивно вызываем forward1 для первого пути в списке
            return self.forward1(QSP(elem.get_path()[0][0], self.arr[self.peak.index(elem.get_path()[0][0])].get_path()), condition, flag=True)
        return elem_res

    
    def make_tab(self):
        for peak in self.arr:
            for condit in self.conditions:
                self.Tab_of_S.append([condit,self.forward1(peak, condit, flag= True)])
        
a1 = Automat()