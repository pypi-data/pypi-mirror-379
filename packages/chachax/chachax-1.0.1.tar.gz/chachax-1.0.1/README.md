# chachax

Decrypt ChaCha

## Features

- Supports Python 3.6+

## Installation

Install the latest version of `chachax` from PyPI:

```bash
pip install chachax
```

## Usage
Here's how to use `chachax` for decryption:

```python
import chachax

encrypted_data = b'...'
key = b'...' # 32 bytes
nonce = b'...' # 12 bytes
rounds = 8 # 8/12/20 | Default 8
counter = 0 # Default 0
dec = chachax.decrypt(encrypted_data, key, Nonce, rounds)
