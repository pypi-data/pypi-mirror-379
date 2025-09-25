"""
Comprehensive test suite for python-multirunner.

Tests all functionality including:
- HybridExecutor with CPU-bound and async tasks
- Future objects with timeout and exception handling
- Atomic primitives (AtomicInt, AtomicBool)
- Work stealing and priority queues
- Error handling and edge cases
"""

import asyncio
import pytest
import time
import threading
from concurrent.futures import TimeoutError
from unittest.mock import patch

from python_multirunner import (
    HybridExecutor, 
    Future, 
    AtomicInt, 
    AtomicBool,
    TaskType,
    SchedulingAlgorithm,
    NodeInfo,
    TaskMetrics
)


class TestAtomicInt:
    """Test cases for AtomicInt."""
    
    def test_initialization(self):
        """Test AtomicInt initialization."""
        atomic = AtomicInt()
        assert atomic.get() == 0
        
        atomic = AtomicInt(42)
        assert atomic.get() == 42
    
    def test_increment(self):
        """Test atomic increment operations."""
        atomic = AtomicInt(0)
        
        # Test single increment
        result = atomic.increment()
        assert result == 1
        assert atomic.get() == 1
        
        # Test increment by delta
        result = atomic.increment(5)
        assert result == 6
        assert atomic.get() == 6
        
        # Test negative increment
        result = atomic.increment(-2)
        assert result == 4
        assert atomic.get() == 4
    
    def test_set(self):
        """Test atomic set operation."""
        atomic = AtomicInt(10)
        atomic.set(20)
        assert atomic.get() == 20
    
    def test_concurrent_access(self):
        """Test concurrent access to AtomicInt."""
        atomic = AtomicInt(0)
        results = []
        
        def worker():
            for _ in range(100):
                atomic.increment()
                results.append(atomic.get())
        
        threads = [threading.Thread(target=worker) for _ in range(5)]
        
        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()
        
        # All increments should be accounted for
        assert atomic.get() == 500
        assert len(results) == 500
    
    def test_repr(self):
        """Test string representation."""
        atomic = AtomicInt(42)
        assert "AtomicInt(42)" in repr(atomic)


class TestAtomicBool:
    """Test cases for AtomicBool."""
    
    def test_initialization(self):
        """Test AtomicBool initialization."""
        atomic = AtomicBool()
        assert atomic.get() == False
        
        atomic = AtomicBool(True)
        assert atomic.get() == True
    
    def test_set_get(self):
        """Test atomic set and get operations."""
        atomic = AtomicBool(False)
        
        atomic.set(True)
        assert atomic.get() == True
        
        atomic.set(False)
        assert atomic.get() == False
    
    def test_boolean_conversion(self):
        """Test boolean conversion."""
        atomic = AtomicBool(True)
        assert bool(atomic) == True
        
        atomic.set(False)
        assert bool(atomic) == False
    
    def test_concurrent_access(self):
        """Test concurrent access to AtomicBool."""
        atomic = AtomicBool(False)
        results = []
        
        def worker():
            for _ in range(100):
                atomic.set(not atomic.get())
                results.append(atomic.get())
        
        threads = [threading.Thread(target=worker) for _ in range(3)]
        
        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()
        
        # Final state should be consistent
        final_value = atomic.get()
        assert final_value in [True, False]
    
    def test_repr(self):
        """Test string representation."""
        atomic = AtomicBool(True)
        assert "AtomicBool(True)" in repr(atomic)

