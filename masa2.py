gravedad_en_marte = 3.72
gravedad_en_neptuno = 11.15
gravedad_en_tierra = 9.81

peso_en_tierra = float (input("ingrese su peso"))
tu_peso_marte_es= (peso_en_tierra/gravedad_en_tierra)*gravedad_en_marte
tu_peso_neptuno_es = (peso_en_tierra/gravedad_en_tierra)*gravedad_en_neptuno
#print("{:.1f}") " ("tu peso en marte es"), tu_peso_marte
#print("{:.1f}") " (tu peso en neptuno es)", tu_peso_neptuno_es
print("tu peso neptuno es {:.1f}".format(tu_peso_neptuno_es))
print("tu peso marte es {:.1f}".format(tu_peso_marte_es))