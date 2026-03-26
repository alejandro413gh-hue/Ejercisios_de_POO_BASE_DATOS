class Animal:

    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    #Getters
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_habitat(self):
        return self.habitat
    def get_dieta(self):
        return self.dieta
    def get_tambaño(self):
        return self.tamaño
    def get_color(self):
        return self.color
    
    #Setters 
    def set_nombre(self,nuevo_dato):
        self._nombre = nuevo_dato
    def set_edad(self,nuevo_dato):
        self._edad = nuevo_dato
    def set_habitat(self,nuevo_dato):
        self._habitat = nuevo_dato
    def set_dieta(self,nuevo_dato):
        self._dieta = nuevo_dato
    def set_tamaño(self,nuevo_dato):
        self._tamaño = nuevo_dato
    def set_color(self,nuevo_dato):
        self._colo = nuevo_dato

    def ver_info(self):
        print(f"  Nombre: {self._nombre}")
        print(f"  Edad: {self._edad}")
        print(f"  Habitat: {self._habitad}")
        print(f"  Dieta: {self._dieta}")
        print(f"  Tamaño: {self._tamaño}")
        print(f"  Color: {self._color}")
        
