# taxteclib

`taxteclib` es una librería Python que centraliza módulos y utilidades comunes para los proyectos de BPS Tax Tec (Argentina). Está pensada para contener funciones, clases y helpers reutilizables que faciliten la construcción de servicios y herramientas internas.

## Características

- Paquete ligero, compatible con Python 3.12
- Estructura lista para pruebas y CI
- Contiene utilidades comunes para la organización BPS Tax Tec ARG

## Instalación (desarrollo)

Recomendado: crear un entorno virtual y usar las utilidades del proyecto.

Con venv:

```pwsh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -e .
```

Si usas `uv` (opcional) y el Makefile del repo:

```pwsh
make local-setup
make install
```

## Uso básico

Ejemplo mínimo usando la clase de ejemplo incluida:

```python
from taxteclib.dummy_class import Dummy

dummy = Dummy()
assert dummy.add(2, 3) == 5
print('2 + 3 =', dummy.add(2, 3))
```

## Ejecutar pruebas

La suite de tests usa `pytest`. Para correrlas localmente:

```pwsh
# dentro del entorno virtual
make test
# o
pytest -q
```

## Contribuir

1. Crea una rama con un nombre descriptivo
2. Asegúrate de pasar los hooks y tests locales (`make local-setup`)
3. Envía un Pull Request contra `main`

Para estilos y checks el repo incluye `ruff` y hooks de pre-commit.

## Licencia

Consulta el archivo `LICENSE` del repositorio para detalles.

---

Archivo antiguo conservado como `README.legacy.md`.

# Python Boilerplate ![status](https://github.com/AR-BPS-TaxTech/python-boilerplate/actions/workflows/app.yml/badge.svg)

Repositorio base para proyectos en Python 3.12, con integración continua y buenas prácticas de desarrollo.

## Personalización y puesta a punto

- **Modifica el archivo `pyproject.toml`** según las necesidades de tu proyecto.
- **Cambia el `origin` de git** para tu repositorio.  
Ejecuta en la terminal:

  ```sh
  git remote set-url origin <URL_DE_TU_REPOSITORIO>
  ```

  Reemplaza `<URL_DE_TU_REPOSITORIO>` por la URL de tu repositorio.
- **Ejecuta `make local-setup`** antes de comenzar para instalar los hooks y preparar el entorno local.
- Para crear un commit, debes pasar la fase de pre-commit que ejecuta los comandos de chequeo y pruebas.

## Requisitos previos

- [uv](https://docs.astral.sh/uv)
- [Make](https://www.gnu.org/software/make/) ([instalación en Windows](#instalación-de-make-en-windows))

## Características principales

- **Rápido inicio:** Estructura lista para comenzar nuevos proyectos.
- **Integración continua:** Github Actions ejecuta pruebas y chequeos en cada push a `main`.
- **Gestión de dependencias:** Usa [uv](https://docs.astral.sh/uv) para instalar y actualizar paquetes.
- **Automatización:** Tareas comunes gestionadas con Makefile.
- **Pre-commit hooks:** Validaciones automáticas antes de cada commit.


## Estructura del proyecto

```
src/        # Código fuente
tests/      # Pruebas unitarias
scripts/    # Scripts y git hooks
Makefile    # Tareas automatizadas
pyproject.toml # Configuración del proyecto
```


## Comandos útiles

Ejecuta tareas con `make <comando>`:

- `install`         Instala dependencias
- `run`             Ejecuta la app
- `test`            Corre pruebas
- `lint`            Analiza estilo
- `format`          Formatea código
- `check-*`         Chequeos varios (lint, typing, format)
- `local-setup`     Configura entorno local (instala hooks)
- `update`          Actualiza dependencias
- `watch`           Pruebas en modo observación
- `add-package package=XXX` Instala el paquete XXX, ej: `make add-package package=requests`
- `build`           Construye la aplicación
- `help`            Muestra ayuda de comandos

> **Recomendación:** Ejecuta `make local-setup` antes de comenzar.


## Paquetes incluidos

- **Pruebas:** `pytest`, `doublex`, `expects`, `doublex-expects`
- **Estilo:** `ruff`, `ty`


## Instalación de Make en Windows

1. Descarga [`make-3.81.exe`](https://sitsa.dl.sourceforge.net/project/gnuwin32/make/3.81/make-3.81.exe?viasf=1).
2. Instala y agrega `C:\Program Files (x86)\GnuWin32\bin` a tu variable de entorno `PATH`.

Esto permitirá ejecutar `make` desde la terminal.
