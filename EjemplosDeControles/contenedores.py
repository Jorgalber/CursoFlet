import flet as ft

def main(page:ft.Page):
    ##datos=ft.Row(controls=[ft.Text("A"),ft.Text("B"),ft.Text("C"),ft.Text("D")])
    lista=["A","B","C","D"]
    etiquetas=[]

    for i in lista:
        etiquetas.append(ft.Text(i))
    datos=ft.Row(controls=etiquetas)
    page.add(datos)

ft.app(target=main)