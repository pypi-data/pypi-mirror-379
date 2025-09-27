#!/usr/bin/env python3
"""
Serial Server HTTP Service that reads from serial port or returns test data
with host-based access control
"""

import http.server
import socketserver
import json
import logging
import os
import serial
import serial.tools.list_ports
import shutil
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Global variables for host control and serial configuration
ALLOWED_HOSTS = {}
LOG_FILE = "requests.log"
SERIAL_CONFIG = {}
TEST_MODE = False

def load_serialsrv_config():
    """
    Load configuration from serialsrv.json
    """
    global ALLOWED_HOSTS, LOG_FILE, SERIAL_CONFIG
    
    # Try to find config file in current directory first, then in package directory
    config_paths = ['serialsrv.json', os.path.join(os.path.dirname(__file__), 'serialsrv.json')]
    
    for config_path in config_paths:
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                ALLOWED_HOSTS = config.get('allowed_hosts', [])
                LOG_FILE = config.get('settings', {}).get('log_file', 'requests.log')
                SERIAL_CONFIG = config.get('serial', {})
                logger.info(f"Loaded {len(ALLOWED_HOSTS)} allowed hosts from {config_path}")
                logger.info(f"Serial config: {SERIAL_CONFIG}")
                return
        except FileNotFoundError:
            continue
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing {config_path}: {e}")
            continue
    
    logger.warning("serialsrv.json not found, allowing all hosts")
    ALLOWED_HOSTS = []
    SERIAL_CONFIG = {}

def is_host_allowed(client_ip, port):
    """
    Check if the client IP is allowed to access the specified port
    """
    if not ALLOWED_HOSTS:
        return True  # If no serialsrv.json, allow all
    
    for host_config in ALLOWED_HOSTS:
        if host_config['ip'] == client_ip and port in host_config['ports']:
            return True
    return False

