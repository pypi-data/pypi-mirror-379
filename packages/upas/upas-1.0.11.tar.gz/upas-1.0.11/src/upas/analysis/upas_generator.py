#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UPAS Generator

Generates final UPAS protocol definitions from analysis results.
"""

from typing import Dict, Any

import json
from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict, Counter
import os
from dataclasses import dataclass
from .parser import PacketInfo
from .pattern import PatternInfo
from .similarity import SimilarityAnalyzer
from .behavior import BehaviorGenerator


class UpasGenerator:
    """Generates UPAS protocol definition from analysis results."""

    def __init__(self, verbose: bool = False, quiet: bool = False):
        self.verbose = verbose
        self.quiet = quiet

    def generate_upas_definition(
        self,
        intermediate: Dict,
        prefix_suffix: Dict[str, PatternInfo],
        payload_groups: Dict,
        embedded_ports: Dict,
        padding_info: Dict,
        sequence_analysis: Dict,
        trigger_analysis: Dict,
        behaviors: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate final UPAS protocol definition following SPECIFICATIONS.md format."""

        upas_def = {
            "protocol": {
                "name": "AnalyzedProtocol",
                "version": "1.0",
                "description": "Protocol extracted from Wireshark trace analysis",
                "category": "industrial",
            },
            "variables": {},
            "transports": {},
            "behaviors": behaviors,
        }

        # Add detected variables (simple hex strings, no brackets)
        for protocol in ["udp", "tcp"]:
            if prefix_suffix[protocol].prefix:
                upas_def["variables"][f"{protocol.upper()}_PREFIX"] = prefix_suffix[
                    protocol
                ].prefix
            if prefix_suffix[protocol].suffix:
                upas_def["variables"][f"{protocol.upper()}_SUFFIX"] = prefix_suffix[
                    protocol
                ].suffix

        # Generate transports section
        upas_def["transports"] = self._generate_transports_section(payload_groups)

        return upas_def

    def _generate_transports_section(self, payload_groups: Dict) -> Dict[str, Any]:
        """Generate transports section following UPAS specifications."""
        transports = {"primary_ethernet": {"type": "ethernet", "services": {}}}

        # Add UDP services if we have UDP flows
        if payload_groups.get("udp"):
            transports["primary_ethernet"]["services"]["udp_service"] = {
                "type": "udp_unicast",
                "bind": "0.0.0.0:0",
            }

        # Add TCP services if we have TCP flows
        if payload_groups.get("tcp"):
            transports["primary_ethernet"]["services"]["tcp_service"] = {
                "type": "tcp_server",
                "bind": "0.0.0.0:0",
            }

        return transports
