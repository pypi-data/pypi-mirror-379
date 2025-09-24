#smeller/commands/base.py

from typing import List, Any
from .base import Command
class GetHelpCommand(Command):


    def serialize(self) -> str:
        return "h"
    def parse_response(self, response_lines: List[str]) -> Any:
        # Здесь можно реализовать более сложный парсинг, если нужно
        #  преобразовать ответ в словарь или другой формат.
        return response_lines