# Network Scanner Usage Instructions

This document provides instructions on how to set up and use the `net_scanner.py` tool to scan your local network for connected devices and identify their vendors.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3:** Download and install Python 3 from [python.org](https://www.python.org/downloads/).
*   **Npcap:** This is a packet capture library for Windows that `scapy` needs. Download and install it from the official website: [https://npcap.com](https://npcap.com). Make sure to install it with the "Install Npcap in WinPcap API-compatible Mode" option checked.

## Setup Instructions

Follow these steps to set up the network scanner:

1.  **Navigate to the Project Directory:**
    Open a Command Prompt or PowerShell and navigate to the `network_scanner` directory:
    ```bash
    cd C:\Users\nsrin\OneDrive\Desktop\Hacking Tools\network_scanner
    ```

2.  **Create a Virtual Environment (Recommended):**
    It's highly recommended to use a virtual environment to manage project dependencies. Create one using the following command:
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    Activate the newly created virtual environment:
    ```bash
    .\venv\Scripts\activate
    ```
    (You should see `(venv)` at the beginning of your command prompt, indicating the virtual environment is active.)

4.  **Install Dependencies:**
    With the virtual environment activated, install the `scapy` library:
    ```bash
    pip install scapy
    ```

5.  **Download OUI Data:**
    Ensure the `oui.txt` file is present in the `network_scanner` directory. This file contains the Organizationally Unique Identifier (OUI) data used to identify device vendors. If it's missing, you can download it from the IEEE website:
    ```bash
    # You might need to use 'curl' if 'wget' is not available on your system
    # curl -o oui.txt http://standards-oui.ieee.org/oui.txt
    wget http://standards-oui.ieee.org/oui.txt
    ```
    *Note: The `net_scanner.py` script is designed to automatically find `oui.txt` if it's in the same directory.*

## Running the Network Scanner

Once the setup is complete, you can run the `net_scanner.py` script:

1.  **Ensure Virtual Environment is Active:**
    If your virtual environment is not active, activate it using the command from step 3 above.

2.  **Execute the Script:**
    Run the script using the `-t` flag to specify the target IP range. Replace `192.168.29.1/24` with your actual network's IP range. A `/24` subnet (e.g., `192.168.1.1/24`) is common for home networks.
    ```bash
    python net_scanner.py -t 192.168.29.1/24
    ```
    *Example for a typical home network:*
    ```bash
    python net_scanner.py -t 192.168.1.1/24
    ```

    The script will then scan the specified network and display a list of connected devices, including their IP addresses, MAC addresses, and identified vendors.

## Troubleshooting

*   **`FileNotFoundError: [Errno 2] No such file or directory: 'oui.txt'`**: Ensure `oui.txt` is in the same directory as `net_scanner.py`.
*   **`scapy.error.Scapy_Exception: The default gateway could not be found.`**: This might indicate an issue with your network configuration or Npcap installation.
*   **No devices found**: Double-check your target IP range. Make sure it correctly represents your local network.
*   **"Unknown Vendor"**: This means the MAC address's OUI was not found in the `oui.txt` database. The database might be outdated, or the device might have a custom/unregistered OUI.
