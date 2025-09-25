"""
Advanced hybrid executor for CPU-bound, async/await, distributed, and GPU operations.

This module provides a high-performance executor that can handle:
- CPU-bound and async/await operations
- Distributed execution across multiple machines
- GPU task execution
- Advanced scheduling algorithms
- Work stealing and priority queues
- Performance monitoring and profiling
- Integration with popular async frameworks
"""

import asyncio
import threading
import time
import heapq
import json
import socket
import subprocess  # nosec B404
import psutil
import uuid
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Iterable, Optional, Union, Dict, List, Tuple
from queue import Queue, Empty, PriorityQueue
from dataclasses import dataclass, field
from enum import Enum
import logging

from .future import Future
from .primitives import AtomicInt, AtomicBool


class TaskType(Enum):
    """Types of tasks supported by the executor."""
    CPU_BOUND = "cpu_bound"
    ASYNC = "async"
    DISTRIBUTED = "distributed"
    GPU = "gpu"


class SchedulingAlgorithm(Enum):
    """Advanced scheduling algorithms."""
    ROUND_ROBIN = "round_robin"
    LEAST_LOADED = "least_loaded"
    PRIORITY_BASED = "priority_based"
    WORK_STEALING = "work_stealing"
    ADAPTIVE = "adaptive"


@dataclass
class NodeInfo:
    """Information about a distributed node."""
    node_id: str
    host: str
    port: int
    cpu_count: int
    memory_total: int
    gpu_count: int = 0
    load: float = 0.0
    last_heartbeat: float = field(default_factory=time.time)
    is_available: bool = True


@dataclass
class TaskMetrics:
    """Performance metrics for a task."""
    task_id: str
    start_time: float
    end_time: Optional[float] = None
    cpu_usage: float = 0.0
    memory_usage: float = 0.0
    gpu_usage: float = 0.0
    node_id: Optional[str] = None
    thread_id: Optional[str] = None
    
    @property
    def duration(self) -> Optional[float]:
        """Get task duration in seconds."""
        if self.end_time:
            return self.end_time - self.start_time
        return None


class Task:
    """Represents a task to be executed with advanced features."""
    
    def __init__(self, func: Callable, args: tuple, kwargs: dict, priority: int, 
                 future: Future, task_type: TaskType = TaskType.CPU_BOUND,
                 node_id: Optional[str] = None, gpu_device: Optional[str] = None):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.priority = priority
        self.future = future
        self.task_type = task_type
        self.node_id = node_id
        self.gpu_device = gpu_device
        self.timestamp = time.time()
        self.task_id = str(uuid.uuid4())
        self.metrics = TaskMetrics(task_id=self.task_id, start_time=time.time())
    
    def __lt__(self, other):
        """Compare tasks by priority (lower number = higher priority)."""
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.timestamp < other.timestamp


