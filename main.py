import pandas as pd

class QSP():
    def __init__(self, name, path:list) -> None:
        self.name = name
        self.path = path

    def __repr__(self):
        return f"{self.name}_"
    
    def get_path(self):
        return self.path
    
    def get_name(self):
        return self.name


class Automat():
    def __init__(self) -> None:
        self.arr = list()
        self.peak = None
        self.conditions = None

        self.add_automat()
        self.fill_automat()
#        self.arr = [[0 for j in range(self.conditions)] for i in range(self.indexes)]
        self.check_ALL_epsilon()
 
    def add_automat(self):
        self.conditions = input("введите состояния автомата >> ").split()
        self.peak = input("Введите вершины >> ").split()

        print(self.conditions)

    def fill_automat(self):
        for name in self.peak:
            path = list()
            inp_pathh = input(f"Введите пути из {name} >> ").split(" ")
            for i in inp_pathh:
                path.append(i.split(","))
            self.arr.append(QSP(name, path))
        print("VSE VERSHINI S PUTYAMI", self.arr)


    def check(self, conv:QSP, condition, flag):
        res = []
        for inconv in conv.path:
            print(" func: check , var: inconv ", inconv)
            if (inconv[1] == condition and flag) or inconv[1] == 'e':
                res.append(inconv[0])
                #self.recheck(res,condition)
        return res
            

    def check_epsilon(self, condition: str, flag:bool):
        peak_to_add = list()
        for conv in self.arr:
            # добавляем вершину и соответствующие ей результаты проверки эпсилон-переходов
            peak_to_add.append([conv.get_name(), self.check(conv, condition,True)])
        return("Хорошие вершины", peak_to_add)

    def check_ALL_epsilon(self):
        for condit in self.conditions:
            print(f"для condit {condit} ", self.check_epsilon(condit, True))

    def make_Stab():
        pass

    def make_Ptab():
        pass

a1 = Automat()