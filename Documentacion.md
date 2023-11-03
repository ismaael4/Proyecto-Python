# Documentación del Proyecto Hockey Pong

Este documento proporciona una breve descripción y documentación de un juego de Ping Pong implementado en Python utilizando la biblioteca Pygame. El juego consiste en una versión simple del clásico juego de Ping Pong, donde dos jugadores controlan paletas en lados opuestos de la pantalla y tratan de golpear una pelota entre sí. El objetivo es anotar puntos al hacer que la pelota pase por la paleta del oponente.

## Descripción del Juego

**Nombre del Juego:** Hockey Pong 

**Descripción:**
- **Objetivo:** Anotar puntos al hacer que la pelota pase por la paleta del oponente.
- **Duración:** El juego dura 2 minutos, y el objetivo es anotar la mayor cantidad de puntos posible en ese tiempo.
- **Controles:**
    - Jugador 1: Teclas "W" (arriba) y "S" (abajo) para mover la paleta hacia arriba y abajo, respectivamente.
    - Jugador 2 (oponente): La IA controla automáticamente la paleta del oponente.
- **Puntuación:** El jugador que anote más puntos al final del juego gana.

## Requisitos y Dependencias

Para ejecutar este juego, se requiere tener instalado Python y la biblioteca Pygame. Asegúrate de tener instaladas las siguientes dependencias:

- Python: [Descarga e instalación de Python](https://www.python.org/downloads/).
- Pygame: Instala Pygame usando pip con el siguiente comando: pip install pygame

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- Archivos de Imágenes:
  - "fondo.png": Imagen de fondo de la pantalla de juego.
  - "palo_blanco.png": Imagen de la paleta del jugador.
  - "palo_negro.png": Imagen de la paleta del oponente.
  - "pelota.png": Imagen de la pelota del juego.

- Código Fuente:
  - El código fuente está contenido en un único archivo Python y consta de las siguientes secciones:
      - Inicialización de Pygame y configuración de la ventana del juego.
      - Carga de imágenes de fondo, paletas y pelota.
      - Definición de variables para las paletas y la pelota, así como para el control del juego.
      - Funciones para mostrar la cuenta regresiva y gestionar el tiempo del juego.
      - Bucle principal del juego que maneja eventos, movimientos, colisiones y actualización de la pantalla.

## Ejecución del Juego

1. Asegúrate de tener Python y Pygame instalados en tu sistema.
2. Coloca las imágenes de fondo y los elementos del juego en la misma ubicación que el archivo Python.
3. Ejecuta el archivo Python en un entorno de Python.

## Personalización

- Puedes personalizar las imágenes de las paletas y la pelota reemplazando los archivos de imágenes con tus propias imágenes.
- Puedes ajustar la velocidad y la reacción del oponente modificando la variable `opponent_speed` en el código.
- Puedes modificar la duración del juego ajustando la variable `game_time` en segundos.

## Créditos

Este juego fue desarrollado utilizando la biblioteca Pygame y se basa en un concepto clásico de juegos de arcade. Los archivos de imágenes utilizados en el juego son parte de los recursos gráficos disponibles en el proyecto.

---
Enlace : https://github.com/ismaael4/Proyecto-Python

¡Disfruta del juego y diviértete jugando al Hockey Pong !
By Ismael Mariscal Santos