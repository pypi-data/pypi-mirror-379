# 📋 UPAS Protocol Specifications

<div align="center">

![UPAS Specs](https://img.shields.io/badge/📋_SPECIFICATIONS-Protocol_Grammar-4CAF50?style=for-the-badge&logoColor=white)

**Complete reference for UPAS protocol definition language and implementation**

</div>

---

## 🎯 **Table of Contents**

- [Protocol Structure](#protocol-structure)
- [Variable System](#variable-system)
- [Advanced Payload Patterns](#advanced-payload-patterns)
- [Multi-Packet Responses](#multi-packet-responses)
- [State Machine](#state-machine)
- [Behavior System](#behavior-system)
- [Transport Layer](#transport-layer)
- [Service Management](#service-management)
- [Built-in Functions](#built-in-functions)
- [Complete Examples](#complete-examples)

---

## 📄 **Protocol Structure**

Every UPAS protocol file follows this fundamental JSON structure:

```json
{
  "protocol": {
    "name": "ProtocolName",
    "version": "1.0",
    "description": "Protocol description",
    "category": "industrial|network|iot|custom"
  },
  "variables": {
    /* Global variables and counters */
  },
  "state_machine": {
    /* State definitions and transitions */
  },
  "transports": {
    /* Network transport configurations */
  },
  "behaviors": {
    /* Protocol behaviors and responses */
  },
  "functions": {
    /* Custom functions (optional) */
  }
}
```

---

## 🔧 **Core Sections**

### **Protocol Section (Required)**

```json
"protocol": {
  "name": "MyProtocol",           // ✅ REQUIRED
  "version": "1.0",               // ✅ REQUIRED
  "description": "Description",   // ❌ Optional
  "category": "industrial",       // ❌ Optional
  "author": "Team Name",          // ❌ Optional
  "created": "2025-01-01T00:00:00.000Z"  // ❌ Optional
}
```

### **Variables Section (Optional)**

```json
"variables": {
  "DEVICE_ID": "ABC123",          // String literal
  "PORT": 8080,                   // Number literal
  "TIMEOUT": 30,                  // Number literal
  "HEX_DATA": "DEADBEEF"          // Hex string (no 0x prefix)
}
```

### **Functions Section (Optional)**

```json
"functions": {
  "increment": "lambda x: (x + 1) % 0xFF",
  "custom_calc": "lambda data: sum(data) & 0xFF"
}
```

### **Transports Section (Required)**

```json
"transports": {
  "primary_ethernet": {
    "type": "ethernet",
    "interface": "eth0",           // Optional interface
    "ip_options": {               // Optional IP settings
      "dont_fragment": true,
      "ttl": 64,
      "tos": 0
    },
    "services": {
      "udp_service": {
        "type": "udp_unicast",
        "bind": "0.0.0.0:8080"
      },
      "tcp_service": {
        "type": "tcp_server",
        "bind": "192.168.1.100:9000"
      },
      "tcp_client": {
        "type": "tcp_client",
        "connect_timeout": 20
      }
    }
  }
}
```

**Supported Transport Types:**

- `ethernet` - Ethernet/IP transport

**Supported Service Types:**

- `udp_unicast` - UDP unicast communication
- `udp_multicast` - UDP multicast communication
- `tcp_server` - TCP server (listen for connections)
- `tcp_client` - TCP client (initiate connections)

---

## 🔧 **Variable System**

### **Static Variables**

Define reusable protocol constants:

```json
"variables": {
  "UDP_PREFIX": "A0B1C2D3E4F5000000000000",
  "UDP_SUFFIX": "EF34AB56",
  "DEVICE_ID": "AB12CD",
  "TCP_PORT": "53116",
  "FMBOX_ID": "AB12CD00"
}
```

### **Variable References**

Use variables in payloads with size specifiers and type conversion:

| Syntax           | Description                       | Example           |
| ---------------- | --------------------------------- | ----------------- |
| `[VAR]`          | Simple variable reference         | `[UDP_PREFIX]`    |
| `[VAR:size]`     | Variable with byte size           | `[DEVICE_ID:3]`   |
| `[VAR:type]`     | Variable with type conversion     | `[TCP_PORT:int]`  |
| `[VAR:size:int]` | Variable with size and conversion | `[PORT_ID:2:int]` |

**Supported type conversions:**

- `int` - Convert hex to decimal integer (for ports, addresses)
- No type specified - Use as hex string

### **Counter Variables**

Built-in counters with automatic increment:

```json
"payload": "[PREFIX:11][COUNTER_8:increment][SUFFIX:4]"
```

Supported counter operations:

- `COUNTER_1`, `COUNTER_2`, `COUNTER_4`, `COUNTER_8` - Counter with byte size
- `:increment` - Auto-increment on each use
- `:reset` - Reset counter to zero

---

## 🎯 **Advanced Payload Patterns**

### **Pattern Matching Keywords**

UPAS supports advanced pattern matching for flexible payload analysis:

| Keyword              | Description             | Example                |
| -------------------- | ----------------------- | ---------------------- |
| `[CAPTURE:VAR:size]` | Capture dynamic value   | `[CAPTURE:TCP_PORT:2]` |
| `[WILDCARD:size]`    | Skip any content        | `[WILDCARD:4]`         |
| `[SKIP:size]`        | Alias for WILDCARD      | `[SKIP:8]`             |
| `[PREFIX:size]`      | Fixed prefix pattern    | `[PREFIX:11]`          |
| `[SUFFIX:size]`      | Fixed suffix pattern    | `[SUFFIX:4]`           |
| `[BINARY:size]`      | Binary pattern matching | `[BINARY:2]`           |

### **Capture Patterns**

Extract dynamic values from received packets for immediate use:

```json
{
  "trigger": {
    "payload_pattern": "[PREFIX:11]40ffff0000ffffffff0804000000[FMBOX_ID:4]0000000600000021[CAPTURE:TCP_PORT:2]0000c0a851fd[SKIP:16][SUFFIX:4]"
  },
  "response": {
    "destination": "192.168.81.253:[TCP_PORT:int]",
    "payload": "[PREFIX:11]280804000000[FMBOX_ID:4]0108000000[FMBOX_ID:4]0000000700000000[SUFFIX:4]"
  }
}
```

**Advanced Features:**

- ✅ Automatic hex → decimal conversion for ports (`[TCP_PORT:int]`)
- ✅ Global variable storage for reuse across behaviors
- ✅ Real-time pattern matching during packet processing
- ✅ Mixed static/dynamic patterns with wildcards

### **Wildcard and Skip Patterns**

Use wildcards to match variable content without capturing:

```json
"payload_pattern": "[PREFIX:8][WILDCARD:16][DATA_FIELD:4][SKIP:8][SUFFIX:4]"
```

This pattern:

1. Matches 8 bytes of fixed prefix
2. Skips 16 bytes of any content
3. Expects specific 4-byte data field
4. Skips 8 bytes of any content
5. Matches 4 bytes of fixed suffix

---

## 🚀 **Multi-Packet Responses**

### **Response Modes**

UPAS supports multiple response strategies for complex protocols:

#### **1. Single Response (Default)**

```json
"response": {
  "mode": "single",
  "destination": "192.168.1.100:8080",
  "payload": ["[PREFIX:4]RESPONSE_DATA[SUFFIX:2]"]
}
```

#### **2. Sequential Responses**

Send packets in sequence with ACK validation:

```json
"response": {
  "mode": "sequence",
  "packets": [
    {
      "id": "handshake",
      "payload": "[PREFIX:4]HANDSHAKE_DATA[SUFFIX:2]",
      "destination": "192.168.1.100:8080",
      "timeout": 5.0,
      "max_retries": 3
    },
    {
      "id": "data_packet",
      "payload": "[PREFIX:4]ACTUAL_DATA[SUFFIX:2]",
      "destination": "192.168.1.100:8080",
      "delay": 0.1
    }
  ],
  "global_timeout": 30.0,
  "fail_fast": true
}
```

#### **3. Burst Responses**

Send multiple packets in parallel:

```json
"response": {
  "mode": "burst",
  "packets": [
    {
      "id": "notification1",
      "payload": "[PREFIX:4]NOTIFY_A[SUFFIX:2]",
      "destination": "192.168.1.100:8080"
    },
    {
      "id": "notification2",
      "payload": "[PREFIX:4]NOTIFY_B[SUFFIX:2]",
      "destination": "192.168.1.101:8080"
    }
  ]
}
```

#### **4. Delayed Sequential Responses**

Sequential packets with custom delays:

```json
"response": {
  "mode": "delayed_sequence",
  "packets": [
    {
      "id": "first",
      "payload": "[PREFIX:4]FIRST_DATA[SUFFIX:2]",
      "delay": 0.0
    },
    {
      "id": "second",
      "payload": "[PREFIX:4]SECOND_DATA[SUFFIX:2]",
      "delay": 2.0
    },
    {
      "id": "third",
      "payload": "[PREFIX:4]THIRD_DATA[SUFFIX:2]",
      "delay": 5.0
    }
  ]
}
```

### **Response Configuration Options**

| Option           | Description                           | Default |
| ---------------- | ------------------------------------- | ------- |
| `mode`           | Response mode (single/sequence/burst) | single  |
| `destination`    | Target address                        | -       |
| `delay`          | Delay before sending (ms)             | 0       |
| `timeout`        | ACK timeout (seconds)                 | 5.0     |
| `max_retries`    | Maximum retry attempts                | 3       |
| `global_timeout` | Overall timeout for all packets       | 30.0    |
| `fail_fast`      | Stop on first failure                 | false   |
| `ack_timeout`    | Legacy ACK timeout                    | 5.0     |
| `retry_count`    | Legacy retry count                    | 3       |

---

## 🔄 **State Machine**

### **State Definition**

Define protocol states with entry/exit actions:

```json
"state_machine": {
  "initial_state": "DISCOVERING",
  "states": {
    "DISCOVERING": {
      "description": "Device discovery phase",
      "entry_action": "start_discovery_timer",
      "exit_action": "stop_discovery_timer"
    },
    "PHASE0": {
      "description": "Initial connection phase",
      "entry_action": "start_connection_process"
    },
    "PHASE1": {
      "description": "Advanced connection phase",
      "entry_action": "start_phase1_process"
    },
    "CONNECTED": {
      "description": "Established session",
      "entry_action": "start_keepalive"
    }
  },
  "transitions": [
    {
      "from": "DISCOVERING",
      "to": "PHASE0",
      "trigger": "manual",
      "action": "start_phase0_process"
    },
    {
      "from": "PHASE0",
      "to": "PHASE1",
      "trigger": "manual",
      "action": "start_connection_phase1"
    }
  ]
}
```

### **Behavior-Driven State Transitions**

Behaviors can trigger state transitions based on execution results:

#### **Simple Transitions**

```json
"init_udp_1": {
  "type": "reactive",
  "trigger": {
    "payload_pattern": "[PREFIX:11]40ffff[CAPTURE:TCP_PORT:2][SUFFIX:4]"
  },
  "response": {
    "payload": ["[PREFIX:11]response_data[SUFFIX:4]"]
  },
  "transition": "PHASE0"  // Transition on successful execution
}
```

#### **Conditional Transitions**

```json
"connection_behavior": {
  "type": "one_shot",
  "transition": {
    "success": "CONNECTED",
    "error": "ERROR"
  }
}
```

### **Behavior State Filtering**

Behaviors run only in specified states:

```json
"udp_keepalive": {
  "type": "periodic",
  "active_states": ["DISCOVERING", "CONNECTED"],
  "interval": 1000
}
```

---

## 🎪 **Behavior System**

### **Behavior Types**

#### **1. Periodic Behaviors**

Execute at regular intervals:

```json
"udp_keepalive": {
  "type": "periodic",
  "transport": "ethernet",
  "interval": 1000,
  "active_states": ["DISCOVERING", "CONNECTED"],
  "destination": "224.0.10.13:7001",
  "payload": ["[PREFIX:11]keepalive_data[SUFFIX:4]"]
}
```

#### **2. Reactive Behaviors**

Respond to incoming packets:

```json
"init_udp_0": {
  "type": "reactive",
  "listen_transport": "ethernet",
  "response_transport": "ethernet",
  "active_states": ["DISCOVERING"],
  "trigger": {
    "source_pattern": "*",
    "payload_pattern": "[PREFIX:11]28[WILDCARD:8]0804000000[FMBOX_ID:4][SKIP:12][SUFFIX:4]"
  },
  "response": {
    "destination": "sender",
    "payload": ["[PREFIX:11]response_to_28[SUFFIX:4]"]
  }
}
```

#### **3. One-Shot Behaviors**

Execute once when entering a state:

```json
"init_tcp_0": {
  "type": "one_shot",
  "transport": "ethernet",
  "service": "tcp_client",
  "active_states": ["PHASE0"],
  "delay": 0,
  "destination": "192.168.81.253:[TCP_PORT:int]",
  "payload": ["[PREFIX:11]connection_init[SUFFIX:4]"]
}
```

#### **4. State-Only Behaviors**

Change state without sending packets:

```json
"timeout_transition": {
  "type": "state_only",
  "active_states": ["DISCOVERING"],
  "delay": 30000,
  "transition": "ERROR"
}
```

### **Trigger Configuration**

For reactive behaviors, configure trigger patterns:

```json
"trigger": {
  "source_pattern": "*",                    // Accept from any source
  "destination_pattern": "192.168.*.*",     // Match destination pattern
  "payload_pattern": "[PREFIX:11]6E0108000000[FMBOX_ID:3]0804000000[FMBOX_ID:3][CAPTURE:DATA1:10][SUFFIX:4]"
}
```

**Pattern Types:**

- `source_pattern` - Match packet source address (supports wildcards)
- `destination_pattern` - Match packet destination address
- `payload_pattern` - Match packet payload with advanced patterns

---

## 🌐 **Transport Layer**

### **Transport Configuration**

Define network transports for packet handling:

```json
"transports": {
  "ethernet": {
    "type": "ethernet",
    "interface": "eth0",
    "promiscuous": true,
    "services": {
      "udp_service": {
        "type": "udp_unicast",
        "bind_port": 7001
      },
      "tcp_client": {
        "type": "tcp_client"
      }
    }
  }
}
```

### **Supported Transport Types**

| Type       | Description            | Use Cases              |
| ---------- | ---------------------- | ---------------------- |
| `ethernet` | Raw ethernet interface | Low-level protocols    |
| `raw`      | Raw socket interface   | Custom packet crafting |

---

## 🛠️ **Service Management**

### **Service Types**

Services define how packets are sent and received:

#### **UDP Services**

```json
"services": {
  "udp_discovery": {
    "type": "udp_multicast",
    "bind_port": 7001,
    "multicast_group": "224.0.10.13"
  },
  "udp_unicast": {
    "type": "udp_unicast",
    "bind_port": 8080
  }
}
```

#### **TCP Services**

```json
"services": {
  "tcp_server": {
    "type": "tcp_server",
    "bind_port": 9090,
    "max_connections": 10
  },
  "tcp_client": {
    "type": "tcp_client"
  }
}
```

### **Service Assignment**

Assign services to behaviors:

```json
"tcp_behavior": {
  "type": "one_shot",
  "transport": "ethernet",
  "service": "tcp_client",    // Use TCP client service
  "destination": "192.168.1.100:8080"
}
```

**Service Types:**

- `udp_unicast` - Point-to-point UDP communication
- `udp_multicast` - UDP multicast for discovery protocols
- `tcp_client` - TCP client connections
- `tcp_server` - TCP server listening

---

## 📚 **Built-in Functions**

### **Counter Functions**

```json
"payload": "[PREFIX:4][COUNTER_4:increment][SUFFIX:2]"
```

### **Time Functions**

```json
"payload": "[PREFIX:4][TIMESTAMP:8:current_time][SUFFIX:2]"
```

### **Custom Functions**

Define custom lambda functions:

```json
"functions": {
  "calculate_checksum": "lambda data: sum(data) & 0xFF",
  "encode_status": "lambda status, battery: (status << 4) | (battery & 0x0F)",
  "convert_temperature": "lambda celsius: int((celsius * 9/5) + 32)"
}
```

---

## 📋 **Complete Examples**

### **Simple Discovery Protocol**

```json
{
  "protocol": {
    "name": "SimpleDiscovery",
    "version": "1.0",
    "description": "Basic device discovery protocol"
  },
  "variables": {
    "PREFIX": "804721C7",
    "SUFFIX": "EF34AB56",
    "DEVICE_ID": "AB12CD"
  },
  "state_machine": {
    "initial_state": "DISCOVERING",
    "states": {
      "DISCOVERING": { "description": "Looking for devices" },
      "CONNECTED": { "description": "Device found" }
    }
  },
  "transports": {
    "ethernet": {
      "type": "ethernet",
      "interface": "eth0",
      "services": {
        "udp_multicast": {
          "type": "udp_multicast",
          "bind_port": 7001,
          "multicast_group": "224.0.10.13"
        }
      }
    }
  },
  "behaviors": {
    "discovery_beacon": {
      "type": "periodic",
      "transport": "ethernet",
      "service": "udp_multicast",
      "active_states": ["DISCOVERING"],
      "interval": 1000,
      "destination": "224.0.10.13:7001",
      "payload": ["[PREFIX:4]discovery_request[DEVICE_ID:3][SUFFIX:4]"]
    },
    "discovery_response": {
      "type": "reactive",
      "listen_transport": "ethernet",
      "response_transport": "ethernet",
      "active_states": ["DISCOVERING"],
      "trigger": {
        "source_pattern": "*",
        "payload_pattern": "[PREFIX:4]device_found[CAPTURE:REMOTE_ID:3][SUFFIX:4]"
      },
      "response": {
        "destination": "sender",
        "payload": ["[PREFIX:4]ack_discovery[DEVICE_ID:3][SUFFIX:4]"]
      },
      "transition": "CONNECTED"
    }
  }
}
```

### **Multi-Packet TCP Handshake**

```json
{
  "protocol": {
    "name": "TCPHandshake",
    "version": "1.0",
    "description": "Complex TCP connection with multi-packet responses"
  },
  "variables": {
    "PREFIX": "A0B1C2D3",
    "SUFFIX": "D3C2B1A0"
  },
  "behaviors": {
    "tcp_connection": {
      "type": "reactive",
      "listen_transport": "ethernet",
      "response_transport": "ethernet",
      "service": "tcp_client",
      "trigger": {
        "payload_pattern": "[PREFIX:4]CONNECT_REQ[CAPTURE:SESSION_ID:4][SUFFIX:4]"
      },
      "response": {
        "mode": "sequence",
        "destination": "sender",
        "packets": [
          {
            "id": "syn_ack",
            "payload": "[PREFIX:4]SYN_ACK[SESSION_ID:4][SUFFIX:4]",
            "timeout": 5.0,
            "max_retries": 3
          },
          {
            "id": "auth_challenge",
            "payload": "[PREFIX:4]AUTH_REQ[SESSION_ID:4]CHALLENGE_DATA[SUFFIX:4]",
            "delay": 0.1
          },
          {
            "id": "connection_ready",
            "payload": "[PREFIX:4]READY[SESSION_ID:4][SUFFIX:4]",
            "delay": 0.2
          }
        ],
        "global_timeout": 30.0,
        "fail_fast": true
      }
    }
  }
}
```

### **Advanced Pattern Matching**

```json
{
  "protocol": {
    "name": "AdvancedPatterns",
    "version": "1.0"
  },
  "behaviors": {
    "complex_parser": {
      "type": "reactive",
      "trigger": {
        "payload_pattern": "[PREFIX:8][WILDCARD:4][CAPTURE:TYPE:1][SKIP:2][CAPTURE:LENGTH:2][CAPTURE:DATA:*][SUFFIX:4]"
      },
      "response": {
        "destination": "sender",
        "payload": ["[PREFIX:8]RESPONSE_[TYPE:1]_LEN_[LENGTH:2][SUFFIX:4]"]
      }
    }
  }
}
```

---

## ⚠️ **Implementation Status**

### ✅ **Fully Implemented**

- JSON protocol definitions
- Ethernet transport with UDP/TCP services
- Periodic, reactive, and one-shot behaviors
- Variable system with built-in functions
- Payload construction with variable substitution
- Multi-packet responses (burst mode)
- State machine with automatic transitions
- Variable capture and skip patterns

### ⚡ **Partially Implemented**

- State machine actions/triggers (not all correspond to actual functions)
- Some transport configuration options
- Advanced payload validation

### ❌ **Not Implemented**

- Transport types other than ethernet
- Complex state machine validation
- Protocol composition/inheritance
- Dynamic protocol loading

---

## 📊 **Payload Construction**

### **Format**

Payloads are arrays of strings that get joined together:

```json
"payload": [
  "HEADER",
  "[VARIABLE:4]",
  "MIDDLE",
  "[COUNTER:1:increment]",
  "FOOTER"
]
```

This becomes: `HEADER[4-byte-variable]MIDDLE[1-byte-counter]FOOTER`

### **Hex Data Format**

- **No `0x` prefix**: Use `DEADBEEF` not `0xDEADBEEF`
- **No spaces**: Use `DEADBEEF` not `DE AD BE EF`
- **Even length**: Pad with leading zero if needed (`0A` not `A`)

### **Multi-Packet Responses**

For burst responses, each packet payload is also an array:

```json
"response": {
  "mode": "burst",
  "packets": [
    {
      "delay": 0,
      "payload": ["PACKET1[VAR:4]"]      // Array format
    },
    {
      "delay": 800,
      "payload": ["PACKET2[VAR:4]"]      // Array format
    }
  ]
}
```

---

<div align="center">

**📋 This specification reflects the exact current implementation in UPAS v1.0.x**

</div>
