class Asiento:
    def __init__(self, precio, color, registro):
        self.precio   = precio 
        self.color    = color
        self.registro = registro
     
    def cambiarColor(self, color):
        if(color in ("verde", "blanco", "rojo", "negro", "amarillo")):
            self.color = color

class Motor:

    def __init__ (self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo            = tipo
        self.registro        = registro

    def cambiarRegistro(self, NewRegister):
        self.registro = NewRegister

    def asignarTipo(self, tipo):
        if tipo == 'gasolina' or tipo == 'electrico':
            self.tipo = tipo

class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo   = modelo
        self.precio   = precio
        self.asientos = asientos
        self.marca    = marca
        self.motor    = motor
        self.registro = registro
        
    def cantidadAsientos(self):
        counter = 0
        for n in self.asientos:
            if (n != None):
                counter += 1
        return counter
    
    def verificarIntegridad(self):
        if (self.registro != self.motor.registro):
            return "Las piezas no son originales"
        
        else:
            for e in self.asientos:
                if (e != None and e.registro != self.registro):
                    return "Las piezas no son originales"
            return "Auto original"  
