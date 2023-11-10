import flet as ft

def main(page: ft.Page):
    def agregar_tareas(e):
        page.add(ft.Checkbox(label=txt_nueva_tarea.value))
    
    txt_nueva_tarea = ft.TextField(hint_text="Nueva tarea",width=300)

    btn_agregar=ft.ElevatedButton("Agregar",on_click=agregar_tareas)

    page.add(ft.Row([txt_nueva_tarea, btn_agregar]))

ft.app(target=main)