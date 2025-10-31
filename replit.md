# QuantumVault - Quantum-Safe Bitcoin Wallet

## Project Overview
QuantumVault is an open-source Bitcoin wallet designed to protect against quantum computing threats. It provides hybrid ECDSA+Dilithium signing, AI-powered threat monitoring, and one-click migration to quantum-safe addresses.

## Project Type
Command-line Python application (no frontend)

## Current State
- Successfully set up in Replit environment
- Python 3.11 installed
- All dependencies installed via pip
- Workflow configured to run the auto-upgrade script

## Architecture
- **Language**: Python 3.11
- **Main Script**: `auto_upgrade.py` - Automatically upgrades legacy Bitcoin UTXOs to quantum-safe Taproot addresses
- **Key Dependencies**:
  - `bitcoinlib` (v0.7.5) - Bitcoin wallet and transaction library
  - `requests` (v2.32.5) - HTTP library for API calls
  
## Key Features
1. **Auto-Upgrade**: Scans wallet for legacy UTXOs and upgrades them to Taproot (P2TR) addresses
2. **Dynamic Fees**: Fetches real-time fee estimates from mempool.space
3. **Network Support**: Configured for testnet by default
4. **Transaction Broadcasting**: Submits transactions to Blockstream API

## Project Structure
```
.
├── auto_upgrade.py       # Main application script
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── License              # MIT License
├── .gitignore           # Git ignore rules
└── replit.md           # Replit project documentation
```

## How It Works
The `QuantumVaultAutoUpgrade` class:
1. Initializes a Bitcoin wallet (testnet by default)
2. Generates Taproot (P2TR) addresses for quantum safety
3. Scans for UTXOs that aren't quantum-safe (not starting with 'tb1p')
4. Creates a transaction to consolidate legacy UTXOs to Taproot address
5. Calculates dynamic fees based on current network conditions
6. Signs and broadcasts the transaction to the Bitcoin testnet

## Usage
The application runs automatically when the workflow starts. It will:
- Create/load a wallet named 'qv_test' on testnet
- Scan for non-quantum-safe UTXOs
- Upgrade them to Taproot addresses if any are found

## Network Information
- **Default Network**: Bitcoin Testnet
- **Fee API**: mempool.space
- **Transaction Broadcast**: blockstream.info

## Recent Changes
- **2025-10-31**: Initial Replit setup
  - Installed Python 3.11
  - Installed bitcoinlib and requests dependencies
  - Created requirements.txt and .gitignore
  - Configured console workflow for auto-upgrade script

## License
MIT License - Copyright (c) 2025 Adam Allex
