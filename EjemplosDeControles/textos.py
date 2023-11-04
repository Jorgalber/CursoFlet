import flet as ft

def main(page:ft.Page):
    Labeltexto=ft.Text(value="¡Hola, mundo!", color="red")
    page.controls.append(Labeltexto)
    page.update()

#ft.app(target=main,view=ft.AppView.WEB_BROWSER, port=1818)

ft.app(target=main)