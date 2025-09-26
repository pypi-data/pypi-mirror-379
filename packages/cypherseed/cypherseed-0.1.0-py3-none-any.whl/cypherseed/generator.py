"""
Passphrase generation functionality for cypherseed.

This module provides the core passphrase generation logic using wordlists
and configurable parameters for security and customization.
"""

import string
from secrets import choice, randbelow
from typing import List, Optional

from .wordlists import load_wordlist


def generate_passphrase(
    wordlist_name: str,
    word_count: int,
    separator: str = '-',
    min_word_length: Optional[int] = None,
    max_word_length: Optional[int] = None,
    include_numbers: bool = False,
    include_symbols: bool = False,
    random_separators: bool = False,
) -> str:
    """
    Generate a high-entropy passphrase.

    Args:
        wordlist_name: Name of the wordlist to use.
        word_count: Number of words in the passphrase.
        separator: Separator between words in the passphrase.
        min_word_length: Minimum length of each word.
        max_word_length: Maximum length of each word.
        include_numbers: Include numbers in the passphrase.
        include_symbols: Include symbols in the passphrase.
        random_separators: Use random numbers/symbols as separators between words.

    Returns:
        Generated passphrase as a string.

    Raises:
        ValueError: If no words meet the specified criteria or invalid parameters.
        FileNotFoundError: If the specified wordlist doesn't exist.
    """
    # validate input parameters
    if word_count <= 0:
        raise ValueError("Word count must be greater than 0.")
    
    if min_word_length is not None and min_word_length <= 0:
        raise ValueError("Minimum word length must be greater than 0.")
    
    if max_word_length is not None and max_word_length <= 0:
        raise ValueError("Maximum word length must be greater than 0.")
    
    if (min_word_length is not None and max_word_length is not None and 
        min_word_length > max_word_length):
        raise ValueError("Minimum word length cannot be greater than maximum word length.")

    # load wordlist
    words = load_wordlist(wordlist_name)

    # filter words based on length criteria
    if min_word_length is not None or max_word_length is not None:
        filtered_words = []
        for word in words:
            word_len = len(word)
            if min_word_length is not None and word_len < min_word_length:
                continue
            if max_word_length is not None and word_len > max_word_length:
                continue
            filtered_words.append(word)
        words = filtered_words

    # check if any words remain after filtering
    if not words:
        raise ValueError(
            f"No words in wordlist '{wordlist_name}' meet the specified length criteria "
            f"(min: {min_word_length}, max: {max_word_length})."
        )

    # generate base passphrase with words
    selected_words = [choice(words) for _ in range(word_count)]
    
    # handle random separators mode
    if random_separators:
        # use random numbers and symbols as separators between words
        safe_separators = string.digits + "!@#$%^&*+=?"
        random_seps = [choice(safe_separators) for _ in range(word_count - 1)]
        
        # interleave words and random separators
        passphrase_parts = []
        for i, word in enumerate(selected_words):
            passphrase_parts.append(word)
            if i < len(random_seps):  # don't add separator after last word
                passphrase_parts.append(random_seps[i])
        
        return ''.join(passphrase_parts)
    
    # create additional elements list for random insertion (original behavior)
    additional_elements = []
    
    # add numbers if requested
    if include_numbers:
        # add multiple digits for better entropy
        num_digits = randbelow(3) + 1  # 1-3 digits
        additional_elements.extend(choice(string.digits) for _ in range(num_digits))
    
    # add symbols if requested
    if include_symbols:
        # use safe symbols that don't cause issues in most contexts
        safe_symbols = "!@#$%^&*+=?"
        num_symbols = randbelow(2) + 1  # 1-2 symbols
        additional_elements.extend(choice(safe_symbols) for _ in range(num_symbols))
    
    # combine words and additional elements
    if additional_elements:
        # randomly insert additional elements among the words
        all_elements = selected_words + additional_elements
        # shuffle the additional elements' positions securely
        for i in range(len(additional_elements)):
            # pick a random position to insert each additional element
            insert_pos = randbelow(len(all_elements))
            element = all_elements.pop()  # take from end
            all_elements.insert(insert_pos, element)
        passphrase_parts = all_elements[:word_count + len(additional_elements)]
    else:
        passphrase_parts = selected_words

    # join with separator
    return separator.join(passphrase_parts)


def generate_multiple_passphrases(
    wordlist_name: str,
    word_count: int,
    count: int = 5,
    **kwargs
) -> List[str]:
    """
    Generate multiple passphrases with the same parameters.

    Args:
        wordlist_name: Name of the wordlist to use.
        word_count: Number of words in each passphrase.
        count: Number of passphrases to generate.
        **kwargs: Additional arguments passed to generate_passphrase.

    Returns:
        List of generated passphrases.

    Raises:
        ValueError: If count is not positive or other parameter validation fails.
    """
    if count <= 0:
        raise ValueError("Count must be greater than 0.")
    
    return [
        generate_passphrase(wordlist_name, word_count, **kwargs)
        for _ in range(count)
    ]


def estimate_passphrase_combinations(
    wordlist_name: str,
    word_count: int,
    min_word_length: Optional[int] = None,
    max_word_length: Optional[int] = None,
    include_numbers: bool = False,
    include_symbols: bool = False,
) -> int:
    """
    Estimate the number of possible combinations for a passphrase configuration.

    Args:
        wordlist_name: Name of the wordlist to use.
        word_count: Number of words in the passphrase.
        min_word_length: Minimum length of each word.
        max_word_length: Maximum length of each word.
        include_numbers: Whether numbers are included.
        include_symbols: Whether symbols are included.

    Returns:
        Estimated number of possible combinations.
    """
    # load and filter wordlist the same way as generate_passphrase
    words = load_wordlist(wordlist_name)
    
    if min_word_length is not None or max_word_length is not None:
        words = [
            word for word in words
            if (min_word_length is None or len(word) >= min_word_length) and
               (max_word_length is None or len(word) <= max_word_length)
        ]
    
    if not words:
        return 0
    
    # base combinations from words
    base_combinations = len(words) ** word_count
    
    # account for additional elements
    multiplier = 1
    if include_numbers:
        # account for 1-3 digits
        multiplier *= sum(10**i for i in range(1, 4))  # rough estimate
    
    if include_symbols:
        # account for 1-2 symbols from safe symbol set
        safe_symbols_count = 12  # "!@#$%^&*+=?"
        multiplier *= sum(safe_symbols_count**i for i in range(1, 3))
    
    return int(base_combinations * multiplier)