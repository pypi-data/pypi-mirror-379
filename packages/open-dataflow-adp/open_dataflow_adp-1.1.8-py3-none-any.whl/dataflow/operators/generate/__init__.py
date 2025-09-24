from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Import from Text2SQL subdirectory
    from .Text2SQL.text2sql_generator import Text2SQLGenerator

else:
    import sys
    from dataflow.utils.registry import LazyLoader, generate_import_structure_from_type_checking

    cur_path = "dataflow/operators/generate/"
    _import_structure = generate_import_structure_from_type_checking(__file__, cur_path)
    sys.modules[__name__] = LazyLoader(__name__, "dataflow/operators/generate/", _import_structure)