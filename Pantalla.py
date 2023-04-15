# Importa la librería PYGAME con el nombre de juego
import pygame as juego

# Clase Pantalla, maneja los datos del escenario y de la ventana
class Pantalla:
    # Constructor, empieza con un ancho, un alto, y si el juego empieza en pausa, por defecto en False
    def __init__(self, ancho, alto, pausa=False):
        # Ancho, alto, juego en pausa, juego perdido
        self.ancho = ancho
        self.alto = alto
        self.pausa = pausa
        self.juegoPerdido = False
        # Teclas (a, d, espacio)
        self.teclaA = juego.K_a
        self.teclaD = juego.K_d
        self.teclaEspacio = juego.K_SPACE
    
    # Da un color de fondo al escenario
    def dibujarFondo(self, color):
        # Rellena el escenario pasado con un color
        self.escenario.fill(color) 
    
    # Escribe un texto en el escenario con unas coordenadas y un color de negro por defecto
    def escribirTexto(self, texto, x, y, color=[0,0,0]):
        # Renderiza la fuente con los datos
        self.fuente.render_to(self.escenario, [x,y], texto, color)
    
    # Método para iniciar la cadena de procesamiento
    def iniciar(self):
        # Inicia el juego
        juego.init()
        # Con el juego iniciado, define una fuente importando el archivo y un tamaño
        self.fuente = juego.freetype.Font("assets/fuente.ttf", 25)
        # Crea un escenario con los datos del juego
        self.escenario = juego.display.set_mode([self.ancho, self.alto])
    
    # Método para configurar el título de la ventana
    def setTitulo(self, texto):
        # Escribe el título de la ventana
        juego.display.set_caption(texto)
    
    # Método para configurar el icono de la ventana
    def setIcono(self, ruta):
        # Carga el icono y lo muestra
        icono = juego.image.load(ruta)
        juego.display.set_icon(icono)
    
    # Método para obtener las teclas presionadas
    def getTeclas(self):
        # Devuelve del juego una lista con las teclas
        return juego.key.get_pressed()
    
    # Muestra el desarrollo del juego
    def mostrarEscena(self):
        # Optimiza el renderizado, más que con un bucle while
        juego.display.flip()
    
    # Finaliza la tarea de ejecución
    def finalizar(self):
        # Se ejecuta, por lo general, al final del código
        juego.quit()
    
    # Devuelve los eventos que han sucedido en ese ciclo
    def getEventos(self):
        # Obtiene esos datos y los devuelve
        return juego.event.get()

    # Método para dibujar capas
    def dibujarCapa(self):
        # Crea una capa nueva
        capa = juego.Surface([self.ancho, self.alto]) # Ancho y alto del lienzo
        capa.set_alpha(128) # Transparencia
        capa.fill([0,0,0]) # Color negro
        # En el propio escenaeio
        self.escenario.blit(capa, [0,0]) # Dibuja la capa creada desde las coordenadas (0,0)