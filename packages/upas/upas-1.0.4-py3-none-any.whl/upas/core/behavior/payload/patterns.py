"""
Enhanced pattern processing for UPAS with advanced matching capabilities
"""

import re
import logging
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class PatternOperation(Enum):
    """Pattern matching operations."""

    EXACT = "exact"
    STARTS_WITH = "starts_with"
    ENDS_WITH = "ends_with"
    CONTAINS = "contains"
    NOT_CONTAINS = "not_contains"
    REGEX = "regex"


@dataclass
class WildcardPattern:
    """Represents a wildcard pattern in payload."""

    name: str
    size: int
    offset: Optional[int] = None

    def __post_init__(self):
        """Validate wildcard pattern."""
        if self.size <= 0:
            raise ValueError(f"Wildcard size must be positive, got {self.size}")

        if self.offset is not None and self.offset < 0:
            raise ValueError(f"Wildcard offset must be non-negative, got {self.offset}")


@dataclass
class PatternMatcher:
    """Pattern matcher configuration."""

    operation: PatternOperation
    pattern: str
    case_sensitive: bool = True

    def __post_init__(self):
        """Validate pattern matcher."""
        if not self.pattern:
            raise ValueError("Pattern cannot be empty")


class EnhancedPatternProcessor:
    """Enhanced pattern processor with wildcard and advanced matching support."""

    def __init__(self):
        """Initialize enhanced pattern processor."""
        self.logger = logging.getLogger(__name__)
        self.wildcard_regex = re.compile(r"\[(?:WILDCARD|SKIP):(\d+)\]")
        self.capture_regex = re.compile(r"\[CAPTURE:([A-Z_][A-Z0-9_]*):(\d+)\]")
        self.variable_regex = re.compile(r"\[([A-Z_][A-Z0-9_]*)\]")
        self.counter_regex = re.compile(r"\[COUNTER:(\d+)(?::([a-z_]+))?\]")

    def extract_wildcards(self, pattern: str) -> List[WildcardPattern]:
        """
        Extract wildcard patterns from a pattern string.

        Supports:
        - [WILDCARD:n] - Generate n bytes of wildcards
        - [SKIP:n] - Same as WILDCARD (alias)

        Args:
            pattern: Pattern string to analyze

        Returns:
            List of wildcard patterns found
        """
        wildcards = []

        for match in self.wildcard_regex.finditer(pattern):
            size = int(match.group(1))
            start_pos = match.start()

            wildcard = WildcardPattern(
                name=f"wildcard_{len(wildcards)}", size=size, offset=start_pos
            )
            wildcards.append(wildcard)

            self.logger.debug(f"Found wildcard: {size} bytes at offset {start_pos}")

        return wildcards

    def create_pattern_mask(self, pattern: str) -> str:
        """
        Create a pattern mask where wildcards and captures are replaced with regex patterns.

        Args:
            pattern: Original pattern with wildcards and captures

        Returns:
            Regex pattern for matching
        """
        # First, escape all regex special characters in the original pattern
        # but preserve our wildcard and capture placeholders
        escaped_pattern = ""
        last_end = 0

        # Find all wildcard and capture matches
        # Combine both wildcard and capture patterns
        combined_regex = (
            r"\[(?:(?:WILDCARD|SKIP):(\d+)|CAPTURE:[A-Z_][A-Z0-9_]*:(\d+))\]"
        )

        for match in re.finditer(combined_regex, pattern):
            # Add escaped text before wildcard/capture
            before_marker = pattern[last_end : match.start()]
            escaped_pattern += re.escape(before_marker)

            # Determine if it's wildcard or capture and get size
            if match.group(1):  # WILDCARD or SKIP
                size = int(match.group(1))
            elif match.group(2):  # CAPTURE
                size = int(match.group(2))
            else:
                size = 1  # Default fallback

            # Add regex pattern for the marker (number of hex chars = size * 2)
            hex_chars = size * 2  # Each byte = 2 hex characters
            escaped_pattern += f"[0-9A-Fa-f]{{{hex_chars}}}"

            last_end = match.end()

        # Add escaped text after last marker
        remaining = pattern[last_end:]
        escaped_pattern += re.escape(remaining)

        return escaped_pattern

    def match_with_wildcards(self, pattern: str, data: str) -> bool:
        """
        Match data against pattern with wildcard support.

        Args:
            pattern: Pattern with possible wildcards
            data: Data to match against

        Returns:
            True if data matches pattern (considering wildcards)
        """
        try:
            # Convert pattern to regex with wildcards
            regex_pattern = self.create_pattern_mask(pattern)

            self.logger.debug(
                f"Matching pattern '{regex_pattern}' against data length {len(data)}"
            )

            # Compile and match
            compiled_pattern = re.compile(regex_pattern, re.DOTALL)
            match = compiled_pattern.fullmatch(data)

            return match is not None

        except re.error as e:
            self.logger.error(f"Regex error in pattern matching: {e}")
            return False

    def apply_pattern_operation(self, data: str, matcher: PatternMatcher) -> bool:
        """
        Apply pattern operation to data.

        Args:
            data: Data to test
            matcher: Pattern matcher configuration

        Returns:
            True if operation matches
        """
        pattern = matcher.pattern
        operation = matcher.operation

        # Handle case sensitivity
        if not matcher.case_sensitive:
            data = data.lower()
            pattern = pattern.lower()

        try:
            if operation == PatternOperation.EXACT:
                return data == pattern

            elif operation == PatternOperation.STARTS_WITH:
                return data.startswith(pattern)

            elif operation == PatternOperation.ENDS_WITH:
                return data.endswith(pattern)

            elif operation == PatternOperation.CONTAINS:
                return pattern in data

            elif operation == PatternOperation.NOT_CONTAINS:
                return pattern not in data

            elif operation == PatternOperation.REGEX:
                compiled_pattern = re.compile(
                    pattern, re.IGNORECASE if not matcher.case_sensitive else 0
                )
                return bool(compiled_pattern.search(data))

            else:
                self.logger.warning(f"Unknown pattern operation: {operation}")
                return False

        except (re.error, TypeError) as e:
            self.logger.error(f"Error in pattern operation {operation}: {e}")
            return False

    def normalize_hex_data(self, data: str) -> str:
        """
        Normalize hex data for pattern matching.

        Args:
            data: Raw hex data (may have spaces, prefixes)

        Returns:
            Normalized hex string
        """
        # Remove common prefixes and spaces
        normalized = data.replace("0x", "").replace(" ", "").upper()

        # Ensure even length
        if len(normalized) % 2 != 0:
            normalized = "0" + normalized

        return normalized

    def hex_to_ascii_safe(self, hex_string: str) -> str:
        """
        Convert hex string to ASCII with safe fallback.

        Args:
            hex_string: Hex string to convert

        Returns:
            ASCII representation or original if conversion fails
        """
        try:
            # Normalize first
            normalized = self.normalize_hex_data(hex_string)

            # Convert to bytes then ASCII
            bytes_data = bytes.fromhex(normalized)
            ascii_data = bytes_data.decode("ascii", errors="replace")

            return ascii_data

        except ValueError:
            # If conversion fails, return original
            return hex_string

    def create_enhanced_matcher(
        self, trigger_config: Dict[str, Any]
    ) -> Optional[PatternMatcher]:
        """
        Create enhanced pattern matcher from trigger configuration.

        Args:
            trigger_config: Trigger configuration

        Returns:
            PatternMatcher if valid config, None otherwise
        """
        # Extract operation type
        operation_name = trigger_config.get("operation", "contains")

        try:
            operation = PatternOperation(operation_name)
        except ValueError:
            self.logger.warning(f"Unknown pattern operation: {operation_name}")
            return None

        # Extract pattern
        pattern = trigger_config.get("pattern")
        if not pattern:
            self.logger.warning("No pattern specified in trigger config")
            return None

        # Extract options
        case_sensitive = trigger_config.get("case_sensitive", True)

        return PatternMatcher(
            operation=operation, pattern=pattern, case_sensitive=case_sensitive
        )


