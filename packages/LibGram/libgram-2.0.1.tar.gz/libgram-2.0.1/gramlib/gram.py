"""
GramLib - Simple and powerful data management library with decorators
"""

import json
import asyncio
from pathlib import Path
from typing import Any, Dict, List, Optional, Callable
from enum import Enum

__version__ = "2.0.1"
__author__ = "GramLib Team"

class DataType(Enum):
    """Data types for table columns"""
    STRING = "string"
    INTEGER = "integer" 
    FLOAT = "float"
    BOOLEAN = "boolean"
    JSON = "json"

class Gramdb:
    """Main database class"""
    
    def __init__(self, name: str, gram: bool = True):
        """
        Initialize database
        
        Args:
            name: Database name (without extension)
            gram: If True - creates .gram file, if False - .json
        """
        self.name = name.split('.')[0]  # Remove extension if present
        self.extension = ".gram" if gram else ".json"
        self.file_path = Path(f"{self.name}{self.extension}")
        
    def __str__(self):
        return f"Gramdb(name='{self.name}', extension='{self.extension}')"

class GramLib:
    """Main class for working with tables"""
    
    def __init__(self, db: Gramdb):
        """
        Initialize GramLib
        
        Args:
            db: Gramdb database object
        """
        self.db = db
        self.current_table = None
        self._columns = {}
    
    # ПРОСТОЙ И НАДЕЖНЫЙ МЕТОД СОЗДАНИЯ ТАБЛИЦЫ
    async def create_table(self, table_name: str, columns: Dict[str, Dict] = None):
        """
        Create table with specified columns
        
        Args:
            table_name: Name of the table
            columns: Dictionary of column definitions
        """
        self.current_table = table_name
        self._columns = columns or {}
        
        structure = {
            "metadata": {
                "name": table_name,
                "columns": self._columns,
                "created_at": str(asyncio.get_event_loop().time())
            },
            "data": []
        }
        
        # Create directory if it doesn't exist
        self.db.file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.db.file_path, 'w', encoding='utf-8') as f:
            json.dump(structure, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"✓ Table '{table_name}' created successfully!")
        return True
    
    # ПРОСТОЙ МЕТОД ДОБАВЛЕНИЯ КОЛОНОК
    def add_column(self, name: str, type: DataType, primary_key: bool = False, 
                   unique: bool = False, nullable: bool = True, default: Any = None):
        """
        Add column to current table
        
        Args:
            name: Column name
            type: Data type
            primary_key: Is primary key
            unique: Unique constraint
            nullable: Can be null
            default: Default value
        """
        if not self.current_table:
            raise ValueError("No table selected. Call create_table() first.")
        
        self._columns[name] = {
            "type": type.value,
            "primary_key": primary_key,
            "unique": unique,
            "nullable": nullable,
            "default": default
        }
        return self
    
    # УНИВЕРСАЛЬНЫЙ МЕТОД ДЛЯ УСТАНОВКИ ТАБЛИЦЫ
    def set_table(self, table_name: str):
        """Set current table for operations"""
        self.current_table = table_name
        return self
    
    # ОСНОВНЫЕ CRUD ОПЕРАЦИИ
    async def insert(self, **kwargs) -> int:
        """Insert data into current table"""
        if not self.current_table:
            raise ValueError("No table selected. Call set_table() first.")
        
        if not self.db.file_path.exists():
            raise FileNotFoundError(f"Database file '{self.db.file_path}' not found.")
        
        # Load existing data
        with open(self.db.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Add new record
        data["data"].append(kwargs)
        
        # Save back
        with open(self.db.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        
        return len(data["data"])
    
    async def select(self, *columns: str, where: Optional[Dict] = None) -> List[Dict]:
        """Select data from current table"""
        if not self.current_table:
            raise ValueError("No table selected. Call set_table() first.")
        
        if not self.db.file_path.exists():
            return []
        
        with open(self.db.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        results = []
        for record in data.get("data", []):
            # Apply WHERE clause if specified
            if where is None or all(record.get(k) == v for k, v in where.items()):
                # Select specific columns or all
                if columns:
                    filtered_record = {col: record.get(col) for col in columns}
                    results.append(filtered_record)
                else:
                    results.append(record)
        
        return results
    
    async def update(self, where: Dict, **kwargs) -> int:
        """Update records in current table"""
        if not self.current_table:
            raise ValueError("No table selected. Call set_table() first.")
        
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
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        
        return updated_count
    
    async def delete(self, where: Dict) -> int:
        """Delete records from current table"""
        if not self.current_table:
            raise ValueError("No table selected. Call set_table() first.")
        
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
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        
        return deleted_count
    
    async def count(self, where: Optional[Dict] = None) -> int:
        """Count records in current table"""
        records = await self.select(where=where)
        return len(records)
    
    # ДОПОЛНИТЕЛЬНЫЕ МЕТОДЫ
    async def table_exists(self) -> bool:
        """Check if table file exists"""
        return self.db.file_path.exists()
    
    async def get_table_info(self) -> Dict:
        """Get table metadata"""
        if not self.db.file_path.exists():
            return {}
        
        with open(self.db.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return data.get("metadata", {})
    
    async def clear_table(self) -> bool:
        """Clear all data from table (keep structure)"""
        if not self.current_table:
            raise ValueError("No table selected.")
        
        if not self.db.file_path.exists():
            return False
        
        with open(self.db.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        data["data"] = []
        
        with open(self.db.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        
        return True

# Alias for compatibility
GramDatabase = Gramdb