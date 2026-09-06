from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:

    def __init__(
        self,
        productos_iniciales: list[Producto] | None = None,
        usuarios_iniciales: list[Usuario] | None = None,
        ventas_iniciales: list[Venta] | None = None
    ) -> None:

        # Colecciones principales. Se mantienen para listar y guardar en JSON.
        self._productos = (
            productos_iniciales.copy()
            if productos_iniciales
            else []
        )

        self._usuarios = (
            usuarios_iniciales.copy()
            if usuarios_iniciales
            else []
        )

        self._ventas = (
            ventas_iniciales.copy()
            if ventas_iniciales
            else []
        )

        # Indices auxiliares de la Semana 12.
        self._productos_por_codigo: dict[str, Producto] = {}
        self._usuarios_por_identificacion: dict[str, Usuario] = {}
        self._ventas_por_usuario: dict[str, list[Venta]] = {}
        self._categorias: set[str] = set()

        self._reconstruir_indices()

    # =========================
    # INDICES
    # =========================

    def _reconstruir_indices(self) -> None:
        # Reconstruye los indices a partir de las listas cargadas desde JSON.
        self._productos_por_codigo = {}
        self._usuarios_por_identificacion = {}
        self._ventas_por_usuario = {}
        self._categorias = set()

        for producto in self._productos:
            self._productos_por_codigo[producto.codigo] = producto
            self._categorias.add(producto.categoria)

        for usuario in self._usuarios:
            self._usuarios_por_identificacion[usuario.identificacion] = usuario

        for venta in self._ventas:
            self._ventas_por_usuario.setdefault(
                venta.usuario_id,
                []
            ).append(venta)

    # =========================
    # CARGAR COLECCIONES
    # =========================

    def cargar_productos(
        self,
        productos: list[Producto]
    ) -> None:

        self._productos = productos.copy()
        self._reconstruir_indices()

    def cargar_usuarios(
        self,
        usuarios: list[Usuario]
    ) -> None:

        self._usuarios = usuarios.copy()
        self._reconstruir_indices()

    def cargar_ventas(
        self,
        ventas: list[Venta]
    ) -> None:

        self._ventas = ventas.copy()
        self._reconstruir_indices()

    # =========================
    # PRODUCTOS
    # =========================

    def registrar_producto(
        self,
        producto: Producto
    ) -> bool:

        if self.buscar_producto(producto.codigo):
            return False

        self._productos.append(producto)
        self._productos_por_codigo[producto.codigo] = producto
        self._categorias.add(producto.categoria)

        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:

        # Busqueda directa mediante dict en lugar de recorrer toda la lista.
        return self._productos_por_codigo.get(codigo.strip())

    def actualizar_producto(
        self,
        codigo: str,
        nuevo_nombre: str,
        nueva_categoria: str,
        nuevo_precio: float,
        nuevo_stock: int
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nuevo_nombre
        producto.categoria = nueva_categoria
        producto.precio = nuevo_precio
        producto.stock = nuevo_stock

        self._reconstruir_indices()

        return True

    def eliminar_producto(
        self,
        codigo: str
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        self._productos_por_codigo.pop(producto.codigo, None)
        self._reconstruir_indices()

        return True

    def listar_productos(self) -> list[Producto]:

        return self._productos.copy()

    # =========================
    # USUARIOS
    # =========================

    def registrar_usuario(
        self,
        usuario: Usuario
    ) -> bool:

        if self.buscar_usuario(
            usuario.identificacion
        ):

            return False

        self._usuarios.append(usuario)
        self._usuarios_por_identificacion[
            usuario.identificacion
        ] = usuario

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:

        # Busqueda directa mediante dict por identificacion.
        return self._usuarios_por_identificacion.get(
            identificacion.strip()
        )

    def listar_usuarios(self) -> list[Usuario]:

        return self._usuarios.copy()

    # =========================
    # VENTA
    # =========================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        # Verificar usuario y producto
        if usuario is None or producto is None:
            return False

        # Verificar cantidad
        if cantidad <= 0:
            return False

        # Verificar stock
        if producto.stock < cantidad:
            return False

        # Crear la venta
        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        # Guardar venta en la colección principal
        self._ventas.append(venta)

        # Actualizar indice de ventas por usuario
        self._ventas_por_usuario.setdefault(
            usuario.identificacion,
            []
        ).append(venta)

        # Disminuir stock
        producto.vender(cantidad)

        return True

    # =========================
    # CONSULTAR VENTAS
    # =========================

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:

        # Busqueda optimizada mediante indice por usuario.
        ventas = self._ventas_por_usuario.get(
            identificacion_usuario.strip(),
            []
        )

        return ventas.copy()

    def listar_ventas(self) -> list[Venta]:

        return self._ventas.copy()

    # =========================
    # CATEGORIAS
    # =========================

    def obtener_categorias_unicas(
        self
    ) -> set[str]:

        # Set mantenido en memoria para evitar recorrer productos
        # cada vez que se consultan las categorias.
        return self._categorias.copy()

    def existe_categoria(
        self,
        categoria: str
    ) -> bool:

        # Validacion de pertenencia usando set.
        return categoria.strip() in self._categorias
