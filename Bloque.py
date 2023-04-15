# Importa la librería PYGAME con el nombre de juego
import pygame as juego

class Bloque:
    # CONSTRUCTOR (x, y, ancho, alto)
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
    
    # El bloque avanzará hacia delante o hacia atrás en el eje X
    def moverX(self, x):
        self.x += x
    
    # El bloque avanzará hacia delante o hacia atrás en el eje Y
    def moverY(self, y):
        self.y += y
    
    # Dibuja el objeto en un escenario pasado
    def dibujar(self, escenario):
        # Crea un rectángulo con unas coordenadas y unas dimensiones
        rectangulo = juego.Rect(self.x, self.y, self.ancho, self.alto)
        color = [0, 0, 0] # Color negro
        # Dibuja el rectángulo creado con el color en un escenario
        juego.draw.rect(escenario, color, rectangulo)
    
    # Devuelve 'True' si golpea otro bloque
    def golpear(self, bloque):
        # Devuelve lo contrario de lo obtenido
        # Ninguna condición debe cumplirse para existir golpe
        return not (
            (self.x + self.ancho < bloque.x) or
            (self.y + self.alto < bloque.y) or
            (self.x > bloque.x + bloque.ancho) or
            (self.y > bloque.y + bloque.alto)
        )