def log_request(client_ip, client_port, method, path, status, response_size=0, user_agent=""):
    """
    Log request to requests.log file
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    log_entry = f"{timestamp} | {status} | {client_ip}:{client_port} | {method} {path} | {response_size} bytes | {user_agent}\n"
    
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(log_entry)
    except Exception as e:
        logger.error(f"Error writing to log file: {e}")

def read_serial_data():
    """
    Read data from serial port
    """
    try:
        if not SERIAL_CONFIG:
            raise Exception("Serial configuration not found in serialsrv.json")
        
        # Get serial port configuration
        port = SERIAL_CONFIG.get('port', '/dev/ttyUSB0')
        baudrate = SERIAL_CONFIG.get('baudrate', 9600)
        timeout = SERIAL_CONFIG.get('timeout', 1)
        
        # Open serial connection
        with serial.Serial(port, baudrate, timeout=timeout) as ser:
            # Read data
            data = ser.readline().decode('utf-8').strip()
            if data:
                # Try to convert to float, if fails return as string
                try:
                    value = float(data)
                    return value, "Serial Value"
                except ValueError:
                    return data, "Serial Value"
            else:
                raise Exception("No data received from serial port")
                
    except Exception as e:
        logger.error(f"Serial read error: {e}")
        raise e

def get_test_response():
    """
    Get test mode response
    """
    return {
        "value": 0,
        "msg": "hello world",
        "mode": "test",
        "result": "OK"
    }

def get_serial_response():
    """
    Get serial port response
    """
    try:
        value, msg = read_serial_data()
        return {
            "value": value,
            "msg": msg,
            "mode": "read",
            "result": "OK"
        }
    except Exception as e:
        return {
            "value": -1,
            "msg": str(e),
            "mode": "read",
            "result": "FAIL"
        }

# Load configuration on startup
load_serialsrv_config()

class SerialServerHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for serial server with host-based access control
    """
    
    def check_access(self):
        """
        Check if the client is allowed to access the service
        """
        client_ip = self.client_address[0]
        server_port = self.server.server_address[1]
        user_agent = self.headers.get('User-Agent', '')
        
        # Check if host is allowed
        if is_host_allowed(client_ip, server_port):
            logger.info(f"ACCEPTED: {self.command} request from {client_ip}:{self.client_address[1]} to port {server_port}")
            log_request(client_ip, self.client_address[1], self.command, self.path, "ACCEPTED", 0, user_agent)
            return True
        else:
            logger.warning(f"DENIED: {self.command} request from {client_ip}:{self.client_address[1]} to port {server_port}")
            log_request(client_ip, self.client_address[1], self.command, self.path, "DENIED", 0, user_agent)
            return False
    
    def do_GET(self):
        """
        Handle GET requests
        """
        # Check access first
        if not self.check_access():
            self.send_response(403)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Access Denied')
            return
        
        logger.info(f"GET request from {self.client_address[0]}:{self.client_address[1]}")
        logger.info(f"Request path: {self.path}")
        
        # Get response data based on mode
        if TEST_MODE:
            message_data = get_test_response()
        else:
            message_data = get_serial_response()
        
        # Prepare response data
        response_data = {
            'message': message_data,
            'timestamp': datetime.now().isoformat(),
            'method': 'GET',
            'path': self.path,
            'client_ip': self.client_address[0],
            'client_port': self.client_address[1]
        }
        
        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        # Send JSON response
        response_json = json.dumps(response_data, indent=2)
        response_bytes = response_json.encode('utf-8')
        self.wfile.write(response_bytes)
        
        # Log successful response
        log_request(self.client_address[0], self.client_address[1], 'GET', self.path, 'ACCEPTED', len(response_bytes), self.headers.get('User-Agent', ''))
        
        logger.info("Response sent successfully")
    
    def do_POST(self):
        """
        Handle POST requests
        """
        # Check access first
        if not self.check_access():
            self.send_response(403)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Access Denied')
            return
        
        logger.info(f"POST request from {self.client_address[0]}:{self.client_address[1]}")
        
        # Get content length
        content_length = int(self.headers.get('Content-Length', 0))
        
        # Read request body
        post_data = ""
        if content_length > 0:
            post_data = self.rfile.read(content_length).decode('utf-8')
            logger.info(f"POST data: {post_data}")
        
        # Get response data based on mode
        if TEST_MODE:
            message_data = get_test_response()
        else:
            message_data = get_serial_response()
        
        # Prepare response data
        response_data = {
            'message': message_data,
            'timestamp': datetime.now().isoformat(),
            'method': 'POST',
            'path': self.path,
            'client_ip': self.client_address[0],
            'client_port': self.client_address[1],
            'received_data': post_data
        }
        
        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        # Send JSON response
        response_json = json.dumps(response_data, indent=2)
        response_bytes = response_json.encode('utf-8')
        self.wfile.write(response_bytes)
        
        # Log successful response
        log_request(self.client_address[0], self.client_address[1], 'POST', self.path, 'ACCEPTED', len(response_bytes), self.headers.get('User-Agent', ''))
        
        logger.info("Response sent successfully")
    
    def do_OPTIONS(self):
        """
        Handle OPTIONS requests for CORS
        """
        # Check access first
        if not self.check_access():
            self.send_response(403)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Access Denied')
            return
        
        logger.info(f"OPTIONS request from {self.client_address[0]}:{self.client_address[1]}")
        
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        # Log successful response
        log_request(self.client_address[0], self.client_address[1], 'OPTIONS', self.path, 'ACCEPTED', 0, self.headers.get('User-Agent', ''))
    
    def log_message(self, format, *args):
        """
        Override log_message to use our logger
        """
        logger.info(f"{self.address_string()} - {format % args}")

def init_config_file():
    """
    Initialize serialsrv.json configuration file in current directory
    """
    try:
        # Get package directory
        package_dir = os.path.dirname(__file__)
        config_source_path = os.path.join(package_dir, 'serialsrv.json')
        
        # Get current working directory
        current_dir = os.getcwd()
        config_dest_path = os.path.join(current_dir, 'serialsrv.json')
        
        # Check if source config file exists
        if not os.path.exists(config_source_path):
            logger.error(f"Source config file not found: {config_source_path}")
            return False
        
        # Check if destination file already exists
        if os.path.exists(config_dest_path):
            print(f"\n⚠️  Configuration file already exists: {config_dest_path}")
            response = input("Do you want to overwrite it? (y/N): ").strip().lower()
            if response not in ['y', 'yes']:
                print("❌ Configuration file creation cancelled")
                return False
        
        # Copy the configuration file
        try:
            shutil.copy2(config_source_path, config_dest_path)
            logger.info(f"Copied serialsrv.json to {current_dir}")
            
            print(f"\n✅ Successfully created configuration file:")
            print(f"   📄 serialsrv.json")
            print(f"\n📁 Current directory: {current_dir}")
            print("💡 You can now edit serialsrv.json to configure your server")
            print("🔧 Available settings:")
            print("   - allowed_hosts: IP addresses and ports")
            print("   - serial: Serial port configuration")
            print("   - settings: Log file and other options")
            return True
            
        except Exception as e:
            logger.error(f"Failed to copy configuration file: {e}")
            return False
            
    except Exception as e:
        logger.error(f"Error initializing configuration file: {e}")
        return False

