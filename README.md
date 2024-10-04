# Hello-PyZMQ

This project demonstrates various usage patterns of ZeroMQ in Python for inter-process communication (IPC), in-process communication, TCP-based communication, and secure communication using CurveZMQ authentication.

## Project Structure

- `certs/` : Directory containing the server and client keys for secure communication.
- `.gitignore` : Git ignore file for ignoring unnecessary files and directories.
- `client-ipc.py` : Client implementation using IPC (inter-process communication).
- `client-tcp-auth.py` : Client implementation using TCP with CURVE authentication.
- `client-tcp.py` : Basic client implementation using TCP without authentication.
- `demo-inproc.py` : Demonstrates in-process messaging between threads in the same process.
- `demo-ipc.py` : Demonstrates inter-process communication using IPC transport.
- `demo-tcp-auth-fail.py` : Demonstrates failed authentication with a client that does not have the proper keys.
- `demo-tcp-auth.py` : Demonstrates secure communication using TCP and CURVE authentication.
- `demo-tcp.py` : Demonstrates simple communication using TCP transport.
- `key_generation.py` : Script to generate the server and client keys for CURVE authentication.
- `server-ipc.py` : Server implementation using IPC (inter-process communication).
- `server-tcp-auth.py` : Server implementation using TCP with CURVE authentication.
- `server-tcp.py` : Basic server implementation using TCP without authentication.

## Setup Instructions

1. **Install Dependencies**

   Make sure you have Python and ZeroMQ (`pyzmq`) installed. You can install `pyzmq` via pip:

   ```bash
   pip install pyzmq
   ```

2. **Generate Certificates**

   To use CURVE authentication, you need to generate the necessary keys for the server and the client. Use the `key_generation.py` script:

   ```bash
   python key_generation.py
   ```

   This will create the necessary key files in the `certs/` directory.

## Running the Demos

### 1. Basic TCP Communication

- **Server**: Run `server-tcp.py`
- **Client**: Run `client-tcp.py`

### 2. Secure TCP Communication (CURVE Authentication)

- **Server**: Run `server-tcp-auth.py`
- **Client**: Run `client-tcp-auth.py`
- **Demo**: Run `demo-tcp-auth.py` to start both server and client.

To verify failure on invalid authentication, use `demo-tcp-auth-fail.py`.

### 3. Inter-Process Communication (IPC)

- **Server**: Run `server-ipc.py`
- **Client**: Run `client-ipc.py`
- **Demo**: Run `demo-ipc.py` to start both server and client.

### 4. In-Process Communication (Inproc)

- **Demo**: Run `demo-inproc.py` to see communication within the same process using threads.

## Notes

- **CURVE Authentication**: CURVE is used for secure communication. The `certs/` directory must contain the generated keys for successful client-server communication.
- **IPC on Windows**: IPC may not be supported on Windows. If you encounter issues, consider using TCP as an alternative transport.

## License

This project is licensed under the MIT License.

