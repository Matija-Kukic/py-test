from fruit import Fruit
class Fruit_bowl():
    def __init__(self,arr):
        self.arr = arr
    def Total_sugar(self):
        ts = 0
        for i in range(len(self.arr)):
            if isinstance(self.arr[i],Fruit):
                ts+=self.arr[i].sugar_per_article
        return ts
