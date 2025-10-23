#motor_juego.py
import pygame
import sys

class MotorJuego:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pygame.time.Clock()
        self.ejecutando = True
        self.pantalla_completa = True
        
        from src_santi.vistas.campo_batalla import CampoBatalla
        from src_santi.vistas.interfaz_usuario import InterfazUsuario
        from src_santi.modelos.jugador import Jugador
        
        # Obtener dimensiones de la pantalla
        info_pantalla = pygame.display.Info()
        self.ancho_pantalla = info_pantalla.current_w
        self.alto_pantalla = info_pantalla.current_h
        
        self.campo_batalla = CampoBatalla(self.pantalla, self.ancho_pantalla, self.alto_pantalla)
        self.interfaz_usuario = InterfazUsuario(self.pantalla, self.ancho_pantalla, self.alto_pantalla)
        
        #jugadores de prueba
        self.jugador1 = Jugador("Jugador1")
        self.jugador2 = Jugador("Jugador2") 
        self.jugador_activo = self.jugador1
        
    def alternar_pantalla_completa(self):
        #se puede alternar entre pantalla completa y ventana
        self.pantalla_completa = not self.pantalla_completa
        if self.pantalla_completa:
            pantalla = pygame.display.set_mode((self.ancho_pantalla, self.alto_pantalla), pygame.FULLSCREEN)
        else:
            pantalla = pygame.display.set_mode((1200, 800))
        
        #actualizar referencias
        self.pantalla = pantalla
        self.campo_batalla.pantalla = pantalla
        self.interfaz_usuario.pantalla = pantalla
        
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
                return False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.ejecutando = False
                    return False
                #prueba ESPACIO para aumentar puntaje
                elif evento.key == pygame.K_SPACE:
                    self.jugador_activo.actualizar_puntaje(200)
                #prueba: L para perder vida
                elif evento.key == pygame.K_l:
                    self.jugador_activo.perder_vida()
                #prueba: B para añadir bono
                elif evento.key == pygame.K_b:
                    self.jugador_activo.agregar_bono("Escudo")
                # NUEVO: F11 para alternar pantalla completa
                elif evento.key == pygame.K_F11:
                    self.alternar_pantalla_completa()
        return True
                    
    def actualizar(self):
        self.campo_batalla.actualizar()
        
    def dibujar(self):
        self.pantalla.fill((0, 0, 0))
        self.campo_batalla.dibujar()
        self.interfaz_usuario.dibujar(self.jugador1, self.jugador2, self.jugador_activo)
        pygame.display.flip()
        
    def ejecutar(self):
        while self.ejecutando:
            if not self.manejar_eventos():
                break
            self.actualizar()
            self.dibujar()
            self.reloj.tick(60)
        
        return True