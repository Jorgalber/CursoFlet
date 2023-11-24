import flet as ft

def main(page:ft.Page):
    firts_name= ft.Ref[ft.TextField]()
    last_name= ft.Ref[ft.TextField]()
    col_controles=ft.Ref[ft.Column]()

    def saludar_clicked(e):
        col_controles.current.controls.append(ft.Text(f"Hola, {firts_name.current.value} {last_name.current.value}!"))
        
        firts_name.current.value=""
        last_name.current.value=""
        
        page.update()
        firts_name.focus()

    btn_saludar= ft.ElevatedButton("Saludar",on_click=saludar_clicked)

    page.add(
        ft.TextField(ref=firts_name, label="Nombre", autofocus=True),
        ft.TextField(ref=last_name,label="Apellido"),
        btn_saludar,
        ft.Column(ref=col_controles)
    )
ft.app(target=main)