import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

    def __init__(self, ruta_datos: str = "datos") -> None:
        self._ruta_datos = Path(ruta_datos)

        self._ruta_productos = (
            self._ruta_datos / "productos.json"
        )

        self._ruta_usuarios = (
            self._ruta_datos / "usuarios.json"
        )

        self._ruta_ventas = (
            self._ruta_datos / "ventas.json"
        )

    # =========================
    # PRODUCTOS
    # =========================

    def cargar_productos(self) -> list[Producto]:
        datos = self._leer_lista(
            self._ruta_productos,
            "productos"
        )

        productos = []

        for item in datos:
            try:
                producto = Producto(
                    item["codigo"],
                    item["nombre"],
                    item["categoria"],
                    item["precio"],
                    item.get("stock", 0)
                )

                productos.append(producto)

            except KeyError:
                print(
                    "Registro de producto incompleto."
                )

            except ValueError as error:
                print(
                    f"Producto con datos invalidos: {error}"
                )

        return productos

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> bool:

        datos = []

        for producto in productos:
            datos.append(
                producto.convertir_a_diccionario()
            )

        return self._guardar_lista(
            self._ruta_productos,
            datos,
            "productos"
        )

    # =========================
    # USUARIOS
    # =========================

    def cargar_usuarios(self) -> list[Usuario]:
        datos = self._leer_lista(
            self._ruta_usuarios,
            "usuarios"
        )

        usuarios = []

        for item in datos:
            try:
                usuario = Usuario(
                    item["identificacion"],
                    item["nombre"],
                    item["correo"]
                )

                usuarios.append(usuario)

            except KeyError:
                print(
                    "Registro de usuario incompleto."
                )

            except ValueError as error:
                print(
                    f"Usuario con datos invalidos: {error}"
                )

        return usuarios

    def guardar_usuarios(
        self,
        usuarios: list[Usuario]
    ) -> bool:

        datos = []

        for usuario in usuarios:
            datos.append(
                usuario.convertir_a_diccionario()
            )

        return self._guardar_lista(
            self._ruta_usuarios,
            datos,
            "usuarios"
        )

    # =========================
    # VENTAS
    # =========================

    def cargar_ventas(self) -> list[Venta]:
        datos = self._leer_lista(
            self._ruta_ventas,
            "ventas"
        )

        ventas = []

        for item in datos:
            try:
                venta = Venta(
                    item["usuario_id"],
                    item["producto_codigo"],
                    item["cantidad"]
                )

                ventas.append(venta)

            except KeyError:
                print(
                    "Registro de venta incompleto."
                )

            except ValueError as error:
                print(
                    f"Venta con datos invalidos: {error}"
                )

        return ventas

    def guardar_ventas(
        self,
        ventas: list[Venta]
    ) -> bool:

        datos = []

        for venta in ventas:
            datos.append(
                venta.convertir_a_diccionario()
            )

        return self._guardar_lista(
            self._ruta_ventas,
            datos,
            "ventas"
        )

    # =========================
    # MÉTODOS INTERNOS
    # =========================

    def _leer_lista(
        self,
        ruta: Path,
        nombre: str
    ) -> list:

        try:
            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                f"El archivo de {nombre} "
                f"no contiene un JSON valido."
            )
            return []

        except PermissionError:
            print(
                f"No existen permisos para leer "
                f"el archivo de {nombre}."
            )
            return []

        if not isinstance(datos, list):
            print(
                f"El archivo de {nombre} "
                f"debe contener una lista."
            )

            return []

        return datos

    def _guardar_lista(
        self,
        ruta: Path,
        datos: list,
        nombre: str
    ) -> bool:

        try:
            ruta.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with open(
                ruta,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

            return True

        except PermissionError:
            print(
                f"No existen permisos para guardar "
                f"el archivo de {nombre}."
            )

            return False