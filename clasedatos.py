class Información:
    
    def mi_lista(self):
        lista_Nomperros=["-Princess Cupcake", "-Bistec", "-Don Pollo"]
        for x in lista_Nomperros:
            print(x)
    
    def mi_tupla(self):
        tupla_Razperros=("-Rottweiler", "-Pug", "-Bulldog")
        for x in tupla_Razperros:
            print(x)
            
    def mi_diccionario(self):
        dic_edperros = {
            "Princess Cupcake:":1,
            "Bistec:": 2,
            "Don Pollo:": 3
        }
        for x,y in dic_edperros.items():
            print(x,y)
        
    def mi_conjunto(self):        
        con_colperros = {"-Negro", "-Blanco", "-Café"}
        for x in con_colperros:
            print(x)
# Creando el objeto
datos=Información()
print("Listado de nombres de perros:")
datos.mi_lista()
print("Listado de Razas de perros:")
datos.mi_tupla()
print("Listado de Edades de perros:")
datos.mi_diccionario()
print("Listado de Colores de perros:")
datos.mi_conjunto()
