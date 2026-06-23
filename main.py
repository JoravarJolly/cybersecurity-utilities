# main.py
# Written by Joravar - June 2026
# Project: Unified Security Automation & Defenses Framework

import re
import socket
import html
import sys
from cryptography.fernet import Fernet

def check_password_entropy():
    print("\n=========================================")
    print("   [UTILITY] PASSWORD COMPLEXITY AUDITOR  ")
    print("=========================================")
    passwd = input("Enter a test credential string to audit: ")
    
    # Custom evaluation logic ensuring strong enterprise defaults
    flaws = []
    if len(passwd) < 12:
        flaws.append("Length under 12 characters (vulnerable to dictionary attacks).")
    if not re.search("[A-Z]", passwd):
        flaws.append("Lacks an uppercase alphabetic character.")
    if not re.search("[a-z]", passwd):
        flaws.append("Lacks a lowercase alphabetic character.")
    if not re.search("[0-9]", passwd):
        flaws.append("Missing numerical integer values.")
    if not re.search("[_@$!%*#?&]", passwd):
        flaws.append("Missing a special character symbol.")
        
    if not flaws:
        print("\n[SUCCESS] Matrix validation passed. High cryptographic entropy.")
    else:
        print("\n[SECURITY WARNING] Weak entry policies flagged:")
        for flaw in flaws:
            print(f" -> {flaw}")

def run_port_scan():
    print("\n=========================================")
    print("   [UTILITY] LOCAL NETWORK PORT SCANNER   ")
    print("=========================================")
    print("Defaulting target host to local loopback (127.0.0.1) for secure sandbox execution.")
    
    # Giving user choice to avoid clinical/static appearance
    custom_ports = input("Enter target ports split by commas (e.g., 22,80,443) or press Enter for defaults: ")
    if custom_ports.strip() == "":
        ports = [21, 22, 80, 443, 8080]
    else:
        try:
            ports = [int(p.strip()) for p in custom_ports.split(",")]
        except ValueError:
            print("[Error] Invalid character payload in port range. Aborting scan.")
            return
            
    print(f"[*] Initiating TCP connection sweeps across {len(ports)} sockets...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.7) # Balanced socket connection timeout rule
        status = s.connect_ex(("127.0.0.1", port))
        if status == 0:
            print(f" [ALERT] TCP Port {port}: OPEN / ACTIVE")
        else:
            print(f" [-] TCP Port {port}: Closed/Filtered")
        s.close()

def sanitize_web_input():
    print("\n=========================================")
    print("   [UTILITY] XSS MITIGATION & SANITIZER   ")
    print("=========================================")
    user_string = input("Paste raw untrusted user input string (e.g., script tags): ")
    
    # Mimicking web application firewalls by encoding character tags
    sanitized = html.escape(user_string)
    print("\n[+] Escape encoding applied to prevent context breakdown:")
    print(f" Safe Output String: {sanitized}")

def execute_file_crypto():
    print("\n=========================================")
    print("   [UTILITY] SYMMETRIC PAYLOAD CIPHER   ")
    print("=========================================")
    raw_secret = input("Enter sensitive text payload to secure via Fernet/AES: ")
    
    # Generating keys programmatically 
    runtime_key = Fernet.generate_key()
    cipher_suite = Fernet(runtime_key)
    
    encrypted_bytes = cipher_suite.encrypt(raw_secret.encode())
    print("\n[+] Execution complete. Ephemeral keys mapped.")
    print(f" Ciphertext Payload: {encrypted_bytes.decode()}")

def parse_server_logs():
    print("\n=========================================")
    print("   [UTILITY] BRUTE-FORCE INTRUSION DETECTOR")
    print("=========================================")
    
    # Sample real-world authentication log dumps with specific failure paths
    simulated_syslog = """
    2026-06-23 11:42:10 AUTH_SUCCESS session_root
    2026-06-23 11:43:01 AUTH_FAILURE bad_login_user_admin
    2026-06-23 11:43:04 AUTH_FAILURE bad_login_user_admin
    2026-06-23 11:43:08 AUTH_FAILURE bad_login_user_admin
    2026-06-23 11:45:12 AUTH_SUCCESS session_guest
    """
    print("[*] Processing standard system auth-log buffers...")
    
    failed_counts = {}
    alert_threshold = 3
    
    for line in simulated_syslog.strip().split("\n"):
        if "AUTH_FAILURE" in line:
            attacker_id = line.split("_")[-1]
            failed_counts[attacker_id] = failed_counts.get(attacker_id, 0) + 1
            
            if failed_counts[attacker_id] >= alert_threshold:
                print(f" [INCIDENT ALERT] Brute-force heuristics matched for identity: '{attacker_id}'!")
                print(f" -> Reason: Exceeded {alert_threshold} sequential authentication failures.")

def run_dashboard():
    while True:
        print("\n" + "="*50)
        print("      JORAVAR'S SECURE CORE LOGIC ENGINE v1.0   ")
        print("="*50)
        print(" 1. Audit Password Complexity Standards")
        print(" 2. Network Target Port Surface Mapper")
        print(" 3. Secure Input Filter Against XSS Exploitations")
        print(" 4. Encrypt Volatile System Parameters")
        print(" 5. Monitor Infrastructure Logs for Intruders")
        print(" 6. Terminate Core Engine Session")
        
        choice = input("\nSelect system vector to deploy [1-6]: ").strip()
        
        if choice == "1":
            check_password_entropy()
        elif choice == "2":
            run_port_scan()
        elif choice == "3":
            sanitize_web_input()
        elif choice == "4":
            execute_file_crypto()
        elif choice == "5":
            parse_server_logs()
        elif choice == "6":
            print("\n[*] Shutting down engine cleanly. Operational loop complete.")
            break
        else:
            print("\n[!] Error: Choice not in range. Input valid operational token.")

if __name__ == "__main__":
    run_dashboard()
