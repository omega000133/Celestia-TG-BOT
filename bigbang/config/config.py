import threading
import contextlib
import asyncio

import os
from dotenv import load_dotenv

load_dotenv()


class TeleConfig:
    def __init__(self, api_key=None):
        self.api_key = api_key


class AlarmCache:
    def __init__(self):
        self.SentTgAlarms = {}
        self.AllAlarms = {}
        self.notifyMux = threading.RLock()


class ChainConfig:
    def __init__(self) -> None:
        self.chain_id = os.getenv("CHAIN_ID", "")
        self.valoper_address = os.getenv("VALOPER_ADDRESS", "")
        self.valoper_address = os.getenv("VALOPER_ADDRESS", "")


class Config:
    def __init__(self):
        self.alertChan = []
        self.updateChan = asyncio.Queue()
        self.logChan = asyncio.Queue()
        self.statsChan = asyncio.Queue()
        self.ctx = contextlib.ExitStack()
        self.cancel = threading.Event()
        self.alarms = AlarmCache()

        # Dashboard settings
        self.EnableDash = False
        self.Listen = ""
        self.HideLogs = False

        # Node down alert settings
        self.NodeDownMin = 0
        self.NodeDownSeverity = ""

        # Prometheus settings
        self.Prom = False
        self.PrometheusListenPort = 0

        self.Telegram = TeleConfig()

        self.chainsMux = threading.RLock()
        self.Chains = {}
