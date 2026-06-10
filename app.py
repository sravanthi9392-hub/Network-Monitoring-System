from flask import Flask, render_template, request
import socket

app = Flask(__name__)

# ----------------------------------
# Connectivity Check
# ----------------------------------
def check_connectivity(host):

    try:

        ip = socket.gethostbyname(host)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(3)

        result = s.connect_ex((ip, 443))

        s.close()

        if result == 0:
            return "Online"
        else:
            return "Offline"

    except:
        return "Offline"


# ----------------------------------
# DNS Lookup
# ----------------------------------
def get_ip(host):

    try:
        return socket.gethostbyname(host)

    except:
        return None


# ----------------------------------
# Port Scanner
# ----------------------------------
def scan_ports(ip):

    ports = {
        21: "FTP - File Transfer",
        22: "SSH - Remote Login",
        53: "DNS - Domain Resolution",
        80: "HTTP - Web Traffic",
        443: "HTTPS - Secure Web Traffic"
    }

    results = []

    for port, service in ports.items():

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(1)

        result = s.connect_ex((ip, port))

        if result == 0:
            status = "Open"
        else:
            status = "Closed"

        results.append((port, service, status))

        s.close()

    return results


# ----------------------------------
# Home Page
# ----------------------------------
@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        host = request.form["host"].strip()

        ip = get_ip(host)

        if ip:

            status = check_connectivity(host)

            ports = scan_ports(ip)

            result = {
                "host": host,
                "ip": ip,
                "status": status,
                "ports": ports
            }

        else:

            result = {
                "error": "Invalid Hostname or IP Address"
            }

    return render_template(
        "index.html",
        result=result
    )


# ----------------------------------
# Run Application
# ----------------------------------
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
