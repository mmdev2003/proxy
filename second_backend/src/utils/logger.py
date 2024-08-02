import json
import logging
import sys

from loguru import logger as log

uvicorn_error = logging.getLogger("uvicorn.error")
uvicorn_error.disabled = True
uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True


def serialize(record):
    try:
        subset = {
            "timestamp": record["time"].isoformat(),
            "level": record["level"].name,
            "message": record["message"],
            "source": f"{record['file']}:{record['function']}:{record['line']}",
        }
        if record["extra"]:
            subset["error"] = str(record["extra"]["extra"])

        return json.dumps(subset)
    except Exception as e:
        print(e)


def patching(record):
    try:
        record["extra"]["serialized"] = serialize(record)
    except Exception as e:
        pass


log.remove()
logger = log.patch(patching)
log.add(sys.stdout, backtrace=False, format="{extra[serialized]}", catch=False)
