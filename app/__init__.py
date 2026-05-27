from pathlib import Path

from flask import Flask, render_template

from config import Config

from .extensions import db, migrate


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    db.init_app(app)
    migrate.init_app(app, db)

    from .clientes.routes import bp_clientes
    from .pedidos.routes import bp_pedidos
    from .productos.routes import bp_productos

    app.register_blueprint(bp_clientes, url_prefix="/clientes")
    app.register_blueprint(bp_productos, url_prefix="/productos")
    app.register_blueprint(bp_pedidos, url_prefix="/pedidos")

    @app.route("/")
    def index():
        from .models import Cliente, Pedido, Producto

        resumen = {
            "productos": Producto.query.count(),
            "clientes": Cliente.query.count(),
            "pedidos": Pedido.query.count(),
            "stock_total": db.session.query(db.func.coalesce(db.func.sum(Producto.stock), 0)).scalar(),
        }
        ultimos_pedidos = Pedido.query.order_by(Pedido.fecha.desc(), Pedido.id.desc()).limit(5).all()
        return render_template("dashboard.html", resumen=resumen, ultimos_pedidos=ultimos_pedidos)

    return app
