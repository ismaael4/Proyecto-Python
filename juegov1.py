import pygame
import sys
import time
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana del juego
WIDTH, HEIGHT = 1200, 730
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hockey Pong")

# Cargar una imagen de fondo
background_image = pygame.image.load("imagenes/fondo.png")

# Cargar imágenes para las barras de jugador
player_paddle_image = pygame.image.load("imagenes/palo_blanco.png")
opponent_paddle_image = pygame.image.load("imagenes/palo_negro.png")

# Cargar la imagen de la pelota
ball_image = pygame.image.load("imagenes/pelota.png")

# Colores
WHITE = (255, 255, 255)

# Paletas
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 100  # Ajusta el tamaño de las paletas según tus preferencias
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Escalar las imágenes de las paletas al tamaño deseado
player_paddle_image = pygame.transform.scale(player_paddle_image, (PADDLE_WIDTH, PADDLE_HEIGHT))
opponent_paddle_image = pygame.transform.scale(opponent_paddle_image, (PADDLE_WIDTH, PADDLE_HEIGHT))

# Pelota
BALL_WIDTH, BALL_HEIGHT = 30, 30  # Tamaño de la pelota (asegúrate de que tu imagen tenga este tamaño)
ball = pygame.Rect(WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)
ball_speed = 8.0  # Velocidad inicial de la pelota
ball_speed_x = ball_speed  # Dirección inicial en X
ball_speed_y = random.choice([ball_speed, -ball_speed])  # Dirección aleatoria en Y

# Variables para el control de la velocidad de la pelota
increase_speed = 1.0  # Incremento de velocidad con cada golpe
ball_hits = 0  # Contador de golpes

# Puntuación
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

# Reloj del juego
clock = pygame.time.Clock()

# Inicializar variables de movimiento del jugador
player_speed = 0

# Clase para representar partículas
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)
        self.size = random.randint(2, 5)
        self.speed = [random.uniform(-2, 2), random.uniform(-2, 2)]
        self.lifetime = 20  # Ajusta la duración de las partículas

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.lifetime -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# Lista para almacenar las partículas
particles = []

# Función para mostrar la cuenta regresiva
def show_countdown():
    for i in range(3, 0, -1):
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render(str(i), True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        time.sleep(1)

# Variable que controla si se está mostrando la cuenta regresiva
countdown_active = False

# Tiempo de juego en segundos (2 minutos)
game_time = 120
start_time = time.time()

# Loop principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = time.time()
    elapsed_time = current_time - start_time

    # Verificar si se ha agotado el tiempo
    if elapsed_time >= game_time:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        if player_score > opponent_score:
            winner_text = font.render("¡HAS GANADO!", True, WHITE)
        elif opponent_score > player_score:
            winner_text = font.render("¡HAS PERDIDO!", True, WHITE)
        else:
            winner_text = font.render("¡Empate!", True, WHITE)
        text_rect = winner_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(winner_text, text_rect)
        pygame.display.update()
        time.sleep(2)  # Esperar 2 segundos antes de salir del juego

        # Salir del juego
        pygame.quit()
        sys.exit()

    # Capturar eventos de teclado para el jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_speed = -5  # Mover hacia arriba
    elif keys[pygame.K_s]:
        player_speed = 5  # Mover hacia abajo
    else:
        player_speed = 0  # Detener el movimiento

    # Actualizar la posición vertical del jugador
    player_paddle.y += player_speed

    # Lógica de movimiento del oponente
    opponent_target_y = ball.y + ball.height / 2 - opponent_paddle.height / 2
    opponent_speed = 8  # Ajusta la velocidad de reacción del oponente según tus preferencias

    if opponent_paddle.y < opponent_target_y:
        opponent_paddle.y += opponent_speed
    elif opponent_paddle.y > opponent_target_y:
        opponent_paddle.y -= opponent_speed

    # Lógica del movimiento de la pelota
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisiones de la pelota con las paletas
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1
        ball_speed_y += increase_speed
        ball_hits += 1

        # Genera partículas en la posición de la colisión
        for _ in range(10):  # Crea 10 partículas en cada colisión
            particles.append(Particle(ball.x + ball.width / 2, ball.y + ball.height / 2))

    # En el bucle principal, después de mover la pelota y las paletas
    for particle in particles:
        particle.move()
        if particle.lifetime <= 0:
            particles.remove(particle)

    # Colisiones de la pelota con los bordes superior e inferior
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Gestionar puntuación
    if ball.left <= 0:
        opponent_score += 1
        countdown_active = True
        ball_speed_x = ball_speed  # Reiniciar la velocidad al perder un punto
        ball_speed_y = random.choice([ball_speed, -ball_speed])
        ball_hits = 0  # Reiniciar el contador de golpes
    elif ball.right >= WIDTH:
        player_score += 1
        countdown_active = True
        ball_speed_x = ball_speed  # Reiniciar la velocidad al ganar un punto
        ball_speed_y = random.choice([ball_speed, -ball_speed])
        ball_hits = 0  # Reiniciar el contador de golpes

    # Muestra la cuenta regresiva después de que alguien anote un punto
    if countdown_active:
        show_countdown()
        ball = pygame.Rect(WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)
        countdown_active = False
        time.sleep(1)  # Agrega un pequeño retraso antes de reanudar el juego

    # Dibujar todo en la pantalla
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))
    screen.blit(ball_image, ball)
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
    time_text = font.render(f"Time: {int(game_time - elapsed_time)}", True, WHITE)
    screen.blit(player_text, (50, 50))
    screen.blit(opponent_text, (WIDTH - 200, 50))
    screen.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, 20))

    # Dibujar paletas usando imágenes escaladas
    screen.blit(player_paddle_image, player_paddle)
    screen.blit(opponent_paddle_image, opponent_paddle)

    # Dibuja las partículas en la pantalla
    for particle in particles:
        particle.draw(screen)

    pygame.display.update()
    clock.tick(60)
