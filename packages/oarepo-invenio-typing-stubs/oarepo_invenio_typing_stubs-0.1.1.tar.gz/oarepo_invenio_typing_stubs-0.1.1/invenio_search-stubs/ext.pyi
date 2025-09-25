from typing import Any, Iterable

from flask import Flask

class _SearchState:
    app: Flask
    mappings: dict[str, str]
    aliases: dict[str, dict[str, str]]
    templates: dict[str, str]
    component_templates: dict[str, str]
    index_templates: dict[str, str]
    current_suffix: str
    client: Any
    cluster_version: list[int]
    cluster_distribution: str
    active_aliases: dict[str, dict[str, str]]

    def register_mappings(self, alias: str, package_name: str) -> None: ...
    def register_templates(self, module: str) -> dict[str, str]: ...
    def load_entry_point_group_mappings(
        self, entry_point_group_mappings: str
    ) -> None: ...
    def create(
        self,
        ignore: list[int] | None = ...,
        ignore_existing: bool = ...,
        index_list: list[str] | None = ...,
    ) -> Iterable[tuple[str, Any]]: ...
    def create_index(
        self,
        index: str,
        mapping_path: str | None = ...,
        prefix: str | None = ...,
        suffix: str | None = ...,
        create_write_alias: bool = ...,
        ignore: list[int] | None = ...,
        dry_run: bool = ...,
    ) -> tuple[tuple[str, Any | None], tuple[str | None, Any | None]]: ...
    def update_mapping(self, index: str, check: bool = ...) -> None: ...
    def put_templates(
        self, ignore: list[int] | None = ...
    ) -> Iterable[tuple[str, Any]]: ...
    def put_component_templates(
        self, ignore: list[int] | None = ...
    ) -> Iterable[tuple[str, Any]]: ...
    def put_index_templates(
        self, ignore: list[int] | None = ...
    ) -> Iterable[tuple[str, Any]]: ...
    def delete(
        self, ignore: list[int] | None = ..., index_list: list[str] | None = ...
    ) -> Iterable[tuple[str, Any]]: ...
    def flush_and_refresh(self, index: str) -> bool: ...

class InvenioSearch:
    _state: _SearchState

    def __init__(self, app: Flask | None = None, **kwargs: Any) -> None: ...
    def init_app(
        self,
        app: Flask,
        entry_point_group_mappings: str = ...,
        entry_point_group_templates: str = ...,
        entry_point_group_component_templates: str = ...,
        entry_point_group_index_templates: str = ...,
        **kwargs: Any,
    ) -> None: ...
    @staticmethod
    def init_config(app: Flask) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
