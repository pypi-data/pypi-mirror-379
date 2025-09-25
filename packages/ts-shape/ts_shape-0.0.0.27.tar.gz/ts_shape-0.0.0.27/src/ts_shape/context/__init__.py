"""Context

Utilities for enriching DataFrames with contextual information and mappings.

Classes:
- ValueMapper: Map categorical codes to readable values from external files.
  - map_values: Merge and replace a target column using a CSV/JSON mapping table.
  - _load_mapping_table: Load a mapping table from CSV or JSON.
"""
