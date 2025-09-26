import subprocess
import sys

# Server details
HOST = "72.60.97.244"   # e.g. 192.168.1.10 or domain
USER = "root"           # e.g. root, debian, jawahar
REMOTE_SCRIPT = "/etc/nginx/sites-available/create_nginx_config.py"  # Path on server

def main():
    print("🌐 Remote Nginx Config Generator")

    # Ask for inputs
    domain = input("👉 Enter domain name (e.g. example.com): ").strip()
    port = input("👉 Enter port number (e.g. 8080): ").strip()

    if not domain or not port.isdigit():
        print("❌ Invalid input. Please provide a domain and numeric port.")
        sys.exit(1)

    # Build SSH command
    cmd = f"ssh {USER}@{HOST} sudo python3 {REMOTE_SCRIPT} {domain} {port}"
    print(f"👉 Running on {HOST}: {cmd}")

    result = subprocess.run(cmd, shell=True, text=True)
    if result.returncode != 0:
        print(f"❌ Remote execution failed with exit code {result.returncode}")
        sys.exit(result.returncode)

    print("✅ Remote script executed successfully")

if __name__ == "__main__":
    main()