"""
Utility functions for cypherseed.

This module provides wordlist management, downloading, and filtering functionality
for maintaining and updating wordlists used by cypherseed.
"""

import re
import sys
from pathlib import Path
from typing import Callable, List, Optional, Set
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    requests = None


def download_wordlist(url: str, destination: Path, timeout: int = 30) -> None:
    """
    Download a wordlist from a given URL and save it to the specified destination.

    Args:
        url: URL of the wordlist to download.
        destination: Path to save the downloaded wordlist.
        timeout: Timeout in seconds for the download request.

    Raises:
        ImportError: If requests library is not available.
        requests.RequestException: If download fails.
        ValueError: If URL is invalid.
    """
    if requests is None:
        raise ImportError("requests library is required for downloading wordlists. Install with: pip install requests")
    
    # validate url
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        raise ValueError(f"Invalid URL: {url}")
    
    try:
        print(f"Downloading wordlist from {url}...")
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        
        # ensure destination directory exists
        destination.parent.mkdir(parents=True, exist_ok=True)
        
        # write content to file
        with open(destination, 'w', encoding='utf-8') as file:
            file.write(response.text)
            
        print(f"Wordlist downloaded successfully to {destination}")
        
    except requests.RequestException as e:
        raise requests.RequestException(f"Failed to download wordlist from {url}: {e}")


def filter_wordlist(
    source: Path, 
    destination: Path, 
    criteria_func: Callable[[str], bool],
    remove_duplicates: bool = True,
    sort_output: bool = True
) -> int:
    """
    Filter a wordlist based on specified criteria and save the filtered list.

    Args:
        source: Path of the source wordlist.
        destination: Path to save the filtered wordlist.
        criteria_func: Function that returns True if a word meets the criteria.
        remove_duplicates: Whether to remove duplicate words.
        sort_output: Whether to sort the output alphabetically.

    Returns:
        Number of words in the filtered wordlist.

    Raises:
        FileNotFoundError: If source file doesn't exist.
    """
    if not source.exists():
        raise FileNotFoundError(f"Source wordlist not found: {source}")
    
    print(f"Filtering wordlist from {source} to {destination}...")
    
    filtered_words = []
    seen_words: Set[str] = set() if remove_duplicates else set()
    total_processed = 0
    
    # ensure destination directory exists
    destination.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(source, 'r', encoding='utf-8') as src:
            for line_num, line in enumerate(src, 1):
                total_processed += 1
                word = line.strip()
                
                # skip empty lines
                if not word:
                    continue
                
                # apply criteria function
                try:
                    if not criteria_func(word):
                        continue
                except Exception as e:
                    print(f"Warning: Error processing word '{word}' at line {line_num}: {e}")
                    continue
                
                # handle duplicates
                if remove_duplicates:
                    if word.lower() in seen_words:
                        continue
                    seen_words.add(word.lower())
                
                filtered_words.append(word)
        
        # sort if requested
        if sort_output:
            filtered_words.sort(key=str.lower)
        
        # write filtered words
        with open(destination, 'w', encoding='utf-8') as dest:
            for word in filtered_words:
                dest.write(f"{word}\n")
        
        print(f"Filtered wordlist saved to {destination}")
        print(f"Processed {total_processed} lines, kept {len(filtered_words)} words")
        
        return len(filtered_words)
        
    except Exception as e:
        raise RuntimeError(f"Error filtering wordlist: {e}")


def create_length_filter(min_length: Optional[int] = None, max_length: Optional[int] = None) -> Callable[[str], bool]:
    """
    Create a word length filter function.

    Args:
        min_length: Minimum word length (inclusive).
        max_length: Maximum word length (inclusive).

    Returns:
        Filter function that checks word length.
    """
    def length_filter(word: str) -> bool:
        word_len = len(word)
        if min_length is not None and word_len < min_length:
            return False
        if max_length is not None and word_len > max_length:
            return False
        return True
    
    return length_filter


def create_alphabet_filter(allow_non_ascii: bool = False, allow_numbers: bool = False) -> Callable[[str], bool]:
    """
    Create a word alphabet filter function.

    Args:
        allow_non_ascii: Whether to allow non-ASCII characters.
        allow_numbers: Whether to allow numbers in words.

    Returns:
        Filter function that checks word characters.
    """
    def alphabet_filter(word: str) -> bool:
        # check for numbers
        if not allow_numbers and any(c.isdigit() for c in word):
            return False
        
        # check for non-ascii characters
        if not allow_non_ascii:
            try:
                word.encode('ascii')
            except UnicodeEncodeError:
                return False
        
        # must contain at least one letter
        if not any(c.isalpha() for c in word):
            return False
        
        return True
    
    return alphabet_filter


def create_pattern_filter(pattern: str, exclude: bool = False) -> Callable[[str], bool]:
    """
    Create a regex pattern filter function.

    Args:
        pattern: Regular expression pattern to match.
        exclude: If True, exclude words that match the pattern; if False, include only matching words.

    Returns:
        Filter function that checks words against the regex pattern.
    """
    try:
        compiled_pattern = re.compile(pattern, re.IGNORECASE)
    except re.error as e:
        raise ValueError(f"Invalid regex pattern '{pattern}': {e}")
    
    def pattern_filter(word: str) -> bool:
        matches = compiled_pattern.search(word) is not None
        return not matches if exclude else matches
    
    return pattern_filter


def create_combined_filter(*filters: Callable[[str], bool]) -> Callable[[str], bool]:
    """
    Combine multiple filter functions with AND logic.

    Args:
        *filters: Variable number of filter functions.

    Returns:
        Combined filter function that requires all filters to pass.
    """
    def combined_filter(word: str) -> bool:
        return all(filter_func(word) for filter_func in filters)
    
    return combined_filter


def analyse_wordlist(wordlist_path: Path) -> dict:
    """
    Analyse a wordlist file and return statistics.

    Args:
        wordlist_path: Path to the wordlist file.

    Returns:
        Dictionary containing wordlist statistics.

    Raises:
        FileNotFoundError: If wordlist file doesn't exist.
    """
    if not wordlist_path.exists():
        raise FileNotFoundError(f"Wordlist not found: {wordlist_path}")
    
    words = []
    duplicates = 0
    empty_lines = 0
    seen = set()
    
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            original_word = line.strip()
            
            if not original_word:
                empty_lines += 1
                continue
            
            word_lower = original_word.lower()
            if word_lower in seen:
                duplicates += 1
            else:
                seen.add(word_lower)
                words.append(original_word)
    
    if not words:
        return {
            "file_path": str(wordlist_path),
            "total_lines": line_num,
            "unique_words": 0,
            "duplicates": duplicates,
            "empty_lines": empty_lines,
            "error": "No valid words found in wordlist"
        }
    
    word_lengths = [len(word) for word in words]
    
    return {
        "file_path": str(wordlist_path),
        "total_lines": line_num,
        "unique_words": len(words),
        "duplicates": duplicates,
        "empty_lines": empty_lines,
        "min_word_length": min(word_lengths),
        "max_word_length": max(word_lengths),
        "avg_word_length": sum(word_lengths) / len(word_lengths),
        "total_characters": sum(word_lengths),
        "has_non_ascii": any(not word.isascii() for word in words),
        "has_numbers": any(any(c.isdigit() for c in word) for word in words),
    }