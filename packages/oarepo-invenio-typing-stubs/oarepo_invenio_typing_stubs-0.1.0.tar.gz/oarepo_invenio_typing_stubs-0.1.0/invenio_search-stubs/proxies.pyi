from typing import Any
from werkzeug.local import LocalProxy

current_search: LocalProxy[Any]
current_search_client: LocalProxy[Any]
