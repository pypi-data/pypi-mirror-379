"""
Password strength calculation functionality for cypherseed.

This module provides entropy calculation and strength analysis for passphrases
generated using wordlists.
"""

import math
from typing import Dict, Union


def calculate_strength(word_count: int, wordlist_size: int) -> float:
    """
    Calculate the strength of a passphrase based on its entropy.

    Entropy is calculated using the formula: entropy = word_count * log2(wordlist_size)

    Args:
        word_count: Number of words in the passphrase.
        wordlist_size: Number of words in the wordlist.

    Returns:
        Entropy of the passphrase in bits.

    Raises:
        ValueError: If word_count or wordlist_size are not positive.
    """
    # input validation
    if wordlist_size <= 0:
        raise ValueError("Wordlist size must be greater than 0.")
    
    if word_count <= 0:
        raise ValueError("Word count must be greater than 0.")

    # calculate entropy in bits
    return word_count * math.log2(wordlist_size)


def calculate_advanced_strength(
    word_count: int, 
    wordlist_size: int,
    include_numbers: bool = False,
    include_symbols: bool = False,
    number_count: int = 1,
    symbol_count: int = 1
) -> float:
    """
    Calculate passphrase strength accounting for additional entropy from numbers and symbols.

    Args:
        word_count: Number of words in the passphrase.
        wordlist_size: Number of words in the wordlist.
        include_numbers: Whether numbers are included in the passphrase.
        include_symbols: Whether symbols are included in the passphrase.
        number_count: Estimated number of digits added.
        symbol_count: Estimated number of symbols added.

    Returns:
        Total entropy in bits including additional elements.

    Raises:
        ValueError: If any count parameter is not positive.
    """
    # validate inputs
    if wordlist_size <= 0 or word_count <= 0:
        raise ValueError("Word count and wordlist size must be greater than 0.")
    
    if number_count <= 0 or symbol_count <= 0:
        raise ValueError("Number count and symbol count must be greater than 0.")

    # base entropy from words
    base_entropy = calculate_strength(word_count, wordlist_size)
    
    additional_entropy = 0.0
    
    # add entropy from numbers (0-9 = 10 possibilities per digit)
    if include_numbers:
        additional_entropy += number_count * math.log2(10)
    
    # add entropy from symbols (assuming 12 safe symbols)
    if include_symbols:
        safe_symbol_count = 12  # "!@#$%^&*+=?"
        additional_entropy += symbol_count * math.log2(safe_symbol_count)
    
    return base_entropy + additional_entropy


def classify_strength(entropy_bits: float) -> str:
    """
    Classify passphrase strength based on entropy bits.

    Args:
        entropy_bits: Entropy value in bits.

    Returns:
        String classification of the strength level.
    """
    if entropy_bits < 30:
        return "Very Weak"
    elif entropy_bits < 50:
        return "Weak"
    elif entropy_bits < 70:
        return "Fair"
    elif entropy_bits < 90:
        return "Good"
    elif entropy_bits < 120:
        return "Strong"
    else:
        return "Very Strong"


def time_to_crack_estimate(entropy_bits: float, guesses_per_second: int = 1_000_000_000) -> Dict[str, Union[str, float]]:
    """
    Estimate time to crack a passphrase based on entropy.

    Args:
        entropy_bits: Entropy value in bits.
        guesses_per_second: Estimated guesses per second by an attacker.

    Returns:
        Dictionary containing time estimates in various units and human-readable format.
    """
    if entropy_bits <= 0:
        return {"human_readable": "Instantly", "seconds": 0.0}
    
    # total possible combinations
    total_combinations = 2 ** entropy_bits
    
    # average time to crack (half the search space)
    avg_combinations_to_crack = total_combinations / 2
    
    # time in seconds
    seconds_to_crack = avg_combinations_to_crack / guesses_per_second
    
    # convert to human readable format
    def format_time(seconds: float) -> str:
        if seconds < 1:
            return "Less than 1 second"
        elif seconds < 60:
            return f"{seconds:.1f} seconds"
        elif seconds < 3600:
            minutes = seconds / 60
            return f"{minutes:.1f} minutes"
        elif seconds < 86400:
            hours = seconds / 3600
            return f"{hours:.1f} hours"
        elif seconds < 31536000:  # 1 year
            days = seconds / 86400
            return f"{days:.1f} days"
        elif seconds < 31536000000:  # 1000 years
            years = seconds / 31536000
            return f"{years:.1f} years"
        else:
            return "Millions of years"
    
    return {
        "seconds": seconds_to_crack,
        "minutes": seconds_to_crack / 60,
        "hours": seconds_to_crack / 3600,
        "days": seconds_to_crack / 86400,
        "years": seconds_to_crack / 31536000,
        "human_readable": format_time(seconds_to_crack)
    }


def analyse_passphrase_strength(
    word_count: int,
    wordlist_size: int,
    include_numbers: bool = False,
    include_symbols: bool = False,
    number_count: int = 1,
    symbol_count: int = 1,
    guesses_per_second: int = 1_000_000_000
) -> Dict[str, Union[str, float, Dict]]:
    """
    Comprehensive analysis of passphrase strength.

    Args:
        word_count: Number of words in the passphrase.
        wordlist_size: Number of words in the wordlist.
        include_numbers: Whether numbers are included.
        include_symbols: Whether symbols are included.
        number_count: Estimated number of digits.
        symbol_count: Estimated number of symbols.
        guesses_per_second: Estimated attack rate.

    Returns:
        Dictionary containing comprehensive strength analysis.
    """
    # calculate entropy
    entropy = calculate_advanced_strength(
        word_count, wordlist_size, include_numbers, include_symbols,
        number_count, symbol_count
    )
    
    # get strength classification
    strength_class = classify_strength(entropy)
    
    # get time estimates
    time_estimates = time_to_crack_estimate(entropy, guesses_per_second)
    
    # calculate base entropy for comparison
    base_entropy = calculate_strength(word_count, wordlist_size)
    
    return {
        "entropy_bits": entropy,
        "base_entropy_bits": base_entropy,
        "additional_entropy_bits": entropy - base_entropy,
        "strength_classification": strength_class,
        "time_to_crack": time_estimates,
        "total_combinations": 2 ** entropy,
        "wordlist_size": wordlist_size,
        "word_count": word_count,
        "includes_numbers": include_numbers,
        "includes_symbols": include_symbols
    }