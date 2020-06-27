# -*- coding: utf-8 -*-
from base64 import b64encode
from hashlib import sha1
from http.server import (
    ThreadingHTTPServer,
    HTTPServer,
    BaseHTTPRequestHandler,
    SimpleHTTPRequestHandler,
)
import errno, socket  # for socket exceptions
import struct
import threading
from pathlib import Path


host = "localhost"
port = 8000

cwd = Path(__file__).parent
home = cwd.joinpath('index.html')


with open(home, "r") as html_file:
    html_page = html_file.read()


class MyThreadingHTTPServer(ThreadingHTTPServer):
    def service_actions(self):
        pass

class WebSocketError(Exception):
    pass


class HTTPWebsocketRequestHandler(SimpleHTTPRequestHandler):
    _ws_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
    _opcode_continu = 0x0
    _opcode_text = 0x1
    _opcode_binary = 0x2
    _opcode_close = 0x8
    _opcode_ping = 0x9
    _opcode_pong = 0xA

    mutex = threading.Lock()

    def on_ws_message(self, message):
        """Override this handler to process incoming websocket messages."""
        pass

    def on_ws_connected(self):
        """Override this handler to process on connected events"""
        pass

    def on_ws_closed(self):
        """Override this handler to process on close events"""
        pass

    def send_message(self, message):
        self._send_message(self._opcode_text, message)

    def setup(self):
        SimpleHTTPRequestHandler.setup(self)
        self.connected = False

    def do_GET(self):
        """
        overwritten from SimpleHTTPRequestHandler
        - handle GET request
        Either it is a simple request for a webpage, in which case an html page is sent back to the client, 
        or it is an upgrade-to-websocket request from the html page, in which case the upgrade-handshake is conducted
        """
        if self.headers.get("Upgrade", None) == "websocket":
            self._handshake()
            self._read_messages()
        else:
            self.send_response(200)

            print(self.path)
            self.end_headers()
            self.wfile.write(html_page.encode())

    def _read_messages(self):
        while self.connected == True:
            try:
                self._read_next_message()
            except (socket.error, WebSocketError) as e:
                # websocket content error, time-out or disconnect.
                self.log_message("RCV: Close connection: Socket Error %s" % str(e.args))
                self._ws_close()
            except Exception as err:
                # unexpected error in websocket connection.
                self.log_error("RCV: Exception: in _read_messages: %s" % str(err.args))
                self._ws_close()

    def _read_next_message(self):
        # self.rfile.read(n) is blocking.
        # it returns however immediately when the socket is closed.
        try:
            self.opcode = ord(self.rfile.read(1)) & 0x0F
            length = ord(self.rfile.read(1)) & 0x7F
            if length == 126:
                length = struct.unpack(">H", self.rfile.read(2))[0]
            elif length == 127:
                length = struct.unpack(">Q", self.rfile.read(8))[0]
            masks = []
            for byte in self.rfile.read(4):
                masks.append(byte)

            decoded = ""
            for char in self.rfile.read(length):
                decoded += chr(char ^ masks[len(decoded) % 4])
            self._on_message(decoded)
        except (struct.error, TypeError) as e:
            # catch exceptions from ord() and struct.unpack()
            if self.connected:
                raise WebSocketError("Websocket read aborted while listening")
            else:
                # the socket was closed while waiting for input
                self.log_error(
                    "RCV: _read_next_message aborted after closed connection"
                )
                pass

    def _send_message(self, opcode, message):
        try:
            # use of self.wfile.write gives socket exception after socket is closed. Avoid.
            self.request.send(bytes([0x80 + opcode]))
            length = len(message)
            if length <= 125:
                self.request.send(bytes([length]))
            elif length >= 126 and length <= 65535:
                self.request.send(chr(126).encode())
                self.request.send(struct.pack(">H", length).encode())
            else:
                self.request.send(chr(127).encode())
                self.request.send(struct.pack(">Q", length).encode())
            if length > 0:
                self.request.send(message.encode())
        except socket.error as e:
            # websocket content error, time-out or disconnect.
            self.log_message("SND: Close connection: Socket Error %s" % str(e.args))
            self._ws_close()
        except Exception as err:
            # unexpected error in websocket connection.
            self.log_error("SND: Exception: in _send_message: %s" % str(err.args))
            self._ws_close()

    def _handshake(self):
        headers = self.headers
        if headers.get("Upgrade", None) != "websocket":
            return
        key = headers["Sec-WebSocket-Key"]
        sha = sha1((key + self._ws_GUID).encode()).hexdigest()
        hex_bytes = bytes.fromhex(sha)
        digest = b64encode(hex_bytes).decode("utf-8")

        self.send_response(101, "Switching Protocols")
        self.send_header("Upgrade", "websocket")
        self.send_header("Connection", "Upgrade")
        self.send_header("Sec-WebSocket-Accept", str(digest))
        self.end_headers()
        self.connected = True
        self.on_ws_connected()

    def _ws_close(self):
        # avoid closing a single socket two time for send and receive.
        self.mutex.acquire()
        try:
            if self.connected:
                self.connected = False
                # Terminate BaseHTTPRequestHandler.handle() loop:
                self.close_connection = 1
                # send close and ignore exceptions. An error may already have occurred.
                try:
                    self._send_close()
                except:
                    pass
                self.on_ws_closed()
            else:
                self.log_message("_ws_close websocket in closed state. Ignore.")
                pass
        finally:
            self.mutex.release()

    def _on_message(self, message):
        # self.log_message("_on_message: opcode: %02X msg: %s" % (self.opcode, message))

        # close
        if self.opcode == self._opcode_close:
            self.connected = False
            # Terminate BaseHTTPRequestHandler.handle() loop:
            self.close_connection = 1
            try:
                self._send_close()
            except:
                pass
            self.on_ws_closed()
        # ping
        elif self.opcode == self._opcode_ping:
            self._send_message(self._opcode_pong, message)
        # pong
        elif self.opcode == self._opcode_pong:
            pass
        # data
        elif (
            self.opcode == self._opcode_continu
            or self.opcode == self._opcode_text
            or self.opcode == self._opcode_binary
        ):
            self.on_ws_message(message)

    def _send_close(self):
        # Dedicated _send_close allows for catch all exception handling
        msg = bytearray()
        msg.append(0x80 + self._opcode_close)
        msg.append(0x00)
        self.request.send(msg)


class HTTPWebsocketHandler(HTTPWebsocketRequestHandler):
    def on_ws_message(self, message):
        print(f"Received {message} from client")
        new_message = message.upper()
        print(f"Sending {new_message}")
        self.send_message(f"{new_message}")

    def on_ws_connected(self):
        print("Websocket connected")
        self.send_message("Hi from the Websocket Server!")

    def on_ws_closed(self):
        print("Websocket closed")


with MyThreadingHTTPServer((host, port), HTTPWebsocketHandler) as httpd:
    try:
        print(f"Starting http server on http://{host}:{port}")
        
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Keyboard interrupt: Shutting http server down")
        httpd.shutdown()
