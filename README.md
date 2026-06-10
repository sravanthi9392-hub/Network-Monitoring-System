# 🌐 Network Monitoring System

A web-based network monitoring application developed using Python, Flask, and Socket Programming. The application allows users to analyze websites or IP addresses by checking host availability and scanning common network service ports.

## Features

- DNS Lookup (Hostname to IP Address Resolution)
- Host Availability Check (Online/Offline Status)
- Port Scanning of Common Network Services
- Service Identification for Open and Closed Ports
- Simple and User-Friendly Web Interface

## Ports Scanned

- Port 21 – FTP (File Transfer Protocol)
- Port 22 – SSH (Secure Shell)
- Port 53 – DNS (Domain Name System)
- Port 80 – HTTP (HyperText Transfer Protocol)
- Port 443 – HTTPS (Secure HyperText Transfer Protocol)

## Technologies Used

- Python
- Flask
- Socket Programming
- HTML
- CSS

## Project Structure

```text
Network-Monitoring-System/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Output

- Displays Hostname and IP Address
- Shows Online/Offline Status
- Scans Common Network Ports
- Displays Service Names for Each Port
- Identifies Whether Ports are Open or Closed