# SerialSrv

A Python HTTP service that reads data from serial ports and provides it via REST API with ABAP integration support.
by Altay Kireççi
opriori (c)(p) 2025-09
https://www.opriori.com

## Features

- 🔌 **Serial Port Reading**: Read data from Arduino, sensors, and other serial devices
- 🌐 **HTTP API**: RESTful API with JSON responses
- 🔒 **Host-based Access Control**: Configurable IP and port restrictions
- 📊 **Comprehensive Logging**: Detailed request logging
- 🔧 **ABAP Integration**: Ready-to-use ABAP client code
- 🧪 **Test Mode**: Mock data for development and testing
- ⚡ **CORS Support**: Cross-origin resource sharing enabled

## Installation

```bash
pip install serialsrv
serialsrv --init
```

## Quick Start

### 1. Basic Usage

```bash
# Copy ABAP files to current directory
serialsrv --abap

# Initialize/creating configuration file
serialsrv --init
# Start the server (default: localhost:7373)
serialsrv

# Start with custom host and port
serialsrv --host 0.0.0.0 --port 8080

# Run in test mode (returns mock data)
serialsrv --test


```

### 2. Configuration

#### Method 1: Using --init parameter (Recommended)
```bash
# Create configuration file in current directory
serialsrv --init

# This will create serialsrv.json with default settings
# You can then edit it to customize your configuration
```

#### Method 2: Manual creation
Create a `serialsrv.json` configuration file:

```json
{
  "allowed_hosts": [
    {
      "ip": "127.0.0.1",
      "ports": [7373, 8080],
      "description": "Localhost access"
    },
    {
      "ip": "192.168.1.100",
      "ports": [7373],
      "description": "Local network access"
    }
  ],
  "serial": {
    "port": "/dev/ttyUSB0",
    "baudrate": 9600,
    "timeout": 1,
    "description": "Arduino connection"
  },
  "settings": {
    "log_file": "requests.log",
    "deny_unknown_hosts": true,
    "log_all_requests": true
  }
}
```

### 3. API Usage

#### GET Request
```bash
curl http://localhost:7373/
```

#### POST Request
```bash
curl -X POST http://localhost:7373/ \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

#### Response Format
```json
{
  "message": {
    "value": 25.5,
    "msg": "Temperature reading",
    "mode": "read",
    "result": "OK"
  },
  "timestamp": "2025-01-26T10:30:45.123456",
  "method": "GET",
  "path": "/",
  "client_ip": "127.0.0.1",
  "client_port": 54321
}
```

## ABAP Integration

The package includes ready-to-use ABAP client code in the `abap/` directory.

### ABAP Client Features

- ✅ HTTP client integration
- ✅ JSON parsing with `/ui2/cl_json`
- ✅ Network connectivity testing
- ✅ Multiple connection options
- ✅ Detailed error handling
- ✅ Debug mode with system information
- ✅ Response headers analysis

### Using ABAP Client

#### Method 1: Using --abap parameter (Recommended)
```bash
# Copy ABAP files to current directory
serialsrv --abap

# This will copy zakir_serial_test.abap to your current directory
# You can then copy it to your SAP system
```

#### Method 2: Manual extraction
1. Copy the ABAP code from `serialsrv/abap/zakir_serial_test.abap`
2. Create a new ABAP program in SAP system
3. Paste the code and configure parameters
4. Run the program to test connectivity

### ABAP Program Parameters

- **Host**: Server hostname (default: localhost)
- **Port**: Server port (default: 7373)
- **Test Options**: Multiple connection testing
- **Debug Mode**: System information and network diagnostics

## Configuration Options

### Serial Configuration

```json
{
  "serial": {
    "port": "/dev/ttyUSB0",     // Serial port path
    "baudrate": 9600,           // Communication speed
    "timeout": 1,               // Read timeout in seconds
    "description": "Arduino"    // Optional description
  }
}
```

### Host Access Control

```json
{
  "allowed_hosts": [
    {
      "ip": "127.0.0.1",        // Client IP address
      "ports": [7373, 8080],    // Allowed ports
      "description": "Local"    // Optional description
    }
  ]
}
```

### Settings

```json
{
  "settings": {
    "log_file": "requests.log",     // Log file path
    "deny_unknown_hosts": true,     // Block unauthorized hosts
    "log_all_requests": true        // Log all requests
  }
}
```

## Command Line Options

```bash
serialsrv [OPTIONS]

Options:
  --host HOST     Host to bind to (default: localhost)
  --port PORT     Port to listen on (default: 7373)
  --test          Run in test mode (returns mock data)
  --abap          Copy ABAP files to current directory and exit
  --init          Initialize serialsrv.json configuration file and exit
  --help          Show help message
```

## Use Cases

### IoT Data Collection
- Read sensor data from Arduino/Raspberry Pi
- Provide real-time data via HTTP API
- Integrate with monitoring systems

### Industrial Automation
- Connect to PLCs and industrial devices
- Provide data to SCADA systems
- Enable remote monitoring

### SAP Integration
- Bridge between serial devices and SAP systems
- Real-time data integration
- Automated data collection

## Development

### Project Structure

```
serialsrv/
├── __init__.py          # Main server code
├── abap/                # ABAP client code
│   └── zakir_serial_test.abap
├── serialsrv.json       # Configuration template
└── requirements.txt     # Dependencies
```

### Dependencies

- `pyserial>=3.5` - Serial port communication
- `requests>=2.25.0` - HTTP client (for testing)

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Use different port
   serialsrv --port 8080
   ```

2. **Serial Port Access Denied**
   ```bash
   # Add user to dialout group (Linux)
   sudo usermod -a -G dialout $USER
   ```

3. **ABAP Connection Failed**
   - Check if Python service is running
   - Verify network connectivity
   - Check firewall settings
   - Use debug mode in ABAP program

### Log Analysis

Check the log file for detailed request information:

```bash
tail -f requests.log
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📧 Email: altay.kirecci@gmail.com
- https://www.opriori.com
- 🐛 Issues: [GitHub Issues](https://github.com/altaykirecci/serialsrv/issues)
- 📖 Documentation: [GitHub Wiki](https://github.com/altaykirecci/serialsrv/wiki)

## Changelog

### v1.0.0
- Initial release
- Serial port reading functionality
- HTTP API with JSON responses
- Host-based access control
- ABAP integration support
- Comprehensive logging
- Test mode support