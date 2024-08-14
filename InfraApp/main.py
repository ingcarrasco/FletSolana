import flet as ft

def main(page: ft.Page):
    page.title = 'InfraApp x'    
    def login_clicked(e):
        username = username_field.value
        password = password_field.value

        # Aquí va tu lógica de validación
        if username == "admin" and password == "password":
            page.add(ft.Text("¡Inicio de sesión exitoso!"))
        else:
            page.add(ft.Text("Nombre de usuario o contraseña incorrectos."))

    username_field = ft.TextField(label="Nombre de usuario")
    password_field = ft.TextField(label="Contraseña", password=True)
    login_button = ft.ElevatedButton("Iniciar sesión", on_click=login_clicked)

    # Creamos un Column para organizar los elementos verticalmente
    column = ft.Column(
        controls=[
            username_field,
            password_field,
            login_button
        ],width=300,
        alignment=ft.MainAxisAlignment.CENTER,  # Centramos verticalmente
        expand = True  # Hace que el Column ocupe todo el espacio disponible
    )
    
    # Creamos un Row para organizar el Column horizontalmente
    row = ft.Row(
        controls=[
            column
        ],
        alignment=ft.CrossAxisAlignment.CENTER,  # Centramos horizontalmente
        expand=True
    )



    page.add(row)

ft.app(main)
