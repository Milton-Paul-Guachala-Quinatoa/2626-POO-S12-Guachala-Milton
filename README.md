# 2626-POO-S12-Guachala-Milton
# Restaurante App - Semana 12

## Estudiante

Milton Paul Guachala Quinatoa

## Descripción

Este proyecto corresponde a la evolución de `restaurante_app` de la Semana 11.

Se conservaron las funcionalidades de productos, usuarios, ventas, control de
stock y persistencia mediante archivos JSON. En esta Semana 12 se mejoró el
rendimiento de las búsquedas y consultas mediante el uso de colecciones
auxiliares en memoria.

Las listas principales se mantienen para almacenar, recorrer, listar y
persistir los objetos. Los diccionarios y el conjunto se utilizan únicamente
como estructuras auxiliares para operaciones frecuentes.

## Mejoras realizadas en la Semana 12

### Índice de productos por código

Se creó el diccionario `_productos_por_codigo`, donde la clave es el código
del producto y el valor es el objeto `Producto`.

Antes, para buscar un producto se recorría toda la lista. Ahora la búsqueda se
realiza directamente mediante el código.

Esto también mejora las validaciones de códigos repetidos, la actualización y
la eliminación de productos.

### Índice de usuarios por identificación

Se creó el diccionario `_usuarios_por_identificacion`, utilizando la
identificación como clave.

La búsqueda de usuarios ya no necesita recorrer toda la lista, por lo que se
facilita la validación de usuarios existentes y las operaciones de venta.

### Índice de ventas por usuario

Se creó el diccionario `_ventas_por_usuario`. Cada identificación de usuario
se relaciona con una lista de sus ventas.

De esta forma, la consulta de ventas de un usuario evita recorrer toda la
colección de ventas.

### Uso de set para categorías

Se utiliza el conjunto `_categorias` para mantener los nombres de categorías
sin duplicados.

También se agregó una validación mediante `existe_categoria()` para comprobar
rápidamente si una categoría pertenece al conjunto.

## Reconstrucción de índices

Cuando el programa inicia, los productos, usuarios y ventas se recuperan desde
los archivos JSON mediante `ArchivoServicio`.

Después de cargar las colecciones, `Restaurante` reconstruye los índices en
memoria mediante `_reconstruir_indices()`.

Esto permite que los datos persistidos y las estructuras auxiliares vuelvan a
estar sincronizados después de cerrar y ejecutar nuevamente el programa.

## Sincronización de las estructuras auxiliares

Los índices se actualizan cuando se registran nuevos productos o usuarios y
cuando se registra una venta.

Al actualizar o eliminar productos también se reconstruyen las estructuras
auxiliares para mantener la información coherente.

Las listas principales no fueron reemplazadas por diccionarios, ya que siguen
siendo necesarias para listar los datos y guardarlos en los archivos JSON.

## Relación Usuario - Producto mediante Venta

La clase `Venta` mantiene la relación entre un usuario y un producto.

Para realizar una venta se utiliza:

```text
vender_producto(codigo_producto, identificacion_usuario, cantidad)
```

Primero se buscan el usuario y el producto utilizando los índices auxiliares.
Después se valida la cantidad y el stock disponible.

Si todas las condiciones se cumplen, se registra la venta, se actualiza el
índice de ventas por usuario y se disminuye el stock del producto.

## Persistencia

La información se conserva en tres archivos JSON:

- `productos.json`: almacena los productos y su stock.
- `usuarios.json`: almacena los usuarios registrados.
- `ventas.json`: almacena las ventas realizadas.

Los índices de la Semana 12 son estructuras en memoria. No se guardan en JSON,
porque se reconstruyen nuevamente al iniciar el programa.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
└── main.py
```

## Forma de ejecución

Abrir una terminal dentro de la carpeta `restaurante_app` y ejecutar:

```text
python main.py
```

También se puede ejecutar directamente desde Visual Studio Code.

## Pruebas realizadas

Se realizaron las siguientes comprobaciones:

1. Se cargaron productos, usuarios y ventas existentes desde JSON.
2. Se comprobó la búsqueda de un producto mediante su código.
3. Se comprobó la búsqueda de un usuario mediante su identificación.
4. Se consultaron las ventas relacionadas con un usuario.
5. Se realizó una venta y se comprobó la disminución del stock.
6. Se verificó que una venta nueva aparezca en el índice del usuario.
7. Se comprobó que las categorías se mantengan sin valores repetidos mediante
   `set`.
8. Se verificó que los índices se reconstruyan después de cargar los datos
   desde JSON.

## Conclusión

En esta Semana 12 se mejoró el rendimiento interno de `restaurante_app`
utilizando colecciones auxiliares.

Las listas principales se conservaron para mantener la estructura del proyecto
y la persistencia de los datos. Los diccionarios permiten realizar búsquedas
directas por código de producto e identificación de usuario, mientras que el
índice de ventas facilita consultar las ventas de un usuario.

El conjunto de categorías permite realizar consultas de pertenencia sin
recorrer nuevamente todos los productos. De esta manera, el proyecto conserva
las funcionalidades de la Semana 11 y mejora la forma en que se realizan
búsquedas, consultas y validaciones.
