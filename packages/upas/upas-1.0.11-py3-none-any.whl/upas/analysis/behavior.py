#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Behavior Generation - Fixed Version

Generates UPAS behavior definitions from analyzed packet groups.
"""

from typing import Dict, List, Any, Optional
from collections import defaultdict

from .parser import PacketInfo
from .pattern import PatternInfo


class BehaviorGenerator:
    """Generates behavior definitions from packet analysis."""

    def __init__(self, verbose: bool = False, quiet: bool = False):
        self.verbose = verbose
        self.quiet = quiet

    def generate_behaviors(
        self,
        payload_groups: Dict,
        prefix_suffix: Dict[str, PatternInfo],
        trigger_analysis: Dict,
        udp_packets: List[PacketInfo],
        tcp_packets: List[PacketInfo],
        target_ip: str = None,
    ) -> Dict[str, Any]:
        """Generate behaviors section following UPAS specifications."""
        behaviors = {}
        handled_packets = set()

        # First, add reactive behaviors based on trigger analysis
        if target_ip and trigger_analysis.get("reactive_pairs"):
            reactive_counter = 1
            response_payload_groups = defaultdict(list)

            for trigger_pair in trigger_analysis["reactive_pairs"]:
                response_payload = trigger_pair["response_payload"]
                response_payload_groups[response_payload].append(trigger_pair)

            # Process each group of reactive pairs
            for response_payload, trigger_pairs in response_payload_groups.items():
                if len(trigger_pairs) == 1:
                    # Single trigger for this response
                    trigger_pair = trigger_pairs[0]
                    behavior_name = f"reactive_{trigger_pair['protocol'].lower()}_{reactive_counter}"
                    behaviors[behavior_name] = (
                        self._create_reactive_behavior_from_trigger(
                            trigger_pair, prefix_suffix
                        )
                    )
                    handled_packets.add(trigger_pair["response_frame"])
                    reactive_counter += 1

                    if not self.quiet:
                        print(
                            f"   Added reactive behavior: {behavior_name} (frame {trigger_pair['response_frame']})"
                        )

                else:
                    # Multiple triggers for same response
                    behavior_name = f"reactive_{trigger_pairs[0]['protocol'].lower()}_{reactive_counter}"
                    behaviors[behavior_name] = (
                        self._create_multi_trigger_reactive_behavior(
                            trigger_pairs, prefix_suffix
                        )
                    )

                    # Mark all response frames as handled
                    for trigger_pair in trigger_pairs:
                        handled_packets.add(trigger_pair["response_frame"])

                    reactive_counter += 1

                    if not self.quiet:
                        frames = [tp["response_frame"] for tp in trigger_pairs]
                        print(
                            f"   Added multi-trigger reactive behavior: {behavior_name} (frames {frames})"
                        )

        # Then add other behaviors (periodic, one-shot) from payload groups
        behavior_counter = len(behaviors) + 1

        # Process UDP groups
        for group_key, group_info in payload_groups.get("udp", {}).items():
            behavior_counter = self._process_protocol_group(
                "udp",
                group_key,
                group_info,
                udp_packets,
                handled_packets,
                behaviors,
                behavior_counter,
                prefix_suffix,
            )

        # Process TCP groups
        for group_key, group_info in payload_groups.get("tcp", {}).items():
            behavior_counter = self._process_protocol_group(
                "tcp",
                group_key,
                group_info,
                tcp_packets,
                handled_packets,
                behaviors,
                behavior_counter,
                prefix_suffix,
            )

        return behaviors

    def _process_protocol_group(
        self,
        protocol: str,
        group_key: str,
        group_info: Dict,
        protocol_packets: List[PacketInfo],
        handled_packets: set,
        behaviors: Dict,
        behavior_counter: int,
        prefix_suffix: Dict,
    ) -> int:
        """Process a single protocol group and generate appropriate behavior."""
        packets_frames = group_info["packets"]

        # Filter out packets that were already handled as reactive responses
        unhandled_frames = [
            frame for frame in packets_frames if frame not in handled_packets
        ]

        if not unhandled_frames:
            if not self.quiet:
                print(
                    f"   Skipping {protocol.upper()} group {group_key}: all packets already handled"
                )
            return behavior_counter

        # Get actual packet objects for unhandled frames
        unhandled_packets = [
            p
            for p in protocol_packets
            if p.frame_number in unhandled_frames and p.payload_hex
        ]

        if not unhandled_packets:
            return behavior_counter

        # Sort by timestamp
        unhandled_packets.sort(key=lambda p: p.timestamp)

        # Check if we have similarity info (indicates potential counters)
        similarity_info = group_info.get("similarity_info")
        has_counters = (
            similarity_info
            and similarity_info["similarity_ratio"] > 0.8
            and len(similarity_info["different_positions"]) <= 4
        )

        # Determine behavior type based on packet count and timing
        if len(unhandled_packets) > 1:
            # Calculate intervals
            intervals = []
            for i in range(1, len(unhandled_packets)):
                interval = (
                    unhandled_packets[i].timestamp - unhandled_packets[i - 1].timestamp
                )
                intervals.append(interval)

            if intervals:
                avg_interval = sum(intervals) / len(intervals)
                variance = sum((i - avg_interval) ** 2 for i in intervals) / len(
                    intervals
                )
                std_dev = variance**0.5

                # For packets with counters, be more permissive about timing variance
                # since they're likely periodic even with slight timing variations
                if has_counters:
                    variance_threshold = 0.5  # 50% variance allowed for counter packets
                    if not self.quiet:
                        print(
                            f"   DEBUG: Counter packets detected in {group_key}, using relaxed variance threshold"
                        )
                else:
                    variance_threshold = 0.3 if protocol == "udp" else 0.2

                if not self.quiet and self.verbose:
                    print(
                        f"   DEBUG: {protocol.upper()} group {group_key}: {len(unhandled_packets)} packets, "
                        f"avg_interval={avg_interval:.3f}s, std_dev={std_dev:.3f}, "
                        f"variance_ratio={std_dev/avg_interval:.3f}, threshold={variance_threshold}"
                    )

                if std_dev / avg_interval < variance_threshold:
                    # Periodic behavior
                    behavior_name = f"{protocol}_periodic_{behavior_counter}"
                    behavior = self._create_periodic_behavior_from_group(
                        unhandled_packets, protocol, prefix_suffix, similarity_info
                    )
                    behaviors[behavior_name] = behavior

                    counter_desc = (
                        f" with counters at positions {similarity_info['different_positions']}"
                        if has_counters
                        else ""
                    )
                    if not self.quiet:
                        print(
                            f"   Added periodic {protocol.upper()} behavior: {behavior_name} "
                            f"({len(unhandled_packets)} packets, ~{avg_interval:.1f}s interval{counter_desc})"
                        )
                else:
                    # Irregular timing - but if has counters, still likely periodic
                    if has_counters:
                        behavior_name = f"{protocol}_periodic_{behavior_counter}"
                        behavior = self._create_periodic_behavior_from_group(
                            unhandled_packets, protocol, prefix_suffix, similarity_info
                        )
                        behaviors[behavior_name] = behavior

                        if not self.quiet:
                            print(
                                f"   Added periodic {protocol.upper()} behavior: {behavior_name} "
                                f"({len(unhandled_packets)} packets with counters, ~{avg_interval:.1f}s interval)"
                            )
                    else:
                        # Truly irregular timing - triggered behavior
                        behavior_name = f"{protocol}_triggered_{behavior_counter}"
                        behavior = self._create_triggered_behavior_from_group(
                            unhandled_packets, protocol, prefix_suffix, similarity_info
                        )
                        behaviors[behavior_name] = behavior

                        if not self.quiet:
                            print(
                                f"   Added triggered {protocol.upper()} behavior: {behavior_name} "
                                f"({len(unhandled_packets)} packets, irregular timing)"
                            )

                behavior_counter += 1
        else:
            # Single packet - but if it has counter structure, it might be part of a periodic series
            if has_counters:
                # Treat as periodic with default interval
                behavior_name = f"{protocol}_periodic_{behavior_counter}"
                behavior = self._create_periodic_behavior_from_group(
                    unhandled_packets, protocol, prefix_suffix, similarity_info
                )
                behaviors[behavior_name] = behavior
                behavior_counter += 1

                if not self.quiet:
                    print(
                        f"   Added periodic {protocol.upper()} behavior: {behavior_name} (single packet with counter structure)"
                    )
            else:
                # True one-shot behavior
                behavior_name = f"{protocol}_one_shot_{behavior_counter}"
                behavior = self._create_triggered_behavior_from_group(
                    unhandled_packets, protocol, prefix_suffix, None
                )
                behaviors[behavior_name] = behavior
                behavior_counter += 1

                if not self.quiet:
                    print(
                        f"   Added one-shot {protocol.upper()} behavior: {behavior_name}"
                    )

        return behavior_counter

        return behavior_counter

    def _create_periodic_behavior_from_group(
        self,
        packets: List[PacketInfo],
        protocol: str,
        prefix_suffix: Dict,
        similarity_info: Optional[Dict],
    ) -> Dict[str, Any]:
        """Create a periodic behavior from a group of packets with potential counters."""
        first_packet = packets[0]

        # Calculate average interval
        if len(packets) > 1:
            intervals = []
            for i in range(1, len(packets)):
                interval = packets[i].timestamp - packets[i - 1].timestamp
                intervals.append(interval)
            avg_interval = sum(intervals) / len(intervals)
        else:
            avg_interval = 5.0  # Default 5 seconds for single packets with counters

        behavior = {
            "type": "periodic",
            "interval": int(avg_interval * 1000),  # Convert to milliseconds
            "transport": "ethernet",
            "destination": f"{first_packet.destination}:{first_packet.dst_port}",
        }

        # Generate payload with counter detection if applicable
        if similarity_info and similarity_info["similarity_ratio"] > 0.8:
            behavior["payload"] = self._generate_payload_with_counters(
                first_packet, prefix_suffix[protocol], similarity_info
            )
        else:
            behavior["payload"] = self._generate_simple_payload(
                first_packet, prefix_suffix[protocol]
            )

        return behavior

    def _create_triggered_behavior_from_group(
        self,
        packets: List[PacketInfo],
        protocol: str,
        prefix_suffix: Dict,
        similarity_info: Optional[Dict],
    ) -> Dict[str, Any]:
        """Create a triggered behavior from a group of packets with potential counters."""
        first_packet = packets[0]

        behavior = {
            "type": "one_shot",
            "transport": "ethernet",
            "destination": f"{first_packet.destination}:{first_packet.dst_port}",
        }

        # Generate payload with counter detection if applicable
        if similarity_info and similarity_info["similarity_ratio"] > 0.8:
            behavior["payload"] = self._generate_payload_with_counters(
                first_packet, prefix_suffix[protocol], similarity_info
            )
        else:
            behavior["payload"] = self._generate_simple_payload(
                first_packet, prefix_suffix[protocol]
            )

        return behavior

    def _create_reactive_behavior_from_trigger(
        self, trigger_pair: Dict, prefix_suffix: Dict
    ) -> Dict[str, Any]:
        """Create a reactive behavior based on trigger-response analysis."""
        # Create a mock PacketInfo for the response to generate payload template
        response_packet = PacketInfo(
            frame_number=trigger_pair["response_frame"],
            timestamp=trigger_pair["response_timestamp"],
            source=trigger_pair["response_source"],
            destination=trigger_pair["response_destination"],
            protocol=trigger_pair["protocol"],
            length=(
                len(trigger_pair["response_payload"]) // 2
                if trigger_pair["response_payload"]
                else 0
            ),
            raw_hex=trigger_pair["response_payload"],
            payload_hex=trigger_pair["response_payload"],
            src_port=trigger_pair["response_src_port"],
            dst_port=trigger_pair["response_dst_port"],
        )

        behavior = {
            "type": "reactive",
            "listen_transport": "ethernet",
            "response_transport": "ethernet",
            "trigger": {
                "source_pattern": f"{trigger_pair['trigger_source']}:{trigger_pair['trigger_src_port']}",
                "destination": f"{trigger_pair['trigger_destination']}:{trigger_pair['trigger_dst_port']}",
                "payload_pattern": (
                    self._apply_pattern_to_payload(
                        trigger_pair["trigger_payload"],
                        prefix_suffix.get(
                            trigger_pair["protocol"].lower(), PatternInfo()
                        ),
                        trigger_pair["protocol"],
                    )
                    if trigger_pair["trigger_payload"]
                    else "any"
                ),
            },
            "response": {
                "delay": int(trigger_pair["delay"] * 1000),  # Convert to milliseconds
                "destination": f"{trigger_pair['trigger_source']}:{trigger_pair['trigger_src_port']}",
                "payload": self._generate_simple_payload(
                    response_packet, prefix_suffix[trigger_pair["protocol"].lower()]
                ),
            },
        }

        return behavior

    def _create_multi_trigger_reactive_behavior(
        self, trigger_pairs: List[Dict], prefix_suffix: Dict
    ) -> Dict[str, Any]:
        """Create a reactive behavior that responds to multiple different triggers with the same response."""
        # Use the first trigger_pair as the template for the response
        first_trigger = trigger_pairs[0]

        # Create a mock PacketInfo for the response
        response_packet = PacketInfo(
            frame_number=first_trigger["response_frame"],
            timestamp=first_trigger["response_timestamp"],
            source=first_trigger["response_source"],
            destination=first_trigger["response_destination"],
            protocol=first_trigger["protocol"],
            length=(
                len(first_trigger["response_payload"]) // 2
                if first_trigger["response_payload"]
                else 0
            ),
            raw_hex=first_trigger["response_payload"],
            payload_hex=first_trigger["response_payload"],
            src_port=first_trigger["response_src_port"],
            dst_port=first_trigger["response_dst_port"],
        )

        # Create multiple trigger patterns
        trigger_patterns = []
        for trigger_pair in trigger_pairs:
            # Apply pattern substitution to trigger payload
            trigger_payload = trigger_pair["trigger_payload"]
            if trigger_payload:
                # Get the correct pattern info for this protocol
                protocol_lower = trigger_pair["protocol"].lower()
                pattern_for_protocol = prefix_suffix.get(protocol_lower, PatternInfo())
                trigger_payload_with_vars = self._apply_pattern_to_payload(
                    trigger_payload, pattern_for_protocol, trigger_pair["protocol"]
                )
            else:
                trigger_payload_with_vars = "any"

            trigger_patterns.append(
                {
                    "source_pattern": f"{trigger_pair['trigger_source']}:{trigger_pair['trigger_src_port']}",
                    "destination": f"{trigger_pair['trigger_destination']}:{trigger_pair['trigger_dst_port']}",
                    "payload_pattern": trigger_payload_with_vars,
                }
            )

        # Calculate average delay
        avg_delay = sum(tp["delay"] for tp in trigger_pairs) / len(trigger_pairs)

        behavior = {
            "type": "reactive",
            "listen_transport": "ethernet",
            "response_transport": "ethernet",
            "triggers": trigger_patterns,  # Multiple triggers
            "response": {
                "delay": int(avg_delay * 1000),  # Convert to milliseconds
                "destination": "sender",  # Special keyword to respond to any sender
                "payload": self._generate_simple_payload(
                    response_packet, prefix_suffix[first_trigger["protocol"].lower()]
                ),
            },
        }

        return behavior

    def _generate_simple_payload(
        self, packet: PacketInfo, pattern_info: PatternInfo
    ) -> List[str]:
        """Generate simple payload following UPAS format with automatic pattern replacement."""
        if not packet.payload_hex:
            return []

        # Apply pattern replacement automatically with correct protocol
        from .pattern import PatternAnalyzer

        pattern_analyzer = PatternAnalyzer(self.verbose, self.quiet)
        result = pattern_analyzer.apply_patterns_to_payload(
            packet.payload_hex, pattern_info, packet.protocol
        )

        return [result]

    def _generate_payload_with_counters(
        self, packet: PacketInfo, pattern_info: PatternInfo, similarity_info: Dict
    ) -> List[str]:
        """Generate payload template with counter variables for detected counter positions."""
        if not packet.payload_hex:
            return []

        payload = packet.payload_hex
        different_positions = similarity_info["different_positions"]

        # If no meaningful patterns detected, use the full payload with counter replacements
        if not pattern_info.prefix and not pattern_info.suffix:
            return self._replace_counters_in_payload(payload, different_positions)

        # Build payload string with prefix/suffix and counters
        payload_str = ""

        # Add prefix if it exists and is meaningful
        if (
            pattern_info.prefix
            and payload.startswith(pattern_info.prefix)
            and len(pattern_info.prefix) >= 16
        ):
            prefix_size = len(pattern_info.prefix) // 2
            payload_str += f"[{packet.protocol.upper()}_PREFIX:{prefix_size}]"
            remaining_payload = payload[len(pattern_info.prefix) :]
            # Adjust counter positions for remaining payload
            prefix_bytes = len(pattern_info.prefix) // 2
            adjusted_positions = [
                pos - prefix_bytes for pos in different_positions if pos >= prefix_bytes
            ]
        else:
            remaining_payload = payload
            adjusted_positions = different_positions

        # Add middle part with counters and suffix
        if (
            pattern_info.suffix
            and remaining_payload.endswith(pattern_info.suffix)
            and len(pattern_info.suffix) >= 8
        ):
            middle_payload = remaining_payload[: -len(pattern_info.suffix)]
            if middle_payload:
                if payload_str:
                    payload_str += " "
                # Replace counters in middle part
                middle_with_counters = self._replace_counters_in_payload(
                    middle_payload, adjusted_positions
                )
                payload_str += " ".join(middle_with_counters)

            if payload_str:
                payload_str += " "
            suffix_size = len(pattern_info.suffix) // 2
            payload_str += f"[{packet.protocol.upper()}_SUFFIX:{suffix_size}]"
        else:
            if remaining_payload:
                if payload_str:
                    payload_str += " "
                # Replace counters in remaining payload
                remaining_with_counters = self._replace_counters_in_payload(
                    remaining_payload, adjusted_positions
                )
                payload_str += " ".join(remaining_with_counters)

        return [payload_str] if payload_str else [payload]

    def _replace_counters_in_payload(
        self, payload_hex: str, counter_positions: List[int]
    ) -> List[str]:
        """Replace detected counter positions with COUNTER variables in hex payload."""
        if not counter_positions:
            return [payload_hex]

        # Sort positions
        counter_positions = sorted(counter_positions)

        # Group consecutive counter positions to create larger counter variables
        counter_groups = []
        current_group = [counter_positions[0]]

        for pos in counter_positions[1:]:
            if pos == current_group[-1] + 1:
                current_group.append(pos)
            else:
                counter_groups.append(current_group)
                current_group = [pos]
        counter_groups.append(current_group)

        # Build payload with counter replacements
        payload_parts = []
        last_pos = 0

        for group in counter_groups:
            start_pos = group[0]
            end_pos = group[-1] + 1

            # Add payload before counter
            if start_pos > last_pos:
                before_hex = payload_hex[last_pos * 2 : start_pos * 2]
                if before_hex:
                    payload_parts.append(before_hex)

            # Add counter variable
            counter_size = len(group)
            counter_bits = counter_size * 8
            payload_parts.append(f"[COUNTER_{counter_bits}:increment]")

            last_pos = end_pos

        # Add remaining payload after last counter
        if last_pos * 2 < len(payload_hex):
            remaining_hex = payload_hex[last_pos * 2 :]
            if remaining_hex:
                payload_parts.append(remaining_hex)

        return payload_parts

    def _apply_pattern_to_payload(
        self, payload: str, pattern_info: PatternInfo, protocol: str
    ) -> str:
        """Apply pattern substitution to any payload."""
        if not payload:
            return payload

        result = payload

        # Replace prefix if detected and present
        if pattern_info.prefix and result.startswith(pattern_info.prefix):
            prefix_size = len(pattern_info.prefix) // 2
            protocol_upper = protocol.upper() if protocol else "UNKNOWN"
            result = (
                f"[{protocol_upper}_PREFIX:{prefix_size}]"
                + result[len(pattern_info.prefix) :]
            )

        # Replace suffix if detected and present
        if pattern_info.suffix and result.endswith(pattern_info.suffix):
            suffix_size = len(pattern_info.suffix) // 2
            protocol_upper = protocol.upper() if protocol else "UNKNOWN"
            result = (
                result[: -len(pattern_info.suffix)]
                + f"[{protocol_upper}_SUFFIX:{suffix_size}]"
            )

        return result
