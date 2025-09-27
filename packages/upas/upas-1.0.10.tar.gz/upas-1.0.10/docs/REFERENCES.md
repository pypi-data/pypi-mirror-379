# 📚 UPAS JSON Reference Card

<div align="center">

![UPAS](https://img.shields.io/badge/📚_UPAS-JSON_Reference-FF9800?style=for-the-badge&logoColor=white)

**Quick reference for required/optional fields and valid values**

</div>

---

## 🎯 **Root Structure**

```json
{
  "protocol": {
    /* ✅ REQUIRED */
  },
  "variables": {
    /* ❌ Optional */
  },
  "functions": {
    /* ❌ Optional */
  },
  "transports": {
    /* ✅ REQUIRED */
  },
  "behaviors": {
    /* ✅ REQUIRED */
  },
  "state_machine": {
    /* ❌ Optional */
  }
}
```

---

## 📦 **Protocol Section**

```json
{
  "protocol": {
    "name": "string", // ✅ REQUIRED
    "version": "string", // ✅ REQUIRED
    "description": "string", // ❌ Optional
    "category": "string", // ❌ Optional
    "author": "string", // ❌ Optional
    "created": "ISO timestamp" // ❌ Optional
  }
}
```

**Valid Categories:** `industrial`, `network`, `custom`, `analysis`

---

## 🔧 **Variables Section**

```json
{
  "variables": {
    "VARIABLE_NAME": "string|number|hex"
  }
}
```

**Examples:**

```json
{
  "variables": {
    "DEVICE_ID": "ABC123", // String
    "PORT": 8080, // Number
    "HEX_DATA": "DEADBEEF", // Hex (no 0x prefix)
    "TIMEOUT": 30 // Number
  }
}
```

---

## ⚙️ **Functions Section**

```json
{
  "functions": {
    "function_name": "lambda expression"
  }
}
```

**Built-in Functions Available:**

- `increment` - Auto-increment counter
- `current_time` - Unix timestamp
- `timestamp` - Unix timestamp
- `timestamp_ms` - Timestamp in milliseconds
- `random_byte` - Random byte (0-255)
- `random_port` - Random port (1024-65535)
- `random_id` - Random ID (0x1000-0xFFFF)

---

## 🌐 **Transports Section**

```json
{
  "transports": {
    "transport_name": {
      "type": "ethernet",          // ✅ REQUIRED
      "interface": "string",       // ❌ Optional
      "ip_options": {              // ❌ Optional
        "dont_fragment": boolean,
        "ttl": number,
        "tos": number
      },
      "services": {                // ✅ REQUIRED
        "service_name": {
          "type": "service_type",  // ✅ REQUIRED
          "bind": "ip:port",       // ❌ Optional
          "connect_timeout": number // ❌ Optional
        }
      }
    }
  }
}
```

**Transport Types:** `ethernet`

**Service Types:**

- `udp_unicast` - UDP unicast
- `udp_multicast` - UDP multicast
- `tcp_server` - TCP server
- `tcp_client` - TCP client

---

## 🎭 **Behaviors Section**

### **Common Fields**

```json
{
  "behavior_name": {
    "type": "behavior_type",       // ✅ REQUIRED
    "enabled": boolean,            // ❌ Optional (default: true)
    "description": "string",       // ❌ Optional
    "active_states": ["state"],    // ❌ Optional
    /* type-specific fields */
  }
}
```

**Behavior Types:** `periodic`, `reactive`, `one_shot`

### **Periodic Behavior**

```json
{
  "periodic_behavior": {
    "type": "periodic",            // ✅ REQUIRED
    "transport": "transport_name", // ✅ REQUIRED
    "service": "service_name",     // ❌ Optional
    "interval": number,            // ✅ REQUIRED (milliseconds)
    "destination": "ip:port",      // ✅ REQUIRED
    "delay": number,               // ❌ Optional (initial delay)
    "repeat_count": number,        // ❌ Optional (-1 = infinite)
    "payload": ["string"]          // ✅ REQUIRED
  }
}
```

### **Reactive Behavior**

```json
{
  "reactive_behavior": {
    "type": "reactive",                    // ✅ REQUIRED
    "listen_transport": "transport_name",  // ✅ REQUIRED
    "response_transport": "transport_name", // ❌ Optional
    "service": "service_name",             // ❌ Optional

    // Single trigger (use either 'trigger' OR 'triggers')
    "trigger": {                           // ✅ REQUIRED (or triggers)
      "source_pattern": "pattern",         // ❌ Optional ("*" = any)
      "destination_pattern": "pattern",    // ❌ Optional ("*" = any)
      "payload_pattern": "pattern"         // ✅ REQUIRED
    },

    // Multiple triggers (alternative)
    "triggers": [                          // ✅ REQUIRED (or trigger)
      {
        "payload_pattern": "pattern"       // ✅ REQUIRED
      }
    ],

    "response": {                          // ✅ REQUIRED
      "delay": number,                     // ❌ Optional
      "destination": "ip:port|sender",     // ✅ REQUIRED
      "payload": ["string"],               // ✅ REQUIRED (unless mode=burst)

      // Multi-packet response
      "mode": "single|burst|sequence",     // ❌ Optional (default: single)
      "packets": [                         // ❌ Optional (for burst/sequence)
        {
          "delay": number,                 // ❌ Optional
          "payload": ["string"]            // ✅ REQUIRED
        }
      ]
    },

    "transition": "state_name"             // ❌ Optional
  }
}
```

### **One-Shot Behavior**

```json
{
  "oneshot_behavior": {
    "type": "one_shot",            // ✅ REQUIRED
    "transport": "transport_name", // ✅ REQUIRED
    "service": "service_name",     // ❌ Optional
    "delay": number,               // ❌ Optional
    "destination": "ip:port",      // ✅ REQUIRED
    "payload": ["string"]          // ✅ REQUIRED
  }
}
```

---

## 🔄 **State Machine Section**

```json
{
  "state_machine": {
    "initial_state": "state_name", // ✅ REQUIRED
    "states": {
      // ✅ REQUIRED
      "state_name": {
        "description": "string", // ❌ Optional
        "entry_action": "action_name", // ❌ Optional
        "exit_action": "action_name" // ❌ Optional
      }
    },
    "transitions": [
      // ❌ Optional
      {
        "from": "state_name|*", // ✅ REQUIRED
        "to": "state_name", // ✅ REQUIRED
        "trigger": "trigger_name", // ❌ Optional
        "condition": "condition_name", // ❌ Optional
        "action": "action_name" // ❌ Optional
      }
    ]
  }
}
```

---

## 📊 **Variable Reference Syntax**

### **Pattern Format**

```
[VARIABLE_NAME:size:function]
```

**Components:**

- `VARIABLE_NAME` - Variable name (required)
- `size` - Size in bytes (optional)
- `function` - Processing function (optional)

### **Special Patterns**

```
[CAPTURE:VAR_NAME:size]        // Capture data to variable
[SKIP:size]                    // Skip bytes in matching
[VAR_NAME:size:function]       // Use variable with function
[VAR_NAME:size]                // Use variable with size
[VAR_NAME]                     // Use variable as-is
```

### **Type Casting**

```json
"destination": "192.168.1.100:[TCP_PORT:int]"
```

**Available Casts:** `:int`

---

## 📝 **Payload Format Rules**

### **Array of Strings**

```json
"payload": [
  "HEADER",                      // Literal hex data
  "[VARIABLE:4]",               // Variable reference
  "MIDDLE",                     // More literal data
  "[COUNTER:1:increment]",      // Variable with function
  "FOOTER"                      // Final literal data
]
```

### **Hex Data Rules**

- ✅ **Use:** `DEADBEEF`
- ❌ **Don't use:** `0xDEADBEEF`, `DE AD BE EF`, `deadbeef`
- ✅ **Pad with zero:** `0A` not `A`
- ✅ **Even length:** Always even number of hex chars

---

## 🔍 **Pattern Matching**

### **Wildcards**

```json
"payload_pattern": "PREFIX*SUFFIX"        // * matches any data
"source_pattern": "*"                     // * matches any IP
"destination_pattern": "*"                // * matches any destination
```

### **Variable Matching**

```json
"payload_pattern": "PREFIX[VAR:4]SUFFIX"  // Match exact variable value
"payload_pattern": "PREFIX[CAPTURE:NEW:4]SUFFIX"  // Capture new data
"payload_pattern": "PREFIX[SKIP:4]SUFFIX" // Skip 4 bytes
```

---

## ⚠️ **Common Validation Errors**

### **Required Fields Missing**

- ❌ `protocol.name` or `protocol.version`
- ❌ `behaviors` section empty
- ❌ `transports` section empty
- ❌ `behavior.type` missing
- ❌ `trigger` AND `triggers` both missing in reactive behavior

### **Invalid Values**

- ❌ `behavior.type` not in: `periodic`, `reactive`, `one_shot`
- ❌ `transport.type` not `ethernet`
- ❌ `service.type` not in valid service types
- ❌ Payload not array of strings
- ❌ Hex data with `0x` prefix or spaces

### **Logic Errors**

- ❌ Reference to non-existent transport/service
- ❌ Both `trigger` and `triggers` defined
- ❌ Neither `trigger` nor `triggers` defined
- ❌ `mode: "burst"` without `packets`
- ❌ Variable reference to undefined variable

---

## 📋 **Checklist for New Protocols**

### ✅ **Required Sections**

- [ ] `protocol` with `name` and `version`
- [ ] `transports` with at least one transport
- [ ] `behaviors` with at least one behavior

### ✅ **Behavior Validation**

- [ ] All behaviors have valid `type`
- [ ] Periodic behaviors have `interval`, `transport`, `destination`, `payload`
- [ ] Reactive behaviors have `listen_transport`, `trigger`/`triggers`, `response`
- [ ] One-shot behaviors have `transport`, `destination`, `payload`

### ✅ **Payload Validation**

- [ ] All payloads are arrays of strings
- [ ] Hex data follows format rules (no 0x, no spaces, even length)
- [ ] Variable references use correct syntax
- [ ] All referenced variables are defined

### ✅ **Transport Validation**

- [ ] All referenced transports exist
- [ ] All referenced services exist
- [ ] Service types are valid

---

<div align="center">

**📚 Quick reference for UPAS v1.0.x JSON protocol definitions**

</div>
