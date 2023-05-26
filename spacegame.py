import pygame
import random
import math
import time

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")

# Cargar fondo
background_image = pygame.image.load("bg.png").convert()
background_image = pygame.transform.scale(background_image, (width, height))

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Cargar imágenes
player_image = pygame.image.load("player.png").convert_alpha()
enemy_image = pygame.image.load("enemy.png").convert_alpha()
bullet_image = pygame.image.load("bullet.png").convert_alpha()

# Redimensionar imágenes
player_image = pygame.transform.scale(player_image, (45, 45))
enemy_image = pygame.transform.scale(enemy_image, (45, 45))
bullet_image = pygame.transform.scale(bullet_image, (45, 45))

# Clases
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.centery = height // 2
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.rect.x = random.randint(0, width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(1, 3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

# Ventana inicial
def show_start_screen():
    screen.fill(BLACK)
    title_font = pygame.font.Font(None, 40)
    text_font = pygame.font.Font(None, 28)
    title_text = title_font.render("Space Invaders", True, WHITE)
    controls_text = text_font.render("-Usa las Flechas para moverte y la tecla Espacio para disparar-", True, WHITE)
    game_over_text = text_font.render("El juego termina si una nave enemiga toca al jugador", True, WHITE)
    start_text = title_font.render("Presiona Enter para comenzar", True, WHITE)
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 2 - 100))
    screen.blit(controls_text, (width // 2 - controls_text.get_width() // 2, height // 2 - 50))
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2))
    screen.blit(start_text, (width // 2 - start_text.get_width() // 2, height // 2 + 50))
    pygame.display.flip()
    wait_for_key()

# Esperar a que se presione una tecla
def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

# Grupos de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Crear el jugador
player = Player()
all_sprites.add(player)

# Crear los enemigos
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Contador de enemigos destruidos
enemies_destroyed = 0

# Fuente para el contador de enemigos destruidos
font = pygame.font.Font(None, 36)

# Variables para el cronómetro
start_time = time.time()
clock_ticks = 0

# Fuente para el cronómetro
timer_font = pygame.font.Font(None, 36)

# Mostrar la ventana inicial
show_start_screen()

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    # Control de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.centery)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # Actualizar
    all_sprites.update()

    # Comprobar colisiones entre el jugador y los enemigos
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    # Comprobar colisiones entre los disparos y los enemigos
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for _ in range(len(hits)):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        enemies_destroyed += 1

    # Dibujar fondo
    screen.blit(background_image, (0, 0))

    # Dibujar
    all_sprites.draw(screen)

    # Mostrar el contador de enemigos destruidos
    text = font.render("Enemigos destruidos: " + str(enemies_destroyed), True, WHITE)
    screen.blit(text, (10, 10))

    # Actualizar el cronómetro
    clock_ticks += 1
    elapsed_time = time.time() - start_time
    timer_text = "Tiempo: " + time.strftime("%M:%S", time.gmtime(elapsed_time))
    timer_render = timer_font.render(timer_text, True, WHITE)
    screen.blit(timer_render, (10, 50))

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)

# Finalizar Pygame
pygame.quit()
