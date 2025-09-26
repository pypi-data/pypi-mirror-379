
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
