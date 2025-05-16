🌐 Proyecto Web Empresarial con Django
Este es mi segundo proyecto - web empresarial - realizado con Python y Django, inspirado en el curso de Hektor Profe. El objetivo principal es crear una web para una empresa que permita gestionar servicios, páginas estáticas, blogs y formularios de contacto, integrando un frontend personalizado y un backend robusto con Django.

🛠 Tecnologías utilizadas
Python 3.11

Django 5.2.1

HTML, CSS, JavaScript básico (adaptación del frontend empresarial)

Virtualenv / Pipenv (gestión de entorno virtual)

SQLite3 (base de datos por defecto, fácil para desarrollo)

Visual Studio Code

📦 Instalación y ejecución del entorno
Clona el repositorio y entra a la carpeta raíz del proyecto:

bash
Copiar
Editar
git clone https://github.com/tu_usuario/tu_repositorio_web_empresarial.git
cd tu_repositorio_web_empresarial
Activa el entorno virtual con pipenv:

bash
Copiar
Editar
pipenv install
pipenv shell
Ejecuta el servidor de desarrollo de Django:

bash
Copiar
Editar
python manage.py runserver
Accede en tu navegador a http://127.0.0.1:8000 para ver la página web empresarial funcionando.

🔑 Conceptos aplicados
✅ Entorno virtual
Gestiono el proyecto con Pipenv para aislar dependencias y controlar versiones con Pipfile y Pipfile.lock.

✅ Estructura del proyecto
webempresa/ contiene el proyecto Django principal.

core/ aplicación principal para manejar las vistas, modelos y rutas de la empresa.

servicios/ aplicación para la gestión del catálogo de servicios.

pages/ para páginas estáticas como inicio, acerca de, contacto.

blog/ para gestionar entradas de blog si se requiere.

templates/ contiene las plantillas HTML basadas en el frontend adaptado del proyecto de Hektor Profe.

static/ recursos estáticos como CSS, JS e imágenes del frontend.

✅ Integración Frontend y Backend
Adapté un frontend empresarial pre-diseñado para que se integre con Django usando plantillas con herencia ({% extends "base.html" %}), y vistas que envían el contexto dinámico para mostrar servicios, posts y datos de contacto.

✅ Modelos y administración
Se crearon modelos para Servicios, Páginas, Entradas de blog y Contactos, con campos específicos y opciones para administración fácil desde el panel de Django Admin.

✅ Formularios y contacto
Implementé formularios para la sección de contacto que permiten enviar mensajes, validación básica y guardado en base de datos o envío por correo electrónico (opcional).

✅ Rutas y vistas
Uso de path() y vistas basadas en funciones o clases para manejar las diferentes secciones de la web:

/ → Página principal con servicios destacados.

/servicios/ → Listado de servicios.

/blog/ → Blog empresarial.

/contacto/ → Formulario de contacto.

/acerca-de/ → Página estática sobre la empresa.

✅ Migraciones y gestión de base de datos
Uso de comandos fundamentales para crear y aplicar migraciones:

bash
Copiar
Editar
python manage.py makemigrations
python manage.py migrate
📚 Conocimientos adquiridos
Integración completa de un frontend empresarial adaptado con Django.

Uso avanzado de plantillas, herencia y bloques para reutilizar código HTML.

Configuración y personalización del panel administrativo para gestionar contenido dinámico.

Creación de formularios con validación y envío de datos.

Uso de rutas y vistas para construir una experiencia web empresarial coherente y funcional.

🎯 Objetivo
El objetivo de este proyecto es desarrollar una web empresarial profesional usando Django, que sea funcional, escalable y fácil de gestionar, además de aprender buenas prácticas para combinar frontend con backend de forma efectiva.

💬 Comentarios
Este proyecto me ha permitido avanzar mucho en el manejo de Django para aplicaciones reales de negocio, entendiendo la arquitectura de aplicaciones, gestión de datos y creación de interfaces web limpias y funcionales.

🔗 Recursos útiles
Proyecto Web Empresarial - Hektor Profe

Documentación oficial de Django

Bootstrap para diseño frontend

🧠 Autor
Mauro Lafuente
Estudiante de desarrollo web y backend