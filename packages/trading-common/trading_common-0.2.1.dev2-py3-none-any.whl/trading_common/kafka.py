import asyncio
from typing import Any, Dict, Optional

from aiokafka import AIOKafkaProducer

from .kafka_common import dumps, encode_key


class Producer:
    def __init__(self, base_cfg: Dict[str, Any], tuning: Dict[str, Any]) -> None:
        """
        base_cfg: settings_kafka.KAFKA_COMMON
        tuning:   settings_kafka.PRODUCER_TUNING
        """
        # aiokafka ожидает плоские kwargs
        self.cfg = {**base_cfg, **tuning}
        self.p: Optional[AIOKafkaProducer] = None

    async def start(self, retries: int = 20) -> None:
        self.p = AIOKafkaProducer(**self.cfg)
        # «мягкие» ретраи, чтобы деплой не падал, если брокер прогревается
        delay = 1.0
        for attempt in range(retries):
            try:
                await self.p.start()
                return
            except Exception:
                await asyncio.sleep(min(delay, 10.0))
                delay *= 1.5
        raise RuntimeError("Kafka producer failed to start after retries")

    async def stop(self) -> None:
        if self.p:
            await self.p.stop()
            self.p = None

    async def send(
        self, topic: str, key: Optional[str], payload: Dict[str, Any]
    ) -> None:
        assert self.p is not None, "Producer not started"
        await self.p.send_and_wait(topic, key=encode_key(key), value=dumps(payload))
