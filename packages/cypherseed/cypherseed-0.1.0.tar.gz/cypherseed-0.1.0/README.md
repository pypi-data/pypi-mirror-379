# cypherseed

[![PyPI version](https://badge.fury.io/py/cypherseed.svg)](https://badge.fury.io/py/cypherseed)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple high-entropy passphrase generation tool that uses mulitple wordlists to create secure, memorable, and cryptographically strong passphrases.

## Features

- **High-entropy passphrases** using cryptographically secure randomness
- **Flexible customization** - word count, length filters, separators
- **Comprehensive strength analysis** with entropy calculations and time-to-crack estimates
- **Wordlist management** - download, filter, and analyse custom wordlists

## Quick Start

### Installation from PyPI

```bash
pip install cypherseed
```

### Installation from Source

```bash
git clone https://github.com/fidacura/cypherseed.git
cd cypherseed

# create venv (recommended)
python -m venv venv
source venv/bin/activate

# install in editable mode
pip install -e .
```

## Command Reference

### Basic Usage

```bash
# generate a simple 4-word passphrase
cypherseed generate 4

# generate with strength analysis
cypherseed generate 6 --show-strength

# use random numbers/symbols as separators
cypherseed generate 5 --random-separators
```

### Generate Passphrases

```bash
# basic generation
cypherseed generate <word_count>

# advanced options
cypherseed generate 6 \
    --wordlist eff_large_wordlist \
    --min-length 4 \
    --max-length 8 \
    --include-numbers \
    --include-symbols \
    --separator "_" \
    --count 3 \
    --show-strength

# use random separators (numbers/symbols between words)
cypherseed generate 4 --random-separators
# output: word7word@word3word

# generate multiple passphrases
cypherseed generate 5 --count 10
```

### Calculate Strength

```bash
# analyse passphrase strength
cypherseed calculate 4 --wordlist default --detailed
cypherseed calculate 6 1296  # 6 words from 1296-word list
```

### Manage Wordlists

```bash
# list available wordlists
cypherseed update --list

# download new wordlist
cypherseed update --download https://example.com/wordlist.txt --destination custom.txt

# filter existing wordlist
cypherseed update \
    --source wordlist.txt \
    --destination filtered.txt \
    --min-length 4 \
    --max-length 8 \
    --exclude-pattern ".*ing$"

# analyse wordlist
cypherseed update --source wordlist.txt --analyse
```

## Available Wordlists

- **default** - 7,776 words (3-9 characters) - Balanced for security and memorability
- **eff_large_wordlist** - 7,776 words (3-9 characters) - EFF's large wordlist
- **eff_short_wordlist** - 1,296 words (3-5 characters) - EFF's short wordlist for limited typing
- **diceware_wordlist** - 7,776 words (2-12 characters) - Classic Diceware wordlist

## Security Features

### Cryptographically Secure Randomness

- Uses Python's `secrets` module for all random operations
- No predictable patterns in word or separator selection

### High Entropy Generation

- 4 words from default wordlist: ~51.7 bits entropy
- 6 words from default wordlist: ~77.5 bits entropy
- Additional entropy from numbers and symbols when enabled

### Strength Analysis

Comprehensive analysis including:

- Entropy calculations in bits
- Strength classifications (Very Weak to Very Strong)
- Time-to-crack estimates
- Total possible combinations

## Examples

### Basic Passphrases

```bash
$ cypherseed generate 4
Generated passphrase: correct-horse-battery-staple

$ cypherseed generate 6 --separator "_"
Generated passphrase: river_mountain_forest_dancing_wizard_crystal
```

### Enhanced Security

```bash
$ cypherseed generate 5 --random-separators
Generated passphrase: house7mountain@river3dancing$wizard

$ cypherseed generate 4 --include-numbers --include-symbols --show-strength
Generated passphrase: correct-horse-battery-7-staple-@-9
Strength Analysis:
  Entropy: 84.5 bits
  Classification: Good
  Time to crack: Millions of years
```

### Strength Analysis

```bash
$ cypherseed calculate 5 --wordlist default --detailed
Passphrase Strength Analysis:
  Word count: 5
  Wordlist size: 7776
  Base entropy: 64.6 bits
  Total entropy: 64.6 bits
  Classification: Fair
  Total combinations: 2.84e+19
  Time to crack (avg): 450.8 years
```

## Development

### Setup Development Environment

```bash
git clone https://github.com/fidacura/cypherseed.git
cd cypherseed

# create virtual environment
python -m venv venv
source venv/bin/activate

# install with development dependencies
pip install -e .
```

### Testing

```bash
# run tests
python -m pytest tests/

# run with coverage
python -m pytest tests/ --cov=cypherseed --cov-report=html
```

## License

This project is licensed under the GNU General Public License v2.0 - see the [LICENSE](LICENSE) file for details.

Copyright (C) 2025 fidacura. This is free software distributed under GPL v2.0 terms.
