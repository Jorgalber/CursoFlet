import flet as ft

def main(page: ft.Page):
    lbl_texto=ft.Text(
        value="Flet",
        size=30,
        color="white",
        bgcolor="blue",
        weight="bold",
        italic=True,
    )
    page.add(lbl_texto)

ft.app(target=main)