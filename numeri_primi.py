'''Dato un limit mi dice tutti i numeri primi fino a limit (incluso)'''
limit = 100
result = [1]
for t in range(2, limit+1):
    primo = True
    for cursor in range(2, t):
        if t % cursor == 0:
            primo = False
            break
    result.append(t)
print(result)