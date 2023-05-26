# Space Invaders

Space Invaders es un juego clásico desarrollado en Python utilizando la biblioteca Pygame.

## Requisitos

- Python 3.x
- Pygame

## Instalación

1. Clona o descarga este repositorio.
2. Asegúrate de tener Python instalado en tu sistema.
3. Instala Pygame ejecutando el siguiente comando en tu terminal: 

```
pip install pygame
```

## Cómo jugar

1. Ejecuta el archivo `space_invaders.py`.
2. En la pantalla inicial, verás las instrucciones y el objetivo del juego.
3. Usa las flechas de dirección para moverte y la tecla de espacio para disparar.
4. El juego termina si una nave enemiga toca al jugador.
5. Destruye la mayor cantidad de enemigos posible y sobrevive el mayor tiempo que puedas.

¡Diviértete jugando a Space Invaders!

## Explicación del código

El código está dividido en varias secciones y utiliza conceptos de programación orientada a objetos para crear las entidades del juego. A continuación, se explica cada sección relevante del código:

### Inicialización y configuración

El código comienza importando los módulos necesarios, como `pygame`, `random`, `math` y `time`. Luego, se inicializa Pygame llamando a `pygame.init()`.

A continuación, se configura la pantalla del juego especificando su ancho y alto, y se carga una imagen de fondo. Además, se definen algunos colores utilizando tuplas RGB.

### Carga de imágenes

El código carga las imágenes necesarias para el juego, incluyendo las imágenes del jugador, enemigos y balas. Estas imágenes se escalan a un tamaño específico utilizando la función `pygame.transform.scale()`.

### Clases

El código define tres clases: `Player`, `Enemy` y `Bullet`. Cada clase hereda de la clase base `pygame.sprite.Sprite`.

- La clase `Player` representa al jugador y define su imagen, posición, velocidad y métodos para actualizar su posición basada en las teclas presionadas.
- La clase `Enemy` representa a los enemigos y define su imagen, posición inicial aleatoria y velocidad de movimiento hacia abajo. También tiene un método para actualizar su posición y reiniciar su posición cuando se sale de la pantalla.
- La clase `Bullet` representa las balas disparadas por el jugador. Define su imagen, posición inicial y velocidad hacia arriba. También tiene un método para actualizar su posición y eliminarla cuando se sale de la pantalla.

### Ventana inicial y esperar tecla

El código define una función `show_start_screen()` que muestra la pantalla inicial del juego. Esta pantalla muestra el título del juego, las instrucciones de control y cómo se termina el juego. También muestra un mensaje para presionar la tecla Enter y comenzar el juego. La función `wait_for_key()` espera hasta que se presione la tecla Enter para continuar.

### Grupos de sprites

El código crea tres grupos de sprites utilizando la clase `pygame.sprite.Group()`: `all_sprites`, `enemies` y `bullets`. Estos grupos se utilizan para almacenar y gestionar todos los sprites del juego.

### Creación de jugadores y enemigos

El código crea una instancia del jugador y lo agrega al grupo `all_sprites`. Luego, crea múltiples instancias de enemigos y las agrega tanto a `all_sprites` como a `enemies`.

### Actualización y detección de colisiones

Dentro del bucle principal del juego, se actualizan las posiciones de todos los sprites llamando al método `update()` en `all_sprites`. Luego, se comprueban las colisiones entre el jugador y los enemigos utilizando `pygame.sprite.spritecollide()`. Si hay una colisión, el juego termina.

También se comprueban las colisiones entre las balas y los enemigos utilizando `pygame.sprite.groupcollide()`. Si hay una colisión, se crean nuevos enemigos y se incrementa el contador de enemigos destruidos.

### Dibujar en pantalla

El código dibuja el fondo, los sprites y la información adicional en la pantalla utilizando el método `blit()` de `screen`. Esto incluye el contador de enemigos destruidos y el cronómetro.

### Bucle principal del juego

El bucle principal del juego se ejecuta mientras la variable `running` sea verdadera. Dentro de este bucle, se controlan los eventos de Pygame, se actualizan las posiciones de los sprites, se comprueban las colisiones y se dibujan los elementos en la pantalla.

El bucle se repite a una velocidad de 60 FPS utilizando `clock.tick(60)`.

### Finalización del juego

Una vez que el bucle principal termina, se llama a `pygame.quit()` para finalizar Pygame y salir del juego.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o tienes ideas para mejorar el juego, no dudes en abrir un problema o enviar una solicitud de extracción.

## Licencia

Este proyecto está bajo la [Licencia MIT](https://opensource.org/licenses/MIT).
