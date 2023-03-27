def segundo_menor(lista):
    m1, m2 = float('inf'), float('inf')
    for x in lista:
      if x <= m1:
        m1, m2 = x, m1
      elif x < m2:
        m2 = x
    return print(m2)

segundo_menor([1,2,3,4,5,6,7,8,9,0])