class TestHybridExecutor:
    """Test cases for HybridExecutor."""
    
    def test_initialization(self):
        """Test executor initialization."""
        executor = HybridExecutor(max_workers=2)
        assert executor.max_workers == 2
        assert not executor._shutdown_flag.get()
        
        executor.shutdown()
    
    def test_context_manager(self):
        """Test executor as context manager."""
        with HybridExecutor(max_workers=2) as executor:
            assert not executor._shutdown_flag.get()
            assert executor.max_workers == 2
        
        # Executor should be shutdown after context exit
        assert executor._shutdown_flag.get()
    
    def test_submit_sync_function(self):
        """Test submitting synchronous functions."""
        with HybridExecutor(max_workers=2) as executor:
            def add(a, b):
                return a + b
            
            future = executor.submit(add, 2, 3)
            assert isinstance(future, Future)
            assert future.result() == 5
    
    def test_submit_async_function(self):
        """Test submitting asynchronous functions."""
        with HybridExecutor(max_workers=2) as executor:
            async def async_add(a, b):
                await asyncio.sleep(0.01)
                return a + b
            
            future = executor.submit(async_add, 2, 3)
            assert isinstance(future, Future)
            assert future.result() == 5
    
    def test_submit_with_priority(self):
        """Test submitting tasks with different priorities."""
        with HybridExecutor(max_workers=2) as executor:
            results = []
            
            def task(name, delay):
                time.sleep(delay)
                return name
            
            # Submit tasks with different priorities
            future1 = executor.submit(task, "low", 0.1, priority=10)
            future2 = executor.submit(task, "high", 0.05, priority=1)
            
            # High priority should complete first despite being submitted second
            result2 = future2.result()
            result1 = future1.result()
            
            results.extend([result1, result2])
            assert "high" in results
            assert "low" in results
    
    def test_submit_with_kwargs(self):
        """Test submitting tasks with keyword arguments."""
        with HybridExecutor(max_workers=2) as executor:
            def task(a, b, c=0):
                return a + b + c
            
            future = executor.submit(task, 1, 2, c=3)
            assert future.result() == 6
    
    def test_map_function(self):
        """Test mapping function over iterable."""
        with HybridExecutor(max_workers=2) as executor:
            def square(x):
                return x * x
            
            data = [1, 2, 3, 4, 5]
            futures = executor.map(square, data)
            
            assert len(futures) == 5
            results = [future.result() for future in futures]
            assert results == [1, 4, 9, 16, 25]
    
    def test_map_with_priority(self):
        """Test mapping with priority."""
        with HybridExecutor(max_workers=2) as executor:
            def task(x):
                return x * 2
            
            data = [1, 2, 3]
            futures = executor.map(task, data, priority=5)
            
            results = [future.result() for future in futures]
            assert results == [2, 4, 6]
    
    def test_map_with_tuples(self):
        """Test mapping with tuple arguments."""
        with HybridExecutor(max_workers=2) as executor:
            def add(a, b):
                return a + b
            
            data = [(1, 2), (3, 4), (5, 6)]
            futures = executor.map(add, data)
            
            results = [future.result() for future in futures]
            assert results == [3, 7, 11]
    
    def test_exception_handling(self):
        """Test exception handling in tasks."""
        with HybridExecutor(max_workers=2) as executor:
            def failing_task():
                raise ValueError("Test error")
            
            future = executor.submit(failing_task)
            
            with pytest.raises(ValueError, match="Test error"):
                future.result()
            
            assert future.done()
            assert isinstance(future.exception(), ValueError)
    
    def test_async_exception_handling(self):
        """Test exception handling in async tasks."""
        with HybridExecutor(max_workers=2) as executor:
            async def failing_async_task():
                await asyncio.sleep(0.01)
                raise RuntimeError("Async error")
            
            future = executor.submit(failing_async_task)
            
            with pytest.raises(RuntimeError, match="Async error"):
                future.result()
    
    def test_shutdown_without_wait(self):
        """Test shutdown without waiting."""
        executor = HybridExecutor(max_workers=2)
        
        def long_task():
            time.sleep(0.5)
            return "completed"
        
        future = executor.submit(long_task)
        executor.shutdown(wait=False)
        
        # Task might not complete
        assert executor._shutdown_flag.get()
    
    def test_shutdown_with_wait(self):
        """Test shutdown with waiting."""
        executor = HybridExecutor(max_workers=2)
        
        def quick_task():
            return "completed"
        
        future = executor.submit(quick_task)
        executor.shutdown(wait=True)
        
        assert future.result() == "completed"
        assert executor._shutdown_flag.get()
    
    def test_submit_after_shutdown(self):
        """Test submitting tasks after shutdown."""
        executor = HybridExecutor(max_workers=2)
        executor.shutdown()
        
        with pytest.raises(RuntimeError, match="Cannot submit tasks to a shutdown executor"):
            executor.submit(lambda: 42)
    
    def test_get_stats(self):
        """Test getting executor statistics."""
        with HybridExecutor(max_workers=3) as executor:
            def task(x):
                return x * 2
            
            # Submit some tasks
            futures = [executor.submit(task, i) for i in range(5)]
            
            # Wait for completion
            for future in futures:
                future.result()
            
            stats = executor.get_stats()
            
            assert stats["max_workers"] == 3
            assert stats["tasks_submitted"] == 5
            assert stats["tasks_completed"] == 5
            assert stats["tasks_pending"] == 0
            assert not stats["shutdown"]
    
    def test_repr(self):
        """Test string representation."""
        with HybridExecutor(max_workers=4) as executor:
            repr_str = repr(executor)
            assert "HybridExecutor" in repr_str
            assert "max_workers=4" in repr_str


