### API de libros

Este proyecto esta hecho con graphql sobre el framework fastAPI

## Instalación de dependencias

Ejecute el comando siguiente sobre el directorio raiz del proyecto para entorno linux

1. crear un virtual environment


```bash
    python -m venv venv
```

2. Activar el entorno

```bash
    source venv/bin/activate
```

3. instalar las dependencias

```bash
    pip install -r requitements.txt
```
## Ejecución

1. ejecute el siguiente comando para levantar un servidor de uvicorn en su maquina.


```bash
    uvicorn main:app --reload
```

# Probar aplicación

En el navegador ingresé a la siguiente dirección: 


```bash
    http://localhost:8000/book
```

En esta dirección vera el entorno de ejecución de consultas de graphql en el cual puede realizar las siguientes operaciones:

1. Crear un libro


```graphql
mutation Ex {
  createBook(
		title: "El librote", 
		subtitle: "el libro mas grande",
		authors: "Ferchito, Fernando",
		categories: "ciencia ficción, Acción",
		editor: "me",
		description: "some description"
		image: "http://images.com.co/image1.png"
	)
```

2. Listar todos los libros

```graphql
query Ex {
	books
	{
		id,
		title,
		subtitle,
		authors,
		categories,
		editor,
		description,
		image
	}
}
```

3. Traer un soo libro por su ID

```graphql
query Ex {
	book(id: 1)
	{
		id,
		title,
		subtitle,
		authors,
		categories,
		editor,
		description,
		image
	}
}
```

4. Actualizar la información de un libro

```graphql
mutation Ex {
  updateBook(
		id: 1,
		title: "El librotote", 
		subtitle: "gran viaje",
		authors: "Fercho",
		categories: "ciencia ficción",
		editor: "me",
		description: "some description"
		image: "http://images.com.co/image1.png"
	)
}
```

5. Eliminar un libro

```graphql
mutation Ex {
  deleteBook(id: 1)
}
```

6. Consultar un libro por un atributo especifico

```graphql
query Ex {
  queryBook(field: "authors", value: "Ferchito"){
		id,
		title,
		subtitle,
		authors,
		categories,
		editor,
		description,
		image
	}
}
```

7. Consultar libros por cualquiera de sus atributos

```graphql
query Ex {
	findBook(value: "Harry") {
		title,
		subtitle,
		authors,
		categories,
		editor,
		description,
		image
	}
}
```

## Existe un despliegue en linea en el siguiente enlace, pero solo permite las consultas de lectura

```
    https://bks_api-1-k1625606.deta.app/book
```
