class Food:
    def __init__(self,Type,article):
        self.Type = Type
        self.article = article
    def __str__(self):
        return f"Food is type: {self.Type}, article {self.article}"

class Fruit(Food):
    def __init__(self,article,sugar_per_article):
        super().__init__("Fruit",article)
        self.sugar_per_article = sugar_per_article

    def __str__(self):
        return f"This fruit is a/an {self.article} and has {self.sugar_per_article}g of sugar."
        

def main():
    f1 = Food("Fruit","Banana")
    f2 = Food("Meat","Chicken")
    f3 = Fruit("Apple", 35)
    print(f1,f2,f3,sep="\n")



main()
