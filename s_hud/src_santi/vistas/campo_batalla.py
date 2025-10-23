#campo_batalla.py
import pygame
import random

class CampoBatalla:
    def __init__(self, pantalla, ancho_pantalla, alto_pantalla):
        self.pantalla = pantalla
        self.ancho_pantalla = ancho_pantalla
        self.alto_campo = int(alto_pantalla * 0.85)
        
        self.estrellas = []
        self._generar_estrellas(150)
    
    #genera estrellas de manera aleatoria en el espacio
    def _generar_estrellas(self, cantidad):
        for _ in range(cantidad):
            self.estrellas.append({
                'x': random.randint(0, self.ancho_pantalla),
                'y': random.randint(0, self.alto_campo),
                'velocidad': random.uniform(0.1, 0.8),
                'tamaño': random.randint(1, 3)
            })
            
    def actualizar(self):
        for estrella in self.estrellas:
            estrella['y'] += estrella['velocidad']
            if estrella['y'] > self.alto_campo:
                estrella['y'] = 0
                estrella['x'] = random.randint(0, self.ancho_pantalla)
                
    def dibujar(self):
        #dibujar estrellas en el fondo
        for estrella in self.estrellas:
            pygame.draw.circle(self.pantalla, (255, 255, 255), 
                             (int(estrella['x']), int(estrella['y'])), estrella['tamaño'])
        
        #linea separadora de las interfaces de usuario
        pygame.draw.line(self.pantalla, (255, 255, 255), 
                        (0, self.alto_campo), (self.ancho_pantalla, self.alto_campo), 2)