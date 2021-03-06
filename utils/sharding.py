import hashlib
import logging
import os


LOG = logging.getLogger(__name__)

SHARDS = int(os.environ.get('SHARDS', 1))
SHARD_ID = int(os.environ.get('SHARD_ID', 0))


def is_in_shard(value):
    if SHARDS == 1:
        return True

    value_md5 = hashlib.md5(value.encode())
    value_hex = value_md5.hexdigest()
    value_int = int(value_hex, base=16)

    in_shard = value_int % SHARDS == SHARD_ID

    if in_shard:
        LOG.debug('IN_SHARD TRUE: %s', value)
    else:
        LOG.debug('IN_SHARD FALSE: %s', value)

    return in_shard
