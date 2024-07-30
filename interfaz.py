import flet as ft

def main(page: ft.Page):
    # Crear los controles de la interfaz
    page.title = "Calculadora de Promedio de Notas"
    
    # Contenedor principal
    container = ft.Column(
        controls=[
            ft.TextField(
                label="Ingrese la nota 1",
                id="nota1",
                keyboard_type=ft.KeyboardType.NUMBER
            ),
            ft.TextField(
                label="Ingrese la nota 2",
                id="nota2",
                keyboard_type=ft.KeyboardType.NUMBER
            ),
            ft.TextField(
                label="Ingrese la nota 3",
                id="nota3",
                keyboard_type=ft.KeyboardType.NUMBER
            ),
            ft.ElevatedButton(text="Calcular Promedio", on_click=calcular_promedio),
            ft.Text(id="resultado", size=20)
        ]
    )
    
    # Añadir el contenedor a la página
    page.add(container)

def calcular_promedio(event: ft.Event):
    # Obtener las notas desde los campos de texto
    nota1 = page.get_control("nota1").value
    nota2 = page.get_control("nota2").value
    nota3 = page.get_control("nota3").value
    
    try:
        # Convertir las notas a flotantes y calcular el promedio
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)
        
        promedio = (nota1 + nota2 + nota3) / 3
        resultado = f"El promedio es: {promedio:.2f}"
    except ValueError:
        resultado = "Por favor ingrese valores válidos en todos los campos."
    
    # Mostrar el resultado en el control de texto
    page.get_control("resultado").value = resultado
    page.update()

# Ejecutar la aplicación
ft.app(target=main)
