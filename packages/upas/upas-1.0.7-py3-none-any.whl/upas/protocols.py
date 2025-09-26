#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Protocol utilities for UPAS analysis
"""

from typing import List, Dict, Any


def get_protocol_info(protocol_name: str) -> Dict[str, Any]:
    """Get information about a protocol."""
    protocols = {
        "ethernet": {"header_size": 14},
        "ipv4": {"header_size": 20},  # Minimum size
        "tcp": {"header_size": 20},  # Minimum size
        "udp": {"header_size": 8},
        "icmp": {"header_size": 8},
    }
    return protocols.get(protocol_name.lower(), {"header_size": 0})


def detect_protocol_stack(lines: List[str]) -> List[str]:
    """Detect the protocol stack from Wireshark output lines."""
    stack = []

    for line in lines:
        line_lower = line.lower()

        if "ethernet ii" in line_lower:
            stack.append("ethernet")
        elif "internet protocol version 4" in line_lower:
            stack.append("ipv4")
        elif "transmission control protocol" in line_lower:
            stack.append("tcp")
        elif "user datagram protocol" in line_lower:
            stack.append("udp")
        elif "internet control message protocol" in line_lower:
            stack.append("icmp")

    return stack


def calculate_payload_offset(data: bytes, protocol_stack: List[str]) -> int:
    """Calculate the offset to the payload based on protocol stack."""
    offset = 0

    for protocol in protocol_stack:
        if protocol == "ethernet":
            offset += 14
        elif protocol == "ipv4":
            # Check actual IP header length
            if offset + 20 <= len(data):
                ip_header_len = (data[offset] & 0x0F) * 4
                offset += ip_header_len
            else:
                offset += 20  # Default
        elif protocol == "tcp":
            # Check actual TCP header length
            if offset + 20 <= len(data):
                tcp_header_len = ((data[offset + 12] >> 4) & 0x0F) * 4
                offset += tcp_header_len
            else:
                offset += 20  # Default
        elif protocol == "udp":
            offset += 8
        elif protocol == "icmp":
            offset += 8

    return offset
