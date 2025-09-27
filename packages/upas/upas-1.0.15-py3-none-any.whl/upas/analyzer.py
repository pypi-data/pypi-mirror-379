#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UPAS Protocol Analyzer

Main analyzer class for UPAS operations.
"""

import json
from typing import Dict, Any, Optional, List
from pathlib import Path
import logging

from .analysis.parser import WiresharkJsonParser, PacketInfo
from .analysis.pattern import PatternAnalyzer, PatternInfo
from .analysis.similarity import SimilarityAnalyzer
from .analysis.behavior import BehaviorGenerator
from .analysis.upas_generator import UpasGenerator


class ProtocolAnalyzer:
    """Main protocol analyzer that orchestrates all analysis steps."""

    def __init__(
        self,
        verbose: bool = False,
        quiet: bool = False,
        target_ip: Optional[str] = None,
    ):
        self.verbose = verbose
        self.quiet = quiet
        self.target_ip = target_ip

        # Initialize specialized analyzers
        self.parser = WiresharkJsonParser(verbose, quiet)
        self.pattern_analyzer = PatternAnalyzer(verbose, quiet)
        self.similarity_analyzer = SimilarityAnalyzer(verbose, quiet)
        self.behavior_generator = BehaviorGenerator(verbose, quiet)
        self.upas_generator = UpasGenerator(verbose, quiet)

        # Packet collections
        self.packets = []
        self.udp_packets = []
        self.tcp_packets = []
        self.target_packets = []
        self.trigger_packets = []

    def analyze_file(
        self,
        filename: str,
        start_frame: Optional[int] = None,
        end_frame: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Analyze a Wireshark JSON export file."""
        # Step 1: Parse packets
        if not self.quiet:
            print("🔍 Step 1: Parsing Wireshark JSON export...")
        self.packets = self.parser.parse_file(filename, start_frame, end_frame)

        if not self.packets:
            raise ValueError("No packets found in trace file")

        return self.analyze_packets(self.packets)

    def analyze_packets(self, packets: List[PacketInfo]) -> Dict[str, Any]:
        """Analyze a list of packets."""
        self.packets = packets
        self._separate_protocols()

        if not self.quiet:
            print(f"📊 Analysis Summary:")
            print(f"   Total packets: {len(self.packets)}")
            print(f"   UDP packets: {len(self.udp_packets)}")
            print(f"   TCP packets: {len(self.tcp_packets)}")
            if self.target_ip:
                print(f"   🎯 Target IP: {self.target_ip}")
                print(f"   Target packets: {len(self.target_packets)}")
                print(f"   Potential trigger packets: {len(self.trigger_packets)}")
            print()

        # Step 2: Generate intermediate representation
        if not self.quiet:
            print("🔍 Step 2: Extracting packet information...")
        intermediate = self._generate_intermediate()

        # Step 3: Identify PREFIX/SUFFIX patterns
        if not self.quiet:
            print("🔍 Step 3: Identifying PREFIX/SUFFIX patterns...")
        prefix_suffix = self.pattern_analyzer.identify_prefix_suffix(
            self.udp_packets, self.tcp_packets, self.target_ip
        )

        # Step 4: Group by similarity and timing
        if not self.quiet:
            print("🔍 Step 4: Grouping packets by similarity and analyzing timing...")
        payload_groups = self.similarity_analyzer.group_by_similarity(
            self.udp_packets, self.tcp_packets, self.target_ip
        )

        # Step 5: Search for embedded ports
        if not self.quiet:
            print("🔍 Step 5: Searching for embedded port information...")
        embedded_ports = self._find_embedded_ports()

        # Step 6: Identify padding patterns
        if not self.quiet:
            print("🔍 Step 6: Identifying padding patterns...")
        padding_info = self._identify_padding()

        # Step 7: Analyze packet sequences and triggers
        if not self.quiet:
            print("🔍 Step 7: Analyzing packet sequences and triggers...")
        sequence_analysis = self._analyze_packet_sequences()

        # Step 8: Analyze triggers if target_ip is specified
        if self.target_ip and not self.quiet:
            print("🔍 Step 8: Analyzing triggers for target responses...")
        trigger_analysis = self._analyze_triggers_for_target() if self.target_ip else {}

        # Step 9: Generate behaviors
        if not self.quiet:
            print("🔍 Step 9: Generating behaviors...")
        behaviors = self.behavior_generator.generate_behaviors(
            payload_groups,
            prefix_suffix,
            trigger_analysis,
            self.udp_packets,
            self.tcp_packets,
            self.target_ip,
        )

        # Step 10: Generate UPAS definition
        if not self.quiet:
            print("🔍 Step 10: Generating UPAS protocol definition...")
        upas_definition = self.upas_generator.generate_upas_definition(
            intermediate,
            prefix_suffix,
            payload_groups,
            embedded_ports,
            padding_info,
            sequence_analysis,
            trigger_analysis,
            behaviors,
        )

        return {
            "intermediate": intermediate,
            "prefix_suffix": prefix_suffix,
            "payload_groups": payload_groups,
            "embedded_ports": embedded_ports,
            "padding_info": padding_info,
            "sequence_analysis": sequence_analysis,
            "trigger_analysis": trigger_analysis,
            "upas_definition": upas_definition,
        }

    def _separate_protocols(self):
        """Separate packets by protocol type and target analysis."""
        for packet in self.packets:
            if packet.protocol.upper() == "UDP":
                self.udp_packets.append(packet)
            elif packet.protocol.upper() == "TCP":
                self.tcp_packets.append(packet)

            # Separate target packets from others if target_ip is specified
            if self.target_ip:
                if packet.source == self.target_ip:
                    self.target_packets.append(packet)
                else:
                    self.trigger_packets.append(packet)

        # Debug: show packet distribution
        if not self.quiet and self.verbose and self.target_ip:
            print(f"   Target packets distribution:")
            target_udp = [
                p
                for p in self.target_packets
                if p.protocol.upper() == "UDP" and p.payload_hex
            ]
            target_tcp = [
                p
                for p in self.target_packets
                if p.protocol.upper() == "TCP" and p.payload_hex
            ]
            print(f"     Target UDP with payload: {len(target_udp)}")
            print(f"     Target TCP with payload: {len(target_tcp)}")
            if target_udp:
                print(
                    f"     UDP frames: {[p.frame_number for p in target_udp[:10]]}..."
                )
            if target_tcp:
                print(
                    f"     TCP frames: {[p.frame_number for p in target_tcp[:10]]}..."
                )

    def _generate_intermediate(self) -> Dict[str, List[Dict]]:
        """Generate intermediate representation."""
        intermediate = {"udp_packets": [], "tcp_packets": []}

        for packet in self.udp_packets:
            intermediate["udp_packets"].append(
                {
                    "frame": packet.frame_number,
                    "timestamp": packet.timestamp,
                    "source": packet.source,
                    "destination": packet.destination,
                    "src_port": packet.src_port,
                    "dst_port": packet.dst_port,
                    "payload_hex": packet.payload_hex,
                    "length": len(packet.payload_hex) // 2 if packet.payload_hex else 0,
                }
            )

        for packet in self.tcp_packets:
            intermediate["tcp_packets"].append(
                {
                    "frame": packet.frame_number,
                    "timestamp": packet.timestamp,
                    "source": packet.source,
                    "destination": packet.destination,
                    "src_port": packet.src_port,
                    "dst_port": packet.dst_port,
                    "payload_hex": packet.payload_hex,
                    "length": len(packet.payload_hex) // 2 if packet.payload_hex else 0,
                }
            )

        return intermediate

    def _find_embedded_ports(self) -> Dict[str, List]:
        """Find potential embedded port numbers in payloads."""
        import struct

        embedded_ports = {"udp": [], "tcp": []}

        # Get all actual ports used in communication
        all_ports = set()
        for packet in self.packets:
            if packet.src_port:
                all_ports.add(packet.src_port)
            if packet.dst_port:
                all_ports.add(packet.dst_port)

        for protocol in ["udp", "tcp"]:
            packets = self.udp_packets if protocol == "udp" else self.tcp_packets

            for packet in packets:
                if not packet.payload_hex:
                    continue

                # Look for port numbers in hex (big-endian and little-endian)
                payload_bytes = bytes.fromhex(packet.payload_hex)

                for i in range(len(payload_bytes) - 1):
                    # Big-endian 16-bit
                    port_be = struct.unpack(">H", payload_bytes[i : i + 2])[0]
                    # Little-endian 16-bit
                    port_le = struct.unpack("<H", payload_bytes[i : i + 2])[0]

                    for port_val, endian in [(port_be, "big"), (port_le, "little")]:
                        if port_val in all_ports and 1024 <= port_val <= 65535:
                            embedded_ports[protocol].append(
                                {
                                    "frame": packet.frame_number,
                                    "position": i,
                                    "port_value": port_val,
                                    "endianness": endian,
                                    "hex_value": payload_bytes[i : i + 2].hex().upper(),
                                    "context": packet.payload_hex[i * 2 : (i + 2) * 2],
                                }
                            )
                            if not self.quiet:
                                print(
                                    f"   {protocol.upper()}: Found port {port_val} at position {i} in frame {packet.frame_number}"
                                )

        return embedded_ports

    def _identify_padding(self) -> Dict[str, List[Dict]]:
        """Identify padding patterns (contiguous zeros)."""
        padding_info = {"udp": [], "tcp": []}

        for protocol in ["udp", "tcp"]:
            packets = self.udp_packets if protocol == "udp" else self.tcp_packets

            for packet in packets:
                if not packet.payload_hex:
                    continue

                # Convert hex to bytes
                try:
                    payload_bytes = bytes.fromhex(packet.payload_hex)
                except ValueError:
                    continue

                # Find contiguous zero sequences (minimum 4 bytes)
                zero_sequences = []
                start_pos = None

                for i, byte_val in enumerate(payload_bytes):
                    if byte_val == 0:
                        if start_pos is None:
                            start_pos = i
                    else:
                        if start_pos is not None:
                            length = i - start_pos
                            if length >= 4:  # Minimum 4 bytes of zeros
                                zero_sequences.append(
                                    {
                                        "position": start_pos,
                                        "length": length,
                                        "frame": packet.frame_number,
                                    }
                                )
                            start_pos = None

                # Check for trailing zeros
                if start_pos is not None:
                    length = len(payload_bytes) - start_pos
                    if length >= 4:
                        zero_sequences.append(
                            {
                                "position": start_pos,
                                "length": length,
                                "frame": packet.frame_number,
                            }
                        )

                # Add significant padding to results
                for seq in zero_sequences:
                    if seq["length"] >= 4:
                        padding_info[protocol].append(seq)
                        if not self.quiet:
                            print(
                                f"   {protocol.upper()}: Found {seq['length']} bytes of padding at position {seq['position']} in frame {seq['frame']}"
                            )

        return padding_info

    def _analyze_packet_sequences(self) -> Dict[str, Any]:
        """Analyze packet sequences to identify triggers and responses."""
        from collections import defaultdict

        sequences = {
            "udp_to_tcp_triggers": [],
            "request_response_pairs": [],
            "periodic_behaviors": [],
            "one_shot_behaviors": [],
        }

        # Group all packets by timestamp to analyze sequences
        all_packets = sorted(self.packets, key=lambda p: p.timestamp)

        # Look for UDP packets that trigger TCP connections
        for i, packet in enumerate(all_packets):
            if packet.protocol == "UDP":
                # Look for TCP packets that start shortly after this UDP packet
                tcp_window = [
                    p
                    for p in all_packets[i + 1 : i + 10]
                    if p.protocol == "TCP" and p.timestamp - packet.timestamp < 1.0
                ]  # Within 1 second

                if tcp_window:
                    sequences["udp_to_tcp_triggers"].append(
                        {
                            "udp_frame": packet.frame_number,
                            "udp_flow": f"{packet.source}:{packet.src_port}->{packet.destination}:{packet.dst_port}",
                            "tcp_frames": [p.frame_number for p in tcp_window],
                            "delay": tcp_window[0].timestamp - packet.timestamp,
                        }
                    )

        # Identify request-response pairs (packets within 0.1s of each other)
        for i, packet in enumerate(all_packets):
            if i < len(all_packets) - 1:
                next_packet = all_packets[i + 1]
                if (
                    next_packet.timestamp - packet.timestamp < 0.1
                    and packet.source == next_packet.destination
                    and packet.destination == next_packet.source
                ):
                    sequences["request_response_pairs"].append(
                        {
                            "request_frame": packet.frame_number,
                            "response_frame": next_packet.frame_number,
                            "delay": next_packet.timestamp - packet.timestamp,
                            "protocol": packet.protocol,
                        }
                    )

        # Identify periodic behaviors (groups of packets with regular intervals)
        flows = defaultdict(list)
        for packet in all_packets:
            if packet.payload_hex:  # Only consider packets with payload
                flow_key = f"{packet.protocol}:{packet.source}:{packet.src_port}->{packet.destination}:{packet.dst_port}"
                flows[flow_key].append(packet)

        for flow_key, flow_packets in flows.items():
            if len(flow_packets) >= 3:
                # Calculate intervals
                intervals = []
                for j in range(1, len(flow_packets)):
                    interval = flow_packets[j].timestamp - flow_packets[j - 1].timestamp
                    intervals.append(interval)

                # Check if intervals are roughly consistent (within 20% variance)
                if intervals:
                    avg_interval = sum(intervals) / len(intervals)
                    variance = sum((i - avg_interval) ** 2 for i in intervals) / len(
                        intervals
                    )
                    std_dev = variance**0.5

                    if std_dev / avg_interval < 0.2:  # Less than 20% variance
                        sequences["periodic_behaviors"].append(
                            {
                                "flow": flow_key,
                                "packets": [p.frame_number for p in flow_packets],
                                "interval": avg_interval,
                                "count": len(flow_packets),
                            }
                        )

        return sequences

    def _analyze_triggers_for_target(self) -> Dict[str, Any]:
        """Analyze what triggers target responses for reactive behaviors."""
        if not self.target_ip:
            return {}

        triggers = {"reactive_pairs": [], "request_response_mapping": {}}

        # Sort all packets by timestamp for sequence analysis
        all_packets = sorted(self.packets, key=lambda p: p.timestamp)

        # Look for patterns: incoming packet → target response
        for i, packet in enumerate(all_packets):
            # Skip if this packet is from the target (we want triggers TO the target)
            if packet.source == self.target_ip:
                continue

            # Look for target responses within a short time window (1 second)
            response_window = [
                p
                for p in all_packets[i + 1 : i + 10]
                if (
                    p.source == self.target_ip
                    and p.timestamp - packet.timestamp < 1.0
                    and p.payload_hex
                )  # Only responses with payload
            ]

            for response in response_window:
                trigger_info = {
                    "trigger_frame": packet.frame_number,
                    "trigger_source": packet.source,
                    "trigger_src_port": packet.src_port,
                    "trigger_destination": packet.destination,
                    "trigger_dst_port": packet.dst_port,
                    "trigger_payload": packet.payload_hex,
                    "trigger_timestamp": packet.timestamp,
                    "response_frame": response.frame_number,
                    "response_source": response.source,
                    "response_src_port": response.src_port,
                    "response_destination": response.destination,
                    "response_dst_port": response.dst_port,
                    "response_payload": response.payload_hex,
                    "response_timestamp": response.timestamp,
                    "delay": response.timestamp - packet.timestamp,
                    "protocol": packet.protocol,
                }

                triggers["reactive_pairs"].append(trigger_info)

                if not self.quiet:
                    print(
                        f"   Found trigger: Frame {packet.frame_number} → Frame {response.frame_number} (delay: {trigger_info['delay']:.3f}s)"
                    )

        return triggers
