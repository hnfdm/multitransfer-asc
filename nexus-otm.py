from web3 import Web3
import time

# Konfigurasi RPC dan Web3
RPC_URL = "https://rpc.nexus.xyz/http"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Pastikan koneksi ke node berhasil
try:
    print("Connected to RPC:", web3.is_connected())
    print("Latest block:", web3.eth.block_number)
except Exception as e:
    print("Error connecting to RPC:", str(e))
    exit()

# Konfigurasi
PRIVATE_KEY = "pk"  # Ganti dengan private key Anda 
SOURCE_ADDRESS = web3.to_checksum_address("0x")  # Ganti dengan alamat pengirim Anda
TARGET_ADDRESSES = [
    "0xC10ffD8a9FCF23EE2Cf1E79a4F21C0A68DCD3eCa",
    "0x06Eb3B10F633A3f864C3a5A54AEb8Dab6b036b17",
    "0x07dFEa84E83A45cFAA4C795e53664A7F35b9be6D",
    "0xaAa921B36d4A8998C88ea089807940d1ba486F7B",
    "0x85A89030F53C8320c1fB1c8CBA99593A7beF234C",
    "0x55b425EA78555a22D889d016019fACF20cB3dE15",
    "0x5d2235E99E6567Af0A2719683170c8d70178b45A",
    "0x158402ad9332727494BEcDFb8CfFf77b78DfD78B",
    "0x3928924ae1503fb0a47a58ffa3110a5817b2ec0a",
    "0x6c99F197Eda74CD1ad1c89b9F49bBecd38ebe716",
    "0xCA28D5e42e44Ab650aee53d4A2F171B69E3349E9",
    "0x2c81e0abd1c932596ac11e2cb0f6ddf8b35a5007",
    "0xbB075bC5017B10000f6f5049F5c0Cad1B89a1a58",
    "0xDc8a8C6996C99ab2b002DBC75182Ab6B2b423449",
    "0xbb5a852eb0bc0385ae7bb27f6a3fea2959442126",
    "0x8C805bFDc1919d92eDcEfD2B513903c244D6da17",
    "0x7C06db5dBF3a737e09d84782f2CD34fbE4786714",
    "0x783839f1a26fbC9b546a937fee2207064Ee1185c",
    "0xB00E160f25f6849eEe861e2Ab99B899a7C7e2fF1",
    "0x1121B5D895DD2DF9a4016f62DF7C921830F8e91E",
    "0x3daeDCd2bc3C0890304A9e92832C661464fFF746",
    "0x5cECda2a28e0652c8A1a0296113C7265c61Ab7A8",
    "0xb9F56C049F5DB533087F1b335A20330275d5eA81",
    "0x0e9369680C5eaf394DFeB01ad5410a18DbE14AD2",
    "0x16E9090f2c5c5CE570761D88eaC39603a555752c",
    "0x897F55Cad8db9b053c03eB48374b3197B5C9AAdf",
    "0x4D47ADeCe3D064A613509a1D076187d733c41fa1",
    "0x2FdEA3b185f37117CEdc37F42f735a39E5510262",
    "0x8C90157903D4F0f8Cc3885B80Ee4CCE65d04863C",
    "0xEF6dF66cFD47dF6022e0c3898c4756876644d863",
    "0x1229bcae6fB7F328EfF9A425a5D073944E5fEb38",
    "0xC65ED9B45DaEA9ae3BbcFA2C841f68488490c7E7",
    "0x8dccadc45543156e3Bf1B14bAF7abbF7f8664d1a",
    "0xBDD726ac9d998a7D6f80d88D10C396C0C82C7330",
    "0xefc6AD79a8cdd15B0452cb22c6e7A0dBbEab04f9",
    "0x8BB2E22AB59145E247E6D06aCA77c5C6E9502321",
    "0xede3B76Aa2F1e1FB4A46FBa58B46957eA31E6da2",
    "0x7078b9Dd23384e8244fEAF83E0B9448C6c29b1FC",
    "0x1dA187FB6470f8556577Ffe0F40717644bf2D0Aa",
    "0x4F1E2FA4a4816Fcda656dF1de6b00Ac430D57376",
    "0x6ddB6D4f3E8369e972e128B8eD950aE2206B7712",
    "0x7a6f331F027e5810eaB75726c231d1c1A40cE191",
    "0xBD148Bf4c74Fd7A8206389Cf46d9d426412f8d1b",
    "0xc934C1051b9380B68e079e4AcA188AbD36654228",
    "0x00668Cc629d57f20125779D71425A8b6032E7720",
    "0x2beEB0FE7C6056E01A4823d981BB5AF0afC06f24",
    "0xCDd5cDEC6B17E339307498da327a67dcD24e8f0c",
    "0xbb663A13abe15F942c261A213711756bF2e4CCC6",
    "0xF762a55639552B1b0850a680Df3E95E989A26175",
    "0xCb1Cf09F9722CCFc5A1257a71090f73B113a2bFd",
    "0x224df1C5592FcB6ed9886AeCee84992A69266F8e",
    "0xB3E685fAbfCD7301b636Fc2b00d451cEF5D12DC7",
    "0xB494aa640bb054d138BaEe4Bd7E5874d90e4FfF3",
    "0xb31A4842922d66141d0f1a6ce39F1aD2D6989487",
    "0x763c8AaBD559bacBA481Ac00d2Cf12fbe45cb70B",
    "0x63396238750Fe9a036B205d6d2E7157F84278Da1",
    "0xB427176c2C7a97D119Fb0dB00be72B8fE64b4918",
    "0xf5ba568F847789c9ef7c1B483e62627D5Bbf0c78",
    "0x0447Dce9393306310E4503848d673f6F4eC857AD",
    "0xC1F1739d9420D7f19d5Ea8154365B64e2f845e91",
    "0x7746C30b88DCA80dC29cc72012bFbC3dDd48aE18",
    "0x85616Fdf33d29a80a1d2A629bB245F2523984bDC",
    "0xB73CfcD4Aa84dbEe763c408Aa40E4B140d439E10",
    "0x2ad1aA9Be039849e1A223be28D66F4D0122F1FB6",
    "0xd1E5dbFA207288124A001D52F74a856f89059def",
    "0x7B5B9DFc37e5B515dfE721Be938dD2625B51c054",
    # Tambahkan alamat target lainnya
]

AMOUNT = web3.to_wei(0.00001, 'ether')  # Jumlah yang akan dikirim per transaksi
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
        'chainId': 392,  # Tambahkan chain ID untuk EIP-155
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

            # Countdown 10 detik sebelum transaksi berikutnya
            print("Menunggu 2 detik sebelum transaksi berikutnya...")
            countdown_seconds = 2  # 2 detik
            while countdown_seconds > 0:
                minutes, seconds = divmod(countdown_seconds, 60)
                print(f"⏳ Waktu tersisa: {minutes:02d}:{seconds:02d}", end="\r")
                time.sleep(1)
                countdown_seconds -= 1

        print("\nSemua transfer selesai. Menunggu 24 jam sebelum memulai lagi...")

        # Timer countdown 5 menit
        countdown_seconds = 5 * 60  # 5 menit dalam detik
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
