"""
Future objects for asynchronous task execution.

This module provides Future objects that represent the result of an asynchronous
computation, similar to concurrent.futures.Future but optimized for the hybrid executor.
"""

import threading
import time
from typing import Any, Optional, Union
from concurrent.futures import TimeoutError


class Future:
    """
    Represents the result of an asynchronous computation.
    
    A Future object represents a computation that may or may not have completed.
    It provides methods to check if the computation is done, get the result,
    or handle exceptions.
    """
    
    def __init__(self):
        """Initialize a new Future object."""
        self._result = None
        self._exception = None
        self._done = False
        self._lock = threading.Lock()
        self._condition = threading.Condition(self._lock)
    
    def result(self, timeout: Optional[float] = None) -> Any:
        """
        Return the result of the computation.
        
        Args:
            timeout: Maximum time to wait for the result in seconds.
                    If None, wait indefinitely.
        
        Returns:
            The result of the computation.
            
        Raises:
            TimeoutError: If the computation doesn't complete within timeout.
            Exception: If the computation raised an exception.
        """
        with self._condition:
            if not self._done:
                if timeout is None:
                    self._condition.wait()
                else:
                    if not self._condition.wait(timeout):
                        raise TimeoutError(f"Future result not available after {timeout} seconds")
            
            if self._exception is not None:
                raise self._exception
            
            return self._result
    
    def done(self) -> bool:
        """
        Return True if the computation is done.
        
        Returns:
            True if the computation is done, False otherwise.
        """
        with self._lock:
            return self._done
    
    def exception(self, timeout: Optional[float] = None) -> Optional[Exception]:
        """
        Return the exception raised by the computation.
        
        Args:
            timeout: Maximum time to wait for the computation to complete.
                    If None, wait indefinitely.
        
        Returns:
            The exception raised by the computation, or None if no exception.
            
        Raises:
            TimeoutError: If the computation doesn't complete within timeout.
        """
        with self._condition:
            if not self._done:
                if timeout is None:
                    self._condition.wait()
                else:
                    if not self._condition.wait(timeout):
                        raise TimeoutError(f"Future exception not available after {timeout} seconds")
            
            return self._exception
    
    def _set_result(self, result: Any) -> None:
        """
        Set the result of the computation.
        
        Args:
            result: The result of the computation.
        """
        with self._condition:
            self._result = result
            self._done = True
            self._condition.notify_all()
    
    def _set_exception(self, exception: Exception) -> None:
        """
        Set the exception raised by the computation.
        
        Args:
            exception: The exception raised by the computation.
        """
        with self._condition:
            self._exception = exception
            self._done = True
            self._condition.notify_all()
    
    def __repr__(self) -> str:
        """Return string representation of the Future."""
        with self._lock:
            if self._done:
                if self._exception is not None:
                    return f"Future(exception={self._exception})"
                else:
                    return f"Future(result={self._result})"
            else:
                return "Future(pending)"
