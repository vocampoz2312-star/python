#1 Puntaje total
level1 = int(input("Puntos nivel 1: "))
level2 = int(input("Puntos nivel 2: "))
level3 = int(input("Puntos nivel 3: "))

total_score = level1 + level2 + level3
print("Puntaje total:", total_score)

#2 Tiempo total en segundos
hours = int(input("Horas: "))
minutes = int(input("Minutos: "))
seconds = int(input("Segundos: "))

total_seconds = hours * 3600 + minutes * 60 + seconds
print("Tiempo total en segundos:", total_seconds)

#3 Daño total
d1 = int(input("Daño ataque 1: "))
d2 = int(input("Daño ataque 2: "))
d3 = int(input("Daño ataque 3: "))

total_damage = d1 + d2 + d3
print("Daño total:", total_damage)

#4 Experiencia total
xp1 = int(input("XP misión 1: "))
xp2 = int(input("XP misión 2: "))
xp3 = int(input("XP misión 3: "))

total_xp = xp1 + xp2 + xp3
print("Experiencia total:", total_xp)

#5 Porcentaje de vida
max_life = float(input("Vida máxima: "))
current_life = float(input("Vida actual: "))

percentage = (current_life / max_life) * 100
print("Vida restante:", percentage, "%")

#6 Oro total
gold1 = int(input("Oro misión 1: "))
gold2 = int(input("Oro misión 2: "))
gold3 = int(input("Oro misión 3: "))

total_gold = gold1 + gold2 + gold3
print("Oro total:", total_gold)

#7 Velocidad promedio
distance = float(input("Distancia recorrida: "))
time = float(input("Tiempo: "))

speed = distance / time
print("Velocidad promedio:", speed)

#8 Costo total de mejoras
c1 = float(input("Costo mejora 1: "))
c2 = float(input("Costo mejora 2: "))
c3 = float(input("Costo mejora 3: "))

total_cost = c1 + c2 + c3
print("Costo total:", total_cost)

#9 Tiempo restante
total_time = float(input("Tiempo total misión: "))
elapsed = float(input("Tiempo transcurrido: "))

remaining = total_time - elapsed
print("Tiempo restante:", remaining)

#10 Nivel promedio
n1 = int(input("Nivel jugador 1: "))
n2 = int(input("Nivel jugador 2: "))
n3 = int(input("Nivel jugador 3: "))

average = (n1 + n2 + n3) / 3
print("Nivel promedio:", average)

#11 Daño crítico
base_damage = float(input("Daño base: "))
critical_multiplier = float(input("Multiplicador crítico: "))

critical_damage = base_damage * critical_multiplier
print("Daño crítico:", critical_damage)

#12 Minutos a horas y minutos
total_minutes = int(input("Minutos totales: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print("Horas:", hours, "Minutos:", minutes)

#13 Porcentaje de misiones
total = int(input("Total misiones: "))
completed = int(input("Misiones completadas: "))

percentage = (completed / total) * 100
print("Porcentaje completado:", percentage, "%")

#14 Costo total tienda
o1 = float(input("Costo objeto 1: "))
o2 = float(input("Costo objeto 2: "))
o3 = float(input("Costo objeto 3: "))

total = o1 + o2 + o3
print("Costo total:", total)

#15 Tiempo promedio partidas
t1 = float(input("Tiempo partida 1: "))
t2 = float(input("Tiempo partida 2: "))
t3 = float(input("Tiempo partida 3: "))

average = (t1 + t2 + t3) / 3
print("Tiempo promedio:", average)

#16 Porcentaje enemigos derrotados
total_enemies = int(input("Total enemigos: "))
defeated = int(input("Enemigos derrotados: "))

percentage = (defeated / total_enemies) * 100
print("Porcentaje derrotados:", percentage, "%")