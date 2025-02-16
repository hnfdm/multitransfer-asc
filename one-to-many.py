from web3 import Web3
import time

# Konfigurasi RPC dan Web3
RPC_URL = "https://rpc-mainnet.inichain.com"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Pastikan koneksi ke node berhasil
if not web3.is_connected():
    print("Gagal terhubung ke RPC")
    exit()

# Konfigurasi
PRIVATE_KEY = "pk"  # Ganti dengan private key Anda 
SOURCE_ADDRESS = web3.to_checksum_address("0xsender")  # Ganti dengan alamat pengirim Anda
TARGET_ADDRESSES = [
    "0xCA28D5e42e44Ab650aee53d4A2F171B69E3349E9",
    "0x2c81e0abd1c932596ac11e2cb0f6ddf8b35a5007",
    "0xbB075bC5017B10000f6f5049F5c0Cad1B89a1a58",
    "0xDc8a8C6996C99ab2b002DBC75182Ab6B2b423449",
    "0xbb5a852eb0bc0385ae7bb27f6a3fea2959442126",
    "0x8C805bFDc1919d92eDcEfD2B513903c244D6da17",
    "0x5d2235E99E6567Af0A2719683170c8d70178b45A",
    "0x158402ad9332727494BEcDFb8CfFf77b78DfD78B",
    "0x3928924ae1503fb0a47a58ffa3110a5817b2ec0a",
    "0x6c99F197Eda74CD1ad1c89b9F49bBecd38ebe716",
    # Tambahkan alamat target lainnya
]

AMOUNT = web3.to_wei(0.0001, 'ether')  # Jumlah yang akan dikirim per transaksi
GAS_LIMIT = 21000
GAS_PRICE = web3.to_wei(2, 'gwei')

# Fungsi untuk mengirim transaksi
def send_transaction(private_key, source_address, target_address, amount):
    nonce = web3.eth.get_transaction_count(source_address)
    tx = {
        'nonce': nonce,
        'to': web3.to_checksum_address(target_address),
        'value': amount,
        'gas': GAS_LIMIT,
        'gasPrice': GAS_PRICE,
        'chainId': 7233,  # Tambahkan chain ID untuk EIP-155
    }

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    return web3.to_hex(tx_hash)

# Fungsi utama
def main():
    while True:
        print("\nMemulai transfer...")
        for i, target_address in enumerate(TARGET_ADDRESSES):
            try:
                tx_hash = send_transaction(PRIVATE_KEY, SOURCE_ADDRESS, target_address, AMOUNT)
                print(f"Transfer ke {target_address} berhasil. Tx Hash: {tx_hash}")
            except Exception as e:
                print(f"Transfer ke {target_address} gagal. Error: {str(e)}")

            # Countdown 5 menit sebelum transaksi berikutnya
            print("Menunggu 5 menit sebelum transaksi berikutnya...")
            countdown_seconds = 5 * 60  # 5 menit dalam detik
            while countdown_seconds > 0:
                minutes, seconds = divmod(countdown_seconds, 60)
                print(f"⏳ Waktu tersisa: {minutes:02d}:{seconds:02d}", end="\r")
                time.sleep(1)
                countdown_seconds -= 1

        print("\nSemua transfer selesai. Menunggu 10 menit sebelum memulai lagi...")

        # Timer countdown 10 menit
        countdown_seconds = 10 * 60  # 10 menit dalam detik
        while countdown_seconds > 0:
            minutes, seconds = divmod(countdown_seconds, 60)
            print(f"⏳ Waktu tersisa: {minutes:02d}:{seconds:02d}", end="\r")
            time.sleep(1)
            countdown_seconds -= 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh user.")
