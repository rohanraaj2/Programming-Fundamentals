food = input()
def blend(food):
 return 'blended ' + food
def chop(food):
 return 'chopped ' + food
def grind(food):
 return 'ground ' + food
def mix(food):
 return 'mixed ' + food
def food_processor(task, food):
 return (task(food))
def knead(food):
return str("kneaded " + food)
print(food_processor(blend, food))
print(food_processor(chop, food))
print(food_processor(grind, food))
print(food_processor(mix, food))
print(food_processor(knead, food))
