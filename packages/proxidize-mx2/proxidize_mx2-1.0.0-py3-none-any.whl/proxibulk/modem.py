"""Modem class and related logic."""
from typing import Optional, Dict, Any
import json

class Modem:
    def __init__(self, index:int, raw:str, host:str, port:int, user:str, pwd:str):
        self.index = index
        self.raw = raw
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.proxy = None  # Set by probe
        self.reachable = False
        self.system_info = {}
        self.network_info = {}
        self.plmn = None
        self.carrier = None
        self.last_action = None
        self.error = None

    def to_row(self):
        return {
            "index": self.index,
            "proxy": self.raw,
            "reachable": self.reachable,
            "plmn": self.plmn or "",
            "carrier": self.carrier or "",
            "last_action": json.dumps(self.last_action) if self.last_action else "",
            "error": (str(self.error) if self.error else "")
        }