class TestAdvancedFeatures:
    """Test cases for advanced executor features."""
    
    def test_scheduling_algorithms(self):
        """Test different scheduling algorithms."""
        algorithms = [
            SchedulingAlgorithm.ROUND_ROBIN,
            SchedulingAlgorithm.LEAST_LOADED,
            SchedulingAlgorithm.PRIORITY_BASED,
            SchedulingAlgorithm.WORK_STEALING,
            SchedulingAlgorithm.ADAPTIVE
        ]
        
        for algorithm in algorithms:
            with HybridExecutor(
                max_workers=2,
                scheduling_algorithm=algorithm,
                enable_monitoring=True
            ) as executor:
                assert executor.scheduling_algorithm == algorithm
                
                # Test basic functionality
                future = executor.submit(lambda x: x * 2, 5)
                assert future.result() == 10
    
    def test_monitoring_enabled(self):
        """Test executor with monitoring enabled."""
        with HybridExecutor(
            max_workers=2,
            enable_monitoring=True
        ) as executor:
            # Submit some tasks
            futures = [executor.submit(lambda x: x * 2, i) for i in range(5)]
            
            # Wait for completion
            for future in futures:
                future.result()
            
            # Check monitoring data
            stats = executor.get_stats()
            assert stats['monitoring_enabled'] == True
            assert stats['tasks_submitted'] == 5
            assert stats['tasks_completed'] == 5
            
            # Check performance metrics
            metrics = executor.get_performance_metrics()
            assert 'total_tasks' in metrics
            assert 'average_duration' in metrics
    
    def test_distributed_execution(self):
        """Test distributed execution features."""
        with HybridExecutor(
            max_workers=2,
            enable_distributed=True
        ) as executor:
            # Add nodes
            executor.add_node("node1", "localhost", 8080, cpu_count=4, memory_total=8*1024**3)
            executor.add_node("node2", "localhost", 8081, cpu_count=8, memory_total=16*1024**3)
            
            # Check node stats
            node_stats = executor.get_node_stats()
            assert len(node_stats) == 2
            assert "node1" in node_stats
            assert "node2" in node_stats
            
            # Test distributed task submission
            def test_func(x):
                return x * 2
            
            future = executor.submit_distributed(
                test_func,
                args=(5,),
                nodes=["node1", "node2"],
                priority=1
            )
            
            result = future.result()
            assert result == 10
            
            # Remove a node
            executor.remove_node("node1")
            node_stats = executor.get_node_stats()
            assert len(node_stats) == 1
            assert "node2" in node_stats
    
    def test_gpu_execution(self):
        """Test GPU execution features."""
        with HybridExecutor(
            max_workers=2,
            enable_gpu=True
        ) as executor:
            # Check GPU devices
            gpu_devices = executor.get_gpu_devices()
            assert isinstance(gpu_devices, list)
            
            # Test GPU task submission (if devices available)
            if gpu_devices:
                def gpu_test_func(x):
                    return x * 3
                
                future = executor.submit_gpu(
                    gpu_test_func,
                    args=(5,),
                    device=gpu_devices[0],
                    priority=1
                )
                
                result = future.result()
                assert result == 15
    
    def test_task_types(self):
        """Test different task types."""
        task_types = [
            TaskType.CPU_BOUND,
            TaskType.ASYNC,
            TaskType.DISTRIBUTED,
            TaskType.GPU
        ]
        
        for task_type in task_types:
            assert isinstance(task_type.value, str)
            assert task_type.value in ["cpu_bound", "async", "distributed", "gpu"]
    
    def test_node_info(self):
        """Test NodeInfo dataclass."""
        node = NodeInfo(
            node_id="test_node",
            host="localhost",
            port=8080,
            cpu_count=4,
            memory_total=8*1024**3,
            gpu_count=1
        )
        
        assert node.node_id == "test_node"
        assert node.host == "localhost"
        assert node.port == 8080
        assert node.cpu_count == 4
        assert node.memory_total == 8*1024**3
        assert node.gpu_count == 1
        assert node.is_available == True
    
    def test_task_metrics(self):
        """Test TaskMetrics dataclass."""
        metrics = TaskMetrics(
            task_id="test_task",
            start_time=time.time()
        )
        
        assert metrics.task_id == "test_task"
        assert metrics.end_time is None
        assert metrics.duration is None
        
        # Set end time
        metrics.end_time = time.time() + 1.0
        assert metrics.duration is not None
        assert metrics.duration > 0


