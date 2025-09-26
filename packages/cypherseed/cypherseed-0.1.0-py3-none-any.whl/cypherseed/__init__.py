"""
Cypherseed ~ A simple high-entropy passphrase generation tool.

This package provides functionality to generate secure, memorable passphrases
using multiple wordlists with customizable parameters.
"""

from .generator import generate_passphrase
from .password_strength import calculate_strength
from .wordlists import load_wordlist

__version__ = "0.1.0"
__author__ = "fidacura"
__email__ = "hey@fidacura.net"

# Define what gets imported with "from cypherseed import *"
__all__ = [
    "generate_passphrase",
    "calculate_strength", 
    "load_wordlist",
]