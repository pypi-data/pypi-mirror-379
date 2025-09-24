#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UPAS Command Line Interface

Main CLI entry point for UPAS operations.
"""

import asyncio
import argparse
import logging
import sys
import json
from pathlib import Path

from .core.engine import ProtocolEngine
from .analyzer import ProtocolAnalyzer


def setup_logging(
    level: str = "INFO", verbose: bool = False, debug: bool = False, quiet: bool = False
) -> None:
    """
    Setup logging configuration with different verbosity levels.

    :param level: Base logging level
    :type level: str
    :param verbose: Enable verbose output (packet details)
    :type verbose: bool
    :param debug: Enable debug output
    :type debug: bool
    :param quiet: Enable quiet mode (no logs)
    :type quiet: bool
    """
    if quiet:
        # Disable all logging
        logging.getLogger().setLevel(logging.CRITICAL + 1)
        return

    if debug:
        # Enable debug level for all modules
        log_level = logging.DEBUG
        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    elif verbose:
        # Enable info level but allow packet details
        log_level = logging.INFO
        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        # In verbose mode, show behavior actions and packet details
        logging.getLogger("src.upas.core.behavior").setLevel(logging.INFO)
        logging.getLogger("src.upas.core.transport").setLevel(logging.INFO)
        logging.getLogger("src.upas.core.state").setLevel(logging.INFO)
    else:
        # Default mode - only show critical behavior events
        logging.basicConfig(
            level=logging.WARNING,
            format="%(asctime)s - %(message)s",
            datefmt="%H:%M:%S",
        )

        # Silence all modules by default
        logging.getLogger("src.upas.core.engine").setLevel(logging.ERROR)
        logging.getLogger("src.upas.core.behavior.executor").setLevel(logging.ERROR)
        logging.getLogger("src.upas.core.behavior.scheduling.scheduler").setLevel(
            logging.ERROR
        )
        logging.getLogger("src.upas.core.transport").setLevel(logging.ERROR)

        # Only show state transitions and behavior triggers
        logging.getLogger("src.upas.core.state").setLevel(logging.WARNING)
        logging.getLogger("src.upas.core.behavior.types").setLevel(logging.WARNING)


async def analyze_trace(
    trace_file: str,
    output: str = None,
    intermediate: str = None,
    verbose: bool = False,
    quiet: bool = False,
    start_frame: int = None,
    end_frame: int = None,
    target: str = None,
) -> int:
    """
    Analyze a Wireshark trace file and generate UPAS protocol definition.

    :param trace_file: Path to Wireshark JSON export file
    :type trace_file: str
    :param output: Output UPAS protocol JSON file
    :type output: str
    :param intermediate: Save intermediate analysis results as JSON
    :type intermediate: str
    :param verbose: Verbose output
    :type verbose: bool
    :param quiet: Quiet mode, minimal output
    :type quiet: bool
    :param start_frame: Start analysis from this frame number
    :type start_frame: int
    :param end_frame: End analysis at this frame number
    :type end_frame: int
    :param target: Target IP address to simulate
    :type target: str
    :return: Exit code
    :rtype: int
    """
    if not quiet:
        print("🔬 UPAS Protocol Analyzer")
        print(f"📁 Analyzing: {trace_file}")
        if start_frame or end_frame:
            print(f"🎯 Frame range: {start_frame or 'start'} - {end_frame or 'end'}")
        if target:
            print(f"🎯 Target IP: {target} (modeling behavior of this host)")
        print("=" * 60)

    # Create analyzer
    analyzer = ProtocolAnalyzer(verbose=verbose, quiet=quiet, target_ip=target)

    try:
        # Analyze the trace file
        results = analyzer.analyze_file(trace_file, start_frame, end_frame)
    except Exception as e:
        if not quiet:
            print(f"❌ Error during analysis: {e}")
        return 1

    # Save intermediate results if requested
    if intermediate:
        try:
            with open(intermediate, "w") as f:
                json.dump(results, f, indent=2, default=str)
            if not quiet:
                print(f"💾 Intermediate results saved to: {intermediate}")
        except Exception as e:
            if not quiet:
                print(f"❌ Error saving intermediate results: {e}")
            return 1

    # Generate output file
    output_file = output or f"{Path(trace_file).stem}_protocol.json"

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results["upas_definition"], f, indent=2, ensure_ascii=False)
        if not quiet:
            print(f"✅ UPAS protocol definition saved to: {output_file}")
    except Exception as e:
        if not quiet:
            print(f"❌ Error saving output file: {e}")
        return 1

    if not quiet:
        print("\n🎉 Analysis completed successfully!")
    return 0


async def run_protocol(
    protocol_file: str,
    duration: int = 0,
    verbose: bool = False,
    debug: bool = False,
    quiet: bool = False,
) -> None:
    """
    Run a protocol from file.

    :param protocol_file: Path to protocol JSON file
    :type protocol_file: str
    :param duration: Run duration in seconds (0 = infinite)
    :type duration: int
    :param verbose: Enable verbose output
    :type verbose: bool
    :param debug: Enable debug output
    :type debug: bool
    :param quiet: Enable quiet mode
    :type quiet: bool
    """
    # Setup logging based on verbosity flags
    setup_logging(verbose=verbose, debug=debug, quiet=quiet)

    engine = ProtocolEngine()

    try:
        # Load and start protocol
        await engine.load_protocol(protocol_file)
        await engine.start()

        if not quiet:
            print(
                f"Protocol started. Running{'...' if duration == 0 else f' for {duration} seconds...'}"
            )

        # Run for specified duration or until interrupted
        if duration > 0:
            await asyncio.sleep(duration)
        else:
            # Run until interrupted
            try:
                while True:
                    await asyncio.sleep(1)
            except KeyboardInterrupt:
                if not quiet:
                    print("\nInterrupted by user")

    except Exception as e:
        if not quiet:
            print(f"Error: {e}")
        return 1
    finally:
        await engine.stop()
        if not quiet:
            print("Protocol stopped")

    return 0


def create_parser() -> argparse.ArgumentParser:
    """
    Create command line argument parser.

    :return: Configured argument parser
    :rtype: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description="UPAS - Universal Protocol Analysis & Simulation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  upas analyze trace.json              # Analyze trace and generate protocol
  upas analyze trace.json -o my.json  # Analyze with custom output file
  upas analyze trace.json --target 192.168.1.100  # Target specific IP
  upas run protocol.json               # Run protocol indefinitely
  upas run protocol.json -d 60         # Run for 60 seconds
  upas validate protocol.json          # Validate protocol file
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Analyze command
    analyze_parser = subparsers.add_parser(
        "analyze", help="Analyze a Wireshark trace file"
    )
    analyze_parser.add_argument(
        "trace_file", help="Wireshark JSON export file to analyze"
    )
    analyze_parser.add_argument("-o", "--output", help="Output UPAS protocol JSON file")
    analyze_parser.add_argument(
        "--intermediate", help="Save intermediate analysis results as JSON"
    )
    analyze_parser.add_argument(
        "-v", "--verbose", action="store_true", help="Verbose output"
    )
    analyze_parser.add_argument(
        "-q", "--quiet", action="store_true", help="Quiet mode, minimal output"
    )
    analyze_parser.add_argument(
        "--start-frame", type=int, help="Start analysis from this frame number"
    )
    analyze_parser.add_argument(
        "--end-frame", type=int, help="End analysis at this frame number"
    )
    analyze_parser.add_argument(
        "--target",
        type=str,
        help="Target IP address to simulate (only model behavior of this host)",
    )

    # Run command
    run_parser = subparsers.add_parser("run", help="Run a protocol")
    run_parser.add_argument("protocol", help="Protocol JSON file")
    run_parser.add_argument(
        "--duration",
        type=int,
        default=0,
        help="Run duration in seconds (0 = infinite)",
    )

    # Verbosity options for run command (mutually exclusive)
    run_verbosity = run_parser.add_mutually_exclusive_group()
    run_verbosity.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose output (show packet details)",
    )
    run_verbosity.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Debug output (show all internal details)",
    )
    run_verbosity.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Quiet mode (no logs)",
    )

    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Validate a protocol file")
    validate_parser.add_argument("protocol", help="Protocol JSON file")
    validate_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose output",
    )

    # List command
    list_parser = subparsers.add_parser("list", help="List available protocols")
    list_parser.add_argument(
        "directory", nargs="?", default=".", help="Directory to search for protocols"
    )

    # Version command
    subparsers.add_parser("version", help="Show version information")

    return parser


