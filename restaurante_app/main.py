import os

from modelos.producto import Producto
from modelos.usuario import Usuario

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


RUTA_DATOS = os.path.join(
    os.path.dirname(__file__),
    "datos"
)


def main() -> None:

    restaurante = Restaurante()

    archivo_servicio = ArchivoServicio(
        RUTA_DATOS
    )

    # Cargar información guardada
    restaurante.cargar_productos(
        archivo_servicio.cargar_productos()
    )

    restaurante.cargar_usuarios(
        archivo_servicio.cargar_usuarios()
    )

    restaurante.cargar_ventas(
        archivo_servicio.cargar_ventas()
    )

    while True:

        print("\n==============================")
        print("      RESTAURANTE APP")
        print("==============================")

        print("1. Registrar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Listar productos")
        print("6. Registrar usuario")
        print("7. Listar usuarios")
        print("8. Mostrar categorias")
        print("9. Vender producto")
        print("10. Consultar ventas de un usuario")
        print("11. Listar ventas")
        print("0. Salir")

        opcion = input(
            "Seleccione una opcion: "
        ).strip()

        # =========================
        # REGISTRAR PRODUCTO
        # =========================

        if opcion == "1":

            try:

                codigo = input(
                    "Codigo: "
                )

                nombre = input(
                    "Nombre: "
                )

                categoria = input(
                    "Categoria: "
                )

                precio = float(
                    input("Precio: ")
                )

                stock = int(
                    input("Stock: ")
                )

                producto = Producto(
                    codigo,
                    nombre,
                    categoria,
                    precio,
                    stock
                )

                if restaurante.registrar_producto(
                    producto
                ):

                    archivo_servicio.guardar_productos(
                        restaurante.listar_productos()
                    )

                    print(
                        "Producto registrado correctamente."
                    )

                else:

                    print(
                        "El codigo ya existe."
                    )

            except ValueError as error:

                print(error)

        # =========================
        # BUSCAR PRODUCTO
        # =========================

        elif opcion == "2":

            codigo = input(
                "Ingrese el codigo: "
            )

            producto = restaurante.buscar_producto(
                codigo
            )

            if producto:

                print(producto)

            else:

                print(
                    "Producto no encontrado."
                )

        # =========================
        # ACTUALIZAR PRODUCTO
        # =========================

        elif opcion == "3":

            try:

                codigo = input(
                    "Codigo del producto: "
                )

                nombre = input(
                    "Nuevo nombre: "
                )

                categoria = input(
                    "Nueva categoria: "
                )

                precio = float(
                    input("Nuevo precio: ")
                )

                stock = int(
                    input("Nuevo stock: ")
                )

                resultado = (
                    restaurante.actualizar_producto(
                        codigo,
                        nombre,
                        categoria,
                        precio,
                        stock
                    )
                )

                if resultado:

                    archivo_servicio.guardar_productos(
                        restaurante.listar_productos()
                    )

                    print(
                        "Producto actualizado correctamente."
                    )

                else:

                    print(
                        "Producto no encontrado."
                    )

            except ValueError as error:

                print(error)

        # =========================
        # ELIMINAR PRODUCTO
        # =========================

        elif opcion == "4":

            codigo = input(
                "Codigo del producto: "
            )

            resultado = (
                restaurante.eliminar_producto(
                    codigo
                )
            )

            if resultado:

                archivo_servicio.guardar_productos(
                    restaurante.listar_productos()
                )

                print(
                    "Producto eliminado correctamente."
                )

            else:

                print(
                    "Producto no encontrado."
                )

        # =========================
        # LISTAR PRODUCTOS
        # =========================

        elif opcion == "5":

            productos = (
                restaurante.listar_productos()
            )

            if not productos:

                print(
                    "No hay productos registrados."
                )

            else:

                for producto in productos:

                    print(producto)

        # =========================
        # REGISTRAR USUARIO
        # =========================

        elif opcion == "6":

            try:

                identificacion = input(
                    "Identificacion: "
                )

                nombre = input(
                    "Nombre: "
                )

                correo = input(
                    "Correo: "
                )

                usuario = Usuario(
                    identificacion,
                    nombre,
                    correo
                )

                resultado = (
                    restaurante.registrar_usuario(
                        usuario
                    )
                )

                if resultado:

                    archivo_servicio.guardar_usuarios(
                        restaurante.listar_usuarios()
                    )

                    print(
                        "Usuario registrado correctamente."
                    )

                else:

                    print(
                        "La identificacion ya existe."
                    )

            except ValueError as error:

                print(error)

        # =========================
        # LISTAR USUARIOS
        # =========================

        elif opcion == "7":

            usuarios = (
                restaurante.listar_usuarios()
            )

            if not usuarios:

                print(
                    "No hay usuarios registrados."
                )

            else:

                for usuario in usuarios:

                    print(usuario)

        # =========================
        # CATEGORIAS
        # =========================

        elif opcion == "8":

            categorias = (
                restaurante.obtener_categorias_unicas()
            )

            if not categorias:

                print(
                    "No hay categorias registradas."
                )

            else:

                for categoria in categorias:

                    print(
                        f"- {categoria}"
                    )

        # =========================
        # VENDER PRODUCTO
        # =========================

        elif opcion == "9":

            try:

                identificacion = input(
                    "Identificacion del usuario: "
                )

                codigo = input(
                    "Codigo del producto: "
                )

                cantidad = int(
                    input("Cantidad: ")
                )

                resultado = (
                    restaurante.vender_producto(
                        codigo,
                        identificacion,
                        cantidad
                    )
                )

                if resultado:

                    # Guardar ventas
                    archivo_servicio.guardar_ventas(
                        restaurante.listar_ventas()
                    )

                    # Guardar stock actualizado
                    archivo_servicio.guardar_productos(
                        restaurante.listar_productos()
                    )

                    print(
                        "Venta registrada correctamente."
                    )

                else:

                    print(
                        "Venta rechazada."
                    )

                    print(
                        "Verifique el usuario, "
                        "producto, cantidad y stock."
                    )

            except ValueError as error:

                print(error)

        # =========================
        # CONSULTAR VENTAS
        # =========================

        elif opcion == "10":

            identificacion = input(
                "Identificacion del usuario: "
            )

            ventas = (
                restaurante.consultar_ventas_usuario(
                    identificacion
                )
            )

            if not ventas:

                print(
                    "No existen ventas para este usuario."
                )

            else:

                print(
                    "\nVentas del usuario:"
                )

                for venta in ventas:

                    producto = (
                        restaurante.buscar_producto(
                            venta.producto_codigo
                        )
                    )

                    if producto:

                        print(
                            f"Producto: {producto.nombre}"
                        )

                        print(
                            f"Codigo: {producto.codigo}"
                        )

                        print(
                            f"Cantidad: {venta.cantidad}"
                        )

                        print("--------------------")

                    else:

                        print(venta)

        # =========================
        # LISTAR VENTAS
        # =========================

        elif opcion == "11":

            ventas = (
                restaurante.listar_ventas()
            )

            if not ventas:

                print(
                    "No hay ventas registradas."
                )

            else:

                for venta in ventas:

                    producto = (
                        restaurante.buscar_producto(
                            venta.producto_codigo
                        )
                    )

                    if producto:

                        nombre_producto = (
                            producto.nombre
                        )

                    else:

                        nombre_producto = (
                            "Producto no disponible"
                        )

                    print(
                        f"Usuario: {venta.usuario_id} | "
                        f"Producto: {nombre_producto} | "
                        f"Codigo: {venta.producto_codigo} | "
                        f"Cantidad: {venta.cantidad}"
                    )

        # =========================
        # SALIR
        # =========================

        elif opcion == "0":

            print(
                "Programa finalizado."
            )

            break

        else:

            print(
                "Opcion invalida."
            )


if __name__ == "__main__":
    main() 