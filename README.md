# 🧮 Formulario con Validación – Proyecto en Python (Back-End)

**Formulario con Validación** es un proyecto desarrollado con **Python**, enfocado exclusivamente en la **lógica de validación de datos de formularios** usando la librería estándar **`re`** (expresiones regulares).  
Su objetivo es comprobar que los campos ingresados por el usuario (como nombre, email o contraseña) cumplan con los formatos correctos antes de ser procesados o almacenados.

---

## 🚀 Tecnologías utilizadas

- **Python 3.x** – Lenguaje principal  
- **Librería `re`** – Para la validación mediante expresiones regulares  
- 🧠 Proyecto de tipo **Back-End (lógica interna)**, sin interfaz visual  

---

## ⚙️ Instalación y ejecución

Sigue estos pasos para ejecutar el proyecto localmente:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Aaronisaias/Formulario-con-Validacion.git
Ingresa al directorio del proyecto:

cd Formulario-con-Validacion
Ejecuta el script principal:

python app.py
El programa mostrará en la terminal si los datos ingresados son válidos o inválidos, según las reglas definidas.

💡 Características principales
✅ Validación de nombre (solo letras y espacios).

📧 Validación de correo electrónico con formato correcto.

🔑 Validación de contraseña segura (mínimo de caracteres, mayúsculas, números, etc.).

🧾 Posibilidad de adaptar las expresiones regulares a diferentes tipos de formulario.

⚙️ Proyecto completamente en consola / back-end, ideal para aprender validación lógica.

🧱 Estructura del proyecto

📦 Formulario-con-Validacion
├── app.py               # Script principal con las funciones de validación
├── validators.py        # (opcional) Archivo con validadores separados
└── README.md
🧠 Ejemplo de funcionamiento
import re

# Validar correo electrónico
email = input("Ingresa tu correo: ")

if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("✅ Correo válido.")
else:
    print("❌ Correo inválido.")
El programa evalúa la entrada y muestra el resultado directamente en la consola.

📘 Recomendaciones de desarrollo
Añade pruebas unitarias con pytest o unittest.

Crea funciones separadas para cada tipo de campo.

Guarda los resultados o logs en un archivo .txt si deseas rastrear los intentos.

Más adelante, puedes integrar esta lógica a un formulario web Flask o Django.

🧑‍💻 Autor
Desarrollado por: Aaron Isaías Medina
📧 Contacto: medinaisaias484@gmail.com
📂 Repositorio: Formulario con Validación
📅 Proyecto Python – Validación de formularios con expresiones regulares (Back-End)
