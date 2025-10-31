from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import Transaction
import requests

class QuantumVaultAutoUpgrade:
    def __init__(self, wallet_name, network='testnet'):
        self.wallet = Wallet(wallet_name, network=network)
        self.network = network

    def get_taproot_address(self):
        key = self.wallet.get_key()
        return key.address(script_type='p2tr')

    def get_dynamic_fee(self):
        try:
            url = f"https://mempool.space/{'testnet/' if self.network == 'testnet' else ''}api/v1/fees/recommended"
            return requests.get(url).json()['fastestFee'] * 250
        except:
            return 2500

    def auto_upgrade_all(self):
        self.wallet.scan()
        utxos = self.wallet.utxos()
        legacy_utxos = [u for u in utxos if not u['address'].startswith('tb1p')]
        
        if not legacy_utxos:
            print("All UTXOs already quantum-safe!")
            return

        print(f"Upgrading {len(legacy_utxos)} UTXOs...")

        tx = Transaction(network=self.network)
        total = 0
        for u in legacy_utxos:
            key = self.wallet.get_key(u['key_id'])
            tx.add_input(u['tx_hash'], u['output_n'], value=u['value'], keys=[key])
            total += u['value']

        fee = self.get_dynamic_fee()
        change = total - fee
        if change < 600:
            fee = total
            change = 0

        if change > 0:
            addr = self.get_taproot_address()
            tx.add_output(change, addr)

        tx.sign()
        raw = tx.raw_hex()

        url = f"https://blockstream.info/{'testnet/' if self.network == 'testnet' else ''}api/tx"
        r = requests.post(url, data=raw)
        if r.status_code == 200:
            print(f"SUCCESS! TxID: {r.text}")
            return r.text
        else:
            print("Failed:", r.text)
            print("Raw TX:", raw)

# Run
up = QuantumVaultAutoUpgrade('qv_test', 'testnet')
up.auto_upgrade_all()