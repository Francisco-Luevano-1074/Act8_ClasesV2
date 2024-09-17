print("Clases v2 El Constructor")

class Perro:
    # Función Constructor
    def __init__(self, color, edad):
        self.color=color
        self.edad=edad
    
    # Funciones creadas por el usuario
    def morder(self):
        print("Chale, el perro me mordió.")
        
    def chatperro(self, mensaje):
        print(f"Chat perro:{mensaje}")
        
    def chatperra(self, mensajepe):
        print(f"Chat perra:{mensajepe}")
    
    def datos(self):
        print(f"Color: {self.color} Edad: {self.edad}")
# Crear objeto
chihuas=Perro("Negro",2)
# Llamadas a funciones
chihuas.datos()
chihuas.morder()
chihuas.chatperro("Hola, perra")
chihuas.chatperra("Hola, Bobby")
chihuas.chatperro("Quieres ser mi guau guau?")
chihuas.chatperra("gruuuuuu.....")
