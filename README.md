# TraductorAzure

## Descripción

Esta es una aplicación web simple construida con Flask que utiliza la API de Microsoft Translator para traducir texto de un idioma a otro. La aplicación permite a los usuarios ingresar texto en un idioma y recibir una traducción en el idioma seleccionado.

## Tecnologías Utilizadas

- **Flask**: Framework web para Python.
- **Bootstrap**: Framework CSS para el diseño responsivo.
- **Microsoft Translator API**: Servicio de traducción de texto.
- **Python-dotenv**: Para gestionar variables de entorno.

## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```

2. **Navega al directorio del proyecto**:

    ```bash
    cd tu-repositorio
    ```

3. **Crea un entorno virtual**:

    ```bash
    python -m venv venv
    ```

4. **Activa el entorno virtual**:

    - En Windows:

      ```bash
      venv\Scripts\activate
      ```

    - En macOS y Linux:

      ```bash
      source venv/bin/activate
      ```

5. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

6. **Configura las variables de entorno**:

    Crea un archivo `.env` en la raíz del proyecto y agrega tus credenciales de la API:

    ```plaintext
    KEY=tu_clave_de_suscripción
    ENDPOINT=https://api.cognitive.microsofttranslator.com/
    LOCATION=tu_ubicación
    ```

7. **Ejecuta la aplicación**:

    ```bash
    python app.py
    ```

8. **Abre tu navegador y ve a**: `http://127.0.0.1:5000/`

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación Flask.
- `templates/`: Carpeta que contiene los archivos HTML.
- `static/`: Carpeta para archivos estáticos como CSS y JavaScript.
- `.env`: Archivo para las variables de entorno (no subas este archivo a GitHub).

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu característica: `git checkout -b mi-nueva-caracteristica`.
3. Haz commit de tus cambios: `git commit -am 'Añadir nueva característica'`.
4. Envía tus cambios a tu fork: `git push origin mi-nueva-caracteristica`.
5. Crea un pull request en el repositorio original.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.


