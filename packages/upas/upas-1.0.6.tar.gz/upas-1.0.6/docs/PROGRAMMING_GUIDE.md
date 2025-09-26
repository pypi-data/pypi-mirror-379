# 🐍 UPAS Programming Guide

## Table of Contents

- [🚀 Quick Start](#-quick-start)
- [🎯 Basic API Usage](#-basic-api-usage)
- [🔄 Protocol Management](#-protocol-management)
- [⚡ State Control](#-state-control)
- [🔄 Dynamic Protocol Switching](#-dynamic-protocol-switching)
- [📊 Monitoring & Callbacks](#-monitoring--callbacks)
- [🏗️ Advanced Engine Control](#-advanced-engine-control)
- [💡 Best Practices](#-best-practices)
- [🔧 Troubleshooting](#-troubleshooting)

---

## 🚀 Quick Start

### Installation

```bash
pip install upas
```

### Simple Protocol Execution

```python
import asyncio
import upas

async def main():
    # Execute protocol for 30 seconds
    manager = await upas.run_protocol('my_protocol.json', duration=30)
    print(f"Protocol completed in state: {manager.get_current_state()}")

asyncio.run(main())
```

---

## 🎯 Basic API Usage

### Loading Protocols

```python
import upas

# Method 1: From file path
protocol_data = upas.load_protocol('protocol.json')

# Method 2: From JSON string
json_string = '{"protocol": {"name": "Test"}, ...}'
manager = upas.ProtocolManager(json_string)

# Method 3: From dictionary
protocol_dict = {
    "protocol": {"name": "MyProtocol", "version": "1.0"},
    "variables": {"MESSAGE": "Hello"},
    # ... rest of protocol definition
}
manager = upas.ProtocolManager(protocol_dict)
```

### Running Protocols

```python
import asyncio
import upas

async def run_examples():
    # Async execution (recommended)
    manager = upas.ProtocolManager('protocol.json')
    await manager.start_async(duration=60)

    # Synchronous execution (background thread)
    manager2 = upas.ProtocolManager('protocol2.json')
    manager2.start(duration=30)
    # ... do other work ...
    manager2.stop()
```

---

## 🔄 Protocol Management

### ProtocolManager Class

The `ProtocolManager` class provides high-level control over protocol execution:

```python
import upas

# Initialize manager
manager = upas.ProtocolManager('protocol.json')

# Control execution
await manager.start_async(duration=120)  # Run for 2 minutes
manager.stop()  # Stop immediately

# Access state information
current_state = manager.get_current_state()
variables = manager.get_variables()

# Modify variables
manager.set_variable('TIMEOUT', 5000)
manager.set_variable('SERVER_IP', '192.168.1.100')
```

### Protocol Information

```python
# Get protocol metadata
protocol_data = upas.load_protocol('protocol.json')
print(f"Name: {protocol_data['protocol']['name']}")
print(f"Version: {protocol_data['protocol']['version']}")
print(f"Behaviors: {list(protocol_data['behaviors'].keys())}")

# Access variables during execution
manager = upas.ProtocolManager('protocol.json')
await manager.start_async(duration=10)

variables = manager.get_variables()
for name, value in variables.items():
    print(f"{name}: {value}")
```

---

## ⚡ State Control

### Manual State Transitions

```python
import upas

async def state_control_example():
    manager = upas.ProtocolManager('protocol.json')
    await manager.start_async(duration=5)  # Initial startup

    # Force transition to specific state
    success = manager.transition_to_state('CONNECTED')
    if success:
        print("Successfully moved to CONNECTED state")
    else:
        print("State transition failed")

    # Continue execution in new state
    await asyncio.sleep(10)

    # Transition to final state
    manager.transition_to_state('DISCONNECTED')
    manager.stop()
```

### State Monitoring

```python
import upas

def monitor_states():
    manager = upas.ProtocolManager('protocol.json')

    # Track state changes
    previous_state = None

    async def check_state():
        nonlocal previous_state
        current = manager.get_current_state()
        if current != previous_state:
            print(f"State changed: {previous_state} → {current}")
            previous_state = current

    # Monitor every second
    async def monitor():
        while manager.running:
            await check_state()
            await asyncio.sleep(1)

    # Run monitoring alongside protocol
    await asyncio.gather(
        manager.start_async(duration=60),
        monitor()
    )
```

---

## 🔄 Dynamic Protocol Switching

### Runtime Protocol Changes

```python
import upas

async def dynamic_switching():
    # Start with discovery protocol
    manager = upas.ProtocolManager('discovery_protocol.json')

    print("Starting discovery phase...")
    await manager.start_async(duration=15)

    # Switch to operational protocol
    print("Switching to operational protocol...")
    await manager.change_protocol('operational_protocol.json')

    # Continue with new protocol
    await asyncio.sleep(30)

    # Switch to maintenance protocol
    print("Switching to maintenance mode...")
    await manager.change_protocol('maintenance_protocol.json')

    await asyncio.sleep(10)
    manager.stop()
```

### Conditional Protocol Switching

```python
import upas

async def conditional_switching():
    manager = upas.ProtocolManager('main_protocol.json')

    # Define switching logic
    def check_switch_condition():
        variables = manager.get_variables()
        error_count = variables.get('ERROR_COUNT', 0)

        if error_count > 5:
            print("Too many errors, switching to recovery protocol")
            return 'recovery_protocol.json'
        elif variables.get('MAINTENANCE_MODE'):
            print("Maintenance mode requested")
            return 'maintenance_protocol.json'
        return None

    # Monitor and switch as needed
    await manager.start_async(duration=5)

    while manager.running:
        new_protocol = check_switch_condition()
        if new_protocol:
            await manager.change_protocol(new_protocol)
        await asyncio.sleep(5)
```

---

## 📊 Monitoring & Callbacks

### State Change Callbacks

```python
import upas

def setup_callbacks():
    manager = upas.ProtocolManager('protocol.json')

    # Register state-specific callbacks
    def on_discovering():
        print("🔍 Entered discovery state - scanning network...")
        manager.set_variable('SCAN_INTERVAL', 1000)

    def on_connected():
        print("✅ Connected successfully - starting data exchange...")
        manager.set_variable('DATA_RATE', 'HIGH')

    def on_error():
        print("❌ Error state - attempting recovery...")
        manager.set_variable('RETRY_COUNT', 0)

    # Register callbacks
    manager.on_state_change('DISCOVERING', on_discovering)
    manager.on_state_change('CONNECTED', on_connected)
    manager.on_state_change('ERROR', on_error)

    return manager
```

### Protocol Change Callbacks

```python
import upas

def setup_protocol_callbacks():
    manager = upas.ProtocolManager('initial_protocol.json')

    # Track protocol changes
    def on_protocol_change(new_protocol_data):
        name = new_protocol_data['protocol']['name']
        version = new_protocol_data['protocol']['version']
        print(f"📋 Switched to protocol: {name} v{version}")

        # Log protocol-specific information
        behaviors = list(new_protocol_data.get('behaviors', {}).keys())
        print(f"   Available behaviors: {behaviors}")

    # Register callback
    manager.on_protocol_change('logger', on_protocol_change)

    return manager
```

### Real-time Statistics

```python
import upas

async def monitor_statistics():
    engine = await upas.create_engine('protocol.json')
    await engine.start()

    # Monitor engine statistics
    while engine.is_running():
        stats = engine.get_statistics()

        print(f"Engine Status:")
        print(f"  State: {stats['current_state']}")
        print(f"  Protocol: {stats['loaded_protocol']}")
        print(f"  Functions: {stats['registered_functions']}")
        print(f"  Running Behaviors: {stats['behaviors']['running']}")
        print("-" * 40)

        await asyncio.sleep(5)

    await engine.stop()
```

---

## 🏗️ Advanced Engine Control

### Direct Engine Management

```python
import upas

async def engine_control():
    # Create engine instance
    engine = await upas.create_engine('protocol.json')

    # Access engine components
    print(f"Transport layer: {engine.transport_layer}")
    print(f"Behavior executor: {engine.behavior_executor}")
    print(f"State machine: {engine.state_machine}")

    # Start engine
    await engine.start()

    # Manual state control
    if engine.state_machine:
        success = engine.transition_state('CUSTOM_STATE')
        print(f"State transition: {'success' if success else 'failed'}")

    # Monitor execution
    await asyncio.sleep(30)

    # Graceful shutdown
    await engine.stop()
```

### Custom Function Integration

```python
import upas

async def custom_functions():
    # Load protocol with custom functions
    protocol_data = upas.load_protocol('protocol.json')

    # Add custom functions to protocol
    protocol_data['functions'] = {
        'custom_checksum': 'lambda data: sum(data) & 0xFF',
        'current_timestamp': 'lambda: int(time.time())',
        'random_id': 'lambda: random.randint(1000, 9999)'
    }

    # Create engine with custom functions
    engine = await upas.create_engine(protocol_data)
    await engine.start()

    # Functions are now available in payload construction
    await asyncio.sleep(10)
    await engine.stop()
```

---

## 💡 Best Practices

### Error Handling

```python
import upas
import logging

async def robust_execution():
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    try:
        manager = upas.ProtocolManager('protocol.json')

        # Set error callback
        def on_error():
            logging.error("Protocol entered error state")
            # Implement recovery logic
            manager.set_variable('RECOVERY_MODE', True)

        manager.on_state_change('ERROR', on_error)

        # Execute with timeout
        await asyncio.wait_for(
            manager.start_async(duration=120),
            timeout=150  # Grace period for cleanup
        )

    except asyncio.TimeoutError:
        logging.error("Protocol execution timed out")
    except Exception as e:
        logging.error(f"Protocol execution failed: {e}")
    finally:
        if 'manager' in locals():
            manager.stop()
```

### Resource Management

```python
import upas
from contextlib import asynccontextmanager

@asynccontextmanager
async def protocol_context(protocol_path):
    """Context manager for protocol execution."""
    manager = upas.ProtocolManager(protocol_path)
    try:
        yield manager
    finally:
        manager.stop()

# Usage
async def managed_execution():
    async with protocol_context('protocol.json') as manager:
        await manager.start_async(duration=60)
        # Protocol automatically stopped when exiting context
```

### Performance Optimization

```python
import upas

async def optimized_execution():
    # Pre-load protocol data
    protocol_data = upas.load_protocol('protocol.json')

    # Reuse engine for multiple executions
    engine = await upas.create_engine(protocol_data)

    for iteration in range(5):
        print(f"Iteration {iteration + 1}")
        await engine.start()
        await asyncio.sleep(30)
        await engine.stop()

        # Brief pause between iterations
        await asyncio.sleep(5)
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Import Errors

```python
# ❌ Incorrect
import upas-cli  # Wrong package name

# ✅ Correct
import upas
```

#### 2. Async/Await Issues

```python
# ❌ Missing await
manager = upas.run_protocol('protocol.json')

# ✅ Correct
manager = await upas.run_protocol('protocol.json')
```

#### 3. State Transition Failures

```python
# Check state machine existence
if manager.engine and manager.engine.state_machine:
    success = manager.transition_to_state('TARGET_STATE')
else:
    print("No state machine configured")
```

### Debug Mode

```python
import upas
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Run with verbose output
manager = await upas.run_protocol('protocol.json', verbose=True)
```

### Protocol Validation

```python
import upas

def validate_before_run(protocol_path):
    try:
        protocol_data = upas.load_protocol(protocol_path)
        required_keys = ['protocol', 'behaviors', 'transports']

        for key in required_keys:
            if key not in protocol_data:
                raise ValueError(f"Missing required key: {key}")

        print("✅ Protocol validation passed")
        return True

    except Exception as e:
        print(f"❌ Protocol validation failed: {e}")
        return False

# Usage
if validate_before_run('protocol.json'):
    manager = await upas.run_protocol('protocol.json')
```

---

## 📚 API Reference Summary

### Core Functions

| Function          | Parameters                    | Returns           | Description                   |
| ----------------- | ----------------------------- | ----------------- | ----------------------------- |
| `run_protocol()`  | `protocol, duration, verbose` | `ProtocolManager` | High-level protocol execution |
| `load_protocol()` | `protocol_path`               | `Dict`            | Load protocol from file       |
| `create_engine()` | `protocol`                    | `ProtocolEngine`  | Create engine instance        |

### ProtocolManager Methods

| Method                  | Parameters        | Returns | Description             |
| ----------------------- | ----------------- | ------- | ----------------------- |
| `start_async()`         | `duration`        | `None`  | Start async execution   |
| `start()`               | `duration`        | `None`  | Start sync execution    |
| `stop()`                | -                 | `None`  | Stop execution          |
| `transition_to_state()` | `state`           | `bool`  | Force state transition  |
| `change_protocol()`     | `new_protocol`    | `None`  | Switch protocol         |
| `get_current_state()`   | -                 | `str`   | Get current state       |
| `get_variables()`       | -                 | `Dict`  | Get protocol variables  |
| `set_variable()`        | `name, value`     | `None`  | Set variable value      |
| `on_state_change()`     | `state, callback` | `None`  | Register state callback |

---

_For more examples and advanced usage, see the [examples/](../examples/) directory and [WIKI.md](../WIKI.md)._
