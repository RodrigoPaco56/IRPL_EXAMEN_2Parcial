from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.extensions import db
from app.models import Producto


bp_productos = Blueprint("productos", __name__, template_folder="../templates")


@bp_productos.route("/")
def index():
    productos = Producto.query.order_by(Producto.nombre).all()
    return render_template("productos/index.html", productos=productos)


@bp_productos.route("/nuevo", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        producto = Producto(
            nombre=request.form["nombre"],
            precio=float(request.form["precio"]),
            stock=int(request.form["stock"]),
        )
        db.session.add(producto)
        db.session.commit()
        flash("Producto creado correctamente.", "success")
        return redirect(url_for("productos.index"))

    return render_template("productos/form.html", producto=None)


@bp_productos.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    producto = Producto.query.get_or_404(id)

    if request.method == "POST":
        producto.nombre = request.form["nombre"]
        producto.precio = float(request.form["precio"])
        producto.stock = int(request.form["stock"])
        db.session.commit()
        flash("Producto actualizado correctamente.", "success")
        return redirect(url_for("productos.index"))

    return render_template("productos/form.html", producto=producto)


@bp_productos.route("/<int:id>/eliminar", methods=["POST"])
def eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash("Producto eliminado correctamente.", "success")
    return redirect(url_for("productos.index"))
