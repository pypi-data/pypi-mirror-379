#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pattern Analysis

Analyzes protocol patterns like prefix/suffix detection.
"""

from typing import List, Dict, Any
from dataclasses import dataclass
from collections import Counter

from .parser import PacketInfo


@dataclass
class PatternInfo:
    """Information about identified patterns."""

    prefix: str = ""
    suffix: str = ""
    variables: Dict[str, Any] = None
    template: str = ""

    def __post_init__(self):
        if self.variables is None:
            self.variables = {}


class PatternAnalyzer:
    """Analyzes packets to identify common patterns."""

    def __init__(self, verbose: bool = False, quiet: bool = False):
        self.verbose = verbose
        self.quiet = quiet

    def identify_prefix_suffix(
        self,
        udp_packets: List[PacketInfo],
        tcp_packets: List[PacketInfo],
        target_ip: str = None,
    ) -> Dict[str, PatternInfo]:
        """Identify common PREFIX and SUFFIX in payloads."""
        patterns = {}

        for protocol in ["udp", "tcp"]:
            packets = udp_packets if protocol == "udp" else tcp_packets

            # CRITICAL FIX: Analyze ALL packets with payload, not just FROM target
            # Pattern detection should work on the entire protocol dataset
            payloads = [p.payload_hex for p in packets if p.payload_hex]

            if not payloads:
                patterns[protocol] = PatternInfo()
                continue

            # Debug: print payloads for analysis
            if not self.quiet and self.verbose:
                print(f"   {protocol.upper()} payloads found ({len(payloads)}):")
                for i, payload in enumerate(payloads):
                    print(
                        f"     {i+1}: {payload[:80]}{'...' if len(payload) > 80 else ''}"
                    )
                print(
                    f"   --> Analyzing {len(payloads)} {protocol.upper()} payloads for patterns"
                )

            # CRITICAL DEBUG: Show exactly what payloads we're analyzing
            if not self.quiet:
                print(f"   🔍 ANALYZING {protocol.upper()} PAYLOADS ({len(payloads)}):")
                for i, payload in enumerate(payloads):
                    source = packets[i].source if i < len(packets) else "unknown"
                    frame = packets[i].frame_number if i < len(packets) else "unknown"
                    print(
                        f"     #{i+1} (frame {frame}, from {source}): {payload[:60]}{'...' if len(payload) > 60 else ''}"
                    )

            # Find common prefix and suffix using strict algorithm
            prefix = self._find_common_prefix_strict(payloads)
            suffix = self._find_common_suffix_strict(payloads)

            patterns[protocol] = PatternInfo(prefix=prefix, suffix=suffix)

            if not self.quiet:
                if prefix or suffix:
                    print(
                        f"   {protocol.upper()}: PREFIX='{prefix}' ({len(prefix)//2} bytes) SUFFIX='{suffix}' ({len(suffix)//2} bytes)"
                    )
                    # Show which payloads match the detected patterns
                    if self.verbose:
                        matching_payloads = []
                        for i, payload in enumerate(payloads):
                            prefix_match = (
                                payload.startswith(prefix) if prefix else True
                            )
                            suffix_match = payload.endswith(suffix) if suffix else True
                            matching_payloads.append(
                                f"     Payload {i+1}: prefix={prefix_match}, suffix={suffix_match}"
                            )
                        print("\n".join(matching_payloads))
                else:
                    print(f"   {protocol.upper()}: No common prefix/suffix found")

        return patterns

    def apply_patterns_to_payload(
        self, payload: str, pattern_info: PatternInfo, protocol: str = None
    ) -> str:
        """Apply detected prefix/suffix patterns to a payload, replacing them with variables."""
        if not payload:
            return payload

        result = payload

        # Replace prefix if detected and present
        if pattern_info.prefix and result.startswith(pattern_info.prefix):
            prefix_size = len(pattern_info.prefix) // 2  # Convert hex chars to bytes
            protocol_upper = protocol.upper() if protocol else "UNKNOWN"
            result = (
                f"[{protocol_upper}_PREFIX:{prefix_size}]"
                + result[len(pattern_info.prefix) :]
            )

        # Replace suffix if detected and present
        if pattern_info.suffix and result.endswith(pattern_info.suffix):
            suffix_size = len(pattern_info.suffix) // 2  # Convert hex chars to bytes
            protocol_upper = protocol.upper() if protocol else "UNKNOWN"
            result = (
                result[: -len(pattern_info.suffix)]
                + f"[{protocol_upper}_SUFFIX:{suffix_size}]"
            )

        return result

    def _find_common_prefix_strict(self, payloads: List[str]) -> str:
        """Find common prefix using strict iterative algorithm."""
        if not payloads or len(payloads) < 2:
            return ""

        min_len = min(len(p) for p in payloads if p)
        if min_len < 4:  # Minimum 2 bytes = 4 hex chars
            return ""

        # Start with 2 bytes (4 hex chars) from first payload
        pattern_len = 4

        while pattern_len <= min_len:
            # Get pattern from first payload
            pattern = payloads[0][:pattern_len]

            # Check if ALL payloads have this exact prefix
            all_match = all(p.startswith(pattern) for p in payloads)

            if all_match:
                # All match, try with one more byte (2 hex chars)
                pattern_len += 2
                # Safety limit: don't go beyond 32 hex chars (16 bytes)
                if pattern_len > 32:
                    break
            else:
                # Not all match
                if pattern_len == 4:
                    # We're still at 2 bytes and it doesn't work
                    return ""  # No prefix
                else:
                    # Return pattern minus 1 byte (previous working pattern)
                    return payloads[0][: pattern_len - 2]

        # If we exit the loop, return the last working pattern
        return payloads[0][: pattern_len - 2] if pattern_len > 4 else ""

    def _find_common_suffix_strict(self, payloads: List[str]) -> str:
        """Find common suffix using strict iterative algorithm."""
        if not payloads or len(payloads) < 2:
            return ""

        min_len = min(len(p) for p in payloads if p)
        if min_len < 4:  # Minimum 2 bytes = 4 hex chars
            return ""

        # Start with 2 bytes (4 hex chars) from first payload
        pattern_len = 4

        while pattern_len <= min_len:
            # Get pattern from end of first payload
            pattern = payloads[0][-pattern_len:]

            # Check if ALL payloads have this exact suffix
            all_match = all(p.endswith(pattern) for p in payloads)

            if all_match:
                # All match, try with one more byte (2 hex chars)
                pattern_len += 2
                # Safety limit: don't go beyond 24 hex chars (12 bytes)
                if pattern_len > 24:
                    break
            else:
                # Not all match
                if pattern_len == 4:
                    # We're still at 2 bytes and it doesn't work
                    return ""  # No suffix
                else:
                    # Return pattern minus 1 byte (previous working pattern)
                    return payloads[0][-(pattern_len - 2) :]

        # If we exit the loop, return the last working pattern
        return payloads[0][-(pattern_len - 2) :] if pattern_len > 4 else ""
