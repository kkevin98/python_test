'''Dato un limit mi dice tutti i numeri primi fino a limit (incluso)
   versione senza flag'''
limit = 100
result = []
for t in range(2, limit+1):
    for cursor in range(2, t):
        if t % cursor == 0:
            break
    else:
        result.append(t)
print(result)