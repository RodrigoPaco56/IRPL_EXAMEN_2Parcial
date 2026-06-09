# Examen_Login - Inventario y Ventas

Sistema monolitico modular desarrollado con Flask, SQLAlchemy, Flask-Migrate, Flask-Login, Flask-Bcrypt y Bootstrap.

## Instalacion

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Migraciones

```bash
flask --app run.py db init
flask --app run.py db migrate -m "Migracion inicial"
flask --app run.py db upgrade
```

## Ejecucion

Tambien puede ejecutar directamente el archivo:

```bash
EJECUTAR_EXAMEN_LOGIN.bat
```

Credenciales de acceso:

```text
Email: admin@techbol.com
Contrasena: 12345
```

```bash
flask --app run.py run --debug
```

Rutas principales:

- `/auth/login`
- `/auth/registro`
- `/productos`
- `/clientes`
- `/pedidos`

El sistema requiere iniciar sesion para acceder al panel, productos, clientes y pedidos.
# MASV_2DO_PARCIAL
