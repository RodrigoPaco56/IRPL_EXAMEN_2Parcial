from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.extensions import db
from app.models import Cliente


bp_clientes = Blueprint("clientes", __name__, template_folder="../templates")


@bp_clientes.route("/")
def index():
    clientes = Cliente.query.order_by(Cliente.nombre).all()
    return render_template("clientes/index.html", clientes=clientes)


@bp_clientes.route("/nuevo", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        cliente = Cliente(
            nombre=request.form["nombre"],
            telefono=request.form["telefono"],
        )
        db.session.add(cliente)
        db.session.commit()
        flash("Cliente creado correctamente.", "success")
        return redirect(url_for("clientes.index"))

    return render_template("clientes/form.html", cliente=None)


@bp_clientes.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    cliente = Cliente.query.get_or_404(id)

    if request.method == "POST":
        cliente.nombre = request.form["nombre"]
        cliente.telefono = request.form["telefono"]
        db.session.commit()
        flash("Cliente actualizado correctamente.", "success")
        return redirect(url_for("clientes.index"))

    return render_template("clientes/form.html", cliente=cliente)


@bp_clientes.route("/<int:id>/eliminar", methods=["POST"])
def eliminar(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    flash("Cliente eliminado correctamente.", "success")
    return redirect(url_for("clientes.index"))
