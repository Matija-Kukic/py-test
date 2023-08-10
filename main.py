from food import Food
from fruit import Fruit
from FruitBowl import Fruit_bowl

def main():
    
    arr = []

    arr.append( Food("Fruit","Banana") )
    arr.append( Food("Meat","Chicken") )
    arr.append(  Fruit("Apple", 35) )
    arr.append( Fruit("Banana", 40) )
    arr.append( Fruit("Peach", 45) )

    print(arr[3].sugar_per_article)
    
    F = Fruit_bowl(arr)
    a = F.Total_sugar()
    print(a)

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()


