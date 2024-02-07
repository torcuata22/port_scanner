Thank you for providing the filenames. Let's update the Read Me file accordingly:

---

# Port Scanner

The Port Scanner is a Python tool designed to scan for open ports on a specified host within a given port range. It provides two scanning modes: a basic scanner that scans ports 1 through 1025, and a more robust scanner that offers customizable port ranges. Additionally, the Port Scanner generates a text file with the results of the scan, allowing for easy reference and analysis.

## Features

- **Basic Port Scanner**: The basic scanner (basic_scanner.py) scans ports 1 through 1025 on the target host, providing a quick and simple method for identifying common open ports.

- **Robust Port Scanner**: The more robust scanner (multi_scanner.py) offers customizable port ranges, allowing users to specify the exact range of ports to scan based on their requirements.

- **Multi-threaded Scanning**: Both scanning modes utilize multi-threading to perform port scanning concurrently, maximizing efficiency and reducing scanning time.

- **Color-coded Output**: Enhances readability of scan results by utilizing color-coded highlighting in the console output to distinguish between open and closed ports.

- **Export Scan Results**: Generates a text file with the results of the scan, providing a convenient way to store and analyze scan data.

## Usage

To use the Port Scanner, follow these steps:

1. **Install Dependencies**: Ensure you have Python 3.11 installed on your system. Additionally, install the required dependencies by running:


   pip install colorama
 

2. **Run the Scanner**: Execute the respective scanner script (`basic_scanner.py` or `multi_scanner.py`) and specify the target host and scanning mode. You can choose between the basic scanner (ports 1-1025) or the robust scanner with a custom port range.


   python basic_scanner.py <host>



   python multi_scanner.py <host> [--ports PORT_RANGE]


   Replace <host> with the IP address or hostname of the target host. Use the --ports flag to specify a custom port range for the robust scanner.

3. **View Scan Results**: After the scan is complete, the results will be displayed in the console output and saved to a text file named scan_results.txt in the current directory.

## Example

Scan a target host using the basic scanner:

python basic_scanner.py <ip_address>


Scan a target host using the robust scanner with a custom port range (e.g., ports 1 through 1000):

python multi_scanner.py <ip_address> --ports 1-1000

## Dependencies

- **Python 3.11**: The Port Scanner is developed using Python 3.11, leveraging its latest features and capabilities.

- **colorama**: Enhances the console output with color-coded highlighting to improve readability of scan results.

## License

This project is licensed under the [MIT License](LICENSE).


