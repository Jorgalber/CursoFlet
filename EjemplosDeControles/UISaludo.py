import flet as ft


def main(page: ft.Page):
    txtNombre=ft.TextField(label="Escribe tu nombre")
    lbl_saludo=ft.Text()
    
    def Saludar(event):
        ##print("Hola " + txtNombre.value)
        lbl_saludo.value="Hola " + txtNombre.value
        page.update()
    
    row=ft.Row(controls=[
        txtNombre,
        ft.ElevatedButton(text="Saludo", on_click=Saludar),
        lbl_saludo

    ])
    page.add(row)

ft.app(target=main)