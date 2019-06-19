# Protipo 2
Este es el segundo protipo de mis horas sociales.

## El objetivo principal es la recoleccion de los siguientes datos:
```
1. Dioxido de carbono Co2 (Principal)
2. Radon lectura por Camara
```

Y guardarlos en una base de datos Postgres 9.6 alpine con docker.
Tambien cumplir con la funcion de exponer los datos por medio de la web usando php con docker.

## Componentes
1. Raspberry Pi 3 Model B
2. Camara USB
3. ADS115 I2C
4. Accelerometer Salidas Analogas
4. Otros componentes comunes

## ¿Como recolectar los datos?
Para lograr las lecturas de Dioxido de carbono y accelerometer se utilizaran entradas analogas del
ADS115 que seran enviadas por I2C atraves de Python

Para obtener lecturas de Radon utilizaremos Python para determinar los pixeles que estan activos
en la captura de la camara, se utilizaran filtros de blanco y negro

Todos registro de datos se guardaran cada minuto en la base de datos
(Lo ideal seria guardar los datos si se detecta radon)

## ¿Como exponer los datos?
Los datos se mostraran en el puerto 80 con la ip definida, aun estaran pendientes cuestiones de
seguridad del servidor con php

## Software
```
apt install python3-pip
pip install opencv-python
```
