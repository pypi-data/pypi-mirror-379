import subprocess
import sys

# Server details
HOST = "72.60.97.244"      # e.g. 192.168.1.10 or domain
USER = "root"   # e.g. root, debian, jawahar
REMOTE_SCRIPT = "/etc/nginx/sites-available/create_nginx_config.py"  # Path to the script on the server
#/etc/nginx/sites-available/create_nginx_config.py

def main():
    if len(sys.argv) != 3:
        print("Usage: python run_remote_nginx.py <domain> <port>")
        sys.exit(1)

    domain = sys.argv[1]
    port = sys.argv[2]

    # Run the script remotely
    cmd = f"ssh {USER}@{HOST} sudo python3 {REMOTE_SCRIPT} {domain} {port}"
    print(f"👉 Running on {HOST}: {cmd}")

    result = subprocess.run(cmd, shell=True, text=True)
    if result.returncode != 0:
        print(f"❌ Remote execution failed with exit code {result.returncode}")
        sys.exit(result.returncode)

    print("✅ Remote script executed successfully")

if __name__ == "__main__":
    main()
