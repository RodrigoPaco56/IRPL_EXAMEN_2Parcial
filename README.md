# TechBol - Inventario y Ventas

Sistema monolitico modular desarrollado con Flask, SQLAlchemy, Flask-Migrate y Bootstrap.

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

```bash
flask --app run.py run --debug
```

Rutas principales:

- `/productos`
- `/clientes`
- `/pedidos`
# MASV_2DO_PARCIAL
