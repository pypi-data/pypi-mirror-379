# pylint: skip-file
import socket
import logging


class SocketClient:
    """用于持续与服务器通信的 TCP Socket 客户端."""

    def __init__(self, host: str, port: int, buffer_size: int = 1024):
        """初始化 Socket 客户端.

        Args:
            host: 要连接的服务器主机名或 IP 地址.
            port: 服务器端口号.
            buffer_size: 接收缓冲区大小（字节）,默认为 1024.
        """
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.socket = None
        self.is_connected = False
        self.receive_thread = None
        self.logger = logging.getLogger(self.__class__.__name__)

    def connect(self) -> tuple[bool, str]:
        """建立与服务器的连接, 连接成功后会自动启动后台线程持续接收数据.

        Returns:
            tuple[bool, str]: 连接成功返回 (True, 描述信息), 否则返回 (False, 错误信息).
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.is_connected = True
            self.logger.info("已连接到服务器 %s: %s", self.host, self.port)
            return True, "连接成功"
        except Exception as e:
            self.logger.warning("连接失败, %s", str(e))
            self.is_connected = False
            return False, str(e)

    def disconnect(self):
        """断开与服务器的连接并释放资源."""
        if self.is_connected:
            self.is_connected = False
            try:
                if self.socket:
                    self.socket.close()
                if self.receive_thread and self.receive_thread.is_alive():
                    self.receive_thread.join(timeout=1)
            except Exception as e:
                self.logger.warning("断开连接时出错: %s", str(e))
            finally:
                self.logger.info("已断开与服务器的连接")

    def send_data(self, data: bytes, wait_response: bool = True) -> tuple[bool, str]:
        """向服务器发送数据.

        Args:
            data: 要发送的字节数据.
            wait_response: 是否需要回复, 默认需要回复.

        Returns:
            tuple[bool, str]: 发送成功返回 (True, 成功信息), 失败返回 (False, 失败信息).
        """
        if not self.is_connected:
            self.logger.warning("未连接到服务器")
            return False, "未连接服务端"

        try:
            self.socket.sendall(data)
            if wait_response:
                response = self.socket.recv(self.buffer_size)
                return True, response.decode("UTF-8")
            return True, "发送成功, 不需要等待回复"
        except Exception as e:
            self.logger.warning("发送数据出错: %s", str(e))
            self.disconnect()
            return False, str(e)

    def __enter__(self):
        """实现上下文管理协议,进入时自动连接."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """实现上下文管理协议,退出时自动断开连接."""
        self.disconnect()
