#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Wireshark JSON Parser

Parses Wireshark JSON export format into structured data.
"""

import json
import hashlib
from typing import List, Optional, Dict, Tuple
from dataclasses import dataclass


# ANSI color codes
class Colors:
    """ANSI color codes for terminal output."""

    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    COLORS = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    BRIGHT_COLORS = [
        BRIGHT_RED,
        BRIGHT_GREEN,
        BRIGHT_YELLOW,
        BRIGHT_BLUE,
        BRIGHT_MAGENTA,
        BRIGHT_CYAN,
    ]


def get_source_color(source: str) -> Tuple[str, str]:
    """Get consistent color for a source (normal and bright)."""
    hash_obj = hashlib.md5(source.encode())
    color_index = int(hash_obj.hexdigest(), 16) % len(Colors.COLORS)
    return Colors.COLORS[color_index], Colors.BRIGHT_COLORS[color_index]


@dataclass
class PacketInfo:
    """Information extracted from a packet."""

    frame_number: int
    timestamp: float
    source: str
    destination: str
    protocol: str  # TCP/UDP/ICMP etc
    length: int
    raw_hex: str
    payload_hex: str  # Payload without headers
    src_port: Optional[int] = None
    dst_port: Optional[int] = None
    tcp_flags: Optional[List[str]] = None


class WiresharkJsonParser:
    """Parse Wireshark JSON export format."""

    def __init__(self, verbose: bool = False, quiet: bool = False):
        self.packets = []
        self.verbose = verbose
        self.quiet = quiet

    def parse_file(
        self,
        filename: str,
        start_frame: Optional[int] = None,
        end_frame: Optional[int] = None,
    ) -> List[PacketInfo]:
        """Parse Wireshark JSON export file."""
        with open(filename, "r") as f:
            data = json.load(f)

        # Process each packet in the JSON array
        for packet_data in data:
            if "_source" not in packet_data or "layers" not in packet_data["_source"]:
                continue

            layers = packet_data["_source"]["layers"]

            # Get frame information
            frame_info = layers.get("frame", {})
            frame_num = int(frame_info.get("frame.number", 0))

            # Check if we should include this frame
            if not self._should_include_frame(frame_num, start_frame, end_frame):
                continue

            packet = self._parse_packet_layers(layers)
            if packet:
                self.packets.append(packet)

        return self.packets

    def _should_include_frame(
        self, frame_num: int, start_frame: Optional[int], end_frame: Optional[int]
    ) -> bool:
        """Check if frame should be included based on range filters."""
        if start_frame is not None and frame_num < start_frame:
            return False
        if end_frame is not None and frame_num > end_frame:
            return False
        return True

    def _parse_packet_layers(self, layers: Dict) -> Optional[PacketInfo]:
        """Parse packet from JSON layers."""
        # Extract frame information
        frame_info = layers.get("frame", {})
        frame_num = int(frame_info.get("frame.number", 0))
        frame_len = int(frame_info.get("frame.len", 0))

        # Extract timestamp (convert from epoch to relative time)
        timestamp = float(frame_info.get("frame.time_relative", 0))

        # Extract IP information
        ip_info = layers.get("ip", {})
        source = ip_info.get("ip.src", "unknown")
        destination = ip_info.get("ip.dst", "unknown")

        # Extract transport protocol information
        protocol = "unknown"
        src_port = None
        dst_port = None
        tcp_flags = None
        payload_hex = ""

        # Check for UDP
        if "udp" in layers:
            protocol = "UDP"
            udp_info = layers["udp"]
            src_port = int(udp_info.get("udp.srcport", 0))
            dst_port = int(udp_info.get("udp.dstport", 0))

            # Extract payload from UDP
            payload_raw = udp_info.get("udp.payload", "")
            if payload_raw:
                payload_hex = payload_raw.replace(":", "").upper()

        # Check for TCP
        elif "tcp" in layers:
            protocol = "TCP"
            tcp_info = layers["tcp"]
            src_port = int(tcp_info.get("tcp.srcport", 0))
            dst_port = int(tcp_info.get("tcp.dstport", 0))

            # Extract TCP flags
            tcp_flags = self._extract_tcp_flags_from_json(tcp_info)

            # Extract payload from TCP
            payload_raw = tcp_info.get("tcp.payload", "")
            if payload_raw:
                payload_hex = payload_raw.replace(":", "").upper()

        # Check for other protocols
        elif "igmp" in layers:
            protocol = "IGMP"
        elif "arp" in layers:
            protocol = "ARP"
        elif "icmp" in layers:
            protocol = "ICMP"

        # Generate raw hex data
        raw_hex = payload_hex

        # Display packet info based on verbosity level
        if not self.quiet:
            self._display_packet_info(
                frame_num,
                timestamp,
                protocol,
                source,
                src_port,
                destination,
                dst_port,
                tcp_flags,
                payload_hex,
            )

        return PacketInfo(
            frame_number=frame_num,
            timestamp=timestamp,
            source=source,
            destination=destination,
            protocol=protocol,
            length=frame_len,
            raw_hex=raw_hex,
            payload_hex=payload_hex,
            src_port=src_port,
            dst_port=dst_port,
            tcp_flags=tcp_flags,
        )

    def _display_packet_info(
        self,
        frame_num,
        timestamp,
        protocol,
        source,
        src_port,
        destination,
        dst_port,
        tcp_flags,
        payload_hex,
    ):
        """Display packet information with color coding."""
        source_color, source_bright_color = get_source_color(source)
        has_payload = payload_hex and len(payload_hex) > 0
        color = source_bright_color if has_payload else source_color

        output_parts = []

        if self.verbose:
            # Verbose mode: show all packets
            output_parts.append(f"[{timestamp:>10.6f}] ")
            output_parts.append(f"{color}Frame {frame_num}: {protocol} {source}")

            if src_port is not None:
                output_parts.append(f":{src_port}")

            output_parts.append(f" -> {destination}")

            if dst_port is not None:
                output_parts.append(f":{dst_port}")

            if protocol == "TCP" and tcp_flags:
                flags_str = ", ".join(tcp_flags)
                output_parts.append(f" [{flags_str}]")

            if has_payload:
                output_parts.append(f", payload: {len(payload_hex)//2} bytes")

            output_parts.append(Colors.RESET)
            print("".join(output_parts))
        else:
            # Normal mode: only show packets with payload
            if has_payload:
                output_parts.append(f"[{timestamp:>10.6f}] ")
                output_parts.append(f"{color}Frame {frame_num}: {protocol} {source}")

                if src_port is not None:
                    output_parts.append(f":{src_port}")

                output_parts.append(f" -> {destination}")

                if dst_port is not None:
                    output_parts.append(f":{dst_port}")

                if protocol == "TCP" and tcp_flags:
                    flags_str = ", ".join(tcp_flags)
                    output_parts.append(f" [{flags_str}]")

                output_parts.append(f", payload: {len(payload_hex)//2} bytes")
                output_parts.append(Colors.RESET)
                print("".join(output_parts))

    def _extract_tcp_flags_from_json(self, tcp_info: Dict) -> Optional[List[str]]:
        """Extract TCP flags from JSON TCP layer."""
        flags = []

        flag_mappings = {
            "tcp.flags.syn": "SYN",
            "tcp.flags.ack": "ACK",
            "tcp.flags.psh": "PSH",
            "tcp.flags.rst": "RST",
            "tcp.flags.fin": "FIN",
            "tcp.flags.urg": "URG",
        }

        for flag_field, flag_name in flag_mappings.items():
            if tcp_info.get(flag_field) == "1":
                flags.append(flag_name)

        # If no individual flags found, try to parse from flags tree
        if not flags and "tcp.flags_tree" in tcp_info:
            flags_tree = tcp_info["tcp.flags_tree"]
            for flag_field, flag_name in flag_mappings.items():
                if flags_tree.get(flag_field) == "1":
                    flags.append(flag_name)

        return flags if flags else None