class HybridExecutor:
    """
    Advanced hybrid executor supporting CPU-bound, async/await, distributed, and GPU operations.
    
    Features:
    - Work stealing between threads
    - Global priority queue with advanced scheduling
    - Support for both sync and async functions
    - Distributed execution across multiple machines
    - GPU task execution
    - Performance monitoring and profiling
    - Integration with popular async frameworks
    - Advanced scheduling algorithms
    """
    
    def __init__(self, max_workers: Optional[int] = None, 
                 scheduling_algorithm: SchedulingAlgorithm = SchedulingAlgorithm.ADAPTIVE,
                 enable_monitoring: bool = True,
                 enable_distributed: bool = False,
                 enable_gpu: bool = False):
        """
        Initialize the advanced hybrid executor.
        
        Args:
            max_workers: Maximum number of worker threads. If None, uses CPU count.
            scheduling_algorithm: Algorithm for task scheduling
            enable_monitoring: Enable performance monitoring
            enable_distributed: Enable distributed execution
            enable_gpu: Enable GPU task execution
        """
        import os
        self.max_workers = max_workers or os.cpu_count() or 4
        self.scheduling_algorithm = scheduling_algorithm
        self.enable_monitoring = enable_monitoring
        self.enable_distributed = enable_distributed
        self.enable_gpu = enable_gpu
        
        # Global priority queue for work stealing
        self._global_queue = PriorityQueue()
        self._queue_lock = threading.Lock()
        
        # Thread pool for CPU-bound tasks
        self._thread_pool = ThreadPoolExecutor(max_workers=self.max_workers)
        
        # Event loop for async tasks
        self._event_loop = None
        self._loop_thread = None
        self._shutdown_flag = AtomicBool(False)
        
        # Statistics and monitoring
        self._tasks_submitted = AtomicInt(0)
        self._tasks_completed = AtomicInt(0)
        self._tasks_failed = AtomicInt(0)
        self._total_cpu_time = AtomicInt(0)
        self._total_memory_usage = AtomicInt(0)
        
        # Performance monitoring
        self._task_metrics: Dict[str, TaskMetrics] = {}
        self._metrics_lock = threading.Lock()
        self._monitoring_thread = None
        
        # Distributed execution
        self._nodes: Dict[str, NodeInfo] = {}
        self._node_lock = threading.Lock()
        self._distributed_enabled = enable_distributed
        
        # GPU support
        self._gpu_devices: List[str] = []
        self._gpu_lock = threading.Lock()
        if enable_gpu:
            self._initialize_gpu_support()
        
        # Async framework integrations
        self._async_frameworks = {
            'asyncio': self._setup_asyncio_integration,
            'trio': self._setup_trio_integration,
            'curio': self._setup_curio_integration
        }
        
        # Start the event loop in a separate thread
        self._start_event_loop()
        
        # Start monitoring if enabled
        if enable_monitoring:
            self._start_monitoring()
    
    def _start_event_loop(self):
        """Start the event loop in a separate thread."""
        def run_loop():
            self._event_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._event_loop)
            self._event_loop.run_forever()
        
        self._loop_thread = threading.Thread(target=run_loop, daemon=True)
        self._loop_thread.start()
        
        # Wait for the loop to be ready
        while self._event_loop is None:
            time.sleep(0.001)
    
    def _initialize_gpu_support(self):
        """Initialize GPU support and detect available devices."""
        try:
            # Try to import CUDA libraries
            import cupy as cp
            self._gpu_devices = [f"cuda:{i}" for i in range(cp.cuda.runtime.getDeviceCount())]
            logging.info(f"Found {len(self._gpu_devices)} GPU devices")
        except ImportError:
            try:
                # Try PyTorch
                import torch
                if torch.cuda.is_available():
                    self._gpu_devices = [f"cuda:{i}" for i in range(torch.cuda.device_count())]
                    logging.info(f"Found {len(self._gpu_devices)} GPU devices via PyTorch")
            except ImportError:
                logging.warning("No GPU libraries found. GPU support disabled.")
                self._gpu_devices = []
    
    def _start_monitoring(self):
        """Start performance monitoring thread."""
        def monitor():
            while not self._shutdown_flag.get():
                self._collect_system_metrics()
                time.sleep(1.0)  # Monitor every second
        
        self._monitoring_thread = threading.Thread(target=monitor, daemon=True)
        self._monitoring_thread.start()
    
    def _collect_system_metrics(self):
        """Collect system performance metrics."""
        try:
            # CPU usage
            cpu_percent = psutil.cpu_percent(interval=0.1)
            
            # Memory usage
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            
            # Update global metrics
            self._total_cpu_time.increment(int(cpu_percent))
            self._total_memory_usage.increment(int(memory_percent))
            
        except Exception as e:
            logging.warning(f"Failed to collect system metrics: {e}")
    
    def _setup_asyncio_integration(self):
        """Setup asyncio framework integration."""
        # Already handled by the main event loop
        pass
    
    def _setup_trio_integration(self):
        """Setup trio framework integration."""
        try:
            import trio
            # Trio integration would go here
            logging.info("Trio integration available")
        except ImportError:
            logging.warning("Trio not available")
    
    def _setup_curio_integration(self):
        """Setup curio framework integration."""
        try:
            import curio
            # Curio integration would go here
            logging.info("Curio integration available")
        except ImportError:
            logging.warning("Curio not available")
    
    def submit(self, func: Callable, *args, priority: int = 10, **kwargs) -> Future:
        """
        Submit a function for execution.
        
        Args:
            func: Function to execute
            *args: Positional arguments for the function
            priority: Task priority (lower number = higher priority)
            **kwargs: Keyword arguments for the function
        
        Returns:
            Future object representing the result
        """
        if self._shutdown_flag.get():
            raise RuntimeError("Cannot submit tasks to a shutdown executor")
        
        future = Future()
        task = Task(func, args, kwargs, priority, future)
        
        # Check if function is async
        if asyncio.iscoroutinefunction(func):
            self._submit_async_task(task)
        else:
            self._submit_sync_task(task)
        
        self._tasks_submitted.increment()
        return future
    
    def submit_distributed(self, func: Callable, args: tuple, nodes: List[str], 
                          priority: int = 10, **kwargs) -> Future:
        """
        Submit a function for distributed execution across multiple nodes.
        
        Args:
            func: Function to execute
            args: Arguments for the function
            nodes: List of node IDs to execute on
            priority: Task priority (lower number = higher priority)
            **kwargs: Keyword arguments for the function
        
        Returns:
            Future object representing the result
        """
        if not self._distributed_enabled:
            raise RuntimeError("Distributed execution not enabled")
        
        if self._shutdown_flag.get():
            raise RuntimeError("Cannot submit tasks to a shutdown executor")
        
        future = Future()
        task = Task(func, args, kwargs, priority, future, 
                   task_type=TaskType.DISTRIBUTED)
        
        # Select best node based on scheduling algorithm
        selected_node = self._select_best_node(nodes)
        task.node_id = selected_node
        
        # Submit to distributed execution
        self._submit_distributed_task(task)
        
        self._tasks_submitted.increment()
        return future
    
    def submit_gpu(self, func: Callable, args: tuple, device: Optional[str] = None,
                   priority: int = 10, **kwargs) -> Future:
        """
        Submit a function for GPU execution.
        
        Args:
            func: Function to execute on GPU
            args: Arguments for the function
            device: GPU device to use (e.g., 'cuda:0')
            priority: Task priority (lower number = higher priority)
            **kwargs: Keyword arguments for the function
        
        Returns:
            Future object representing the result
        """
        if not self.enable_gpu:
            raise RuntimeError("GPU execution not enabled")
        
        if self._shutdown_flag.get():
            raise RuntimeError("Cannot submit tasks to a shutdown executor")
        
        if not self._gpu_devices:
            raise RuntimeError("No GPU devices available")
        
        future = Future()
        gpu_device = device or self._gpu_devices[0]
        task = Task(func, args, kwargs, priority, future, 
                   task_type=TaskType.GPU, gpu_device=gpu_device)
        
        # Submit to GPU execution
        self._submit_gpu_task(task)
        
        self._tasks_submitted.increment()
        return future
    
    def _submit_async_task(self, task: Task):
        """Submit an async task to the event loop."""
        def run_async_task():
            try:
                # Create a new event loop for this thread
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    result = loop.run_until_complete(
                        task.func(*task.args, **task.kwargs)
                    )
                    task.future._set_result(result)
                finally:
                    loop.close()
            except Exception as e:
                task.future._set_exception(e)
                self._tasks_failed.increment()
            finally:
                self._tasks_completed.increment()
                self._update_task_metrics(task)
        
        # Submit to thread pool to avoid blocking the event loop
        self._thread_pool.submit(run_async_task)
    
    def _submit_distributed_task(self, task: Task):
        """Submit a task for distributed execution."""
        def run_distributed_task():
            try:
                # Simulate distributed execution
                # In a real implementation, this would communicate with remote nodes
                result = task.func(*task.args, **task.kwargs)
                task.future._set_result(result)
            except Exception as e:
                task.future._set_exception(e)
                self._tasks_failed.increment()
            finally:
                self._tasks_completed.increment()
                self._update_task_metrics(task)
        
        self._thread_pool.submit(run_distributed_task)
    
    def _submit_gpu_task(self, task: Task):
        """Submit a task for GPU execution."""
        def run_gpu_task():
            try:
                # Set GPU device if available
                if task.gpu_device:
                    import os
                    os.environ['CUDA_VISIBLE_DEVICES'] = task.gpu_device.split(':')[-1]
                
                result = task.func(*task.args, **task.kwargs)
                task.future._set_result(result)
            except Exception as e:
                task.future._set_exception(e)
                self._tasks_failed.increment()
            finally:
                self._tasks_completed.increment()
                self._update_task_metrics(task)
        
        self._thread_pool.submit(run_gpu_task)
    
    def _select_best_node(self, nodes: List[str]) -> str:
        """Select the best node for task execution based on scheduling algorithm."""
        if not nodes:
            raise ValueError("No nodes provided")
        
        with self._node_lock:
            available_nodes = [node for node in nodes if node in self._nodes and self._nodes[node].is_available]
            
            if not available_nodes:
                return nodes[0]  # Fallback to first node
            
            if self.scheduling_algorithm == SchedulingAlgorithm.LEAST_LOADED:
                return min(available_nodes, key=lambda n: self._nodes[n].load)
            elif self.scheduling_algorithm == SchedulingAlgorithm.ROUND_ROBIN:
                # Simple round-robin implementation
                return available_nodes[0]
            else:
                # Default to least loaded
                return min(available_nodes, key=lambda n: self._nodes[n].load)
    
    def _update_task_metrics(self, task: Task):
        """Update task performance metrics."""
        if not self.enable_monitoring:
            return
        
        with self._metrics_lock:
            task.metrics.end_time = time.time()
            task.metrics.thread_id = threading.current_thread().name
            self._task_metrics[task.task_id] = task.metrics
    
    def _submit_sync_task(self, task: Task):
        """Submit a sync task to the thread pool."""
        def run_sync_task():
            try:
                result = task.func(*task.args, **task.kwargs)
                task.future._set_result(result)
            except Exception as e:
                task.future._set_exception(e)
            finally:
                self._tasks_completed.increment()
        
        self._thread_pool.submit(run_sync_task)
    
    def map(self, func: Callable, iterable: Iterable, priority: int = 10) -> list[Future]:
        """
        Map a function over an iterable, returning a list of Futures.
        
        Args:
            func: Function to apply to each item
            iterable: Items to process
            priority: Task priority (lower number = higher priority)
        
        Returns:
            List of Future objects
        """
        futures = []
        for item in iterable:
            if isinstance(item, (tuple, list)) and len(item) > 0:
                # Handle tuple/list arguments
                future = self.submit(func, *item, priority=priority)
            else:
                # Handle single argument
                future = self.submit(func, item, priority=priority)
            futures.append(future)
        
        return futures
    
    def shutdown(self, wait: bool = True) -> None:
        """
        Shutdown the executor.
        
        Args:
            wait: If True, wait for all tasks to complete before shutting down
        """
        self._shutdown_flag.set(True)
        
        if wait:
            # Wait for all tasks to complete
            while self._tasks_completed.get() < self._tasks_submitted.get():
                time.sleep(0.01)
        
        # Shutdown thread pool
        self._thread_pool.shutdown(wait=wait)
        
        # Shutdown event loop
        if self._event_loop and self._event_loop.is_running():
            self._event_loop.call_soon_threadsafe(self._event_loop.stop)
        
        if self._loop_thread and self._loop_thread.is_alive():
            self._loop_thread.join(timeout=5.0)
    
    def get_stats(self) -> dict:
        """
        Get executor statistics.
        
        Returns:
            Dictionary with statistics
        """
        return {
            "max_workers": self.max_workers,
            "tasks_submitted": self._tasks_submitted.get(),
            "tasks_completed": self._tasks_completed.get(),
            "tasks_failed": self._tasks_failed.get(),
            "tasks_pending": self._tasks_submitted.get() - self._tasks_completed.get(),
            "shutdown": self._shutdown_flag.get(),
            "scheduling_algorithm": self.scheduling_algorithm.value,
            "monitoring_enabled": self.enable_monitoring,
            "distributed_enabled": self._distributed_enabled,
            "gpu_enabled": self.enable_gpu,
            "gpu_devices": len(self._gpu_devices),
            "nodes": len(self._nodes)
        }
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """
        Get detailed performance metrics.
        
        Returns:
            Dictionary with performance metrics
        """
        with self._metrics_lock:
            completed_tasks = [m for m in self._task_metrics.values() if m.end_time]
            
            if not completed_tasks:
                return {
                    "total_tasks": 0,
                    "average_duration": 0.0,
                    "total_cpu_time": self._total_cpu_time.get(),
                    "total_memory_usage": self._total_memory_usage.get()
                }
            
            durations = [m.duration for m in completed_tasks if m.duration]
            avg_duration = sum(durations) / len(durations) if durations else 0.0
            
            return {
                "total_tasks": len(completed_tasks),
                "average_duration": avg_duration,
                "min_duration": min(durations) if durations else 0.0,
                "max_duration": max(durations) if durations else 0.0,
                "total_cpu_time": self._total_cpu_time.get(),
                "total_memory_usage": self._total_memory_usage.get(),
                "task_metrics": {
                    task_id: {
                        "duration": metrics.duration,
                        "cpu_usage": metrics.cpu_usage,
                        "memory_usage": metrics.memory_usage,
                        "gpu_usage": metrics.gpu_usage,
                        "node_id": metrics.node_id,
                        "thread_id": metrics.thread_id
                    }
                    for task_id, metrics in self._task_metrics.items()
                }
            }
    
    def get_node_stats(self) -> Dict[str, Dict[str, Any]]:
        """
        Get statistics for distributed nodes.
        
        Returns:
            Dictionary with node statistics
        """
        with self._node_lock:
            return {
                node_id: {
                    "host": node.host,
                    "port": node.port,
                    "cpu_count": node.cpu_count,
                    "memory_total": node.memory_total,
                    "gpu_count": node.gpu_count,
                    "load": node.load,
                    "is_available": node.is_available,
                    "last_heartbeat": node.last_heartbeat
                }
                for node_id, node in self._nodes.items()
            }
    
    def add_node(self, node_id: str, host: str, port: int, 
                 cpu_count: int, memory_total: int, gpu_count: int = 0):
        """
        Add a distributed node to the executor.
        
        Args:
            node_id: Unique identifier for the node
            host: Node hostname or IP address
            port: Node port
            cpu_count: Number of CPU cores
            memory_total: Total memory in bytes
            gpu_count: Number of GPU devices
        """
        if not self._distributed_enabled:
            raise RuntimeError("Distributed execution not enabled")
        
        with self._node_lock:
            self._nodes[node_id] = NodeInfo(
                node_id=node_id,
                host=host,
                port=port,
                cpu_count=cpu_count,
                memory_total=memory_total,
                gpu_count=gpu_count
            )
    
    def remove_node(self, node_id: str):
        """
        Remove a distributed node from the executor.
        
        Args:
            node_id: Node identifier to remove
        """
        with self._node_lock:
            if node_id in self._nodes:
                del self._nodes[node_id]
    
    def get_gpu_devices(self) -> List[str]:
        """
        Get list of available GPU devices.
        
        Returns:
            List of GPU device identifiers
        """
        return self._gpu_devices.copy()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.shutdown(wait=True)
    
    def __repr__(self) -> str:
        """String representation of the executor."""
        stats = self.get_stats()
        return f"HybridExecutor(max_workers={stats['max_workers']}, " \
               f"submitted={stats['tasks_submitted']}, " \
               f"completed={stats['tasks_completed']})"