def copy_abap_files():
    """
    Copy ABAP files from package to current directory
    """
    try:
        # Get package directory
        package_dir = os.path.dirname(__file__)
        abap_source_dir = os.path.join(package_dir, 'abap')
        
        # Get current working directory
        current_dir = os.getcwd()
        
        # Check if ABAP source directory exists
        if not os.path.exists(abap_source_dir):
            logger.error(f"ABAP source directory not found: {abap_source_dir}")
            return False
        
        # List all ABAP files in the package
        abap_files = [f for f in os.listdir(abap_source_dir) if f.endswith('.abap')]
        
        if not abap_files:
            logger.warning("No ABAP files found in package")
            return False
        
        # Copy each ABAP file
        copied_files = []
        for abap_file in abap_files:
            source_path = os.path.join(abap_source_dir, abap_file)
            dest_path = os.path.join(current_dir, abap_file)
            
            try:
                shutil.copy2(source_path, dest_path)
                copied_files.append(abap_file)
                logger.info(f"Copied {abap_file} to {current_dir}")
            except Exception as e:
                logger.error(f"Failed to copy {abap_file}: {e}")
        
        if copied_files:
            print(f"\n✅ Successfully copied {len(copied_files)} ABAP file(s) to current directory:")
            for file in copied_files:
                print(f"   📄 {file}")
            print(f"\n📁 Current directory: {current_dir}")
            print("💡 You can now copy these files to your SAP system")
            return True
        else:
            logger.error("No ABAP files were copied")
            return False
            
    except Exception as e:
        logger.error(f"Error copying ABAP files: {e}")
        return False

def start_server(port=7373, host='localhost'):
    """
    Start the HTTP server on specified port with host-based access control
    """
    try:
        with socketserver.TCPServer((host, port), SerialServerHandler) as httpd:
            logger.info(f"Serial Server starting on {host}:{port}")
            logger.info("Available endpoints:")
            logger.info(f"  GET  http://{host}:{port}/")
            logger.info(f"  POST http://{host}:{port}/")
            logger.info(f"Host access control: {'ENABLED' if ALLOWED_HOSTS else 'DISABLED'}")
            logger.info(f"Log file: {LOG_FILE}")
            logger.info(f"Mode: {'TEST' if TEST_MODE else 'SERIAL'}")
            if not TEST_MODE and SERIAL_CONFIG:
                logger.info(f"Serial port: {SERIAL_CONFIG.get('port', 'Not configured')}")
            logger.info("Press Ctrl+C to stop the server")
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        logger.info("Server interrupted by user")
    except OSError as e:
        if e.errno == 98:  # Address already in use
            logger.error(f"Port {port} is already in use. Please choose a different port.")
        else:
            logger.error(f"Error starting server: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

def main():
    """
    Main function
    """
    import argparse

    
    


    parser = argparse.ArgumentParser(description='Serial Port Reader HTTP Service')
    print("Serial Port Reader HTTP Service")
    print("with SAP ABAP integration")
    print("opriori (c)(p) 2025-09-1.0.1")
    print("https://www.opriori.com")
    print("")
    print("developed by Altay Kireççi")
    print("for donation contact: altay.kirecci@gmail.com")
    print("for support visit: https://www.opriori.com")
    print("GitHub: https://github.com/altaykirecci")
    print("LinkedIn: https://www.linkedin.com/in/altaykireci")
    print("pypi: https://pypi.org/user/altaykireci/")
    print("")


    parser.add_argument('--port', type=int, default=7373, help='Port to listen on (default: 7373)')
    parser.add_argument('--host', default='localhost', help='Host to bind to (default: localhost)')
    parser.add_argument('--test', action='store_true', help='Run in test mode (returns test data instead of reading serial port)')
    parser.add_argument('--abap', action='store_true', help='Copy ABAP files to current directory and exit')
    parser.add_argument('--init', action='store_true', help='Initialize serialsrv.json configuration file and exit')
    
    args = parser.parse_args()
    
    # Handle configuration file initialization
    if args.init:
        print("🔧 SerialSrv - Configuration Initializer")
        print("=" * 50)
        success = init_config_file()
        if success:
            print("\n🎉 Configuration file ready!")
        else:
            print("\n❌ Failed to create configuration file")
            exit(1)
        return
    
    # Handle ABAP file copying
    if args.abap:
        print("🔧 SerialSrv - ABAP File Extractor")
        print("=" * 50)
        success = copy_abap_files()
        if success:
            print("\n🎉 ABAP files ready for SAP integration!")
        else:
            print("\n❌ Failed to copy ABAP files")
            exit(1)
        return
    
    # Set test mode globally
    global TEST_MODE
    TEST_MODE = args.test
    
    start_server(port=args.port, host=args.host)

if __name__ == "__main__":
    main()
