# 🎯 UPAS - Universal Protocol Analysis & Simulation

<div align="center">

![UPAS Logo](https://img.shields.io/badge/🎯_UPAS-Protocol_Engine-4CAF50?style=for-the-badge&logoColor=white)

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](#)
[![Python](https://img.shields.io/badge/python-3.7+-green.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](#)
[![Status](https://img.shields.io/badge/status-Production_Ready-brightgreen.svg)](#)
[![CI/CD Pipeline](https://github.com/BitsDiver/upas-cli/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/BitsDiver/upas-cli/actions/workflows/ci-cd.yml)

**Advanced Protocol Reverse Engineering & Network Service Emulation Platform**

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-documentation) • [🎮 Examples](#-examples) • [🛠️ Development](#-development)

</div>

---

## 🎯 **What is UPAS?**

UPAS (Universal Protocol Analysis & Simulation) is a production-ready framework for **protocol reverse engineering**, **network service emulation**, and **advanced protocol testing**. Originally designed for industrial protocol analysis, UPAS enables security researchers, network engineers, and developers to:

- 🔍 **Reverse engineer** complex network protocols with dynamic pattern matching
- 🎭 **Emulate sophisticated network services** with multi-packet response capabilities
- 🏭 **Simulate industrial protocols** (Modbus, CAN, custom IoT systems)
- 🛡️ **Test security vulnerabilities** in network stacks and devices
- 📡 **Develop protocol analyzers** with real-time variable extraction
- 🎪 **Create behavior simulations** with intelligent state management

---

## ✨ **Key Features**

### 🎯 **Advanced Pattern Matching**

- **Dynamic variable capture**: Extract values with `[CAPTURE:VAR:size]`
- **Wildcard operations**: Skip content with `[SKIP:n]` and `[WILDCARD:n]`
- **Binary pattern support**: Hex patterns with mixed static/dynamic content
- **Real-time analysis**: Immediate pattern matching during packet processing

### 🚀 **Multi-Packet Response System**

- **Sequential responses**: Ordered packets with ACK validation and retry logic
- **Burst responses**: Parallel transmission for complex protocols
- **Delayed sequences**: Custom timing control for realistic simulation
- **Response strategies**: Single, sequence, burst, and delayed modes

### 🔄 **Intelligent State Management**

- **Behavior-driven transitions**: State changes triggered by execution success
- **State-only behaviors**: Transitions without packets (timeouts, delays)
- **Conditional filtering**: Behaviors active only in specific protocol phases
- **Entry/exit actions**: Automatic behavior execution on state changes

### 🌐 **Service-Aware Transport**

- **Automatic routing**: TCP/UDP service selection via transport layer
- **Multi-service support**: UDP unicast/multicast, TCP client/server
- **Advanced socket management**: Robust connection handling with fallbacks
- **Interface control**: Multi-homed systems with interface binding

---

## 🚀 **Quick Start**

### Installation

UPAS is designed for minimal dependencies with optional feature sets:

```bash
# 🎯 Minimal Installation (Recommended - Zero dependencies)
pip install upas

# 🔬 With Analysis Features (PCAP support)
pip install upas[analysis]

# 🌐 With IoT Features (MQTT, Serial)
pip install upas[iot]

# 🚀 Full Installation (All features)
pip install upas[full]
```

> **📋 Installation Modes:** See the [WIKI](WIKI.md#installation-modes--use-cases) for detailed information about each installation mode and their specific use cases.

### Basic Usage

```bash
# Run protocol with clean output (default)
upas run examples/simple_beacon.json

# Verbose logging with execution details
upas run examples/heartbeat_monitor.json -v

# Full debug logging for development
upas run examples/iot_discovery.json -d

# Quiet mode (errors only)
upas run examples/simple_beacon.json -q

# Run with specific network interface
upas run examples/modbus_simulation.json --interface eth0
```

### Simple Protocol Example

```json
{
  "protocol": {
    "name": "UDP_Beacon",
    "version": "1.0",
    "description": "Basic UDP beacon example"
  },
  "variables": {
    "MESSAGE": "Hello UPAS",
    "COUNTER": 0
  },
  "functions": {
    "increment": "lambda x: (x + 1) % 0xFF"
  },
  "transports": {
    "ethernet": {
      "type": "ethernet",
      "services": {
        "udp_service": {
          "type": "udp_unicast",
          "bind": "0.0.0.0:12345"
        }
      }
    }
  },
  "behaviors": {
    "beacon": {
      "type": "periodic",
      "interval": 2000,
      "transport": "ethernet",
      "destination": "127.0.0.1:12346",
      "payload": ["BEACON", "[MESSAGE]", "[COUNTER:1:increment]"]
    }
  }
}
```

---

## 🐍 **Programmatic API**

UPAS provides a powerful Python API for integrating protocol simulation into your applications.

### Basic Usage

```python
import asyncio
import upas

async def main():
    # Run protocol for 30 seconds
    manager = await upas.run_protocol('protocol.json', duration=30)

    # Check current state
    print(f"Current state: {manager.get_current_state()}")

    # Get protocol variables
    variables = manager.get_variables()
    print(f"Variables: {variables}")

asyncio.run(main())
```

### Advanced Protocol Control

```python
import upas

async def advanced_example():
    # Create protocol manager
    manager = upas.ProtocolManager('protocol.json')

    # Register state change callbacks
    def on_connected():
        print("Protocol connected! Switching to monitoring mode...")
        manager.set_variable("MODE", "MONITORING")

    manager.on_state_change("CONNECTED", on_connected)

    # Start protocol
    await manager.start_async(duration=60)

    # Dynamic state transition
    success = manager.transition_to_state("AUTHENTICATED")
    if success:
        print("Successfully transitioned to AUTHENTICATED state")

    # Stop when done
    manager.stop()
```

### Dynamic Protocol Switching

```python
import upas

async def protocol_switching():
    # Start with discovery protocol
    manager = await upas.run_protocol('discovery.json')

    # Register protocol change callback
    def on_protocol_change(new_protocol):
        print(f"Switched to: {new_protocol['protocol']['name']}")

    manager.on_protocol_change("switch", on_protocol_change)

    # Wait for discovery completion
    await asyncio.sleep(10)

    # Switch to operational protocol
    await upas.change_protocol(manager, 'operational.json')

    # Continue with new protocol
    await asyncio.sleep(30)
    manager.stop()
```

### Engine-Level Control

```python
import upas

async def engine_control():
    # Create and configure engine directly
    engine = await upas.create_engine('protocol.json')

    # Start engine
    await engine.start()

    # Monitor execution
    while engine.is_running():
        stats = engine.get_statistics()
        print(f"State: {stats['current_state']}, Behaviors: {stats['behaviors']}")
        await asyncio.sleep(1)

    # Stop engine
    await engine.stop()
```

### API Reference

| Function                | Description                     |
| ----------------------- | ------------------------------- |
| `run_protocol()`        | High-level protocol execution   |
| `ProtocolManager()`     | Advanced protocol control class |
| `load_protocol()`       | Load protocol from file         |
| `create_engine()`       | Create engine instance          |
| `transition_to_state()` | Force state transition          |
| `change_protocol()`     | Dynamic protocol switching      |

---

## 🎮 **Examples**

### 🔧 **Protocol Testing & Simulation**

```bash
# Modbus RTU simulation
upas run examples/modbus_simulation.json -v

# Custom IoT protocol with state machine
upas run examples/iot_discovery.json -d
```

### 🌐 **Network Service Emulation**

```bash
# IoT device discovery protocol
upas run examples/iot_discovery.json

# Sensor network simulation
upas run examples/sensor_network.json
```

### 📡 **Advanced Protocol Analysis**

```bash
# Multi-phase protocol testing
upas run examples/advanced_protocol_example.json

# Protocol composition chains
upas run protocols/compositions/hybrid_discovery.json
```

---

## 📖 **Documentation**

### 📚 **Core Documentation**

- **[📋 SPECIFICATIONS.md](docs/SPECIFICATIONS.md)** - Complete protocol language reference
- **[📚 REFERENCES.md](docs/REFERENCES.md)** - JSON syntax quick reference
- **[🔧 WIKI.md](WIKI.md)** - Implementation guide and advanced features
- **[📦 Protocol Library](protocols/README.md)** - Standard protocol collection

### 🎯 **Key Concepts**

#### **Pattern Matching Syntax**

```json
"payload_pattern": "[PREFIX:8][CAPTURE:SESSION_ID:4][SKIP:8]DATA[SUFFIX:4]"
```

#### **Multi-Packet Responses**

```json
"response": {
  "mode": "sequence",
  "packets": [
    {"id": "ack", "payload": ["ACK[SESSION_ID:4]"], "timeout": 5.0},
    {"id": "data", "payload": ["DATA[RESPONSE:*]"], "delay": 0.1}
  ]
}
```

#### **State Machine Control**

```json
"active_states": ["DISCOVERING", "CONNECTED"],
"transition": "AUTHENTICATED"
```

---

## 🏗️ **Protocol Development**

### Quick Start Template

```json
{
  "protocol": {
    "name": "Your_Protocol",
    "version": "1.0",
    "description": "Protocol description"
  },
  "variables": {
    "PORT": 8080,
    "MESSAGE": "Hello World"
  },
  "transports": {
    "ethernet": {
      "type": "ethernet",
      "services": {
        "udp_service": {
          "type": "udp_unicast",
          "bind": "0.0.0.0:[PORT]"
        }
      }
    }
  },
  "behaviors": {
    "periodic_beacon": {
      "type": "periodic",
      "interval": 1000,
      "transport": "ethernet",
      "destination": "127.0.0.1:8081",
      "payload": ["[MESSAGE]"]
    }
  }
}
```

### Protocol Validation

```bash
# Validate single protocol
upas validate examples/simple_beacon.json

# Validate all protocols in directory
upas validate protocols/

# Validate with verbose output
upas validate examples/ -v
```

---

## 🛠️ **Development**

### Project Structure

```
upas-cli/
├── src/upas/              # Core UPAS framework
│   ├── core/              # Engine, behaviors, transport
│   │   ├── behavior/      # Behavior system
│   │   ├── transport/     # Network transport layer
│   │   └── protocol/      # Protocol engine
│   ├── analysis/          # Protocol analysis tools
│   └── cli.py             # Command-line interface
├── protocols/             # Standard protocol library
│   ├── behaviors/         # Reusable behavior components
│   ├── transports/        # Transport configurations
│   └── compositions/      # Protocol compositions
├── examples/              # Usage examples
├── docs/                  # Documentation
└── tests/                 # Test suite
```

### Installation for Development

```bash
# Clone repository
git clone https://github.com/BitsDiver/upas-cli.git
cd upas-cli

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\\Scripts\\activate   # Windows

# Install in development mode
pip install -e .
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest --cov=src/upas tests/
```

### Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Testing

```bash
# Run unit tests
python -m pytest tests/

# Run integration tests
python -m pytest tests/integration/

# Run specific test module
python -m pytest tests/test_engine.py -v

# Generate coverage report
python -m pytest --cov=src/upas --cov-report=html tests/
```

---

## 🎯 **Use Cases**

### 🛡️ **Security Research**

- **IoT penetration testing** - Emulate vulnerable devices for security assessment
- **Protocol fuzzing** - Generate malformed packets for vulnerability discovery
- **Network reconnaissance** - Service discovery and protocol fingerprinting

### 🏭 **Industrial Automation**

- **HMI simulation** - Test SCADA interfaces and human-machine interactions
- **PLC emulation** - Industrial protocol testing and commissioning
- **Network validation** - Protocol compliance and interoperability testing

### 🔬 **Research & Development**

- **Protocol prototyping** - Rapid development of custom network protocols
- **Network simulation** - Large-scale network behavior modeling
- **Educational tools** - Network protocol education and training

---

## 📞 **Support & Community**

### 🤝 **Getting Help**

- **🐙 GitHub Issues**: [Report bugs & request features](https://github.com/BitsDiver/upas-cli/issues)
- **📖 Documentation**: Complete guides in `docs/` directory
- **💬 Discussions**: Community Q&A and feature discussions
- **🔧 Wiki**: [Advanced configuration examples](WIKI.md)

### 🎓 **Learning Resources**

- **[📋 Protocol Specifications](docs/SPECIFICATIONS.md)** - Complete language reference
- **[📚 Quick Reference](docs/REFERENCES.md)** - Essential syntax guide
- **[🏭 Real-World Examples](examples/)** - Production protocol samples
- **[🧪 Test Cases](tests/)** - Comprehensive test suite examples

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 BitsDiver

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 **Acknowledgments**

UPAS was developed through extensive real-world testing with industrial protocols and IoT devices. Special thanks to the cybersecurity and industrial automation communities for their feedback and contributions.

---

<div align="center">

## 🎯 **UPAS v1.0.0 - Production Ready**

**✨ Advanced Protocol Analysis & Simulation Platform ✨**

**🚀 [Get Started](#-quick-start) • 📖 [Documentation](docs/SPECIFICATIONS.md) • 🎮 [Examples](examples/) • 🤝 [Contribute](#-development)**

---

_Developed with ❤️ for the network protocol analysis community_

</div>
