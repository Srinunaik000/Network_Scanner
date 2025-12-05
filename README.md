# Network Scanner

A Python-based network scanner that discovers devices on your local network and identifies their manufacturers using OUI data.

## Features

*   **Network Discovery:** Scans a specified IP range to find active devices.
*   **MAC Address Resolution:** Retrieves MAC addresses of discovered devices.
*   **Vendor Identification:** Looks up the manufacturer (vendor) of each device using an OUI (Organizationally Unique Identifier) database.

## Prerequisites

*   **Python 3**
*   **Npcap** (for Windows users, required by Scapy)

## Setup

1.  **Clone the Repository (or download the files):**
    ```bash
    git clone <repository_url>
    cd network_scanner
    ```
    (If you downloaded the files manually, navigate to the `network_scanner` directory.)

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate # On Linux/macOS
    ```

3.  **Install Dependencies:**
    ```bash
    pip install scapy
    ```

4.  **Download OUI Data:**
    Ensure `oui.txt` is in the same directory as `net_scanner.py`. If missing, download it:
    ```bash
    wget http://standards-oui.ieee.org/oui.txt
    # or using curl:
    # curl -o oui.txt http://standards-oui.ieee.org/oui.txt
    ```

## Usage

Run the script with your target IP range:

```bash
python net_scanner.py -t 192.168.1.1/24
```

Replace `192.168.1.1/24` with your network's specific IP range.

## Example Output

```
IP                  MAC Address                 Vendor
-------------------------------------------------------------------------
192.168.1.1         aa:bb:cc:dd:ee:ff           Router Manufacturer
192.168.1.10        00:11:22:33:44:55           Device Vendor Inc.
192.168.1.15        ff:ee:dd:cc:bb:aa           Another Company
```

## Troubleshooting

Refer to `INSTRUCTIONS.md` for more detailed troubleshooting steps.
