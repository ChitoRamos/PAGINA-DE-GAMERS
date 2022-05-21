#!/usr/bin/env python
"""
This script runs the python_webapp_flask application using a development server.
"""
# -*- coding: utf-8 -*-
from os import environ
import Gamersapp

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    Gamersapp.app.run(HOST, PORT, debug = True) # Establecer en 'False' al trabajar en producción
