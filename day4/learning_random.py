import random , mymodule
#randint(a,b) returns a integer a<= N <=b
#number=random.randint(10, 100)
# random() random floating point number 0.0 <= X < 1.0 
#print(random.random()) if we multiply we can find 0.0 <= X < 1.0 * N
# uniform(a,b) returns a floating number N such that
# a <= N <=b for a <=b and b <= N <=a for b<= a
#print(random.uniform(1, 10)) 1 and 10 included but not in random()

coin=["heads","tails"]
print(random.choice(coin))