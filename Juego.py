# Importa la pantalla, el bloque, generar randoms, la librería pygame, y utilidades matemáticas
from Pantalla import Pantalla
from Bloque import Bloque
from random import randrange
import pygame as juego
import math

# CREACIÓN DE OBJETOS
pantalla = Pantalla(338, 600) # ancho, alto
personaje = Bloque(144, 500, 50, 50) # X, Y, ancho, alto
enemigos = [] # Enemigos
puntos = 0 # Puntos
record = 0 # Record

# CONFIGURACIÓN PREVIA DE LA VENTANA (título, icono, inicio)
pantalla.setTitulo("Random Blocks")
pantalla.setIcono("assets/icono.png")
pantalla.iniciar()

# Hace que el bucle se repita por siempre hasta que se finalice desde dentro
repetir = True
while repetir:
    # ACTUALIZACIÓN DE DATOS
    # Si la pantalla no está en pausa, actualiza los datos
    if pantalla.pausa is False:
        # Obtiene las teclas presionadas
        teclas = pantalla.getTeclas()
        
        # Si se presiona la tecla A y su ubicación es mayor que 0, permite avanzar
        if teclas[pantalla.teclaA] and personaje.x > 0:
            # Movimiento negativo
            personaje.moverX(-0.1)
        # Si se presiona la tecla D y su ubicación es menor que el ancho del lienzo y su propio ancho
        # Permite avanzar
        if teclas[pantalla.teclaD] and personaje.x < 338 - personaje.ancho:
            # Movimiento positivo
            personaje.moverX(0.1)
        
        # Si todavía no existen enemigos o el último creado ha alcanzado un límite
        if len(enemigos) == 0 or enemigos[len(enemigos)-1].y > 200:
            # Se crea un enemigo en una ubicación X aleatoria, fuera del lienzo, con un ancho y un alto de 50
            enemigos.append(Bloque(randrange(338-50), -50, 50, 50))
            
        # Actualiza cada enemigo de los existentes
        for enemigo in enemigos:
            # Si el personaje golpea alguno de los enemigos
            if personaje.golpear(enemigo):
                # Aparece la pantalla de pausa y el juego se ha perdido
                pantalla.pausa = True
                pantalla.juegoPerdido = True
            
            # Mueve el enemigo
            enemigo.moverY(0.2)
        
        # Avanza los puntos con valores decimales para evitar una suma de puntos muy alta
        puntos += 0.001
    
    # Eventos generales que siempre ocurren independientemente de si la pantalla está en pausa o no
    # Obtiene todos los eventos que han sucedido
    for evento in pantalla.getEventos():
        # Si el usuario presiona el botón de cerrar de la esquina superior derecha
        if evento.type == juego.QUIT:
            # Deja de repetir el bucle y por lo tanto, cierra el juego
            repetir = False
        
        # Si el evento es del tipo 'tecla presionada'
        if evento.type == juego.KEYDOWN:
            # La tecla presionada es el espacio
            if evento.key == juego.K_SPACE:
                # Verifica si el juego estaba perdido
                if pantalla.juegoPerdido:
                    # En ese caso, borra los enemigos para repetir la partida
                    enemigos = []
                    
                    # Guarda el record si es menor a los puntos
                    if record < puntos:
                        # Pasa los puntos directamente truncados
                        record = math.trunc(puntos)
                    
                    # Resetea los puntos a 0 y el juego ya no está perdido
                    puntos = 0
                    pantalla.juegoPerdido = False
                
                # Establece la pantalla de pausa al valor contrario
                pantalla.pausa = not pantalla.pausa
    
    # DIBUJO DE GRÁFICOS
    # Dibuja el fondo de la pantalla
    pantalla.dibujarFondo([58, 175, 169])
    
    # Dibuja el personaje en el escenario de la pantalla
    personaje.dibujar(pantalla.escenario)
    
    # Para cada enemigo de los existentes
    for enemigo in enemigos:
        # Lo dibuja en el escenario
        enemigo.dibujar(pantalla.escenario)
        
        # Si el enemigo llega al final del lienzo
        if enemigo.y > 600:
            # Lo elimina (es el primero)
            enemigos.pop(0)
    
    # Escribe los puntos (valor truncado por ser decimal)
    pantalla.escribirTexto("PUNTOS: "+ str(math.trunc(puntos)), 5, 5, [255,255,255])
    
    # Si el record es diferente de 0, es porque ya existe un record, y por lo tanto, lo escribe
    if record != 0:
        # No lo trunca porque este valor fue pasado directamente truncado
        pantalla.escribirTexto("RECORD: "+ str(record), 5, 35, [255,255,255])
        
    # Si la pantalla está en pausa
    if pantalla.pausa:
        # Dibuja una capa transparente
        pantalla.dibujarCapa()
        
        # Si el juego está perdido
        if pantalla.juegoPerdido:
            # Muestra un mensaje del fin del juego
            pantalla.escribirTexto("Fin del juego", 338/2-95, 600/2-50, [255,255,255])
        else:
            # De lo contrario un mensaje de pausa
            pantalla.escribirTexto("Pausa", 338/2-45, 600/2-50, [255,255,255])
        
        # Por siempre, una notificación para pulsar la tecla espacio y cambiar el estado
        pantalla.escribirTexto("Tecla espacio", 338/2-95, 600/2, [255,255,255])
    
    # Muestra la escena
    pantalla.mostrarEscena()

# La última línea de código que se ejecuta, que termina correctamente el proceso
pantalla.finalizar()