"""
Python Multirunner - Advanced hybrid executor for Python 3.13+ without GIL.

This package provides a high-performance executor that supports:
- CPU-bound and async/await operations
- Distributed execution across multiple machines
- GPU task execution
- Advanced scheduling algorithms
- Work stealing and priority queues
- Performance monitoring and profiling
- Integration with popular async frameworks
- Atomic primitives for thread-safe operations
"""

from .executor import (
    HybridExecutor, 
    TaskType, 
    SchedulingAlgorithm, 
    NodeInfo, 
    TaskMetrics
)
from .future import Future
from .primitives import AtomicInt, AtomicBool

__version__ = "0.1.0"
__author__ = "Raphael Raasch"
__email__ = "devraasch@gmail.com"

__all__ = [
    "HybridExecutor",
    "TaskType",
    "SchedulingAlgorithm", 
    "NodeInfo",
    "TaskMetrics",
    "Future", 
    "AtomicInt",
    "AtomicBool",
]
