import flet as ft

def main(page: ft.Page):
    txt_firts_name=ft.TextField(hint_text="Nombre")
    txt_last_name=ft.TextField(hint_text="Apellido")
    
    #Propiedad disable Individual
    # txt_firts_name.disabled=True
    # txt_last_name.disabled=True

    col_controles=ft.Column(controls=([txt_firts_name,txt_last_name]))

    #Propiedad disable grupo
    col_controles.disabled=True
    
    page.add(col_controles)

ft.app(target=main)