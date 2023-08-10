from food import Food
class Fruit(Food):
    def __init__(self,article,sugar_per_article):
        super().__init__("Fruit",article)
        self.sugar_per_article = sugar_per_article

    def __str__(self):
        return f"This fruit is a/an {self.article} and has {self.sugar_per_article}g of sugar."
  
