#profe sorry que lo subi late, yo estaba enferma y me mandaron a mi casa desde el miercoles y el lunes también.
import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#000000"
    page.title = "Mixer"

    def update_color(e):
        rojo = int(rojo_slider.value)
        verde = int(verde_slider.value)
        azul = int(azul_slider.value)
        hex_color = f"#{rojo:02x}{verde:02x}{azul:02x}"
        page.bgcolor = hex_color
        rgb_text.value = f"RGB: ({rojo}, {verde}, {azul})"
        hex_text.value = f"Hex: {hex_color.upper()}"
        page.update()

    rojo_slider = ft.Slider(min=0, max=255, value=0, label="Rojo", on_change=update_color)
    verde_slider = ft.Slider(min=0, max=255, value=0, label="Verde", on_change=update_color)
    azul_slider = ft.Slider(min=0, max=255, value=0, label="Azul", on_change=update_color)

    rgb_text = ft.Text(value="RGB: (0, 0, 0)", size=20)
    hex_text = ft.Text(value="Hex: #000000", size=20)

    page.add(
        rojo_slider,
        verde_slider,
        azul_slider,
        rgb_text,
        hex_text
    )

ft.app(target=main)
   