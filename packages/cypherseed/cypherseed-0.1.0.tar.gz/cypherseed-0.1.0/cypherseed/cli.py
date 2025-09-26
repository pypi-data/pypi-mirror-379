"""
Command-line interface for cypherseed.

This module provides the CLI functionality with subcommands for generating passphrases,
calculating strength, and managing wordlists.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

from . import __version__
from .generator import generate_passphrase, generate_multiple_passphrases
from .password_strength import analyse_passphrase_strength, calculate_strength
from .utils import (
    analyse_wordlist,
    create_alphabet_filter,
    create_combined_filter,
    create_length_filter,
    create_pattern_filter,
    download_wordlist,
    filter_wordlist,
)
from .wordlists import get_available_wordlists, get_wordlist_info, load_wordlist


def cmd_generate(args: argparse.Namespace) -> None:
    """
    Handle the 'generate' subcommand to create passphrases.

    Args:
        args: Parsed command line arguments.
    """
    try:
        # generate single or multiple passphrases
        if args.count and args.count > 1:
            passphrases = generate_multiple_passphrases(
                wordlist_name=args.wordlist,
                word_count=args.word_count,
                count=args.count,
                separator=args.separator,
                min_word_length=args.min_length,
                max_word_length=args.max_length,
                include_numbers=args.include_numbers,
                include_symbols=args.include_symbols,
                random_separators=args.random_separators,
            )
            
            print()  # empty line before output
            print(f"Generated {args.count} passphrases:")
            for i, passphrase in enumerate(passphrases, 1):
                print(f"{i:2d}. {passphrase}")
        else:
            passphrase = generate_passphrase(
                wordlist_name=args.wordlist,
                word_count=args.word_count,
                separator=args.separator,
                min_word_length=args.min_length,
                max_word_length=args.max_length,
                include_numbers=args.include_numbers,
                include_symbols=args.include_symbols,
                random_separators=args.random_separators,
            )
            print()  # empty line before output
            print(f"Generated passphrase: {passphrase}")

        # show strength analysis if requested
        if args.show_strength:
            try:
                # load wordlist to get actual size after filtering
                wordlist = load_wordlist(args.wordlist)
                
                # apply same filtering as generator
                if args.min_length or args.max_length:
                    wordlist = [
                        word for word in wordlist
                        if (args.min_length is None or len(word) >= args.min_length) and
                           (args.max_length is None or len(word) <= args.max_length)
                    ]
                
                if wordlist:
                    analysis = analyse_passphrase_strength(
                        word_count=args.word_count,
                        wordlist_size=len(wordlist),
                        include_numbers=args.include_numbers,
                        include_symbols=args.include_symbols,
                    )
                    
                    print()  # empty line before strength analysis
                    print("Strength Analysis:")
                    print(f"  Entropy: {analysis['entropy_bits']:.1f} bits")
                    print(f"  Classification: {analysis['strength_classification']}")
                    print(f"  Time to crack: {analysis['time_to_crack']['human_readable']}")
                    print(f"  Total combinations: {analysis['total_combinations']:.2e}")
                
            except Exception as e:
                print(f"Warning: Could not calculate strength: {e}")
        
        print()  # empty line after output

    except Exception as e:
        print(f"Error generating passphrase: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_calculate(args: argparse.Namespace) -> None:
    """
    Handle the 'calculate' subcommand to analyse passphrase strength.

    Args:
        args: Parsed command line arguments.
    """
    try:
        if args.wordlist:
            # calculate based on actual wordlist
            wordlist = load_wordlist(args.wordlist)
            
            # apply filtering if specified
            if args.min_length or args.max_length:
                wordlist = [
                    word for word in wordlist
                    if (args.min_length is None or len(word) >= args.min_length) and
                       (args.max_length is None or len(word) <= args.max_length)
                ]
            
            wordlist_size = len(wordlist)
            print()  # empty line before output
            print(f"Using wordlist '{args.wordlist}' with {wordlist_size} words")
        else:
            # use provided wordlist size
            wordlist_size = args.wordlist_size
        
        # calculate strength
        if args.detailed:
            analysis = analyse_passphrase_strength(
                word_count=args.word_count,
                wordlist_size=wordlist_size,
                include_numbers=getattr(args, 'include_numbers', False),
                include_symbols=getattr(args, 'include_symbols', False),
            )
            
            print()  # empty line before output
            print("Passphrase Strength Analysis:")
            print(f"  Word count: {analysis['word_count']}")
            print(f"  Wordlist size: {analysis['wordlist_size']}")
            print(f"  Base entropy: {analysis['base_entropy_bits']:.1f} bits")
            
            if analysis['additional_entropy_bits'] > 0:
                print(f"  Additional entropy: {analysis['additional_entropy_bits']:.1f} bits")
            
            print(f"  Total entropy: {analysis['entropy_bits']:.1f} bits")
            print(f"  Classification: {analysis['strength_classification']}")
            print(f"  Total combinations: {analysis['total_combinations']:.2e}")
            print(f"  Time to crack (avg): {analysis['time_to_crack']['human_readable']}")
            print()  # empty line after output
            
        else:
            # simple calculation
            strength = calculate_strength(args.word_count, wordlist_size)
            print()  # empty line before output
            print(f"Passphrase strength: {strength:.2f} bits")
            print()  # empty line after output

    except Exception as e:
        print(f"Error calculating strength: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_update(args: argparse.Namespace) -> None:
    """
    Handle the 'update' subcommand to manage wordlists.

    Args:
        args: Parsed command line arguments.
    """
    try:
        # download wordlist
        if args.download:
            destination = Path(args.destination) if args.destination else Path("downloaded_wordlist.txt")
            download_wordlist(args.download, destination)
            
            if args.analyse:
                print(f"\nAnalyzing downloaded wordlist...")
                stats = analyse_wordlist(destination)
                print_wordlist_stats(stats)
        
        # filter existing wordlist
        elif args.source and args.destination:
            source = Path(args.source)
            destination = Path(args.destination)
            
            # create filter function based on arguments
            filters = []
            
            if args.min_length or args.max_length:
                filters.append(create_length_filter(args.min_length, args.max_length))
            
            if not args.allow_non_ascii or not args.allow_numbers:
                filters.append(create_alphabet_filter(
                    allow_non_ascii=args.allow_non_ascii,
                    allow_numbers=args.allow_numbers
                ))
            
            if args.exclude_pattern:
                filters.append(create_pattern_filter(args.exclude_pattern, exclude=True))
            
            if args.include_pattern:
                filters.append(create_pattern_filter(args.include_pattern, exclude=False))
            
            # combine all filters
            if filters:
                criteria_func = create_combined_filter(*filters)
            else:
                criteria_func = lambda word: True  # no filtering
            
            # filter wordlist
            word_count = filter_wordlist(
                source=source,
                destination=destination,
                criteria_func=criteria_func,
                remove_duplicates=not args.keep_duplicates,
                sort_output=not args.no_sort
            )
            
            if args.analyse:
                print(f"\nAnalyzing filtered wordlist...")
                stats = analyse_wordlist(destination)
                print_wordlist_stats(stats)
        
        # analyse existing wordlist
        elif args.analyse and args.source:
            source = Path(args.source)
            stats = analyse_wordlist(source)
            print_wordlist_stats(stats)
        
        # list available wordlists
        elif args.list:
            print("Available wordlists:")
            for wordlist in get_available_wordlists():
                try:
                    info = get_wordlist_info(wordlist)
                    print(f"  {wordlist}: {info['size']} words "
                          f"(length: {info['min_word_length']}-{info['max_word_length']})")
                except Exception as e:
                    print(f"  {wordlist}: Error loading - {e}")
        
        else:
            print("No action specified. Use --help for usage information.", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"Error in update command: {e}", file=sys.stderr)
        sys.exit(1)


def print_wordlist_stats(stats: dict) -> None:
    """
    Print wordlist statistics in a formatted way.

    Args:
        stats: Dictionary containing wordlist statistics.
    """
    if "error" in stats:
        print(f"Error: {stats['error']}")
        return
    
    print(f"Wordlist Statistics:")
    print(f"  File: {stats['file_path']}")
    print(f"  Total lines: {stats['total_lines']}")
    print(f"  Unique words: {stats['unique_words']}")
    print(f"  Duplicates: {stats['duplicates']}")
    print(f"  Empty lines: {stats['empty_lines']}")
    print(f"  Word length: {stats['min_word_length']}-{stats['max_word_length']} "
          f"(avg: {stats['avg_word_length']:.1f})")
    print(f"  Total characters: {stats['total_characters']}")
    print(f"  Contains non-ASCII: {'Yes' if stats['has_non_ascii'] else 'No'}")
    print(f"  Contains numbers: {'Yes' if stats['has_numbers'] else 'No'}")


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="cypherseed",
        description="Generate high-entropy passphrases using wordlists",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"cypherseed {__version__}"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # generate subcommand
    generate_parser = subparsers.add_parser("generate", help="Generate passphrases")
    generate_parser.add_argument(
        "word_count",
        type=int,
        help="Number of words in the passphrase"
    )
    generate_parser.add_argument(
        "--wordlist",
        type=str,
        default="default",
        help="Name of the wordlist to use (default: default)"
    )
    generate_parser.add_argument(
        "--separator",
        type=str,
        default="-",
        help="Separator between words (default: -)"
    )
    generate_parser.add_argument(
        "--min-length",
        type=int,
        help="Minimum length of each word"
    )
    generate_parser.add_argument(
        "--max-length",
        type=int,
        help="Maximum length of each word"
    )
    generate_parser.add_argument(
        "--include-numbers",
        action="store_true",
        help="Include numbers in the passphrase"
    )
    generate_parser.add_argument(
        "--include-symbols",
        action="store_true",
        help="Include symbols in the passphrase"
    )
    generate_parser.add_argument(
        "--random-separators",
        action="store_true",
        help="Use random numbers/symbols as separators between words (overrides --separator)"
    )
    generate_parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of passphrases to generate (default: 1)"
    )
    generate_parser.add_argument(
        "--show-strength",
        action="store_true",
        help="Show strength analysis of generated passphrase"
    )
    
    # calculate subcommand
    calc_parser = subparsers.add_parser("calculate", help="Calculate passphrase strength")
    calc_parser.add_argument(
        "word_count",
        type=int,
        help="Number of words in the passphrase"
    )
    # either wordlist or wordlist_size is required
    calc_group = calc_parser.add_mutually_exclusive_group(required=True)
    calc_group.add_argument(
        "--wordlist",
        type=str,
        help="Name of the wordlist to analyse"
    )
    calc_group.add_argument(
        "wordlist_size",
        type=int,
        nargs="?",
        help="Size of the wordlist (number of words)"
    )
    calc_parser.add_argument(
        "--min-length",
        type=int,
        help="Minimum word length (when using --wordlist)"
    )
    calc_parser.add_argument(
        "--max-length",
        type=int,
        help="Maximum word length (when using --wordlist)"
    )
    calc_parser.add_argument(
        "--include-numbers",
        action="store_true",
        help="Account for numbers in strength calculation"
    )
    calc_parser.add_argument(
        "--include-symbols",
        action="store_true",
        help="Account for symbols in strength calculation"
    )
    calc_parser.add_argument(
        "--detailed",
        action="store_true",
        help="Show detailed strength analysis"
    )
    
    # update subcommand
    update_parser = subparsers.add_parser("update", help="Manage wordlists")
    update_parser.add_argument(
        "--download",
        metavar="URL",
        type=str,
        help="URL to download a new wordlist from"
    )
    update_parser.add_argument(
        "--source",
        metavar="FILE",
        type=str,
        help="Source wordlist file path for filtering"
    )
    update_parser.add_argument(
        "--destination",
        metavar="FILE",
        type=str,
        help="Destination file path for the updated wordlist"
    )
    update_parser.add_argument(
        "--min-length",
        type=int,
        help="Minimum word length for filtering"
    )
    update_parser.add_argument(
        "--max-length",
        type=int,
        help="Maximum word length for filtering"
    )
    update_parser.add_argument(
        "--exclude-pattern",
        type=str,
        help="Regex pattern to exclude words"
    )
    update_parser.add_argument(
        "--include-pattern",
        type=str,
        help="Regex pattern to include only matching words"
    )
    update_parser.add_argument(
        "--allow-non-ascii",
        action="store_true",
        help="Allow non-ASCII characters in words"
    )
    update_parser.add_argument(
        "--allow-numbers",
        action="store_true",
        help="Allow numbers in words"
    )
    update_parser.add_argument(
        "--keep-duplicates",
        action="store_true",
        help="Keep duplicate words (case-insensitive)"
    )
    update_parser.add_argument(
        "--no-sort",
        action="store_true",
        help="Don't sort the output alphabetically"
    )
    update_parser.add_argument(
        "--analyse",
        action="store_true",
        help="Analyse the wordlist after processing"
    )
    update_parser.add_argument(
        "--list",
        action="store_true",
        help="List available built-in wordlists"
    )
    
    return parser


def main() -> None:
    """
    Main entry point for the CLI.
    """
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # dispatch to appropriate command handler
    if args.command == "generate":
        cmd_generate(args)
    elif args.command == "calculate":
        cmd_calculate(args)
    elif args.command == "update":
        cmd_update(args)
    else:
        parser.print_help()
        sys.exit(1)