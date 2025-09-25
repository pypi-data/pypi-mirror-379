"""
Atomic primitives for thread-safe operations in Python 3.13+ without GIL.

This module provides atomic integer and boolean operations that are safe for
concurrent access across multiple threads.
"""

import threading
from typing import Union


class AtomicInt:
    """
    Thread-safe atomic integer with basic operations.
    
    Provides atomic get() and increment() operations that are safe for
    concurrent access across multiple threads.
    """
    
    def __init__(self, initial_value: int = 0):
        """
        Initialize atomic integer with initial value.
        
        Args:
            initial_value: Initial value for the atomic integer
        """
        self._value = initial_value
        self._lock = threading.Lock()
    
    def get(self) -> int:
        """
        Get the current value atomically.
        
        Returns:
            Current value of the atomic integer
        """
        with self._lock:
            return self._value
    
    def increment(self, delta: int = 1) -> int:
        """
        Increment the value atomically and return the new value.
        
        Args:
            delta: Amount to increment by (default: 1)
            
        Returns:
            New value after increment
        """
        with self._lock:
            self._value += delta
            return self._value
    
    def set(self, value: int) -> None:
        """
        Set the value atomically.
        
        Args:
            value: New value to set
        """
        with self._lock:
            self._value = value
    
    def __repr__(self) -> str:
        return f"AtomicInt({self.get()})"


class AtomicBool:
    """
    Thread-safe atomic boolean with basic operations.
    
    Provides atomic get() and set() operations that are safe for
    concurrent access across multiple threads.
    """
    
    def __init__(self, initial_value: bool = False):
        """
        Initialize atomic boolean with initial value.
        
        Args:
            initial_value: Initial value for the atomic boolean
        """
        self._value = initial_value
        self._lock = threading.Lock()
    
    def get(self) -> bool:
        """
        Get the current value atomically.
        
        Returns:
            Current value of the atomic boolean
        """
        with self._lock:
            return self._value
    
    def set(self, value: bool) -> None:
        """
        Set the value atomically.
        
        Args:
            value: New value to set
        """
        with self._lock:
            self._value = value
    
    def __bool__(self) -> bool:
        """Allow boolean conversion."""
        return self.get()
    
    def __repr__(self) -> str:
        return f"AtomicBool({self.get()})"
