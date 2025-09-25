import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class NODE_MT_category_layout(_bpy_types.Menu):
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def draw(self, _context) -> None:
        """

        :param _context:
        """

def add_closure_zone(layout, label) -> None: ...
def add_color_mix_node(context, layout) -> None: ...
def add_empty_group(layout) -> None: ...
def add_foreach_geometry_element_zone(layout, label) -> None: ...
def add_node_type(
    layout, node_type, *, label=None, poll=None, search_weight=0.0, translate=True
) -> None:
    """Add a node type to a menu."""

def add_node_type_with_outputs(
    context, layout, node_type, subnames, *, label=None, search_weight=0.0
) -> None: ...
def add_node_type_with_searchable_enum(
    context, layout, node_idname, property_name, search_weight=0.0
) -> None: ...
def add_node_type_with_searchable_enum_socket(
    context, layout, node_idname, socket_identifier, enum_names, search_weight=0.0
) -> None: ...
def add_repeat_zone(layout, label) -> None: ...
def add_simulation_zone(layout, label) -> None:
    """Add simulation zone to a menu."""

def draw_assets_for_catalog(layout, catalog_path) -> None: ...
def draw_node_group_add_menu(context, layout) -> None:
    """Add items to the layout used for interacting with node groups."""

def draw_root_assets(layout) -> None: ...
