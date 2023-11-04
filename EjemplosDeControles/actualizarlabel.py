import time
import flet as ft

def main(page:ft.Page):
    Lbltexto=ft.Text()
    page.add(Lbltexto)

    for i in range(11):
        Lbltexto.value=f"Paso {i}"
        page.update()
        time.sleep(1)
        if i==10:
            Lbltexto.value=f"Fin"
            page.update()

ft.app(target=main)