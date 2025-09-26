from typing import Optional, List, Dict, Any


class UDFBuilder:
    """
    Builder for a User-Defined Field (UDF).
    Represents a single field to be added to a UDT.
    """

    def __init__(self, name: str, field_type: str):
        """
        Initializes a UDF definition.

        Args:
            name (str): Field name (e.g., "CustomerName"). Must be unique within the table.
            field_type (str): Field type (e.g., "db_Alpha", "db_Float", "db_Date").
        """
        self.name = name
        self.type = field_type
        self.size: Optional[int] = None
        self.description: Optional[str] = None
        self.subtype: Optional[str] = None
        self.default_value: Optional[str] = None
        self.mandatory: str = "tNO"  # "tYES" or "tNO"

    def with_size(self, size: int) -> "UDFBuilder":
        """Sets the field size (for string types)."""
        self.size = size
        return self

    def with_description(self, description: str) -> "UDFBuilder":
        """Sets the field description."""
        self.description = description
        return self

    def with_subtype(self, subtype: str) -> "UDFBuilder":
        """
        Sets the field subtype (e.g., "st_Sum" for totals, "st_Price" for prices).
        """
        self.subtype = subtype
        return self

    def mandatory(self) -> "UDFBuilder":
        """Marks the field as mandatory."""
        self.mandatory = "tYES"
        return self

    def with_default(self, value: str) -> "UDFBuilder":
        """Sets a default value."""
        self.default_value = value
        return self

    def build(self) -> Dict[str, Any]:
        """Builds the UDF payload for /UserFieldsMD."""
        payload = {
            "Name": self.name,
            "Type": self.type,
            "TableName": self._table_name,  # Will be set by UDTBuilder
            "Mandatory": self.mandatory,
        }
        if self.size is not None:
            payload["Size"] = self.size
            payload["EditSize"] = self.size
        if self.description:
            payload["Description"] = self.description
        if self.subtype:
            payload["SubType"] = self.subtype
        if self.default_value:
            payload["DefaultValue"] = self.default_value
        return payload

    def _bind_to_table(self, table_name: str) -> None:
        """Internal method to bind this UDF to a table name."""
        self._table_name = table_name


class UDTBuilder:
    """
    Builder for a User-Defined Table (UDT).
    Supports main and child tables (e.g., document and document lines).
    """

    def __init__(self, table_name: str, table_type: str):
        """
        Initializes a UDT definition.

        Args:
            table_name (str): Logical table name (e.g., "MyOrder").
            table_type (str): Table type (e.g., "bott_Document", "bott_DocumentLines", "bott_NoObject").
        """
        self.table_name = table_name
        self.table_type = table_type
        self.description: Optional[str] = None
        self._fields: List[UDFBuilder] = []

    def with_description(self, description: str) -> "UDTBuilder":
        """Sets the table description."""
        self.description = description
        return self

    def add_field(self, field: UDFBuilder) -> "UDTBuilder":
        """Adds a UDF to this table."""
        self._fields.append(field)
        return self

    def build_table_payload(self) -> Dict[str, Any]:
        """Builds the payload for /UserTablesMD."""
        payload = {
            "TableName": self.table_name,
            "TableType": self.table_type,
        }
        if self.description:
            payload["TableDescription"] = self.description
        return payload

    def build_fields_payloads(self) -> List[Dict[str, Any]]:
        """Builds a list of UDF payloads for /UserFieldsMD."""
        table_db_name = f"@{self.table_name.upper()}"
        for field in self._fields:
            field._bind_to_table(table_db_name)
        return [field.build() for field in self._fields]


class UDOBuilder:
    """
    Builder for a User-Defined Object (UDO).
    Combines a main UDT and optional child UDTs into a registered UDO.
    """

    def __init__(self, code: str, name: str, main_table: str, object_type: str):
        """
        Initializes a UDO definition.

        Args:
            code (str): Unique UDO code (e.g., "MyOrder").
            name (str): Display name (e.g., "My Orders").
            main_table (str): Main UDT name (must match a UDTBuilder.table_name).
            object_type (str): Object type (e.g., "boud_Document", "boud_MasterData").
        """
        self.code = code
        self.name = name
        self.main_table = main_table
        self.object_type = object_type
        self._child_tables: List[UDTBuilder] = []
        self.can_cancel: str = "tNO"
        self.can_close: str = "tNO"

    def add_child_table(self, child_table: UDTBuilder) -> "UDOBuilder":
        """Adds a child UDT (e.g., document lines)."""
        self._child_tables.append(child_table)
        return self

    def enable_cancel(self) -> "UDOBuilder":
        """Enables the Cancel action for this UDO."""
        self.can_cancel = "tYES"
        return self

    def enable_close(self) -> "UDOBuilder":
        """Enables the Close action for this UDO."""
        self.can_close = "tYES"
        return self

    def build(self) -> Dict[str, Any]:
        """Builds the payload for /UserObjectsMD."""
        child_entries = []
        for child in self._child_tables:
            child_entries.append({
                "TableName": child.table_name,
                "ObjectName": child.table_name  # Default: same as table name
            })

        payload = {
            "Code": self.code,
            "Name": self.name,
            "TableName": self.main_table,
            "ObjectType": self.object_type,
            "CanCancel": self.can_cancel,
            "CanClose": self.can_close,
        }
        if child_entries:
            payload["UserObjectMD_ChildTables"] = child_entries
        return payload