import binascii

from .exception_handlers.duplicate_packet import DuplicatePacket
from .exception_handlers.out_of_order import OutOfOrder
from .pest_command.message_exception import *
from .log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris.exception_dispatch")


class ExceptionDispatch:
    def __init__(self):
        self.handlers = {
            OUT_OF_ORDER_SELF: OutOfOrder(),
            OUT_OF_ORDER_NET: OutOfOrder(),
            OUT_OF_ORDER_BOTH: OutOfOrder(),
            DUPLICATE_PACKET: DuplicatePacket(),
        }

    def handle(self, exception):
        try:
            return self.handlers[exception.error_code].handle(exception)
        except KeyError as e:
            # just log it
            error_code = e.args[0]
            packet_info = exception.metadata["packet_info"]
            address = packet_info[0]
            port = packet_info[1]
            packet_sample = packet_info[2]

            if error_code == STALE_PACKET:
                logger.error(
                    "[%s:%d] -> stale packet: %s"
                    % (address, port, binascii.hexlify(exception.object.message_hash))
                )
            elif error_code == DUPLICATE_PACKET:
                logger.error(
                    "[%s:%d] -> duplicate packet: %s"
                    % (address, port, binascii.hexlify(exception.object.message_hash))
                )
            elif error_code == MALFORMED_PACKET:
                logger.error(
                    "[%s:%d] -> malformed packet: %s" % (address, port, packet_sample)
                )
            elif error_code == INVALID_SIGNATURE:
                logger.error(
                    "[%s:%d] -> invalid packet signature: %s"
                    % (address, port, packet_sample)
                )
            elif error_code == UNSUPPORTED_VERSION:
                logger.error(
                    "[%s:%d] -> pest version not supported: %s"
                    % (address, port, packet_sample)
                )
            elif error_code == UNSUPPORTED_COMMAND:
                logger.error(
                    "[%s:%d] -> pest command not supported: %s"
                    % (address, port, packet_sample)
                )
            elif error_code == INVALID_HANDLE_ENCODING:
                logger.error(
                    "[%s:%d] -> invalid handle encoding: %s"
                    % (address, port, packet_sample)
                )
            else:
                logger.error("No handler for exception: %s" % exception.error_code)
