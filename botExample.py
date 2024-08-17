#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Author    : Carlos Carrasco
# Email     : mgtr.carloscarrasco@gmail.com
# Date      : Marzo 2024
#

# Librerías para el correcto funcionamiento.
# Libraries for proper functioning.
import telebot
from telebot.types import *
import keys
import locale


# Inicio de bot
# Bot startup
bot = telebot.TeleBot(keys.API_TOKEN)


# Configuración formato numérico de Chile
# Numeric format configuration for Chile
locale.setlocale(locale.LC_ALL, "es_CL.UTF-8")


# Función global
# Global Function
def format_currency(value):
    return locale.currency(value, grouping=True)


# Función que inicia el /Start
# Function that starts with command /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Hola, soy un 🤖 de Ejemplo.\nPuedes preguntar lo siguiente:⬇️\n/info\nPara conocer las funciones de este bot",
    )


# Función de información
# Information function
@bot.message_handler(commands=["info"])
def info(message):
    bot.send_message(
        message.chat.id,
        "/message\nEsta función envía un mensaje\n/document\nEsta función envía un documento\n/contact\nEsta función envía un contacto\n/audio\nEsta función envía un audio\n/location\nEsta función envía una ubicación\n/image\nEsta función envía una foto\n/video\nEsta función envía un video",
    )


# Función de mensaje
# Message function
@bot.message_handler(commands=["message"])
def mensaje(message):
    try:
        bot.send_message(message.chat.id, "Hola 👋 este es un ejemplo de mensaje")
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el documento: {str(e)}")


# Función de documento
# Document function
@bot.message_handler(commands=["document"])
def documento(message):
    try:
        with open(keys.PATH_DOCUMENT, "rb") as documento:
            bot.send_document(message.chat.id, documento)
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el documento: {str(e)}")


# Función de contacto
# Contact function
@bot.message_handler(commands=["contact"])
def contacto(message):
    try:
        carlos = "Carlos Carrasco"
        numero_carlos = "+123456789"
        bot.send_contact(message.chat.id, numero_carlos, first_name=carlos)
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el documento: {str(e)}")


# Función de audio
# Audio function
@bot.message_handler(commands=["audio"])
def audio(message):
    try:
        # Enviar el archivo de audio en formato M4A
        bot.send_audio(message.chat.id, open(keys.PATH_AUDIO, "rb"))
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el audio: {str(e)}")


# Función de ubicación
# Location function
@bot.message_handler(commands=["location"])
def location(message):
    try:
        latitude = -33.43768005616671
        longitude = -70.65051265006004

        bot.send_location(message.chat.id, latitude, longitude)
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar la ubicación: {str(e)}")


# Función de imagen
# Image function
@bot.message_handler(commands=["image"])
def imagen(message):
    try:
        with open(keys.PATH_IMAGE, "rb") as imagen:
            bot.send_photo(message.chat.id, imagen)
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el documento: {str(e)}")


# Función de video
# Video function
@bot.message_handler(commands=["video"])
def video(message):
    try:
        bot.send_video(message.chat.id, open(keys.PATH_VIDEO, "rb"))
        bot.send_message(message.chat.id, "Función realizada con éxito✅🎉🥳")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error al enviar el video: {str(e)}")


bot.infinity_polling()