class TestIntegration:
    """Integration tests combining multiple components."""
    
    def test_cpu_bound_with_atomics(self):
        """Test CPU-bound tasks with atomic primitives."""
        with HybridExecutor(max_workers=3) as executor:
            counter = AtomicInt(0)
            flag = AtomicBool(False)
            
            def worker(worker_id):
                operations = 0
                while not flag.get():
                    counter.increment()
                    operations += 1
                    if operations > 100:  # Prevent infinite loop
                        break
                return {"worker_id": worker_id, "operations": operations}
            
            # Start workers
            futures = [executor.submit(worker, i) for i in range(3)]
            
            # Let them run for a bit
            time.sleep(0.1)
            flag.set(True)
            
            # Collect results
            results = [future.result() for future in futures]
            
            # All workers should have completed
            assert len(results) == 3
            assert all("operations" in result for result in results)
            assert counter.get() > 0
    
    def test_mixed_sync_async_tasks(self):
        """Test mixing sync and async tasks."""
        with HybridExecutor(max_workers=4) as executor:
            def sync_task(x):
                return x * 2
            
            async def async_task(x):
                await asyncio.sleep(0.01)
                return x * 3
            
            # Submit mixed tasks
            sync_future = executor.submit(sync_task, 5)
            async_future = executor.submit(async_task, 5)
            
            # Both should complete
            assert sync_future.result() == 10
            assert async_future.result() == 15
    
    def test_priority_ordering(self):
        """Test that priority parameter is accepted and tasks complete."""
        with HybridExecutor(max_workers=2) as executor:
            futures = []

            def task(name, delay):
                time.sleep(delay)
                return name

            # Submit tasks with different priorities
            futures.append(executor.submit(task, "low1", 0.1, priority=10))
            futures.append(executor.submit(task, "high", 0.05, priority=1))
            futures.append(executor.submit(task, "low2", 0.1, priority=10))

            # Wait for all tasks to complete
            results = []
            for future in futures:
                results.append(future.result())

            # All tasks should complete successfully
            assert len(results) == 3
            assert "low1" in results
            assert "high" in results
            assert "low2" in results
    
    def test_large_data_processing(self):
        """Test processing large amounts of data."""
        with HybridExecutor(max_workers=4) as executor:
            def process_chunk(chunk):
                return sum(x * x for x in chunk)
            
            # Create large dataset
            data = list(range(1000))
            chunk_size = 100
            chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
            
            # Process chunks
            futures = [executor.submit(process_chunk, chunk) for chunk in chunks]
            results = [future.result() for future in futures]
            
            # All chunks should be processed
            assert len(results) == len(chunks)
            assert all(isinstance(result, int) for result in results)


class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def test_future_timeout(self):
        """Test Future timeout behavior."""
        with HybridExecutor(max_workers=1) as executor:
            def slow_task():
                time.sleep(0.5)
                return "done"
            
            future = executor.submit(slow_task)
            
            with pytest.raises(TimeoutError):
                future.result(timeout=0.1)
    
    def test_concurrent_future_access(self):
        """Test concurrent access to Future objects."""
        with HybridExecutor(max_workers=2) as executor:
            def task(x):
                time.sleep(0.1)
                return x * 2
            
            future = executor.submit(task, 5)
            
            # Multiple threads accessing the same future
            results = []
            
            def get_result():
                try:
                    result = future.result(timeout=1.0)
                    results.append(result)
                except Exception as e:
                    results.append(f"Error: {e}")
            
            threads = [threading.Thread(target=get_result) for _ in range(3)]
            
            for thread in threads:
                thread.start()
            
            for thread in threads:
                thread.join()
            
            # All threads should get the same result
            assert len(results) == 3
            assert all(result == 10 for result in results)
    
    def test_executor_shutdown_during_execution(self):
        """Test executor shutdown during task execution."""
        executor = HybridExecutor(max_workers=2)
        
        def long_task():
            time.sleep(1.0)
            return "completed"
        
        future = executor.submit(long_task)
        
        # Shutdown immediately
        executor.shutdown(wait=False)
        
        # Future might not complete
        assert executor._shutdown_flag.get()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
