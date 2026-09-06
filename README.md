# 2626-POO-S12-Guachala-Milton
Restaurante App - Semana 12

Estudiante: Milton Paul Guachala Quinatoa

De qué trata esta tarea

Esta es la continuación del restaurante_app que hice en la semana 11. No agregué funciones nuevas ni cambié lo que ya funcionaba, solo mejoré la forma en que el programa busca y consulta la información, usando diccionarios y un set como pedía la guía.

Las listas de productos, usuarios y ventas se quedaron igual, porque todavía se necesitan para guardar todo en los JSON y para listar los datos en pantalla. Lo que agregué son estructuras extra (dict y set) que ayudan a que las búsquedas sean más rápidas.

Qué mejoré

Buscar producto por código Antes, para buscar un producto tocaba recorrer toda la lista uno por uno hasta encontrarlo. Ahora hice un diccionario _productos_por_codigo donde la clave es el código del producto, entonces la búsqueda es directa.

Buscar usuario por identificación Hice lo mismo con los usuarios, un diccionario _usuarios_por_identificacion para no tener que recorrer toda la lista cada vez que se necesita un usuario.

Consultar ventas de un usuario Este era el que más se demoraba antes, porque tenía que revisar todas las ventas registradas para encontrar las de un usuario. Ahora tengo un diccionario _ventas_por_usuario donde cada usuario ya tiene su propia lista de ventas guardada, entonces la consulta es más rápida.

Categorías con set Para las categorías de los productos usé un set llamado _categorias, porque ahí no importa el orden y no puede haber repetidos. También hice una función existe_categoria() para verificar rápido si una categoría ya existe.

Cómo se mantienen actualizados los índices

Cada vez que se registra, actualiza o elimina un producto o un usuario, o se hace una venta, los diccionarios se actualizan también para que no queden desactualizados.

Cuando se cierra el programa y se vuelve a abrir, los datos se cargan de nuevo desde los JSON y ahí mismo se reconstruyen los índices con la función _reconstruir_indices(), para que todo quede sincronizado otra vez.

Estructura del proyecto
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante.py
└── main.py
Cómo ejecutarlo

Desde la carpeta restaurante_app:

python main.py
Pruebas que hice
Cargué los productos, usuarios y ventas que ya tenía guardados
Busqué un producto por su código y sí lo encontró bien
Busqué un usuario por su identificación y también funcionó
Consulté las ventas de un usuario y salieron todas
Vendí un producto y el stock bajó correctamente
Cerré el programa y lo volví a abrir para ver si los datos y los índices seguían bien, y sí funcionó
Conclusión

Con esto el programa sigue haciendo lo mismo que en la semana 11 (vender productos, controlar el stock, guardar en JSON), pero ahora las búsquedas de producto, usuario y ventas por usuario son más rápidas porque uso diccionarios en vez de recorrer toda la lista cada vez.