async def validate_protocol(protocol_file: str) -> int:
    """
    Validate a protocol file.

    :param protocol_file: Path to protocol file
    :type protocol_file: str
    :return: Exit code
    :rtype: int
    """
    engine = ProtocolEngine()

    try:
        await engine.load_protocol(protocol_file)
        print(f"✓ Protocol file '{protocol_file}' is valid")
        return 0
    except Exception as e:
        print(f"✗ Protocol file '{protocol_file}' is invalid: {e}")
        return 1


def list_protocols(directory: str) -> int:
    """
    List available protocol files.

    :param directory: Directory to search
    :type directory: str
    :return: Exit code
    :rtype: int
    """
    search_path = Path(directory)

    if not search_path.exists():
        print(f"Directory '{directory}' does not exist")
        return 1

    json_files = list(search_path.glob("*.json"))

    if not json_files:
        print(f"No JSON protocol files found in '{directory}'")
        return 0

    print(f"Protocol files in '{directory}':")
    for json_file in sorted(json_files):
        print(f"  {json_file.name}")

    return 0


def show_version() -> None:
    """Show version information."""
    print("UPAS - Universal Protocol Analysis & Simulation")
    print("Version: 1.0.0")
    print("Author: BitsDiver Team")
    print("License: MIT")
    print("Repository: https://github.com/BitsDiver/upas-cli")


def main() -> int:
    """
    Main CLI entry point.

    :return: Exit code
    :rtype: int
    """
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Setup logging for commands that need it
    if args.command == "run":
        return asyncio.run(
            run_protocol(
                args.protocol, args.duration, args.verbose, args.debug, args.quiet
            )
        )
    elif hasattr(args, "verbose") and args.command == "validate":
        setup_logging(verbose=args.verbose)
    elif hasattr(args, "verbose") and args.command == "analyze":
        pass  # Analyze command has its own logging setup

    # Handle commands
    if args.command == "analyze":
        return asyncio.run(
            analyze_trace(
                args.trace_file,
                args.output,
                args.intermediate,
                args.verbose,
                args.quiet,
                args.start_frame,
                args.end_frame,
                args.target,
            )
        )

    elif args.command == "validate":
        return asyncio.run(validate_protocol(args.protocol))

    elif args.command == "list":
        return list_protocols(args.directory)

    elif args.command == "version":
        show_version()
        return 0

    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
