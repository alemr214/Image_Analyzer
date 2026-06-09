# Image Analyzer

Un analizador de imágenes en Python que permite cargar una imagen, ver sus propiedades básicas y aplicar operaciones simples como extraer canales de color, rotar y reducir el tamaño.

## Descripción

Este proyecto ofrece una interfaz gráfica sencilla basada en `tkinter` para:

- seleccionar una imagen (`.png`, `.jpg`, `.jpeg`)
- mostrar ancho, alto y número de canales
- guardar el canal rojo, verde o azul como nueva imagen
- guardar una versión rotada en 90 grados
- guardar una versión reducida mediante muestreo cada `n` pixeles

Las operaciones de imagen se realizan con `numpy`, `matplotlib` y `Pillow`.

## Requisitos

- Python 3.11 o superior
- Terminal / consola con acceso al directorio del proyecto

Dependencias principales:

- numpy
- matplotlib
- pillow
- tkinter (incluido con Python en la mayoría de distribuciones)

Para instalar todas las dependencias, ejecuta:

```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación:

```bash
python src/main.py
```

### Pasos

1. Haz clic en `Seleccionar imagen`.
2. Escoge un archivo de imagen válido.
3. Observa la ruta y las propiedades de la imagen (ancho, alto, canales).
4. Usa los botones disponibles para:
   - extraer el canal rojo, verde o azul
   - rotar la imagen 90°
   - reducir la imagen ingresando un valor en `Veces a reducir`
5. Las imágenes resultantes se guardan en el mismo directorio con sufijos como `_rojo.png`, `_verde.png`, `_azul.png`, `_rotada.png` y `_reducida.png`.

## Estructura del proyecto

- `src/main.py`: punto de entrada principal de la aplicación.
- `src/ui/window.py`: interfaz gráfica y lógica de los botones.
- `src/model/image.py`: clase que representa metadatos de la imagen.
- `src/utils/image_utils.py`: funciones para convertir, rotar, reducir y extraer canales.
