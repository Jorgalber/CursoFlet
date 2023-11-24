import flet as ft

def main(page: ft.Page):
    btn_accion=ft.ElevatedButton("¡Click!")
    page.add(btn_accion)

ft.app(target=main,view=ft.WEB_BROWSER)