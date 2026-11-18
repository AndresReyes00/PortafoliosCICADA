# CICADA

**Desarrollo de software · Backend · Soluciones digitales**

Cicada es un proyecto web desarrollado con Django, orientado a presentar servicios de desarrollo de software, conocimientos técnicos, proyectos y publicaciones mediante una plataforma moderna, modular y escalable.

La aplicación se encuentra en una etapa inicial de desarrollo, centrada en la construcción de su identidad visual, arquitectura frontend y landing page.

## 1. Descripción del proyecto

Cicada nace como una iniciativa enfocada en el desarrollo de soluciones digitales, con especial interés en ingeniería backend, aplicaciones web, gestión de datos y arquitectura de software.

El objetivo inicial es construir una plataforma que permita:

- Presentar la identidad y los servicios del proyecto.
- Mostrar tecnologías y competencias técnicas.
- Publicar proyectos mediante un portafolio dinámico.
- Compartir artículos y conocimientos técnicos.
- Recibir mensajes de contacto.
- Administrar progresivamente el contenido desde un backend desarrollado con Django.

La arquitectura está diseñada para incorporar nuevas funcionalidades sin necesidad de reconstruir la interfaz principal.

## 2. Tecnologías utilizadas

| Tecnología | Propósito |
|---|---|
| Python | Lenguaje principal del backend |
| Django | Framework web y arquitectura del servidor |
| Django Templates | Renderizado dinámico de HTML |
| Bootstrap 5.3 | Diseño responsive y componentes |
| Bootstrap Icons | Iconografía |
| HTML5 | Estructura de las páginas |
| CSS3 | Personalización de la identidad visual |
| JavaScript | Interactividad mediante Bootstrap |
| django-environ | Gestión de variables de entorno |
| Pillow | Soporte para campos de imágenes |
| SQLite | Base de datos inicial de desarrollo |

La aplicación utiliza renderizado del lado del servidor mediante Django Templates. No requiere un framework frontend adicional en su etapa actual.

## 3. Identidad visual

### Marca

**Nombre:** Cicada

**Concepto:** identidad tecnológica minimalista, basada en una representación geométrica de una cigarra.

### Logotipo

La identidad visual oficial utiliza un símbolo de cigarra con las siguientes características:

- Geometría simétrica.
- Alas abiertas con nervaduras angulares.
- Ojos circulares.
- Antenas curvas.
- Cuerpo segmentado.
- Trazos blancos definidos.
- Estética minimalista y tecnológica.

El diseño original debe conservarse en futuras aplicaciones de marca.

### Paleta de colores

| Elemento | Color | HEX |
|---|---|---|
| Fondo principal | Negro profundo | `#111111` |
| Superficie secundaria | Gris oscuro | `#1A1A1A` |
| Tarjetas | Gris carbón | `#202020` |
| Texto principal | Blanco | `#FFFFFF` |
| Texto secundario | Gris suave | `#A1A1AA` |
| Barras de progreso | Blanco suave | `#F5F5F5` |

La interfaz sigue un sistema monocromático. Los colores azules, celestes y morados no forman parte de la identidad principal.

### Principios de diseño

1. Minimalismo visual.
2. Contraste entre blanco y negro.
3. Jerarquía tipográfica clara.
4. Componentes reutilizables.
5. Diseño responsive.
6. Transiciones y efectos visuales discretos.
7. Consistencia entre las secciones de la aplicación.

## 4. Arquitectura del proyecto

La aplicación utiliza una arquitectura basada en el patrón Model-Template-View (MTV) de Django.

**Model:** representa y gestiona los datos.

**Template:** define la presentación HTML.

**View:** procesa las solicitudes y proporciona información a las plantillas.

La landing utiliza actualmente una vista basada en clases mediante `TemplateView`.

### Estructura de referencia

```text
cicada/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── landing/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── landing/
│           └── index.html
│
├── templates/
│   ├── base.html
│   └── includes/
│       ├── navbar.html
│       └── footer.html
│
├── static/
│   ├── css/
│   │   ├── base.css
│   │   └── landing.css
│   └── img/
│       ├── cicada.png
│       └── giron.jpg
│
├── media/
├── .env
├── .gitignore
├── manage.py
└── requirements.txt
```

Esta estructura representa la organización propuesta durante el desarrollo y puede ampliarse a medida que se incorporen nuevas aplicaciones.

## 5. Configuración del entorno

