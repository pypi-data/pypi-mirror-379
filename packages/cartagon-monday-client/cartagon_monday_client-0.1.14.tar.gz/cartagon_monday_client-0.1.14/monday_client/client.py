from ftplib import all_errors
import requests
import json
from .exceptions import MondayAPIError
from .utils import monday_request
from .fragments import ALL_COLUMNS_FRAGMENT
import logging
from datetime import datetime


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # o configurable vía entorno




class MondayClient:
    def __init__(self, api_key: str, base_url: str = "https://api.monday.com/v2"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": api_key,
            "Content-Type": "application/json",
            "API-Version": "2025-01"
        }

    def execute_query(
        self,
        query: str,
        *,
        return_key: str | None = None,
        log_query_preview: bool = False
        ) -> dict:
        """
        Ejecuta una consulta/mutación GraphQL contra Monday y maneja errores de forma explícita.

        Parámetros
        ----------
        query : str
            Cadena GraphQL completa (query o mutation) con los argumentos inline o uso de variables
            si tu util monday_request las soporta internamente.
        return_key : str | None, opcional
            Si se indica, devuelve directamente `data[return_key]`. Útil para mutaciones
            que siempre devuelven un nodo raíz conocido (p. ej. "create_item").
        log_query_preview : bool, opcional
            Si True, registra una vista previa de la query (primeras ~200 chars) para facilitar el debug.

        Returns
        -------
        dict
            El objeto `data` de GraphQL (o `data[return_key]` si se ha indicado).

        Raises
        ------
        ValueError
            Si `query` está vacía o no es string.
        MondayAPIError
            Si la API devuelve `errors` o la respuesta no contiene `data`.
        """
        import time

        if not isinstance(query, str) or not query.strip():
            raise ValueError("execute_query: 'query' debe ser una cadena GraphQL no vacía")

        t0 = time.time()
        if log_query_preview:
            # Evitamos volcar todo por si hay datos sensibles
            preview = " ".join(query.split())[:200]
            logger.debug("GraphQL preview: %s%s", preview, "…" if len(preview) == 200 else "")

        resp = monday_request(query, self.api_key)  # mantiene tu flujo actual
        dt = (time.time() - t0) * 1000
        logger.debug("GraphQL ejecutado en %.1f ms", dt)

        # Validación de estructura
        if not isinstance(resp, dict):
            raise MondayAPIError(f"Respuesta inválida (tipo {type(resp).__name__}): {resp!r}")

        # Manejo detallado de errores GraphQL
        if "errors" in resp and resp["errors"]:
            # Extraemos el primer error relevante para el mensaje
            err = resp["errors"][0]
            msg = err.get("message") or "Error GraphQL"
            path = ".".join(str(p) for p in (err.get("path") or [])) or None
            code = (err.get("extensions") or {}).get("code")
            reset = (err.get("extensions") or {}).get("reset_in_x_seconds")

            details = [msg]
            if code:
                details.append(f"code={code}")
            if path:
                details.append(f"path={path}")
            if reset is not None:
                details.append(f"retry_in={reset}s")

            # Incluimos todos los errores en debug para autopsia posterior
            logger.debug("GraphQL errors: %s", resp["errors"])
            raise MondayAPIError(" | ".join(details))

        if "data" not in resp:
            raise MondayAPIError(f"Respuesta inesperada (sin 'data'): {resp!r}")

        data = resp["data"]

        if return_key is not None:
            if return_key not in data:
                raise MondayAPIError(
                    f"Clave '{return_key}' no encontrada en data. Claves disponibles: {list(data.keys())}"
                )
            return data[return_key]

        return data

    def test_connection(self) -> bool:
        """
        Verifica si la API de Monday.com está accesible y válida para la clave proporcionada.

        Envía una consulta sencilla al endpoint `me` y comprueba si la respuesta
        incluye el objeto de usuario actual.

        Returns
        -------
        bool
            True si la llamada GraphQL devolvió un objeto `me` válido; False si
            ocurrió un error (clave inválida, sin permisos, u otros errores de API).
        """
        query = """
        query {
            me {
                id
                name
                email
            }
        }
        """
        try:
            data = self.execute_query(query)
            return "me" in data
        except MondayAPIError:
            return False

    def get_boards(
        self, 
        limit: int = 10, 
        page: int = 1, 
        fields: list[str] | None = None
        ) -> list[dict]:
        
        """
        Devuelve una lista de tableros de Monday.com con paginación sencilla.

        Construye y ejecuta una consulta GraphQL para obtener hasta `limit`
        tableros en la página `page`, solicitando los campos indicados.

        Parameters
        ----------
        limit : int, optional
            Número máximo de tableros a devolver por llamada (por defecto 10).
        page : int, optional
            Índice de página a recuperar (debe ser >= 1; por defecto 1).
        fields : list[str] | None, optional
            Lista de campos GraphQL a solicitar para cada tablero. Si es None,
            se usan por defecto ['id', 'name', 'workspace_id', 'state', 'board_kind'].

        Returns
        -------
        list[dict]
            Lista de diccionarios, cada uno representando un tablero con los campos
            solicitados.

        Raises
        ------
        ValueError
            Si `page` es menor que 1.
        MondayAPIError
            Si la consulta GraphQL falla o devuelve errores.
        """
        
        if page < 1:
            raise ValueError("page debe ser >= 1")
        if not fields:
            fields = fields or ["id", "name", "workspace_id", "state", "board_kind"]
            fields_block = "\n".join(fields)
            # fields_block = "id name column_values { ... }"
        else:
            fields_block = fields
        
        query = f"""
        query {{
          boards(limit: {limit}, page: {page}) {{
            {fields_block}
          }}
        }}
        """
        return self.execute_query(query)["boards"]

    def get_all_items(
        self,
        board_id: int,
        limit: int = 50,
        fields: list[str] | None = None,
        columns_ids: list[str] | None = None
    ) -> list[dict]:
        """
        Recupera todos los ítems de un tablero de Monday.com, utilizando paginación por cursor.

        Se realiza una primera llamada anidada en `boards { items_page }` para obtener
        la primera página de hasta `limit` ítems y su `cursor`. A continuación, mientras
        exista un `cursor`, se consulta `next_items_page` para seguir obteniendo más ítems
        hasta agotarlos todos.

        Parameters
        ----------
        board_id : int
            Identificador del tablero del que extraer los ítems.
        limit : int, optional
            Número máximo de ítems a devolver por página (por defecto 50).
        fields : list[str] | None, optional
            Lista de campos GraphQL a solicitar para cada ítem. Si es None,
            se usarán por defecto `['id', 'name', 'column_values{...}']`
            Con todos los tipos de columnas diferentes en la query, ... on xxxx.
        columns_ids : list[str] | None, optional
            Lista de IDs de columnas para filtrar los `column_values`. Si se
            proporciona, solo se devuelven valores de esas columnas; si es None,
            se devuelven todas las columnas definidas en el template interno.

        Returns
        -------
        list[dict]
            Lista de diccionarios, uno por cada ítem del tablero, con los campos solicitados.

        Raises
        ------
        MondayAPIError
            Si la llamada GraphQL falla tras los reintentos configurados.
        """
        
        
          
        
        if columns_ids:
          ids = f'(ids:{json.dumps(columns_ids)})'
        else:
          ids = ""
        
        if not fields:
            fields = ["id", "name", f"column_values {{ {ALL_COLUMNS_FRAGMENT} }}"]
            fields_block = "\n".join(fields)
            # fields_block = "id name column_values { ... }"
        else:
            fields_block = fields

        # 1) Primera página: items_page anidado en boards
        query_first = f"""
        query {{
          boards(ids: [{board_id}]) {{
            items_page(limit: {limit}) {{
              cursor
              items {{
                {fields_block}
              }}
            }}
          }}
        }}
        """

        
        data = self.execute_query(query_first)
        boards = data.get("boards", [])
        if not boards:
            logger.warning("No se recuperó ningún tablero para board_id=%s", board_id)
            return []  # devolvemos lista vacía si no existe/está vacío

        
        
        page   = data["boards"][0]["items_page"]
        items  = page["items"]
        cursor = page.get("cursor")
        
        

        # 2) Mientras exista cursor, usar next_items_page en el root
        while cursor:
            query_next = f"""
            query {{
              next_items_page(limit: {limit}, cursor: "{cursor}") {{
                cursor
                items {{
                  {fields_block}
                }}
              }}
            }}
            """
            data = self.execute_query(query_next)
            page = data["next_items_page"]
            items.extend(page["items"])
            cursor = page.get("cursor")

        return items


    def create_item(
            self,
            board_id: int,
            item_name: str,
            group_id: str | None = None,
            column_values: dict | None = None
            ) -> dict:
        """
        Crea un nuevo ítem en un tablero de Monday.com usando una mutación GraphQL inline.

        Construye todos los argumentos (board_id, item_name, group_id y column_values)
        directamente en la cadena de la mutación, serializando `column_values` como
        JSON escapado para evitar el uso de variables externas.

        Parameters
        ----------
        board_id : int
            ID del tablero donde se creará el ítem.
        item_name : str
            Texto que se asignará como nombre al nuevo ítem.
        group_id : str | None, optional
            ID del grupo dentro del tablero; si es None, Monday.com usará
            el grupo por defecto.
        column_values : dict | None, optional
            Diccionario con pares columna→valor para inicializar campos. Ejemplo:
                {
                    "texto_id": "Contenido inicial",
                    "estado_id": {"label": "Done"},
                    "numero_id": 42
                }

        Returns
        -------
        dict
            Datos devueltos por la mutación `create_item`, normalmente un dict con
            las claves `"id"` y `"name"` del ítem creado.

        Raises
        ------
        MondayAPIError
            Si la petición GraphQL falla o la API devuelve errores (por ejemplo,
            tablero o grupo inexistente, permisos insuficientes, formato inválido).
        """
        # Construimos la lista de argumentos en formato GraphQL
        args_parts = [
            f"board_id: {board_id}",
            f'item_name: "{item_name}"',
            "create_labels_if_missing: true",
        ]
        if group_id:
            args_parts.append(f'group_id: "{group_id}"')
        
        if column_values is not None:
            # 1) Serializamos el dict a JSON normal:
            json_payload = json.dumps(column_values)
            # 2) Lo serializamos de nuevo para que sea un string JSON escapado:
            escaped = json.dumps(json_payload)
            # ahora escaped es algo como "\"{\\\"col\\\":\\\"val\\\"}\""
            args_parts.append(f"column_values: {escaped}")

        # Unimos todo con comas
        args_str = ", ".join(args_parts)

        # Montamos la mutación con los args inline
        query = f"""
        mutation {{
        create_item({args_str}) {{
            id
            name
        }}
        }}
        """
        print('Query para crear ítem:', query)  # Debug: mostramos la query completa
        # Llamamos a execute_query solo con la query
        data = self.execute_query(query)
        return data["create_item"]
    
    
    def create_subitem(
            self,
            parent_item_id: int,
            subitem_name: str,
            column_values:dict | None = None
            ):
        """
        Crea un nuevo subítem en un ítem de Monday.com usando una mutación GraphQL inline.

        Construye todos los argumentos (parent_item_id, subitem_name) directamente
        en la cadena de la mutación.

        Parameters
        ----------
        parent_item_id : int
            ID del ítem padre donde se creará el subítem.
        subitem_name : str
            Texto que se asignará como nombre al nuevo subítem.
        column_values : dict | None, optional
            Diccionario con pares columna→valor para inicializar campos. Ejemplo:
                {
                    "texto_id": "Contenido inicial",
                    "estado_id": {"label": "Done"},
                    "numero_id": 42
                }

        Returns
        -------
        dict
            Datos devueltos por la mutación `create_subitem`, normalmente un dict con
            las claves `"id"` y `"name"` del subítem creado.

        Raises
        ------
        MondayAPIError
            Si la petición GraphQL falla o la API devuelve errores (por ejemplo,
            ítem padre inexistente, permisos insuficientes).
        """
        # Construimos la lista de argumentos en formato GraphQL
        args_parts = [
            f"parent_item_id: {parent_item_id}",
            f'item_name: "{subitem_name}"',
            "create_labels_if_missing: true",
        ]
        
        if column_values is not None:
            # 1) Serializamos el dict a JSON normal:
            json_payload = json.dumps(column_values)
            # 2) Lo serializamos de nuevo para que sea un string JSON escapado:
            escaped = json.dumps(json_payload)
            # ahora escaped es algo como "\"{\\\"col\\\":\\\"val\\\"}\""
            args_parts.append(f"column_values: {escaped}")

        # Unimos todo con comas
        args_str = ", ".join(args_parts)

        # Montamos la mutación con los args inline
        query = f"""
            mutation {{
                create_subitem({args_str}) {{
                    id
                    board {{
                        id
                        }}
                        }}
                }}"""
        
        # Llamamos a execute_query solo con la query
        data = self.execute_query(query)
        
        return data["create_subitem"]
    
    


    def update_simple_column_value(
            self,
            item_id: int,
            board_id: int,
            column_id: str,
            value: str
            ) -> dict:
        """
        Actualiza el valor de una única columna simple en un ítem de Monday.com.

        Construye la mutación GraphQL inline inyectando directamente los
        parámetros, sin uso de variables.

        Parámetros
        ----------
        item_id : int
            ID del ítem que se va a modificar.
        board_id : int
            ID del tablero que contiene el ítem.
        column_id : str
            ID de la columna simple a actualizar (por ejemplo texto, número, fecha).
        value : str
            Nuevo valor para la columna (siempre como cadena).

        Devuelve
        -------
        dict
            Resultado de la mutación `change_simple_column_value`, normalmente
            un dict con la clave `"id"` del ítem actualizado.

        Lanza
        -----
        MondayAPIError
            Si la petición GraphQL falla o la API devuelve errores
            (por ejemplo, columna inexistente o permisos insuficientes).
        """
        # 1) Construimos el mutation inline sin variables GraphQL
        query = f"""
        mutation {{
        change_simple_column_value(
            item_id: {item_id},
            board_id: {board_id},
            create_labels_if_missing: true,
            column_id: "{column_id}",
            value: "{value}"
        ) {{
            id
        }}
        }}
        """
        print("Query para cambiar valor de columna simple: %s", query)
        
        
        # 2) Llamamos a execute_query sólo con la query
        data = self.execute_query(query)

        # 3) Devolvemos el bloque change_simple_column_value
        return data["change_simple_column_value"]


    def update_multiple_column_values(
            self,
            item_id: int,
            board_id: int,
            column_values: dict
        ) -> dict:
        """
        Actualiza varios valores de columnas de un ítem en Monday.com en una sola llamada.

        Serializa internamente `column_values` como un string JSON escapado para
        inyectarlo directamente en la mutación GraphQL, sin usar variables
        externas. El diccionario `column_values` debe seguir el formato de la
        API de Monday.com, por ejemplo:

            {
                "text_column_id": "Nuevo texto",
                "status_column_id": {"label": "Done"},
                "numbers_column_id": 123.45
            }

        Parameters
        ----------
        item_id : int
            ID del ítem a actualizar.
        board_id : int
            ID del tablero donde está el ítem.
        column_values : dict
            Diccionario con pares columna→valor.
            EJEMPLO:
            column_values = {
                "text_mkspdtnk": "test",
                "board_relation_mksr28n3": {
                    "item_ids": ["1744185415"]
                },
                "dropdown_mksr4677":{
                    "labels": ["fghcf"]
                },
                "text_mksp6y2d":"dfhsdf"
            }

        Returns
        -------
        dict
            Información del cambio (campo id).

        Raises
        ------
        MondayAPIError
            Si la petición GraphQL falla o devuelve errores (IDs inválidos,
            permisos, etc.).
        """
        import json

        # 1) Serializamos column_values a JSON “normal”
        json_payload = json.dumps(column_values)
        # 2) Lo serializamos de nuevo para que GraphQL lo reciba como un string escapado
        escaped = json.dumps(json_payload)

        # 3) Montamos la mutación inline
        query = f"""
        mutation {{
        change_multiple_column_values(
            item_id: {item_id},
            board_id: {board_id},
            create_labels_if_missing: true,
            column_values: {escaped}
        ) {{
            id
        }}
        }}
        """

        # 4) Ejecutamos sólo con la query
        data = self.execute_query(query)

        # 5) Devolvemos el resultado
        return data["change_multiple_column_values"]



    def get_items_by_column_value(
        self,
        board_id: int,
        column_id: str,
        value: str,
        fields: list[str] | None = None,
        operator: str = "any_of",
        limit: int = 200
    ) -> list[dict]:
        """
        Recupera uno o varios ítems de un tablero filtrando por el valor de una columna,
        y paginando automáticamente hasta obtener todos los resultados o agotar el cursor.

        Ejecuta primero una consulta anidada en `boards { items_page }` con filtro
        `query_params.rules`, y luego, mientras el campo `cursor` no sea null,
        va solicitando páginas adicionales a `next_items_page` en el root, acumulando
        todos los ítems en una lista.

        Parameters
        ----------
        board_id : int
            ID del tablero de Monday.com donde buscar.
        column_id : str
            ID de la columna en la que aplicar el filtro.
        value : str
            Valor que se comparará contra el contenido de la columna.
        fields : list[str] | None, optional
            Lista de campos GraphQL a solicitar para cada ítem. Si es None,
            se usarán por defecto `['id', 'name', 'column_values{...}']`
            Con todos los tipos de columnas diferentes en la query, ... on xxxx.
        operator : str, optional
            Operador de comparación permitido por GraphQL (e.g. `any_of`, `not_any_of`,
            `is_empty`, `greater_than`, `contains_text`, etc.). Por defecto `"any_of"`.
            Lista completa de operadores en la doc: any_of, not_any_of, is_empty,
            is_not_empty, greater_than, greater_than_or_equals, lower_than,
            lower_than_or_equal, between, contains_text, not_contains_text,
            contains_terms, starts_with, ends_with, within_the_next,
            within_the_last :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}.
        limit : int, optional
            Número máximo de ítems a devolver por página (por defecto 1).

        Returns
        -------
        list[dict]
            Lista de diccionarios, uno por cada ítem filtrado. Cada dict incluye
            las claves `id`, `name` y `column_values` (con `column.id`, `column.title`
            y `text`).

        Raises
        ------
        MondayAPIError
            Si la consulta GraphQL falla o la API devuelve errores.
        """
        # Montamos la primera consulta con filtro en items_page
        
        if not fields:
            fields = ["id", "name", f"column_values {{ {ALL_COLUMNS_FRAGMENT} }}"]
            fields_block = "\n".join(fields)
            # fields_block = "id name column_values { ... }"
        else:
            fields_block = fields
        
        
        query_first = f"""
        query {{
        boards(ids: [{board_id}]) {{
            items_page(
            limit: {limit},
            query_params: {{
                rules: [{{
                column_id: "{column_id}",
                compare_value: ["{value}"],
                operator: {operator}
                }}]
            }}
            ) {{
            cursor
            items {{
                {fields_block}
            }}
            }}
        }}
        }}
        """

        data = self.execute_query(query_first)
        boards = data.get("boards", [])
        if not boards:
            return []

        page = boards[0]["items_page"]
        items = page.get("items", [])
        cursor = page.get("cursor")

        # Paginación: obtener siguientes páginas desde next_items_page
        while cursor:
            query_next = f"""
            query {{
            next_items_page(
                limit: {limit},
                cursor: "{cursor}"
            ) {{
                cursor
                items {{
                {fields_block}
                }}
            }}
            }}
            """
            nxt = self.execute_query(query_next)
            page = nxt.get("next_items_page", {})
            items.extend(page.get("items", []))
            cursor = page.get("cursor")

        return items
        
        
        
    def get_item(self,
                item_id: int,
                columns_ids: list[str] | None = None) -> dict:
        """
        Obtiene un ítem específico de Monday.com por su ID.

        Parameters
        ----------
        item_id : int
            ID del ítem a obtener.
        columns_ids : list[str] | None, optional
            Lista de IDs de columnas a incluir en la respuesta. Si es None, se
            devolverán todas las columnas.

        Returns
        -------
        dict
            Diccionario con los datos del ítem, incluyendo sus columnas y valores.

        Raises
        ------
        MondayAPIError
            Si la consulta GraphQL falla o la API devuelve errores.
        """
        # 1) argumento para column_values
        if columns_ids:
            # json.dumps -> '["sadfg","sdfs"]'
            cols_list = json.dumps(columns_ids)
            ids_arg = f"(ids:{cols_list})"
        else:
            ids_arg = ""
        
        query = f'''
            query {{
            items(ids:{item_id}) {{
                name
                id
                column_values{ids_arg} {{
                column{{
                    title
                    id
                }}
                {ALL_COLUMNS_FRAGMENT}
                }}
            }}
            }}
        '''
        
        response = self.execute_query(query)
        items = response.get("items", [])
        
        if not items:
            raise MondayAPIError(f"No se encontró el ítem con ID {item_id}")

        return items[0]
    
    
    
    def board_columns(self, board_id: str) -> list[dict]:
        """
        Obtiene las columnas de un tablero específico de Monday.com.

        Parameters
        ----------
        board_id : int
            ID del tablero cuyas columnas se quieren obtener.

        Returns
        -------
        list[dict]
            Lista de diccionarios, cada uno con los campos `id`, `title`, `type`,
            `settings_str` y `width`.

        Raises
        ------
        MondayAPIError
            Si la consulta GraphQL falla o la API devuelve errores.
        """
        query = f"""
        query {{
            boards(ids: [{board_id}]) {{
                columns {{
                    id
                    title
                    type
                }}
            }}
        }}
        """

        response = self.execute_query(query)
        boards = response.get("boards", [])

        if not boards:
            raise MondayAPIError(f"No se encontró el tablero con ID {board_id}")

        return boards[0]["columns"]
    
    
    def item_columns(self, item_id: str) -> list[dict]:
        """
        Obtiene las columnas de un ítem específico de Monday.com.
        Crea un subitem en un item del tablero, obtiene las columnas y despues lo borra

        Parameters
        ----------
        item_id : int
            ID del ítem cuyas columnas se quieren obtener.

        Returns
        -------
        list[dict]
            Lista de diccionarios, cada uno con los campos `id`, `title`, `type`,
            `settings_str` y `width`.

        Raises
        ------
        MondayAPIError
            Si la consulta GraphQL falla o la API devuelve errores.
        """
        query = f"""
        query {{
            items(ids: [{item_id}]) {{
                column_values {{
                    column {{
                        id
                        title
                        type
                    }}
                }}
            }}
        }}
        """

        response = self.execute_query(query)
        items = response.get("items", [])

        if not items:
            raise MondayAPIError(f"No se encontró el ítem con ID {item_id}")

        return items[0]["column_values"]
    
    
    


    def subitems_columns(self, board_id:str) -> list[dict]:
        """
        Obtiene las columnas de los subitems de un tablero específico de Monday.com.
        Crea un subitem en un item del tablero, obtiene las columnas y despues lo borra

        Parameters
        ----------
        board : str
            ID del tablero cuyas columnas se quieren obtener.

        Returns
        -------
        list[dict]
            Lista de diccionarios, cada uno con los campos `id`, `title`, `type`,
            `settings_str` y `width`.

        Raises
        ------
        MondayAPIError
            Si la consulta GraphQL falla o la API devuelve errores.
        """
        
        
        # Obtener 1 item del tablero para crear un subitem
        item_id = self.get_all_items(board_id)[0]['id']
                
        #crear un subitem a ese item padre
        subitem = self.create_subitem(item_id,'FLAG')
        
        subitem_id = subitem.get("id")
        
        if not subitem_id:
            raise MondayAPIError(f"No se pudo crear el subitem para verificar las columnas")
        
        subitem_board_id = subitem.get("board", {}).get("id")
        
        #obtener las columnas del subitem_board_id
        columns = self.board_columns(subitem_board_id)
       
        

        #borrar el subitem creado
        delete = self.delete_item(subitem_id)

        if delete is not True:
            raise MondayAPIError(f"No se pudo borrar el subitem")
        
        
        return columns


      
    def delete_item(self, item_id: str) -> None:
        """
        Elimina un ítem específico de Monday.com por su ID.

        Parameters
        ----------
        item_id : int
            ID del ítem a eliminar.

        Raises
        ------
        MondayAPIError
            Si la consulta GraphQL falla o la API devuelve errores.
        """
        query = f"""
        mutation {{
            delete_item(
                item_id: {item_id}
            ) {{
                id
            }}
        }}
        """

        response = self.execute_query(query)
        if "errors" in response:
            raise MondayAPIError(f"Error al eliminar el ítem con ID {item_id}: {response['errors']}")
        
        return True
    
    
    

    def create_item_update(self,
                            item_id: str,
                            body: str,
                            mention_user:list[dict] = []) -> dict:
            """
            Crea un cambio (update) para un ítem específico en Monday.com.

            Parameters
            ----------
            item_id : str
                ID del ítem al que se le realizará el cambio.
            body : str
                Cuerpo del cambio en formato HTML.
            mention_user : list[dict]
                Lista de diccionarios con los usuarios y tipo a mencionar en el cambio.

            Returns
            -------
            dict
                Diccionario con los datos del cambio creado, incluyendo su ID
                Ejemplo: [{id: 1234567890, type: User}].

            Raises
            ------
            MondayAPIError
                Si la consulta GraphQL falla o la API devuelve errores.
            """
            
            if mention_user:
                clean_mentions = json.dumps(mention_user).replace('"', '')
                mention_user = f"mentions_list:{clean_mentions}"
            else:
                mention_user = ""
            
            
            
            
            query = f"""
            mutation {{
                create_update(
                    item_id: {item_id},
                    body: "{body}",
                    {mention_user}
                ) {{
                    id
                }}
            }}
            """
            
            print(f'query = {query}')

            response = self.execute_query(query)
            if "errors" in response:
                raise MondayAPIError(f"Error al crear el cambio para el ítem con ID {item_id}: {response['errors']}")

            return response["create_update"]
        
        
    def create_column_values(self,columns: list[dict], fail_on_duplicate=True):
        """
            Construye un diccionario con los valores de columnas para Monday API.

            Parámetros
            ----------
            columns : list[dict]
                Lista de columnas con el formato:
                [
                    {
                        "id": "column_id",        # ID de la columna en Monday
                        "value": "column_value",  # Valor de la columna
                        "type": "column_type"     # Tipo de la columna
                    },
                    ...
                ]

            fail_on_duplicate : bool, opcional
                Si True (default), lanza un error al encontrar IDs de columna repetidos.
                Si False, el último valor sobreescribe al anterior.

            Tipos soportados
            ----------------
            - checkbox → bool
                {"checked": true/false}

            - board_relation → list[int]
                {"item_ids": [id1, id2, ...]}

            - date → dict con {"date": "YYYY-MM-DD", "time": "HH:MM" (opcional)}

            - dropdown → str o list[str]
                {"labels": ["Opción1", "Opción2", ...]}

            - email → str o dict con {"email": "...", "text": "..."}
                Si se pasa string, se usa como email y como text.

            - link → str o dict con {"url": "...", "text": "..."}
                Si se pasa string, se usa como url y como text.

            - long_text → str

            - name → str
                (aunque normalmente se pasa fuera de column_values en create_item,
                aquí se soporta para updates)

            - numbers → int | float | str numérico
                Siempre se envía como string.

            - people → list[int | dict]
                - Si se pasa int → {"id": int, "kind": "person"}
                - Si se pasa dict → {"id": int, "kind": "person|team"}

            - phone → str o dict con {"phone": "...", "countryShortName": "..."}
                El número se normaliza (sin espacios, guiones ni paréntesis).

            - status → str (label) o int (index)

            - text → str

            - timeline → dict con {"from": "YYYY-MM-DD", "to": "YYYY-MM-DD"}

            Retorno
            -------
            dict
                Diccionario listo para usar en `column_values`, donde cada clave es
                el `column_id` y el valor corresponde al formato esperado por Monday.
            
            Ejemplo
            -------
            >>> create_column_values([
            ...     {"id": "text_col", "value": "Hola mundo", "type": "text"},
            ...     {"id": "status_col", "value": "Working on it", "type": "status"}
            ... ])
            {
                "text_col": "Hola mundo",
                "status_col": {"label": "Working on it"}
        }
        """
        column_values = {}
        
        for col in columns:
            col_id   = col["id"]
            col_type = col.get("type")
            raw_val  = col.get("value")
            
            if col_id in column_values:
                if fail_on_duplicate:
                    raise ValueError(f"Column id duplicada: {col_id}")
                # Si no fallas, aquí podrías combinar según el tipo.
        
            if col_type == 'checkbox':
                value = {'checked': bool(raw_val)}
            elif col_type == 'board_relation':
                if not isinstance(raw_val, (list, tuple)):
                    raise TypeError(f"{col_id}: board_relation espera lista de IDs")
                value = {'item_ids': list(raw_val)}
            elif col_type == 'date':
                if not isinstance(raw_val, dict):
                    raise TypeError(f"{col_id}: date espera diccionario con al menos 'date'")
                # Validar fecha
                try:
                    datetime.strptime(raw_val['date'], "%Y-%m-%d")
                except (KeyError, ValueError):
                    raise ValueError(f"{col_id}: 'date' debe estar en formato YYYY-MM-DD")
                value = {"date": raw_val['date']}
                # Validar hora si viene
                if 'time' in raw_val:
                    try:
                        datetime.strptime(raw_val['time'], "%H:%M")
                    except ValueError:
                        raise ValueError(f"{col_id}: 'time' debe estar en formato HH:MM (24h)")
                    value["time"] = raw_val['time']
            elif col_type == "dropdown":
                if isinstance(raw_val, str):
                    # Caso: un único valor
                    value = {"labels": [raw_val]}
                elif isinstance(raw_val, (list, tuple)):
                    # Caso: lista de valores
                    if not all(isinstance(v, str) for v in raw_val):
                        raise TypeError(f"{col_id}: dropdown espera lista de strings")
                    value = {"labels": list(raw_val)}
                else:
                    raise TypeError(f"{col_id}: dropdown espera string o lista de strings")
                
            elif col_type == "email":
                if isinstance(raw_val, str):
                    # Si solo pasan un email en string, lo convertimos
                    value = {"email": raw_val, "text": raw_val}
                elif isinstance(raw_val, dict) and "email" in raw_val:
                    if not isinstance(raw_val["email"], str):
                        raise TypeError(f"{col_id}: 'email' debe ser string")
                    value = {
                        "email": raw_val["email"],
                        "text": raw_val.get("text", raw_val["email"])
                    }
                else:
                    raise TypeError(f"{col_id}: email espera string o dict con 'email'")
            
            elif col_type == "link":
                if isinstance(raw_val, str):
                    # Si solo pasan un string, lo tomamos como url y lo usamos también como texto
                    value = {"url": raw_val, "text": raw_val}
                elif isinstance(raw_val, dict) and "url" in raw_val:
                    if not isinstance(raw_val["url"], str):
                        raise TypeError(f"{col_id}: 'url' debe ser string")
                    value = {
                        "url": raw_val["url"],
                        "text": raw_val.get("text", raw_val["url"])
                    }
                else:
                    raise TypeError(f"{col_id}: link espera string o dict con 'url'")
            
            elif col_type == "long_text":
                if not isinstance(raw_val, str):
                    raise TypeError(f"{col_id}: long_text espera un string")
                value = raw_val
                
            elif col_type == "name":
                if not isinstance(raw_val, str):
                    raise TypeError(f"{col_id}: name espera un string")
                # en lugar de meterlo en column_values, lo devolvemos en otro campo
                value = raw_val
                
            elif col_type == "numbers":
                if not isinstance(raw_val, (int, float, str)):
                    raise TypeError(f"{col_id}: numbers espera int, float o string numérico")
                try:
                    # Validamos que realmente se puede convertir a número
                    float(raw_val)
                except ValueError:
                    raise ValueError(f"{col_id}: numbers debe contener un valor numérico válido")
                value = str(raw_val)               
             
            elif col_type == "people":
                if not isinstance(raw_val, (list, tuple)):
                    raise TypeError(f"{col_id}: people espera lista de IDs o lista de dicts con id/kind")

                persons_and_teams = []
                for entry in raw_val:
                    if isinstance(entry, int):
                        # int = persona por defecto
                        persons_and_teams.append({"id": entry, "kind": "person"})
                    elif isinstance(entry, dict):
                        uid = entry.get("id")
                        kind = entry.get("kind", "person")  # por defecto "person" si no se especifica
                        if kind not in ("person", "team"):
                            raise ValueError(f"{col_id}: 'kind' debe ser 'person' o 'team'")
                        persons_and_teams.append({"id": uid, "kind": kind})
                    else:
                        raise TypeError(f"{col_id}: cada valor debe ser int (persona) o dict con id/kind")

                value = {"personsAndTeams": persons_and_teams}
                
            elif col_type == "phone":
                if isinstance(raw_val, str):
                    # Limpiamos espacios, guiones y paréntesis
                    phone_clean = raw_val.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
                    value = {"phone": phone_clean, "countryShortName": ""}
                elif isinstance(raw_val, dict) and "phone" in raw_val:
                    if not isinstance(raw_val["phone"], str):
                        raise TypeError(f"{col_id}: 'phone' debe ser string")
                    phone_clean = (
                        raw_val["phone"]
                        .replace(" ", "")
                        .replace("-", "")
                        .replace("(", "")
                        .replace(")", "")
                    )
                    value = {
                        "phone": phone_clean,
                        "countryShortName": raw_val.get("countryShortName", "")
                    }
                else:
                    raise TypeError(f"{col_id}: phone espera string o dict con 'phone'")
            
            
            elif col_type == "status":
                if isinstance(raw_val, str):
                    value = {"label": raw_val}
                elif isinstance(raw_val, int):
                    value = {"index": raw_val}
                else:
                    raise TypeError(f"{col_id}: status espera string (label) o int (index)")
            
            elif col_type == "text":
                if not isinstance(raw_val, str):
                    raise TypeError(f"{col_id}: text espera un string")
                value = raw_val
            
            elif col_type == "timeline":
                if not isinstance(raw_val, dict) or not {"from", "to"}.issubset(raw_val):
                    raise TypeError(f"{col_id}: timeline espera dict con 'from' y 'to' en formato YYYY-MM-DD")

                try:
                    datetime.strptime(raw_val["from"], "%Y-%m-%d")
                    datetime.strptime(raw_val["to"], "%Y-%m-%d")
                except ValueError:
                    raise ValueError(f"{col_id}: 'from' y 'to' deben estar en formato YYYY-MM-DD")

                value = {"from": raw_val["from"], "to": raw_val["to"]}
            
            
            
            
            
            
            
            
            
            
            
                        
                        
            column_values[col_id] = value
                
        
        
        return column_values

