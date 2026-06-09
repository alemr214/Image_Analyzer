import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

try:
    from model.image import Image
    from utils.image_utils import (
        convert_image_array,
        extract_red_channel,
        extract_green_channel,
        extract_blue_channel,
        rotate_image,
        shrink_image,
        print_save_image,
    )
except ModuleNotFoundError:
    from src.model.image import Image
    from src.utils.image_utils import (
        convert_image_array,
        extract_red_channel,
        extract_green_channel,
        extract_blue_channel,
        rotate_image,
        shrink_image,
        print_save_image,
    )

image_base = Image()


def build_app() -> tk.Tk:
    root = tk.Tk()
    root.title("Analizador de Imágenes")

    frame = tk.Frame(root)
    frame.pack(padx=50, pady=30)

    label_route = tk.Label(frame, text="Ninguna imagen seleccionada")
    label_info = tk.Label(frame, text="")

    def update_route_label() -> None:
        if image_base.route:
            label_route.config(text=f"Ruta: {image_base.route}")
        else:
            label_route.config(text="Ninguna imagen seleccionada")
        update_image_info()

    def update_image_info() -> None:
        if image_base.route:
            label_info.config(
                text=(
                    f"Ancho: {image_base.weight} px  "
                    f"Alto: {image_base.height} px  "
                    f"Canales: {image_base.channels}"
                )
            )
            label_info.pack(pady=5)
        else:
            label_info.config(text="")
            label_info.pack_forget()

    def load_image_data():
        if not image_base.route:
            return None
        img_array = convert_image_array(image_base)
        image_base.weight = img_array.shape[1]
        image_base.height = img_array.shape[0]
        image_base.channels = img_array.shape[2] if img_array.ndim == 3 else 1
        return img_array

    def ensure_image_loaded() -> bool:
        if not image_base.route:
            messagebox.showwarning("Atención", "Debes seleccionar una imagen primero.")
            return False
        return True

    def save_and_notify(result_array, suffix: str) -> None:
        image_path = Path(image_base.route)
        output_name = image_path.with_name(f"{image_path.stem}_{suffix}.png")
        print_save_image(str(output_name), result_array)
        messagebox.showinfo(
            "Imagen guardada", f"Se guardó la imagen: {output_name.name}"
        )

    def select_image() -> None:
        system_route = filedialog.askopenfilename(
            title="Selecciona una imagen",
            filetypes=[
                ("Imágenes", "*.png *.jpg *.jpeg"),
                ("Todos los archivos", "*.*"),
            ],
        )
        if not system_route:
            return
        image_base.route = system_route
        load_image_data()
        update_route_label()

    def apply_red_filter() -> None:
        if not ensure_image_loaded():
            return
        img_array = load_image_data()
        if img_array is not None:
            save_and_notify(extract_red_channel(img_array), "rojo")

    def apply_green_filter() -> None:
        if not ensure_image_loaded():
            return
        img_array = load_image_data()
        if img_array is not None:
            save_and_notify(extract_green_channel(img_array), "verde")

    def apply_blue_filter() -> None:
        if not ensure_image_loaded():
            return
        img_array = load_image_data()
        if img_array is not None:
            save_and_notify(extract_blue_channel(img_array), "azul")

    def apply_rotate_image() -> None:
        if not ensure_image_loaded():
            return
        img_array = load_image_data()
        if img_array is not None:
            save_and_notify(rotate_image(img_array), "rotada")

    def apply_shrink_image() -> None:
        if not ensure_image_loaded():
            return
        img_array = load_image_data()
        if img_array is not None:
            save_and_notify(
                shrink_image(img_array, int(input_shrink.get())), "reducida"
            )

    btn_select_image = tk.Button(frame, text="Seleccionar imagen", command=select_image)
    btn_red_filter = tk.Button(
        frame, text="Extraer canal rojo", command=apply_red_filter
    )
    btn_green_filter = tk.Button(
        frame, text="Extraer canal verde", command=apply_green_filter
    )
    btn_blue_filter = tk.Button(
        frame, text="Extraer canal azul", command=apply_blue_filter
    )
    btn_rotate_image = tk.Button(
        frame, text="Rota la imagen 90°", command=apply_rotate_image
    )
    btn_shrink_image = tk.Button(
        frame, text="Reduce la imagen", command=apply_shrink_image
    )
    shrink_frame = tk.Frame(frame)
    shrink_label = tk.Label(shrink_frame, text="Veces a reducir: ")
    input_shrink = tk.Spinbox(shrink_frame, width=10, from_=0, to=100)

    btn_select_image.pack(pady=5)
    label_route.pack(pady=5)
    label_info.pack(pady=5)
    btn_red_filter.pack(pady=5)
    btn_green_filter.pack(pady=5)
    btn_blue_filter.pack(pady=5)
    btn_rotate_image.pack(pady=5)
    shrink_frame.pack(pady=5)
    shrink_label.pack(side=tk.LEFT)
    input_shrink.pack(side=tk.LEFT, padx=(8, 0))
    btn_shrink_image.pack(pady=5)

    return root
