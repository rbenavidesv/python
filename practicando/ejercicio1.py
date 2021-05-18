def calcular_impuesto(edad, ingreso):
    porcentaje = 0.4
   
    if edad >=18 and ingreso >= 1000 :
        return ingreso * porcentaje
    else:
       return 0
    
print (int(calcular_impuesto(18,1000)))
print (int(calcular_impuesto(40,10000)))
print (calcular_impuesto(17,5000))