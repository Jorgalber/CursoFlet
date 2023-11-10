import flet as ft

def main(page:ft.Page):
    firts_name= ft.TextField(label="Nombre", autofocus=True)
    last_name= ft.TextField(label="Apellido")
    col_controles=ft.Column()

    def saludar_clicked(e):
        col_controles.controls.append(ft.Text(f"Hola, {firts_name.value} {last_name.value}!"))
        
        firts_name.value=""
        last_name.value=""
        
        page.update()
        firts_name.focus()

    btn_saludar= ft.ElevatedButton("Saludar",on_click=saludar_clicked)

    page.add(
        firts_name,
        last_name,
        btn_saludar,
        col_controles
    )
ft.app(target=main)