#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Key size (in bytes) for the AES session key and its IV.
SESSION_KEY_SIZE = IV_SIZE = 32

# Used to derive other key material, e.g. for AES and HMAC.
MASTER_KEY_SIZE = 32

# The maximum padding length to be appended to the puzzle.
MAX_PADDING_LENGTH = 4096

# Length of the time-lock puzzle (consisting of `n' and `Ck') in bytes.
PUZZLE_LENGTH = 128

# The length of the puzzle's modulus `n' in bits.
PUZZLE_MODULUS_LENGTH = 512

# Approximate CPU time in seconds necessary to solve the puzzle.
PUZZLE_UNLOCK_TIME = 120

# Length of the magic values in bytes.
MAGIC_LENGTH = 32

# States which are used for the protocol state machine.
ST_WAIT_FOR_PUZZLE = 0
ST_SOLVING_PUZZLE = 1
ST_WAIT_FOR_MAGIC = 2
ST_CONNECTED = 3

# Length of len field (in bytes).
HDR_LENGTH = 16 + 2 + 2

# Length of HMAC-SHA256-128.
HMAC_LENGTH = 16

# TODO - what do we choose? should fit into an ethernet (non-jumbo) frame
MTU = 1448

# The prefix before the session key which is ``locked'' inside the time-lock
# puzzle.  The client looks for this prefix to verify that the puzzle was
# unlocked successfully.
MASTER_KEY_PREFIX = "MasterKey="

# Used in log messages.
TRANSPORT_NAME = "ScrambleSuit"

# Digest size of SHA256 (in bytes).
SHA256_DIGEST_SIZE = 32
