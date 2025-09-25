# cartagon-monday-client

Cliente **Python** para integraciones con la **API GraphQL de Monday.com**.  
Incluye manejo de reintentos (HTTP 5xx, 403 vacíos, `ComplexityException`), paginación con `items_page` → `next_items_page`, y utilidades para crear/actualizar ítems, filtrar por columnas y obtener ítems individuales.

> **Requisitos**: Python **3.10+** (usa anotaciones como `str | None`).

---

## Instalación

```bash
pip install cartagon-monday-client
```

> El **nombre de importación** es con **guion bajo**:

```python
from cartagon_monday_client.client import MondayClient
```

---

## Inicio rápido

```python
from cartagon_monday_client.client import MondayClient

token = "TU_API_TOKEN"  # Genera el token en Monday.com (perfil de desarrollador)
client = MondayClient(api_key=token)

# 1) Probar conexión
print(client.test_connection())  # True si la API responde y el token es válido

# 2) Listar tableros
boards = client.get_boards(limit=5, page=1)
for b in boards:
    print(f"{b['id']}: {b['name']}")

# 3) Obtener todos los ítems de un board (paginación automática)
items = client.get_all_items(board_id=123456789, limit=100)
print("Total ítems:", len(items))

# 4) Filtrar ítems por valor de columna (con paginación)
results = client.get_items_by_column_value(
    board_id=123456789,
    column_id="status",
    value="Done",
    operator="any_of",  # ver operadores abajo
    limit=50            # por página
)
print("Resultados filtrados:", len(results))

# 5) Crear un ítem
nuevo = client.create_item(
    board_id=123456789,
    item_name="Tarea de ejemplo",
    column_values={"status": {"label": "Stuck"}}
)
print("Ítem creado:", nuevo)

# 6) Actualizar columna simple
upd1 = client.update_simple_column_value(
    item_id=987654321,
    board_id=123456789,
    column_id="text_column",
    value="Texto actualizado"
)
print("Update simple:", upd1)

# 7) Actualizar múltiples columnas
upd2 = client.update_multiple_column_values(
    item_id=987654321,
    board_id=123456789,
    column_values={
        "status": {"label": "Done"},
        "priority": {"label": "High"}
    }
)
print("Update múltiple:", upd2)

# 8) Obtener un ítem por ID (opcionalmente filtrando columnas)
item = client.get_item(item_id=987654321, columns_ids=["status", "text_column"])
print(item)
```

---

## Qué hace este cliente

- **Reintentos inteligentes** (`monday_request`):
  - Reintenta automáticamente ante **HTTP 5xx**, **403** con respuesta vacía y **`ComplexityException`** (con espera indicada/estimada).
  - Para otros errores GraphQL **no retriables** (p. ej. `InvalidBoardIdException`), **lanza de inmediato** `MondayAPIError` con el mensaje real de la API.
- **Paginación por cursor**:
  - **Primera página**: `boards { items_page(limit: ...) { cursor, items { ... } } }`
  - **Siguientes**: `next_items_page(cursor: ..., limit: ...)` hasta que `cursor` sea `null`.
- **Mutaciones con `column_values`**:
  - Monday requiere un **string JSON**; el cliente hace la **doble serialización** internamente para que GraphQL lo acepte.
- **Fragmento reutilizable de columnas**:
  - Se usa un fragmento grande para `column_values` que incluye tipos comunes (texto, status, people, tags, relation, link, date, numbers, etc.).

---

## API de `MondayClient`

### `MondayClient(api_key: str, base_url: str = "https://api.monday.com/v2")`
Crea la instancia autenticada.

---

### `test_connection() -> bool`
Verifica la conectividad mediante la consulta `me`.

---

### `get_boards(limit: int = 10, page: int = 1, fields: list[str] | None = None) -> list[dict]`
Devuelve tableros con paginación simple.
- `fields` por defecto: `["id", "name", "workspace_id", "state", "board_kind"]`.

**Ejemplo**
```python
boards = client.get_boards(limit=5, page=1)
```

---

