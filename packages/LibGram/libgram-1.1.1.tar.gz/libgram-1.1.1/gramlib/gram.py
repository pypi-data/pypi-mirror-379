

import json
import asyncio
from pathlib import Path
from typing import Any, Dict, List, Optional, Callable
from enum import Enum
from dataclasses import dataclass

__version__ = "1.1.1"
__author__ = "GramLib Team"

class DataType(Enum):
    """Data types for table columns"""
    STRING = "string"
    INTEGER = "integer" 
    FLOAT = "float"
    BOOLEAN = "boolean"
    JSON = "json"

@dataclass
class TableConfig:
    """Table configuration"""
    name: str
    columns: Dict[str, Dict] = None
    data: List[Dict] = None

class Gramdb:
    """Main database class"""
    
    def init(self, name: str, gram: bool = True):
        """
        Initialize database
        
        Args:
            name: Database name
            gram: If True - creates .gram file, if False - .json
        """
        self.name = name
        self.extension = ".gram" if gram else ".json"
        self.file_path = Path(f"{name}{self.extension}")
        self.tables: Dict[str, TableConfig] = {}
        
    def str(self):
        return f"Gramdb(name='{self.name}', extension='{self.extension}')"

class GramLib:
    """Main class for working with tables via decorators"""
    
    def init(self, db: Gramdb):
        """
        Initialize GramLib
        
        Args:
            db: Gramdb database object
        """
        self.db = db
        self._current_table: Optional[str] = None
        
    def create_table(self, table_name: str):
        """
        Decorator for table creation
        
        Example:
            @gram.create_table("users")
            async def create_users_table(gram):
                gram.column("id", DataType.INTEGER, primary_key=True)
                await gram.create_table()
        """
        def decorator(func: Callable):
            async def wrapper(*args, **kwargs):
                table_config = TableConfig(name=table_name)
                self.db.tables[table_name] = table_config
                self._current_table = table_name
                result = await func(self, *args, **kwargs)
                return result
            return wrapper
        return decorator
    
    def with_table(self, table_name: str):
        """
        Decorator for table operations
        
        Example:
            @gram.with_table("users")
            async def add_user(gram):
                await gram.insert(name="John")
        """
        def decorator(func: Callable):
            async def wrapper(*args, **kwargs):
                self._current_table = table_name
                if table_name not in self.db.tables:
                    raise ValueError(f"Table '{table_name}' not found")
                return await func(self, *args, **kwargs)
            return wrapper
        return decorator
    
    async def create_table(self):
        """
        Create table (called from create_table decorator)
        Automatically overwrites existing file without asking
        """
        if not self._current_table:
            raise ValueError("No table selected")
        
        table_config = self.db.tables[self._current_table]
        
        structure = {
            "metadata": {
                "name": table_config.name,
                "columns": table_config.columns or {},
                "created_at": str(asyncio.get_event_loop().time())
            },
            "data": table_config.data or []
        }
        
        # Автоматически перезаписываем файл без проверок
        with open(self.db.file_path, 'w', encoding='utf-8') as f:
            json.dump(structure, f, indent=2, ensure_ascii=False)
        
        # Сообщаем, если файл был перезаписан
        if self.db.file_path.exists():
            print(f"Таблица '{self._current_table}' перезаписана успешно!")
        else:
            print(f"Таблица '{self._current_table}' создана успешно!")
        
        return True
    
    def column(self, name: str, type: DataType, primary_key: bool = False, 
               unique: bool = False, nullable: bool = True, default: Any = None):
        """
        Add column to current table
        
        Args:
            name: Column name
            type: Data type (DataType)
            primary_key: Primary key
            unique: Unique value
            nullable: Can be null
            default: Default value
        """
        if not self._current_table:
            raise ValueError("No table selected")
        
        table_config = self.db.tables[self._current_table]
        if table_config.columns is None:
            table_config.columns = {}
            
        table_config.columns[name] = {
            "type": type.value,
            "primary_key": primary_key,
            "unique": unique,
            "nullable": nullable,
            "default": default
        }
        return self
    
    async def insert(self, **kwargs) -> int:
        """
        Insert data into table
        
        Args:
            **kwargs: Data to insert (column_name=value)
            
        Returns:
            ID of new record
        """
        if not self._current_table:
            raise ValueError("No table selected")
        
        # Load existing data or create new structure
        if self.db.file_path.exists():
            with open(self.db.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            # If file doesn't exist, create basic structure
            table_config = self.db.tables[self._current_table]
            data = {
                "metadata": {
                    "name": table_config.name,
                    "columns": table_config.columns or {},
                    "created_at": str(asyncio.get_event_loop().time())
                },
                "data": []
            }
        
        data["data"].append(kwargs)
        
        with open(self.db.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return len(data["data"])
    
    async def select(self, *columns: str, where: Optional[Dict] = None) -> List[Dict]:
        """
        Select data from table
        
        Args:
            *columns: Columns to select (empty for all columns)
            where: Filter conditions {field: value}
            
        Returns:
            List of records
        """
        if not self._current_table:
            raise ValueError("No table selected")
        
        if not self.db.file_path.exists():
            return []
        
        with open(self.db.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        results = []
        for record in data.get("data", []):
            if where is None or all(record.get(k) == v for k, v in where.items()):
                if columns:
                    filtered_record = {col: record.get(col) for col in columns}
                    results.append(filtered_record)
                else:
                    results.append(record)
        
        return results
    
    async def update(self, where: Dict, **kwargs) -> int:
        """
        Update data in table
        
        Args:
            where: Conditions to find records
            **kwargs: New values
            
        Returns:
            Number of updated records
        """
        if not self._current_table:
            raise ValueError("No table selected")
        
        if not self.db.file_path.exists():
            return 0
        
        with open(self.db.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            updated_count = 0
        for record in data["data"]:
            if all(record.get(k) == v for k, v in where.items()):
                record.update(kwargs)
                updated_count += 1
        
        if updated_count > 0:
            with open(self.db.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        
        return updated_count
    
    async def delete(self, where: Dict) -> int:
        """
        Delete data from table
        
        Args:
            where: Conditions to find records
            
        Returns:
            Number of deleted records
        """
        if not self._current_table:
            raise ValueError("No table selected")
        
        if not self.db.file_path.exists():
            return 0
        
        with open(self.db.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        initial_count = len(data["data"])
        data["data"] = [record for record in data["data"] 
                       if not all(record.get(k) == v for k, v in where.items())]
        
        deleted_count = initial_count - len(data["data"])
        
        if deleted_count > 0:
            with open(self.db.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        
        return deleted_count
    
    async def count(self, where: Optional[Dict] = None) -> int:
        """
        Count records
        
        Args:
            where: Filter conditions
            
        Returns:
            Number of records
        """
        records = await self.select(where=where)
        return len(records)

# Alias for compatibility
GramDatabase = Gramdb
