# SPDX-License-Identifier: BSD-3-Clause OR Apache-2.0
import select
from time import time
from datetime import datetime, timezone

UNIX_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)
DTN_EPOCH = datetime(2000, 1, 1, tzinfo=timezone.utc)
CCSDS_EPOCH = datetime(1958, 1, 1, tzinfo=timezone.utc)

UNIX_TO_DTN_OFFSET = (DTN_EPOCH - UNIX_EPOCH).total_seconds()
assert UNIX_TO_DTN_OFFSET == 946684800

CCSDS_TO_UNIX_OFFSET = (UNIX_EPOCH - CCSDS_EPOCH).total_seconds()
CCSDS_TO_DTN_OFFSET = (DTN_EPOCH - CCSDS_EPOCH).total_seconds()


class CommunicationError(Exception):
    pass


def ccsdstime():
    """Obtains the current CCSDS timestamp.

    Returns:
        float: CCSDS timestamp
    """
    return time() + CCSDS_TO_UNIX_OFFSET


def sock_recv_raw(sock, count, timeout=None):
    """Tries to receive an exact number of bytes from a socket.

    Args:
        sock: socket object
        count (int): non-zero number of bytes to be received
        timeout (float): maximum time to wait, in s (None for infinite timeout)
    Returns:
        bytes: Received raw data
    """
    assert count
    buf = b""
    while len(buf) < count:
        if timeout:
            ready = select.select([sock], [], [], timeout)
        else:
            ready = select.select([sock], [], [])
        if not ready[0]:
            raise CommunicationError("select operation ran into timeout")
        r = sock.recv(count - len(buf))
        if not len(r):
            raise CommunicationError(
                "received 0 bytes (e.g. because the socket was closed)"
            )
        buf += r
    return buf
