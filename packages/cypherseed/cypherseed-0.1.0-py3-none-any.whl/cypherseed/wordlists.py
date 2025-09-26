"""
Wordlist loading functionality for cypherseed.

This module handles loading wordlists from the package's wordlists directory.
"""

import sys
from pathlib import Path
from typing import List

if sys.version_info >= (3, 9):
    from importlib import resources
else:
    import importlib_resources as resources


def load_wordlist(name: str) -> List[str]:
    """
    Load words from a specified wordlist.

    Args:
        name: The name of the wordlist file (without .txt extension).

    Returns:
        List of words from the wordlist.

    Raises:
        FileNotFoundError: If the specified wordlist doesn't exist.
        ValueError: If the wordlist is empty or malformed.
    """
    # handle both with and without .txt extension
    wordlist_name = name if name.endswith('.txt') else f'{name}.txt'
    
    wordlist_data = None
    
    # approach 1: direct file path (most reliable for development and installed)
    try:
        # get the directory of this current file
        current_dir = Path(__file__).parent
        wordlist_path = current_dir / "wordlists" / wordlist_name
        
        if wordlist_path.exists():
            wordlist_data = wordlist_path.read_text(encoding='utf-8')
    except Exception:
        pass
    
    # approach 2: try importlib.resources (for some installed scenarios)
    if wordlist_data is None:
        try:
            if sys.version_info >= (3, 9):
                wordlists_files = resources.files("cypherseed") / "wordlists"
                wordlist_data = (wordlists_files / wordlist_name).read_text(encoding='utf-8')
            else:
                # fallback for python < 3.9
                try:
                    import importlib_resources
                    wordlists_files = importlib_resources.files("cypherseed") / "wordlists" 
                    wordlist_data = (wordlists_files / wordlist_name).read_text(encoding='utf-8')
                except ImportError:
                    pass
        except Exception:
            pass
    
    # approach 3: try pkg_resources as last resort
    if wordlist_data is None:
        try:
            import pkg_resources
            wordlist_data = pkg_resources.resource_string(
                "cypherseed", f"wordlists/{wordlist_name}"
            ).decode('utf-8')
        except Exception:
            pass
    
    if wordlist_data is None:
        available_wordlists = get_available_wordlists()
        raise FileNotFoundError(
            f"Wordlist '{name}' not found. Available wordlists: {', '.join(available_wordlists)}"
        )
    
    # parse the wordlist data
    words = [line.strip() for line in wordlist_data.splitlines() if line.strip()]
    
    if not words:
        raise ValueError(f"Wordlist '{name}' is empty or contains no valid words.")
    
    return words


def get_available_wordlists() -> List[str]:
    """
    Get a list of available wordlist names.

    Returns:
        List of available wordlist names (without .txt extension).
    """
    wordlists = []
    
    # approach 1: direct file path (most reliable)
    try:
        current_dir = Path(__file__).parent
        wordlists_dir = current_dir / "wordlists"
        
        if wordlists_dir.exists():
            wordlists = [
                f.name[:-4]  # remove .txt extension
                for f in wordlists_dir.iterdir()
                if f.name.endswith('.txt') and f.is_file()
            ]
    except Exception:
        pass
    
    # approach 2: try importlib.resources (for installed packages)
    if not wordlists:
        try:
            if sys.version_info >= (3, 9):
                wordlists_dir = resources.files("cypherseed") / "wordlists"
                wordlists = [
                    f.name[:-4]  # remove .txt extension
                    for f in wordlists_dir.iterdir() 
                    if f.name.endswith('.txt')
                ]
            else:
                # fallback for python < 3.9
                try:
                    import importlib_resources
                    wordlists_dir = importlib_resources.files("cypherseed") / "wordlists"
                    wordlists = [
                        f.name[:-4]  # remove .txt extension
                        for f in wordlists_dir.iterdir() 
                        if f.name.endswith('.txt')
                    ]
                except ImportError:
                    pass
        except Exception:
            pass
    
    # approach 3: try pkg_resources as last resort
    if not wordlists:
        try:
            import pkg_resources
            wordlists = [
                f[:-4]  # remove .txt extension
                for f in pkg_resources.resource_listdir("cypherseed", "wordlists")
                if f.endswith('.txt')
            ]
        except Exception:
            pass
    
    # fallback to known wordlists if all else fails
    if not wordlists:
        wordlists = ['default', 'eff_large_wordlist', 'eff_short_wordlist', 'diceware_wordlist']
    
    return sorted(wordlists)


def get_wordlist_info(name: str) -> dict:
    """
    Get information about a specific wordlist.

    Args:
        name: The name of the wordlist file (without .txt extension).

    Returns:
        Dictionary containing wordlist information (name, size, etc.).

    Raises:
        FileNotFoundError: If the specified wordlist doesn't exist.
    """
    words = load_wordlist(name)
    
    return {
        'name': name,
        'size': len(words),
        'min_word_length': min(len(word) for word in words),
        'max_word_length': max(len(word) for word in words),
        'avg_word_length': sum(len(word) for word in words) / len(words),
    }