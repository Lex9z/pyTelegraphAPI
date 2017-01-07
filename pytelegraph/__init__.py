#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pytelegraph.elements
import pytelegraph.worker

class Telegraph:
	
	def __init__(self):
		self.access_token = None

	def create_account(self, short_name, author_name, author_url):
		'''Crea una cuenta nueva en Telegraph.

		Con este método podéis crear un cuenta nueva. Será
		retorndo un objeto `Account`, el cual tendrá también
		un `access_token`: útil para realizar cambios futuros.

		:param short_name: corto nombre usado para la identificación interna.
		:param author_name: nombre usado en cada artículo.
		:param author_url: URL que hace referencia al autor.
		'''
		pass

	def edit_account_info(self, access_token, short_name=None, author_name=None, author_url=None):
		'''Edita la información de una cuenta.

		Con este método podéis editar la información de un
		cuenta en Telegraph, los argumentos que tengan valor
		`None` no serán enviados, por eso, sólo los valores
		recibidos serán editados.

		:param access_token: token de acceso a la cuenta de telegraph.
		:param short_name: si es definido, cambiamos el short_name.
		:param author_name: si es definido, cambiamos el author_name.
		:param author_url: si es definido, cambiamos el author_url.
		'''
		pass

	def get_account_info(self, access_token, fields):
		'''Obtiene información de la cuenta.

		Este método'permite obtener información de dicha cuenta.
		Para este, tenéis que especificar en la tupla `fields` el
		campo requerido. Los campos disponibles son: short_name,
		author_name, author_url, auth_url, page_count.

		:param access_token: token de acceso a la cuenta de telegraph.
		:param fields: tupla que contiene una lista de string con los campos requeridos.

		Ejemplo:
		>>> get_account_info(access_token=..., fields=('auth_url', 'page_count'))
		'''
		pass

	def revoke_access_token(self, access_token):
		'''Cambia el token de una cuenta de Telegraph.

		Este método recibe el anterior token de la cuenta
		de Telegraph y retorna uno nuevo.

		:param access_token: token antigua de la cuenta de telegraph.
		'''
		pass

	def create_page(self, access_token, title, author_name, author_url, content, return_content=False):
		'''Crea una nueva página/artículo.

		Permite crear un nuevo artículo, con los datos enviados.
		Si return_content es `True`, será retornado un objeto
		`Page`.

		:param access_token: token de acceso a la cuenta de telegraph.
		:param title: título del artículo.
		:param author_name: nombre a mostrar del autor.
		:param author_url: URL del perfil del autor.
		:param content: lista de objetos `Node`, ver http://telegra.ph/api#Node
		:param return_content: toma valor `True` para retornar un objeto `Page`. Es `False` por defecto.
		'''
		pass

	def edit_page(self, access_token, path, title, content, author_name, author_url, return_content=False):
		'''Permite editar un artículo existente.

		Al terminar, retorna un objeto `Page`.

		:param access_token: token de acceso a la cuenta de telegraph.
		:param path: ruta del artículo.
		:param title: título del artículo.
		:param content: contenido del artículo, lista de `Node`, ver http://telegra.ph/api#Node
		:param author_name: nombre del autor, se mostrará bajo el título del artículo.
		:param author_url: URL del perfil del autor.
		:param return_content: toma valor `True` para retornar un objeto `Page`. Es `False` por defecto.
		'''
		pass

	def get_page(self, path, return_content=False):
		'''Retorna un objeto `Page` con la página solicitada.

		:param path: ruta del artículo.
		:param return_content: toma valor `True` para retornar un objeto `Page`. Es `False` por defecto.
		'''
		pass

	def get_page_list(self, access_token, offset=0, limit=50):
		'''Permite obtener una lista de páginas de dicha cuenta.

		Retorna una lista, ordenada por orden de creación, perteneciente
		a la cuenta de Telegraph. Lo retorna mediante un objeto
		`PageList`.

		:param access_token: token de acceso a la cuenta de telegraph.
		:param offset: número secuencial de la primera página a devolver.
		:param limit: limites de página a devolver.
		'''
		pass

	def get_views(self, path, year, month, day, hour):
		'''Retorna el número de vistas de una página en un tiempo específico.

		:param path: ruta del artículo.
		:param year: entero que indica el año para buscar.
		:param month: entero que indica el mes para buscar.
		:param day: entero que indica el día para buscar.
		:param hour: entero que indica la hora para buscar.
		'''
		pass