### `get_all_items(board_id: int, limit: int = 50, fields: list[str] | None = None, columns_ids: list[str] | None = None) -> list[dict]`
Devuelve **todos** los ítems del tablero `board_id` usando cursor.
- Si pasas `columns_ids`, aplica `column_values(ids: [...])` para limitar columnas.
- Usa un fragmento amplio con múltiples tipos de columna (texto, date, status, people, dropdown, timeline, link, numbers, formula, doc, checkbox, phone, world clock, location, country, dependency, email, hour, rating, tags, time tracking, creation log, color picker, last updated, item id, vote, button, mirror, file, long text, board relation).

**Ejemplo**
```python
items = client.get_all_items(board_id=123456789, limit=100)
```

---

### `get_items_by_column_value(board_id: int, column_id: str, value: str, operator: str = "any_of", limit: int = 1) -> list[dict]`
Filtra ítems por valor de **una columna** con `query_params.rules` y pagina automáticamente.

**Operadores habituales**  
> (La disponibilidad depende del tipo de columna)
- Selección / equivalencia: `any_of`, `not_any_of`
- Vacío / no vacío: `is_empty`, `is_not_empty`
- Texto: `contains_text`, `not_contains_text`, `contains_terms`, `starts_with`, `ends_with`
- Numérico / Fecha: `greater_than`, `greater_than_or_equals`, `lower_than`, `lower_than_or_equal`, `between`
- Intervalos relativos (fechas): `within_the_next`, `within_the_last`

**Ejemplo**
```python
results = client.get_items_by_column_value(
    board_id=123456789,
    column_id="status",
    value="Done",
    operator="any_of",
    limit=50
)
```

---

### `create_item(board_id: int, item_name: str, group_id: str | None = None, column_values: dict | None = None) -> dict`
Crea un ítem en el tablero.
- Inserta argumentos **inline**; `column_values` se serializa como **string JSON** (requisito de Monday).

**Ejemplo**
```python
new_item = client.create_item(
    board_id=123456789,
    item_name="Tarea de ejemplo",
    column_values={"status": {"label": "Working on it"}}
)
```

---

### `update_simple_column_value(item_id: int, board_id: int, column_id: str, value: str) -> dict`
Actualiza el valor de **una columna simple** (texto, número, fecha…).

**Ejemplo**
```python
resp = client.update_simple_column_value(
    item_id=987654321,
    board_id=123456789,
    column_id="text_column",
    value="Texto actualizado"
)
```

---

### `update_multiple_column_values(item_id: int, board_id: int, column_values: dict) -> dict`
Actualiza **varias columnas** en un único llamado.
- `column_values` se convierte a **string JSON** (doble `json.dumps`).

**Ejemplo**
```python
resp = client.update_multiple_column_values(
    item_id=987654321,
    board_id=123456789,
    column_values={
        "status": {"label": "Done"},
        "priority": {"label": "High"}
    }
)
```

---

### `get_item(item_id: int, columns_ids: list[str] | None = None) -> dict`
Obtiene un ítem por ID.  
- Si `columns_ids` no es `None`, limita `column_values` a esas columnas (`ids: [...]`).  
- Lanza `MondayAPIError` si el ítem no existe.

**Ejemplo**
```python
item = client.get_item(item_id=987654321, columns_ids=["status","text_column"])
```

---

## Manejo de errores

- **Errores retriables**:
  - **HTTP 5xx** → reintento.
  - **HTTP 403** con respuesta vacía → reintento.
  - **`ComplexityException`** → espera indicada/estimada y reintento.
- **Errores no retriables**:
  - Cualquier otro error GraphQL (p. ej. *InvalidBoardIdException*) → **se lanza inmediatamente** `MondayAPIError` con el mensaje real.
- **Agotamiento de reintentos**:
  - Lanza `MondayAPIError([{"message": "Max retries reached"}])`.

---

## Desarrollo y tests (opcional)

Instala las dependencias de desarrollo con *extras*:

```bash
pip install cartagon-monday-client[dev]
# o, si estás en el repo local:
pip install .[dev]
```

Ejecutar tests:

```bash
pytest -q
```

---

## Licencia

**MIT** — ver archivo `LICENSE`.

---

## Enlaces

- PyPI: https://pypi.org/project/cartagon-monday-client/
- (Si el repo es público) Código fuente / Issues: añade aquí la URL de tu repositorio.
