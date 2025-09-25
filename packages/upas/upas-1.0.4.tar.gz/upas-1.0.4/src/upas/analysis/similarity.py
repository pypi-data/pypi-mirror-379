#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Similarity Analysis

Analyzes payload similarity between packets to detect counters and patterns.
"""

from typing import List, Dict, Any, Optional
from collections import defaultdict

from .parser import PacketInfo


class SimilarityAnalyzer:
    """Analyzes payload similarity between packets."""

    def __init__(self, verbose: bool = False, quiet: bool = False):
        self.verbose = verbose
        self.quiet = quiet

    def group_by_similarity(
        self,
        udp_packets: List[PacketInfo],
        tcp_packets: List[PacketInfo],
        target_ip: str = None,
    ) -> Dict[str, Dict]:
        """Group packets by protocol, size and flow - then analyze for similar patterns."""
        groups = {"udp": {}, "tcp": {}}

        for protocol in ["udp", "tcp"]:
            packets = udp_packets if protocol == "udp" else tcp_packets

            # If target_ip is specified, only analyze packets FROM the target
            if target_ip:
                packets = [
                    p for p in packets if p.source == target_ip and p.payload_hex
                ]

            # Group by flow and payload size (not exact payload)
            flow_groups = defaultdict(list)
            for packet in packets:
                if packet.payload_hex:
                    # For UDP multicast, group by destination only (not full flow)
                    # This helps group periodic packets that have counters
                    if protocol == "udp" and packet.destination.startswith("224."):
                        # UDP multicast - group by destination and payload size
                        flow_key = f"multicast->{packet.destination}:{packet.dst_port}"
                        payload_size = len(packet.payload_hex)
                        key = f"{flow_key}:size_{payload_size}"
                    else:
                        # Regular flow grouping
                        flow_key = f"{packet.source}:{packet.src_port}->{packet.destination}:{packet.dst_port}"
                        payload_size = len(packet.payload_hex)
                        key = f"{flow_key}:size_{payload_size}"

                    flow_groups[key].append(packet)

            # Analyze each group for patterns
            for key, group_packets in flow_groups.items():
                if len(group_packets) >= 1:
                    # Sort by timestamp
                    group_packets.sort(key=lambda p: p.timestamp)

                    # Analyze timing if multiple packets
                    if len(group_packets) > 1:
                        intervals = []
                        for i in range(1, len(group_packets)):
                            interval = (
                                group_packets[i].timestamp
                                - group_packets[i - 1].timestamp
                            )
                            intervals.append(interval)

                        avg_interval = sum(intervals) / len(intervals)
                        rounded_interval = round(avg_interval * 2) / 2

                        # Check payload similarity to detect counters
                        similarity_info = self.analyze_payload_similarity(group_packets)

                        groups[protocol][key] = {
                            "packets": [p.frame_number for p in group_packets],
                            "count": len(group_packets),
                            "avg_interval": avg_interval,
                            "rounded_interval": rounded_interval,
                            "payload_template": group_packets[0].payload_hex,
                            "similarity_info": similarity_info,
                            "flow": key.split(":size_")[0],  # Extract flow part
                        }

                        if not self.quiet:
                            if (
                                similarity_info
                                and similarity_info["similarity_ratio"] < 1.0
                            ):
                                different_bytes = len(
                                    similarity_info["different_positions"]
                                )
                                print(
                                    f"   {protocol.upper()}: {len(group_packets)} similar packets ({different_bytes} differing bytes), interval ~{rounded_interval}s, flow: {key}"
                                )
                            else:
                                print(
                                    f"   {protocol.upper()}: {len(group_packets)} identical packets, interval ~{rounded_interval}s, flow: {key}"
                                )
                    else:
                        # Single packet flow
                        groups[protocol][key] = {
                            "packets": [group_packets[0].frame_number],
                            "count": 1,
                            "payload_template": group_packets[0].payload_hex,
                            "flow": key.split(":size_")[0],
                        }

        return groups

    def analyze_payload_similarity(
        self, packets: List[PacketInfo]
    ) -> Optional[Dict[str, Any]]:
        """Analyze payload similarity between packets to detect patterns."""
        if len(packets) < 2:
            return None

        # Use first packet as reference
        reference_payload = packets[0].payload_hex
        if not reference_payload:
            return None

        reference_bytes = bytes.fromhex(reference_payload)

        # Compare all packets with reference
        total_bytes = len(reference_bytes)
        different_positions = set()

        for packet in packets[1:]:
            if not packet.payload_hex:
                continue

            try:
                packet_bytes = bytes.fromhex(packet.payload_hex)
            except ValueError:
                continue

            # Only compare if same length
            if len(packet_bytes) != len(reference_bytes):
                continue

            # Find differing bytes
            for i, (ref_byte, pkt_byte) in enumerate(
                zip(reference_bytes, packet_bytes)
            ):
                if ref_byte != pkt_byte:
                    different_positions.add(i)

        similar_bytes = total_bytes - len(different_positions)

        return {
            "total_bytes": total_bytes,
            "similar_bytes": similar_bytes,
            "different_positions": list(different_positions),
            "similarity_ratio": similar_bytes / total_bytes if total_bytes > 0 else 0,
        }
