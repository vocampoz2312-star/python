# Crear variables con el número de manzanas
john = 3
mary = 5
adam = 6

# Imprimir las variables en una sola línea separadas por coma
print(john, mary, adam)

# Crear variable con el total de manzanas
total_apples = john + mary + adam

# Imprimir el total
print(total_apples)

# Imprimir texto junto con variable (conversión a string)
print("Número total de manzanas:", total_apples)

# -------------------------------
# EXPERIMENTACIÓN (operaciones)
# -------------------------------

# Nuevas variables
extra_apples = 10
lost_apples = 2

# Operaciones aritméticas
sum_result = total_apples + extra_apples
sub_result = total_apples - lost_apples
mul_result = john * mary
div_result = adam / 2
floor_div = adam // 2

# Mostrar resultados
print("Suma:", sum_result)
print("Resta:", sub_result)
print("Multiplicación:", mul_result)
print("División:", div_result)
print("División entera:", floor_div)

# -------------------------------
# REASIGNACIÓN DE VARIABLES
# -------------------------------

john = john + 1  # Juan obtiene una manzana más
print("John ahora tiene:", john)

# -------------------------------
# EJEMPLO BÁSICO DE VARIABLE
# -------------------------------

var = 1
print(var)

var = var + 1
print(var)

# -------------------------------
# EJEMPLO DE TEXTO + VARIABLE
# -------------------------------

version = "3.8.5"
print("Python version: " + version)

# -------------------------------
# EJEMPLO MATEMÁTICO (Pitágoras)
# -------------------------------

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5

print("c =", c)