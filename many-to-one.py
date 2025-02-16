import time
from web3 import Web3

# Konfigurasi RPC dan alamat tujuan
RPC_URL = "https://dream-rpc.somnia.network"
TARGET_ADDRESS = "0xb21D7BC72e7214cf5D0EBbEB34cF1D57c602b989"  # Ganti dengan alamat tujuan
AMOUNT = 0.003  # Dalam ETH
PRIVATE_KEYS = [
    "pk1",
    "pk2",
    "pk3",
    "pk4",
    "pk5", 
    "pk6",
]  # Ganti dengan private keys dari akun Anda

# Inisialisasi koneksi ke RPC
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.is_connected():
    raise ConnectionError("Tidak dapat terhubung ke RPC. Periksa koneksi atau URL RPC.")

# Fungsi untuk melakukan transfer
def send_transaction(private_key, target_address, amount_eth):
    account = web3.eth.account.from_key(private_key)
    nonce = web3.eth.get_transaction_count(account.address)
    gas_price = web3.eth.gas_price
    tx = {
        "nonce": nonce,
        "to": target_address,
        "value": web3.to_wei(amount_eth, "ether"),
        "gas": 21000,
        "gasPrice": gas_price,
    }
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    return web3.to_hex(tx_hash)

def print_banner():
    print("\033[96m" + "=" * 57 + "\033[0m")  # Cyan
    print("\033[1;35m" + " SOMNIA TESTNET | AIRDROP ASC " + "\033[0m".center(57))  # Bold Magenta
    print("\033[96m" + "=" * 57 + "\033[0m")  # Cyan
    print("\033[93m" + "Credit By       : Airdrop ASC" + "\033[0m")  # Yellow
    print("\033[93m" + "Telegram Channel: @airdropasc" + "\033[0m")  # Yellow
    print("\033[93m" + "Telegram Group  : @autosultan_group" + "\033[0m")  # Yellow
    print("\033[96m" + "=" * 57 + "\033[0m")  # Cyan

# Loop utama untuk transfer setiap 6 jam
def main():
    while True:
        for i, private_key in enumerate(PRIVATE_KEYS):
            try:
                tx_hash = send_transaction(private_key, TARGET_ADDRESS, AMOUNT)
                print(f"Transfer {i + 1} aman dong. Tx Hash: {tx_hash}")
            except Exception as e:
                print(f"Transfer {i + 1} error cok. Error: {str(e)}")
        print("Transaksi selesai. Auto send lagi dalam 6 jam.")

        # Timer countdown 6 jam
        countdown_seconds = 6 * 60 * 60  # 6 jam dalam detik
        while countdown_seconds > 0:
            hours, remainder = divmod(countdown_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"⏳ Waktu tersisa: {hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
            time.sleep(1)
            countdown_seconds -= 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program dihentikan.")
