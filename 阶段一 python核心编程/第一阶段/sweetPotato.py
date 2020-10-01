# 烤红薯
class SweetPotato(object):
    def __init__(self):
        # 定义红薯初始状态
        self.time = 0
        self.state = "生的"
        self.condiments = []

    def cook(self, time):
        # 将烤红薯的时间进行累加
        self.time += time
        if 0 <= self.time < 3:
            self.state = "生的"
        elif 3 <= self.time < 5:
            self.state = "半生不熟"
        elif 5 <= self.time < 8:
            self.state = "烤熟了"
            # 烤熟了添加调料
            self.add_condimentes("辣椒面儿")
        elif self.time >= 8:
            self.state = "烤糊了"

    def __str__(self):
        return f"烤了{self.time}分钟了，状态是{self.state}，调料有{self.condiments}"

    def add_condimentes(self, condiment):
        # 添加调料
        self.condiments.append(condiment)


sweetpotato = SweetPotato()
print(sweetpotato)

sweetpotato.cook(2)
print(sweetpotato)

sweetpotato.cook(2)
print(sweetpotato)

sweetpotato.cook(2)
print(sweetpotato)

sweetpotato.cook(2)
print(sweetpotato)
