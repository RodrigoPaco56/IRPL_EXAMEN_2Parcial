from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.extensions import db
from app.models import Cliente, Pedido, Producto


bp_pedidos = Blueprint("pedidos", __name__, template_folder="../templates")


@bp_pedidos.route("/")
def index():
    pedidos = Pedido.query.order_by(Pedido.fecha.desc(), Pedido.id.desc()).all()
    return render_template("pedidos/index.html", pedidos=pedidos)


@bp_pedidos.route("/nuevo", methods=["GET", "POST"])
def crear():
    productos = Producto.query.order_by(Producto.nombre).all()
    clientes = Cliente.query.order_by(Cliente.nombre).all()

    if request.method == "POST":
        pedido = Pedido(
            fecha=datetime.strptime(request.form["fecha"], "%Y-%m-%d").date(),
            monto=float(request.form["monto"]),
            producto_id=int(request.form["producto_id"]),
            cliente_id=int(request.form["cliente_id"]),
        )
        db.session.add(pedido)
        db.session.commit()
        flash("Pedido creado correctamente.", "success")
        return redirect(url_for("pedidos.index"))

    return render_template("pedidos/form.html", pedido=None, productos=productos, clientes=clientes)


@bp_pedidos.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    pedido = Pedido.query.get_or_404(id)
    productos = Producto.query.order_by(Producto.nombre).all()
    clientes = Cliente.query.order_by(Cliente.nombre).all()

    if request.method == "POST":
        pedido.fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d").date()
        pedido.monto = float(request.form["monto"])
        pedido.producto_id = int(request.form["producto_id"])
        pedido.cliente_id = int(request.form["cliente_id"])
        db.session.commit()
        flash("Pedido actualizado correctamente.", "success")
        return redirect(url_for("pedidos.index"))

    return render_template("pedidos/form.html", pedido=pedido, productos=productos, clientes=clientes)


@bp_pedidos.route("/<int:id>/eliminar", methods=["POST"])
def eliminar(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    flash("Pedido eliminado correctamente.", "success")
    return redirect(url_for("pedidos.index"))
