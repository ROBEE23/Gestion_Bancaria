# Gestion_Bancaria
Sistema Bancario en Consola (POO)  Este proyecto es una aplicación CLI (Interfaz de Línea de Comandos) desarrollada en Python que simula la gestión básica de un sistema bancario. 
Texto para la Descripción de GitHub (About / README.md)
Si necesitas el texto descriptivo directo para pegarlo en la sección About de tu repositorio de GitHub o al inicio del archivo README.md, puedes usar la siguiente ficha:

Descripción corta (About):
CLI bancario desarrollado en Python orientado a objetos con operaciones financieras básicas y persistencia de datos en JSON.

Descripción extendida (README):
Sistema bancario de consola desarrollado en Python aplicando principios de Programación Orientada a Objetos (POO). El proyecto permite a los usuarios aperturar cuentas, consultar saldos, realizar depósitos, retirar dinero y efectuar transferencias entre cuentas activas de forma segura. La aplicación almacena el estado de las cuentas localmente en formato JSON, garantizando la persistencia de los datos sin depender de bases de datos externas.
# Bank System CLI

Simulador de operaciones bancarias mediante línea de comandos implementado en Python utilizando Programación Orientada a Objetos (POO).
Justificación

El desarrollo de este sistema de Gestión Bancaria surge de la necesidad de aplicar los principios de la Programación Orientada a Objetos (POO) en un escenario práctico del mundo real. La administración de cuentas y transacciones financieras exige un control riguroso de la información, donde la encapsulación y el modelado correcto de entidades son fundamentales para evitar inconsistencias en los saldos. Asimismo, la implementación de un mecanismo de persistencia local mediante archivos JSON resuelve el problema de la pérdida de datos al cerrar la aplicación, ofreciendo una solución ligera y funcional sin la complejidad inicial de desplegar un gestor de bases de datos completo. Este proyecto sienta las bases arquitectónicas para futuras migraciones hacia interfaces gráficas o bases de datos relacionales.

Metodología

Para el desarrollo del proyecto se empleó una metodología iterativa dividida en las siguientes fases:

Análisis y Modelado de Clases:
Se identificaron los requerimientos del sistema y se diseñaron las entidades principales (Cliente, CuentaBancaria, Banco), definiendo sus atributos, métodos operativos (depósitos, retiros, transferencias) y modificadores de acceso.

Implementación de la Lógica de Negocio:
Se codificaron las clases en Python, estableciendo las validaciones necesarias para garantizar que las operaciones financieras respeten las reglas del sistema (por ejemplo, saldo suficiente antes de realizar un retiro).

Desarrollo del Módulo de Persistencia:
Se integraron las funciones de lectura y escritura en formato JSON para serializar los objetos de las clases a diccionarios y deserializarlos al iniciar la aplicación.

Construcción de la Interfaz y Pruebas:
Se implementó una interfaz de consola con menús interactivos para que el usuario navegue entre las opciones disponibles. Finalmente, se realizaron pruebas de entrada de datos y manejo de excepciones para corregir fallos en la ejecición.
## Características
- Generación de números de cuenta aleatorios de 5 dígitos.
- Depósitos, retiros y transferencias entre cuentas activas.
- Persistencia de datos local en formato JSON.

## Requisitos
- Python 3.8+

## Ejecución
```bash
python main.py
