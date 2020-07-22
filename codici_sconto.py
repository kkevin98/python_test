'''
    Prendo dei clienti con dei coupon, poi stampo lo sconto
    che spetta a ciascuno di loro. Metodo per evitare la clausola switch/case
    (o elif in python)
'''
customers = [
    dict(id=1, total=200, coupon_code='F20'),  # F20: fixed, £20
    dict(id=2, total=150, coupon_code='P30'),  # P30: percent, 30%
    dict(id=3, total=100, coupon_code='P50'),  # P50: percent, 50%
    dict(id=4, total=110, coupon_code='F15'),  # F15: fixed, £15
]
libretto_coupon = {
    'F20': (20, 0),
    'P30': (0, 0.3),
    'P50': (0, 0.5),
    'F15': (15, 0)
}
for customer in customers:
    code = customer['coupon_code']
    fisso, percentuale = libretto_coupon.get(code, (0, 0))
    customer['sconto'] = fisso + customer['total']*percentuale
for customer in customers:
    print(customer)