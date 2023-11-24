import flet as ft

def main(page: ft.Page):
    page.title='Contador'
    page.vertical_alignment="center"
    page.horizontal_alignment="center"

    txt_number=ft.TextField(value="0",text_align="right",width=100)

    def minus_click(e):
        txt_number.value=int(txt_number.value)-1
        page.update()
    def plus_click(e):
        txt_number.value=int(txt_number.value)+1
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE,
                on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD,
                on_click=plus_click)
            ], alignment="center",
        )
    )
#Modo escritorio
ft.app(target=main)