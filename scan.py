import yara

def load_yara_rules():
    rules = yara.compile(filepath='./yara_rules/malicious_rules.yar')
    return rules

def scan_file(file_path):
    rules = load_yara_rules()
    matches = rules.match(file_path)
    
    if matches:
        print(f"[WARNING] Potential threat detected in {file_path}")
        # Tambahkan tindakan misalnya hapus file, kirim notifikasi, dll.
    else:
        print(f"[INFO] File {file_path} is clean.")