### Requisitos

- Python 3.10 o superior compatible con la versión instalada de Django.
- pip.
- Entorno virtual de Python.
- Git.

### Clonar el repositorio

```bash
git clone <repository-url>
cd cicada
```

### Crear un entorno virtual

```bash
python -m venv .venv
```

Activación en Windows:

```powershell
.venv\Scripts\activate
```

Activación en Linux o macOS:

```bash
source .venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

Dependencias principales previstas:

```text
Django
django-environ
Pillow
```

### Variables de entorno

El proyecto utiliza `django-environ` para separar la configuración sensible del código fuente.

Crear un archivo `.env` en la raíz:

```dotenv
SECRET_KEY=replace-with-your-secret-key
DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=sqlite:///db.sqlite3
```

Ejemplo de lectura desde `settings.py`:

```python
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=["localhost", "127.0.0.1"]
)

DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}
```

El archivo `.env` no debe incluirse en el control de versiones.

## 6. Archivos estáticos y multimedia

Los archivos estáticos incluyen estilos CSS, JavaScript, logotipos e imágenes de interfaz.

```python
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = BASE_DIR / "staticfiles"
```

Los archivos multimedia se reservan para imágenes y documentos cargados mediante la aplicación.

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

Durante el desarrollo, Django puede servir archivos multimedia mediante su configuración de URLs. En producción se deberá utilizar un mecanismo adecuado de almacenamiento y entrega de archivos.

## 7. Sistema de plantillas

Cicada utiliza herencia de plantillas para mantener una interfaz consistente.

### `base.html`

Plantilla principal responsable de:

- Estructura HTML.
- Carga de Bootstrap.
- Carga de Bootstrap Icons.
- Carga de estilos globales.
- Inclusión de navbar y footer.
- Bloques para contenido dinámico.
- Carga de JavaScript.
- Presentación de mensajes de Django.

### `navbar.html`

Componente de navegación responsive que incluye:

- Identidad Cicada.
- Inicio.
- Tecnologías.
- Proyectos.
- Blog.
- Contacto.
- Estructura preparada para autenticación.

Los enlaces de autenticación dependen de la implementación futura de sus rutas.

### `footer.html`

Componente global que incluye:

- Identidad de marca.
- Descripción del proyecto.
- Enlaces de navegación.
- Redes sociales.
- Acceso a contacto.
- Copyright dinámico.

Los enlaces sociales deberán actualizarse con los perfiles definitivos.

## 8. Landing page

La página principal está dividida en cinco secciones.

### 8.1 Hero

Sección introductoria con:

- Fotografía inspirada en la arquitectura colonial de Girón, Santander, Colombia.
- Superposición oscura para mejorar la legibilidad.
- Título principal.
- Descripción del proyecto.
- Botones hacia portafolio y contacto.
- Emblema de Cicada ubicado a la derecha.

La presentación del logotipo está diseñada para integrarse visualmente con el fondo mediante un tratamiento oscuro y efectos discretos.

### 8.2 Tecnologías

Sección destinada a mostrar conocimientos y herramientas.

Tecnologías iniciales:

- Python.
- Django.
- JavaScript.
- SQL.
- Linux.

Cada tecnología utiliza una barra de progreso de Bootstrap para representar visualmente su nivel.

Los valores se definen desde la vista Django mediante `get_context_data()`.

Los porcentajes actuales son orientativos y pueden modificarse posteriormente.

### 8.3 Portafolio

Sección preparada para mostrar proyectos almacenados en la base de datos.

Cada proyecto podrá incluir:

- Título.
- Imagen.
- Descripción.
- Tecnologías utilizadas.
- Enlace al detalle del proyecto.

La integración con modelos Django está pendiente. La plantilla contiene una estructura de referencia comentada y un estado visual temporal.

### 8.4 Blog

Sección destinada a publicaciones técnicas, documentación y artículos.

Cada publicación podrá incluir:

- Título.
- Imagen.
- Fecha de publicación.
- Resumen.
- Enlace al artículo completo.

La conexión con la base de datos y la administración de publicaciones están pendientes.

### 8.5 Contacto

Formulario de contacto con los campos:

| Campo | Nombre HTML |
|---|---|
| Nombre | `name` |
| Correo electrónico | `email` |
| Asunto | `subject` |
| Mensaje | `message` |

El formulario utiliza el método POST e incluye protección CSRF mediante Django.

Actualmente, su interfaz está preparada, pero el procesamiento del formulario todavía no está implementado.

El atributo `action="#"` es temporal y no constituye un endpoint funcional de almacenamiento.

## 9. Vista principal

La landing utiliza `TemplateView`.

```python
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "landing/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["technologies"] = [
            {
                "name": "Python",
                "level": 85,
                "icon": "bi bi-code-slash",
            },
            {
                "name": "Django",
                "level": 80,
                "icon": "bi bi-server",
            },
            {
                "name": "JavaScript",
                "level": 60,
                "icon": "bi bi-filetype-js",
            },
            {
                "name": "SQL",
                "level": 75,
                "icon": "bi bi-database",
            },
            {
                "name": "Linux",
                "level": 55,
                "icon": "bi bi-terminal",
            },
        ]

        return context
