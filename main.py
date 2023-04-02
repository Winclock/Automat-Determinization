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
        self.res_of_S = []  # двумерный массив где каждый вложенный массив соответствует множеству вершины с эпсилон-переходами соответствующей вершины
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

    #Работает только с проверкой 1 путя
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


    def forward1(self, elem: str, condition: str, flag):
        elem_res = []                       # Можно сделать содержимое классом QSP чтобы удобно хранить и состояние и путь. !!! НЕ РЕАЛИЗОВАННО !!!
        for path in elem.get_path() :
            if path[1] == 'e':
                elem_res.append(path[0])    #Засовывает имя пути если туда идет епсилон.
            if path[1] == condition:
                flag = False                #Меняем флаг на False т.к. нужное состояние можно встретить только 1 раз.
                elem_res.append(path[0])    #Засовывает имя пути если туда идет нужное состояние.
            if flag == False:
                return elem_res             #Если flag == False значит мы прошли все возможные эпсилоны и нужное состояние.
        return elem_res                     #Возвращаем пустой список если никакое условие не сработало
    
    def make_tab(self):
        for peak in self.arr:
            for condit in self.conditions:
                self.Tab_of_S.append([condit,self.forward1(peak, condit, flag= True)])
        
a1 = Automat()