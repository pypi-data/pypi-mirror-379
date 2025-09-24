"""
GramLib - Simple and powerful data management library with decorators
"""

import json
import asyncio
from pathlib import Path
from typing import Any, Dict, List, Optional, Callable
from enum import Enum
from dataclasses import dataclass

__version__ = "2.0.0"
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
    
    def __init__(self, name: str, gram: bool = True):
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
        
    def __str__(self):
        return f"Gramdb(name='{self.name}', extension='{self.extension}')"

class GramLib:
    """Main class for working with tables via decorators"""
    
    def __init__(self, db: Gramdb):
        self.db = db
        self._current_table: Optional[str] = None
        
    def create_table(self, table_name: str):
        """
        Decorator for table creation - ПРАВИЛЬНАЯ РЕАЛИЗАЦИЯ
        """
        def decorator(func: Callable):
            def sync_wrapper(*args, **kwargs):
                # Создаем асинхронную обертку
                async def async_wrapper():
                    # Устанавливаем текущую таблицу
                    table_config = TableConfig(name=table_name)
                    self.db.tables[table_name] = table_config
                    self._current_table = table_name
                    
                    # Вызываем функцию пользователя
                    return await func(self)
                
                # Возвращаем корутину
                return async_wrapper()
            
            return sync_wrapper
        return decorator
    
    def with_table(self, table_name: str):
        """
        Decorator for table operations - ПРАВИЛЬНАЯ РЕАЛИЗАЦИЯ
        """
        def decorator(func: Callable):
            def sync_wrapper(*args, **kwargs):
                # Создаем асинхронную обертку
                async def async_wrapper():
                    self._current_table = table_name
                    if table_name not in self.db.tables:
                        raise ValueError(f"Table '{table_name}' not found")
                    
                    # Вызываем функцию пользователя
                    return await func(self)
                
                # Возвращаем корутину
                return async_wrapper()
            
            return sync_wrapper
        return decorator
    
    async def create_table(self):
        """Create table"""
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
        
        with open(self.db.file_path, 'w', encoding='utf-8') as f:
            json.dump(structure, f, indent=2, ensure_ascii=False)
        
        print(f"Table '{self._current_table}' created successfully!")
        return True
    
    def column(self, name: str, type: DataType, primary_key: bool = False, 
               unique: bool = False, nullable: bool = True, default: Any = None):
        """Add column to current table"""
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
        """Insert data into table"""
        if not self._current_table:
            raise ValueError("No table selected")
        
        if self.db.file_path.exists():
            with open(self.db.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = {"metadata": {"columns": {}}, "data": []}
        
        data["data"].append(kwargs)
        
        with open(self.db.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return len(data["data"])
    
    async def select(self, *columns: str, where: Optional[Dict] = None) -> List[Dict]:
        """Select data from table"""
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
        """Update data in table"""
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
        """Delete data from table"""
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
        """Count records"""
        records = await self.select(where=where)
        return len(records)

# Alias for compatibility
GramDatabase = Gramdb