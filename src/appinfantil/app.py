"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.widgets import widgets
from toga import togaui

import cv2

import zbarlight 
from PIL import Image
from PIL io import BytesIO


class Appinfantil(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = widgets.Box(children=[boton_estudiante, boton_profesor])
        self.main_window.show()
        # Crear botones de login
        # Agregar botones a la ventana principal
        boton_estudiante = widgets.Button('Estudiante', on_press=self.mostrar_ventana_login)
        boton_profesor = widgets.Button('Profesor', on_press=self.mostrar_ventana_login)

        # Mostrar la ventana principal
        self.main_window.show()
#------------------------------------------------------------
#------------------------------------------------------------
def mostrar_ventana_login(self, widget):
    # Crear la ventana de login
    ventana_login = togaui.MainWindow(title="Login")

    # Crear campos de texto para correo y contraseña
    campo_correo = widgets.TextInput(placeholder='Correo electrónico')
    campo_contraseña = widgets.PasswordInput(placeholder='Contraseña')

    # Crear botón de inicio de sesión
    boton_iniciar_sesion = widgets.Button('Iniciar sesión', on_press=self.login)

    # Agregar campos de texto y botón a la ventana de login
    ventana_login.content = widgets.Box(
        children=[campo_correo, campo_contraseña, boton_iniciar_sesion]
    )
     # Mostrar la ventana de login
    ventana_login.show()
#------------------------------------------------------------
#------------------------------------------------------------
def login(self, widget, campo_correo, campo_contraseña):
        # obtener los valores de los campos de texto
        email = campo_correo.value
        password = campo_contraseña.value

        # logica de autenticación
        if self.authenticacion(email, password):
            self.show_iniciar_sesion()
        else:
            self.show_error()
#------------------------------------------------------------
#------------------------------------------------------------
def authenticacion(self, email, password):
        # placeholder para los usuarios registrados
        users = {
            'user1@example.com': 'password1',
            'user2@example.com': 'password2',
            'user3@example.com': 'password3',
        }

        # verificar si el usuario existe y la contraseña es correcta
        if email in users and users[email] == password:
            return True
        else:
            return False
#------------------------------------------------------------
#------------------------------------------------------------
def show_error(self):
        # cear un mensaje de error
        dialog = togaui.MessageBox(
            title="Error de incio de sesion",
            message="Email no valido o contraseña incorrecta :C."
        )
        dialog.show()
#------------------------------------------------------------
#------------------------------------------------------------
def iniciar_sesion(self, widget):
        # Verificar el correo y contraseña ingresados
        # Redirigir al usuario a la ventana principal o mostrar mensaje de error
        
        # Ejemplo de redirección a la ventana principal
        main_window = togaui.MainWindow(title="App Infantil")

        # Crear etiqueta de bienvenida con el nombre del usuario
        etiqueta_bienvenida = widgets.Label("¡Hola, Nombre Apellido!")

        # Crear botones QR y Colección
        boton_qr = widgets.Button('QR', on_press=self.mostrar_ventana_qr)
        boton_coleccion = widgets.Button('Colección', on_press=self.mostrar_ventana_coleccion)

        # Crear botón de cerrar sesión
        boton_cerrar_sesion = widgets.Button('Cerrar sesión', on_press=self.cerrar_sesion)

        # Agregar elementos a la ventana principal
        main_window.content = widgets.Box(
            children=[etiqueta_bienvenida, boton_qr, boton_coleccion, boton_cerrar_sesion]
        )

        # Mostrar la ventana principal
        main_window.show()
#------------------------------------------------------------
#------------------------------------------------------------
def leer_codigos_qr(self, widget,carousel):
        # Acceder a la cámara para capturar imágenes
        # Esto puede variar dependiendo de la plataforma y las bibliotecas utilizadas
        # Aquí se muestra un ejemplo utilizando la biblioteca OpenCV
        

        # Inicializar el capturador de video
        cap = cv2.VideoCapture(0)

        qr_contents = []
        qr_count = 0

        while qr_count < 5:
            # Leer el cuadro actual del video
            ret, frame = cap.read()

            # Convertir la imagen en formato PIL
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Escanear los códigos QR presentes en la imagen
            codes = zbarlight.scan_codes('qrcode', pil_image)

            if codes:
                qr_contents.extend(codes)
                qr_count += 1

        # Liberar los recursos de la cámara
        cap.release()

def mostrar_Carrusel(self, widget,carousel,qr_contents):
        # Mostrar el contenido de los códigos QR
        for content in qr_contents:
            carousel.content = widgets.Box(children=qr_contents)
            label = widgets.Label(content)
            mostrar_ventana_carrusel.content.add(label)

        # Mostrar la ventana de resultados
        carousel.show()
#------------------------------------------------------------
#------------------------------------------------------------
def mostrar_ventana_qr(self, widget):
        # Crear la ventana para leer códigos QR
        ventana_qr = togaui.MainWindow(title="Lectura de QR")

        # Crear botón de leer QR
        boton_leer = widgets.Button('Leer QR', on_press=self.leer_codigos_qr)
        
        # ...

        # Crear botón de enviar
        boton_enviar = widgets.Button('Enviar', on_press=self.mostar_Carrusel)

        # Crear botón de volver
        boton_volver = widgets.Button('Volver', on_press=self.volver_a_ventana_principal)

        # Agregar botones a la ventana QR
        ventana_qr.content = widgets.Box(children=[boton_enviar, boton_volver, boton_leer])

        # Mostrar la ventana QR
        ventana_qr.show()
#------------------------------------------------------------
#------------------------------------------------------------
def mostrar_ventana_carrusel(self, widget):
        # Crear la ventana de carrusel para mostrar los datos de los códigos QR
        ventana_carrusel = togaui.MainWindow(title="Carrusel de QR")

        # Lógica para mostrar los datos de los códigos QR en forma de carrusel
        carousel = widgets.ScrollContainer(horizontal=False)
        # ...

        # Mostrar la ventana de carrusel
        ventana_carrusel.show()
#------------------------------------------------------------
#------------------------------------------------------------
def mostrar_ventana_coleccion(self, widget):
        # Crear la ventana de colección de códigos QR
        ventana_coleccion = togaui.MainWindow(title="Colección de QR")

        #placeholder
        qr_codes = [
            {'code': 'qr_code_1', 'theme': 'Theme 1'},
            {'code': 'qr_code_2', 'theme': 'Theme 2'},
            {'code': 'qr_code_3', 'theme': 'Theme 1'},
            {'code': 'qr_code_4', 'theme': 'Theme 3'},
            {'code': 'qr_code_5', 'theme': 'Theme 2'},
        ]

        # Lógica para mostrar la colección de códigos QR
        codigos_qr_por_tema = self.organiza_codigos_qr_por_tema(qr_codes)#esto de la base de datos
        #fin placeholder
        # crear una seccion donde se muestren los codigos qr por tema
        theme_box = widgets.Box()

        # crear una seccion donde se guarden los botones
        qr_box = widgets.Box()

        # Crear un botón por cada tema
        for theme in codigos_qr_por_tema.keys():
            button = widgets.Button(theme, on_press=self.show_qr_codes, args=(codigos_qr_por_tema[theme], qr_box))
            theme_box.add(button)

        # añadir los temas y botones a la ventana
        ventana_coleccion.content = widgets.Box(
            children=[theme_box, qr_box],
            style=Pack(direction=COLUMN)
        )
        # ...

        # Crear botón de volver
        boton_volver = widgets.Button('Volver', on_press=self.volver_a_ventana_principal)

        # Agregar botón a la ventana de colección
        ventana_coleccion.content = widgets.Box(children=[boton_volver])

        # Mostrar la ventana de colección
        ventana_coleccion.show()
#------------------------------------------------------------
#------------------------------------------------------------
def cerrar_sesion(self, widget):
        # Lógica para cerrar la sesión del usuario
        # ...

        # Regresar a la ventana de login
        self.mostrar_ventana_login(None)

#------------------------------------------------------------
#------------------------------------------------------------
def volver_a_ventana_principal(self, widget):
    # Volver a la ventana principal
    self.startup()
#------------------------------------------------------------
#------------------------------------------------------------
def cerrar_sesion(self, widget):
        # Lógica para cerrar la sesión del usuario
        # ...

        # Regresar a la ventana de login
        self.mostrar_ventana_login(None)
#------------------------------------------------------------
#------------------------------------------------------------
def volver_a_ventana_principal(self, widget):
    # Volver a la ventana principal
    self.startup()
#------------------------------------------------------------
#------------------------------------------------------------
def main():
    return Appinfantil()


if __name__ == '__main__':
    main().main_loop()