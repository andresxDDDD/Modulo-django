# Modulo-django
DESARROLLO DE APLICACIONES WEB CON PYTHON DJANGO
🚀 Guía de Instalación: Django 6.2Este documento detalla el proceso paso a paso para configurar un entorno de desarrollo profesional con Django 6.2.📋 Requisitos PreviosAntes de comenzar, asegúrate de tener instalado:Python 3.10 o superior (Django 6.x requiere versiones recientes de Python).Pip (Gestor de paquetes de Python).🛠️ Paso 1: Configuración del Entorno VirtualEl entorno virtual es una herramienta que crea un espacio aislado para tu proyecto. Esto evita conflictos entre las versiones de las librerías de diferentes proyectos.Crear el entorno:Bashpython -m venv venv

¿Para qué sirve? venv crea una carpeta llamada "venv" que contendrá una copia propia de Python y de pip.Activar el entorno:Windows: .\venv\Scripts\activateMac/Linux: source venv/bin/activate📦 Paso 2: Instalación de LibreríasHe preparado una lista de dependencias esenciales para un inicio profesional.Archivo requirements.txtCrea un archivo llamado requirements.txt en la raíz de tu carpeta y pega lo siguiente:Plaintext# Framework Principal
Django==6.2

# Utilidades
python-dotenv==1.0.1  # Manejo de variables de entorno (seguridad)
pillow==10.2.0        # Manejo de imágenes
psycopg2-binary==2.9.9 # Driver para bases de datos PostgreSQL (opcional)
Ejecutar la instalaciónCon el entorno virtual activado, ejecuta:Bashpip install -r requirements.txt
🏗️ Paso 3: Inicialización del Proyecto DjangoAhora que las librerías están instaladas, crearemos la estructura base del sitio.Crear el proyecto:Bashdjango-admin startproject config .
(El punto . al final evita que Django cree una subcarpeta innecesaria).Ejecutar migraciones iniciales:Bashpython manage.py migrate
¿Para qué sirve? Crea las tablas necesarias en la base de datos (por defecto SQLite) para el sistema de usuarios y administración de Django.Crear un Superusuario:Bashpython manage.py createsuperuser
🖥️ Paso 4: Verificación y UsoPara encender el servidor de desarrollo, ejecuta:Bashpython manage.py runserver
URL del sitio: http://127.0.0.1:8000/Panel de Administración: http://127.0.0.1:8000/admin/📂 Glosario de Archivos GeneradosArchivoFunciónmanage.pyLa navaja suiza. Sirve para correr el servidor, crear bases de datos y ejecutar comandos.settings.pyEl corazón del proyecto. Aquí configuras la base de datos, zona horaria y apps instaladas.urls.pyEl mapa de navegación. Define a qué parte del código va el usuario según la URL que escriba.wsgi.py / asgi.pyConfiguración para que tu proyecto pueda "hablar" con servidores web reales cuando lo subas a internet.