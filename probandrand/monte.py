import random 
inside_circle=0
total_points= 10000

for i in range(total_points):
    x = random.random()
    y = random.random()

    if x*x+ y*y <=1:
        inside_circle+=1

pi = 4 * inside_circle/total_points
print("Estimated Value of Pi= ",pi)