class PayloadAnalyzer:
    """Analyzes payload for patterns and wildcard extraction."""

    def __init__(self):
        """Initialize payload analyzer."""
        self.pattern_processor = EnhancedPatternProcessor()
        self.logger = logging.getLogger(__name__)

    def analyze_trigger_pattern(
        self, data: str, trigger_config: Dict[str, Any]
    ) -> bool:
        """
        Analyze data against trigger pattern with enhanced matching.

        Args:
            data: Data to analyze
            trigger_config: Trigger configuration

        Returns:
            True if data matches trigger pattern
        """
        # Handle legacy "pattern" field (backward compatibility)
        if "pattern" in trigger_config and "operation" not in trigger_config:
            # Legacy mode: contains matching
            pattern = trigger_config["pattern"]
            return pattern in data

        # Enhanced mode: use pattern operations
        matcher = self.pattern_processor.create_enhanced_matcher(trigger_config)
        if not matcher:
            return False

        # Apply hex normalization if needed
        if trigger_config.get("hex_mode", False):
            data = self.pattern_processor.normalize_hex_data(data)
            matcher.pattern = self.pattern_processor.normalize_hex_data(matcher.pattern)

        # Check for wildcards in pattern
        if "[WILDCARD:" in matcher.pattern or "[SKIP:" in matcher.pattern:
            return self.pattern_processor.match_with_wildcards(matcher.pattern, data)
        else:
            return self.pattern_processor.apply_pattern_operation(data, matcher)

    def extract_pattern_variables(self, pattern: str, data: str) -> Dict[str, str]:
        """
        Extract variables from data using pattern with CAPTURE keywords.
        This method requires a payload builder to expand regular variables first.

        Args:
            pattern: Pattern with CAPTURE, wildcards and variables
            data: Data to extract from

        Returns:
            Dictionary of extracted variables
        """
        variables = {}

        try:
            # This is a simplified implementation
            # For a complete implementation, we need access to PayloadBuilder
            # to expand regular variables before extracting CAPTURE variables

            # Find all CAPTURE patterns
            capture_matches = list(
                re.finditer(r"\[CAPTURE:([A-Z_][A-Z0-9_]*):(\d+)\]", pattern)
            )

            if not capture_matches:
                return variables

            # For now, implement a basic extraction assuming pattern structure
            # This is a simplified version - a full implementation would need
            # to parse the entire pattern and match segment by segment

            for match in capture_matches:
                var_name = match.group(1)
                size_bytes = int(match.group(2))

                # Store placeholder - actual extraction would need full pattern parsing
                # This is where we'd need the PayloadBuilder to expand other variables
                self.logger.debug(
                    f"Found CAPTURE pattern for {var_name} (size: {size_bytes} bytes)"
                )

                # For testing, we can try to extract if it's at a known position
                # But this is not a complete implementation
                variables[var_name] = "00" * size_bytes  # Placeholder

        except Exception as e:
            self.logger.error(f"Error extracting pattern variables: {e}")

        return variables

    def match_pattern_with_capture(
        self, pattern: str, data: str, payload_builder=None
    ) -> Tuple[bool, Dict[str, str]]:
        """
        Match pattern against data and extract CAPTURE variables.
        This method properly handles variable expansion and capture extraction.

        Args:
            pattern: Pattern with variables, CAPTURE, wildcards
            data: Data to match against
            payload_builder: PayloadBuilder instance for variable expansion

        Returns:
            Tuple of (match_success, captured_variables)
        """
        captured_vars = {}

        try:
            # Parse pattern into segments for detailed matching
            segments = self._parse_pattern_for_matching(pattern, payload_builder)

            # Match segments against data
            match_success, captured_vars = self._match_pattern_segments(data, segments)

            return match_success, captured_vars

        except Exception as e:
            self.logger.error(f"Error in pattern matching with capture: {e}")
            return False, {}

    def _parse_pattern_for_matching(
        self, pattern: str, payload_builder=None
    ) -> List[Dict[str, Any]]:
        """
        Parse pattern into segments for matching.

        Args:
            pattern: Pattern to parse
            payload_builder: PayloadBuilder for variable expansion

        Returns:
            List of pattern segments
        """
        segments = []
        pos = 0

        while pos < len(pattern):
            bracket_start = pattern.find("[", pos)

            if bracket_start == -1:
                # No more variables, rest is fixed text
                if pos < len(pattern):
                    fixed_text = pattern[pos:]
                    if fixed_text and payload_builder:
                        expanded = payload_builder.build_payload([fixed_text])
                        if expanded:
                            segments.append(
                                {"type": "fixed", "value": expanded.upper()}
                            )
                break

            # Add fixed text before bracket
            if bracket_start > pos:
                fixed_text = pattern[pos:bracket_start]
                if fixed_text and payload_builder:
                    expanded = payload_builder.build_payload([fixed_text])
                    if expanded:
                        segments.append({"type": "fixed", "value": expanded.upper()})

            # Find matching bracket
            bracket_end = pattern.find("]", bracket_start)
            if bracket_end == -1:
                break

            # Extract variable content
            var_content = pattern[bracket_start + 1 : bracket_end]
            pos = bracket_end + 1

            # Parse variable content
            if var_content.startswith("CAPTURE:"):
                # [CAPTURE:VAR_NAME:size]
                parts = var_content[8:].split(":")  # Remove 'CAPTURE:'
                if len(parts) >= 2:
                    var_name = parts[0]
                    size = int(parts[1])
                    segments.append(
                        {"type": "capture", "var_name": var_name, "size_bytes": size}
                    )
            elif var_content.startswith("WILDCARD:") or var_content.startswith("SKIP:"):
                # [WILDCARD:size] or [SKIP:size]
                parts = var_content.split(":")
                if len(parts) >= 2:
                    size = int(parts[1])
                    segments.append({"type": "wildcard", "size_bytes": size})
            else:
                # Regular variable [VAR_NAME:size] or [VAR_NAME:size:function]
                if payload_builder:
                    var_pattern = f"[{var_content}]"
                    expanded = payload_builder.build_payload([var_pattern])
                    if expanded:
                        segments.append({"type": "fixed", "value": expanded.upper()})

        return segments

    def _match_pattern_segments(
        self, data: str, segments: List[Dict[str, Any]]
    ) -> Tuple[bool, Dict[str, str]]:
        """
        Match data against pattern segments and extract captures.

        Args:
            data: Data to match
            segments: Parsed pattern segments

        Returns:
            Tuple of (match_success, captured_variables)
        """
        data_pos = 0
        captured_vars = {}

        for segment in segments:
            segment_type = segment["type"]

            if segment_type == "fixed":
                # Match fixed text
                expected = segment["value"]
                expected_len = len(expected)

                if data_pos + expected_len > len(data):
                    return False, {}

                actual = data[data_pos : data_pos + expected_len]
                if actual.upper() != expected.upper():
                    return False, {}

                data_pos += expected_len

            elif segment_type == "capture":
                # Capture variable bytes
                var_name = segment["var_name"]
                size_bytes = segment["size_bytes"]
                capture_len = size_bytes * 2  # 2 hex chars per byte

                if data_pos + capture_len > len(data):
                    return False, {}

                captured_value = data[data_pos : data_pos + capture_len]
                captured_vars[var_name] = captured_value
                data_pos += capture_len

                self.logger.debug(f"Captured {var_name} = {captured_value}")

            elif segment_type == "wildcard":
                # Skip wildcard bytes
                size_bytes = segment["size_bytes"]
                skip_len = size_bytes * 2  # 2 hex chars per byte

                if data_pos + skip_len > len(data):
                    return False, {}

                data_pos += skip_len

        # Check if we consumed the entire data
        if data_pos != len(data):
            return False, {}

        return True, captured_vars


# Convenience functions for backward compatibility
def create_pattern_matcher(operation: str, pattern: str, **kwargs) -> PatternMatcher:
    """Create a pattern matcher with given operation and pattern."""
    try:
        op_enum = PatternOperation(operation)
    except ValueError:
        op_enum = PatternOperation.CONTAINS

    return PatternMatcher(
        operation=op_enum,
        pattern=pattern,
        case_sensitive=kwargs.get("case_sensitive", True),
    )


def match_pattern(data: str, pattern: str, operation: str = "contains") -> bool:
    """Quick pattern matching function."""
    processor = EnhancedPatternProcessor()
    matcher = create_pattern_matcher(operation, pattern)
    return processor.apply_pattern_operation(data, matcher)
