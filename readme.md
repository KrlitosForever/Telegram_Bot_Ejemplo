# <p align="center"> Telegram Bot Ejemplo </p>

[![🚀 Deploy Server](https://github.com/KrlitosForever/Telegram_Bot_Ejemplo/actions/workflows/master.yml/badge.svg)](https://github.com/KrlitosForever/Telegram_Bot_Ejemplo/actions/workflows/master.yml)

<p align="center">Bot de Telegram destinado a ser una guía a todos aquellos que están aprendido a utilizar la librería telebot.

* [Pasos previos.](#pasos-previos)
* [Instalación pyTelegramBotAPI.](#Instalación-pyTelegramBotAPI)
* [Carga archivo.](#carga-archivo)
* [Ejecutar archivo.](#ejecutar-archivo)
* [Interacción con el Bot.](#Interacción-con-el-Bot)

## Pasos previos

Lo primero es tener una cuenta de telegram. Una vez tengamos nuestra cuenta debemos buscar a @BotFather a quien le pediremos crear un nuevo bot (/newbot). Posterior a eso debemos ingresar la información que nos solicita para poder crearlo.

## Instalación pyTelegramBotAPI

Todos los pasos de instalación de este repositorio se encuentran en el siguiente enlace:
[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI.git)

## Carga archivo

Una vez clonado el repositorio de [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI.git) debemos situarnos dentro de la carpeta y copiar el archivo **BotExample.py**

## Ejecutar archivo

Para ejecutar el archivo debemos ejecutar la siguiente instrucción en la terminal:

```python
python3 BotExample.py
```

Si todo a salido de manera correcta nuestro bot estaría corriendo y debería poder ejecutar las funciones creadas como las que se muestran a continuación.

* message - Esta función envía un mensaje
* document - Esta función envía un documento
* contact - Esta función envia un contacto
* audio - Esta función envía un audio
* location - Esta función envía una ubicación
* image - Esta función envía una foto
* video - Esta función envia un video

## Interacción con el Bot

Para poder interactuar con el bot debes buscarlo en telegram **@Chile_telebot**
![chile_telebot](https://github.com/user-attachments/assets/1b6ce059-4517-4246-b35a-43b255df1eed)

# ¡Crea tu propio Bot de Telegram! 🤖✨

¡Hola! Hoy te traigo una guía divertida y sencilla para crear tu propio bot de Telegram utilizando Python. A lo largo de este post, te explicaré cada función de nuestro archivo `botExample.py`, desde la instalación de las librerías necesarias hasta cómo utilizar cada función del bot. ¡Vamos a ello! 🚀

## Instalación de librerías 📦

Antes de comenzar, asegúrate de tener Python instalado en tu máquina. Luego, necesitarás instalar la librería `pyTelegramBotAPI`. Puedes hacerlo ejecutando el siguiente comando en tu terminal:

```bash
pip install pyTelegramBotAPI
```

## Configuración inicial 🔧

Para que nuestro bot funcione, necesitarás un token de API que puedes obtener creando un bot a través de [BotFather](https://core.telegram.org/bots#botfather) en Telegram. Una vez que tengas tu token, guárdalo en un archivo llamado `keys.py` de la siguiente manera:

```python
API_TOKEN = 'TU_TOKEN_AQUÍ'
```

## Función Global: Formatear Moneda 💰

La primera función que vamos a ver es `format_currency`. Esta función se encarga de formatear valores monetarios según el estándar chileno.

```python
def format_currency(value):
    return locale.currency(value, grouping=True)
```

**Uso:** Puedes llamar a esta función pasando un número como argumento, y te devolverá el valor formateado. 

## Función de Inicio: /start 🎉

La función `send_welcome` se activa cuando un usuario inicia el bot con el comando `/start`. Aquí le damos la bienvenida y le mostramos las opciones disponibles.

```python
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Hola, soy un 🤖 de Ejemplo.\nPuedes preguntar lo siguiente:⬇️\n/info\nPara conocer las funciones de este bot"
    )
```

## Función de Información: /info 📜

La función `info` proporciona una lista de comandos que el bot puede manejar. Cuando el usuario envía `/info`, recibe un resumen de las funcionalidades.

```python
@bot.message_handler(commands=["info"])
def info(message):
    bot.send_message(
        message.chat.id,
        "/message\nEsta función envía un mensaje\n/document\nEsta función envía un documento\n/contact\nEsta función envía un contacto\n/audio\nEsta función envía un audio\n/location\nEsta función envía una ubicación\n/image\nEsta función envía una foto\n/video\nEsta función envía un video"
    )
```

## Función de Mensaje: /message 💬

La función `mensaje` permite al bot enviar un mensaje simple al usuario. Si todo sale bien, el bot confirmará que la acción se realizó con éxito.

```python
@bot.message_handler(commands=["message"])
def mensaje(message):
    try:
        bot.send_message(message.chat.id, "Hola 👋 este es un ejemplo de mensaje")
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el documento: {str(e)}")
```

## Función de Documento: /document 📄

Con la función `documento`, el bot puede enviar un archivo que hayas especificado. Asegúrate de tener el archivo en la ruta correcta.

```python
@bot.message_handler(commands=["document"])
def documento(message):
    try:
        with open(keys.PATH_DOCUMENT, "rb") as documento:
            bot.send_document(message.chat.id, documento)
            bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el documento: {str(e)}")
```

## Función de Contacto: /contact 📞

La función `contacto` permite enviar un contacto específico. Puedes personalizar el nombre y el número de teléfono.

```python
@bot.message_handler(commands=["contact"])
def contacto(message):
    try:
        carlos = "Carlos Carrasco"
        numero_carlos = "+123456789"
        bot.send_contact(message.chat.id, numero_carlos, first_name=carlos)
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el documento: {str(e)}")
```

### Función de Audio: /audio 🎵

La función `audio` envía un archivo de audio en formato M4A. Asegúrate de tener el archivo disponible en la ruta especificada.

```python
@bot.message_handler(commands=["audio"])
def audio(message):
    try:
        bot.send_audio(message.chat.id, open(keys.PATH_AUDIO, "rb"))
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el audio: {str(e)}")
```

## Función de Ubicación: /location 📍

La función `location` permite enviar la ubicación geográfica. En este ejemplo, se ha fijado una ubicación específica en Santiago, Chile.

```python
@bot.message_handler(commands=["location"])
def location(message):
    try:
        latitude = -33.43768005616671
        longitude = -70.65051265006004
        bot.send_location(message.chat.id, latitude, longitude)
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar la ubicación: {str(e)}")
```

## Función de Imagen: /image 🖼️

La función `imagen` permite al bot enviar una foto. Asegúrate de tener la imagen en la ruta correcta.

```python
@bot.message_handler(commands=["image"])
def imagen(message):
    try:
        with open(keys.PATH_IMAGE, "rb") as imagen:
            bot.send_photo(message.chat.id, imagen)
            bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el documento: {str(e)}")
```

## Función de Video: /video 🎥

Finalmente, la función `video` permite enviar un archivo de video. Asegúrate de que el archivo esté disponible en la ruta especificada.

```python
@bot.message_handler(commands=["video"])
def video(message):
    try:
        bot.send_video(message.chat.id, open(keys.PATH_VIDEO, "rb"))
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el video: {str(e)}")
```

## Conclusión 🎊

¡Y eso es todo! Ahora tienes un bot de Telegram funcional que puede enviar mensajes, documentos, contactos, audios, ubicaciones, imágenes y videos. No dudes en personalizarlo y agregar más funcionalidades. ¡Diviértete programando! 🎉

Si quieres ver el código completo, puedes encontrarlo en el siguiente repositorio de GitHub: [https://github.com/KrlitosForever/Telegram_Bot_Ejemplo](https://github.com/KrlitosForever/Telegram_Bot_Ejemplo)