```

Las consultas de proyectos y publicaciones se añadirán cuando sus modelos estén definidos.

## 10. Ejecutar el proyecto

Aplicar migraciones:

```bash
python manage.py migrate
```

Iniciar el servidor:

```bash
python manage.py runserver
```

Acceder desde el navegador:

```text
http://127.0.0.1:8000/
```

## 11. Estado del desarrollo

| Módulo | Estado |
|---|---|
| Configuración inicial Django | Configuración propuesta |
| Variables de entorno | Configuración definida |
| Identidad visual Cicada | Definida |
| Navbar responsive | Implementación frontend |
| Footer | Implementación frontend |
| Hero | Implementación frontend |
| Sección de tecnologías | Implementación con datos de contexto |
| Portafolio dinámico | Pendiente |
| Blog dinámico | Pendiente |
| Procesamiento de contacto | Pendiente |
| Dashboard administrativo personalizado | Pendiente |
| Autenticación personalizada | Pendiente |
| Despliegue en producción | Pendiente |

Los estados describen el avance del código trabajado hasta este punto; no representan pruebas automatizadas ni una verificación del repositorio.

## 12. Próximas etapas

### Fase 1 — Finalización del frontend

- [ ] Optimizar el logotipo para uso web con transparencia.
- [ ] Revisar la adaptación responsive.
- [ ] Unificar los detalles visuales de todos los componentes.
- [ ] Optimizar las imágenes estáticas.
- [ ] Revisar accesibilidad y contraste.

### Fase 2 — Portafolio dinámico

- [ ] Diseñar el modelo `Project`.
- [ ] Implementar imágenes y descripciones.
- [ ] Configurar administración de proyectos.
- [ ] Conectar proyectos a la landing.
- [ ] Crear páginas de detalle.

### Fase 3 — Blog

- [ ] Diseñar el modelo de publicaciones.
- [ ] Implementar creación y edición de artículos.
- [ ] Crear listado de publicaciones.
- [ ] Crear vista de detalle.
- [ ] Integrar el blog con la landing.

### Fase 4 — Contacto y dashboard

- [ ] Crear modelo para mensajes de contacto.
- [ ] Implementar validación del formulario.
- [ ] Crear una vista para procesar solicitudes POST.
- [ ] Almacenar mensajes en la base de datos.
- [ ] Construir un dashboard de administración.
- [ ] Implementar lectura y gestión de mensajes.

### Fase 5 — Seguridad y despliegue

- [ ] Revisar variables de entorno para producción.
- [ ] Configurar HTTPS.
- [ ] Configurar almacenamiento de archivos.
- [ ] Ejecutar comprobaciones de seguridad de Django.
- [ ] Preparar despliegue.
- [ ] Implementar pruebas automatizadas.

## 13. Filosofía de desarrollo

Cicada prioriza una arquitectura sencilla, modular y mantenible.

El desarrollo seguirá los siguientes principios:

- **Simplicidad:** evitar dependencias y abstracciones innecesarias.
- **Modularidad:** separar responsabilidades entre aplicaciones, vistas y plantillas.
- **Reutilización:** compartir componentes y estilos globales.
- **Escalabilidad:** preparar la arquitectura para funcionalidades futuras.
- **Mantenibilidad:** conservar un código organizado, legible y documentado.
- **Consistencia visual:** respetar la identidad oficial de Cicada.

---

**Cicada — Software Development**

*Construyendo soluciones digitales para el mundo real.*

**Estado:** Desarrollo inicial  
**Framework principal:** Django  
**Interfaz:** Bootstrap 5  
**Identidad visual:** Blanco y negro
