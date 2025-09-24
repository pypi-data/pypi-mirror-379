# smeller/commands/set_channel_params.py
from typing import List, Any, Optional, Dict
from .base import Command

class SetChannelParametersCommand(Command):
    def __init__(self, channel: int, on_tick: int, off_tick: int, **kwargs):
        self.channel = channel
        self.on_tick = on_tick
        self.off_tick = off_tick
        self.kwargs = kwargs

    def serialize(self) -> str:
        params = [f"p {self.channel} {self.on_tick} {self.off_tick}"]
        # Добавляем дополнительные параметры, если они есть
        params.extend(f"{k} {v}" for k, v in self.kwargs.items())
        return " ".join(params)

    def parse_response(self, response_lines: List[str]) -> Any:
        # Реализуй парсинг ответа.  Возможно, возвращай словарь с результатами.
        # Или создай отдельный класс Response для этого.
        if response_lines:
            return response_lines[0]  # Простой пример - возвращаем первую строку
        return None