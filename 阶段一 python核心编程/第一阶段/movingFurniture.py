# 搬家具

# 创建家具类
class Furniture(object):
    def __init__(self, name, area):
        # 家具名字和占地面积
        self.name = name
        self.area = area


# 创建房子类
class House(object):
    def __init__(self, address, area):
        # 房子的地址
        self.address = address
        # 房子的面积
        self.area = area
        # 房子剩余面积
        self.free_area = area
        # 房子内的家具名
        self.furnitures = []

    def movineFurniture(self, furniture):
        # 房子剩余面积大于家具面积
        if self.free_area > furniture.area:
            self.free_area -= furniture.area
            self.furnitures.append(furniture.name)
        else:
            print("房子剩余面积比该家具面积小，搬不进去了")

    def __str__(self):
        return f"房子位置在{self.address},占地面积是{self.area},剩余面积是{self.free_area},家具有{self.furnitures}"


bed = Furniture("双人床", 5)
sofa = Furniture("沙发", 4)
playground = Furniture("操场", 200)

beijing_home = House("北京", 120)
beijing_home.movineFurniture(bed)
print(beijing_home)

beijing_home.movineFurniture(sofa)
print(beijing_home)

beijing_home.movineFurniture(playground)
print(beijing_home)

