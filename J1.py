P = int(input())
C = int(input())
points = P*50
points_loss = C*10

F = points - points_loss

if points > points_loss:
    F+= 500

print(F)
