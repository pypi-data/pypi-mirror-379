from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Type

from .filters import (
    AndFilter,
    BaseFilter,
    CommandFilter,
    PayloadFilter,
    StateFilter,
    TextFilter,
)
from ..magic import MagicFilter, MagicFilterAdapter
from ..types import VKEvent, Message, Callback


class EventTypeFilter(BaseFilter):
    """Скрытый фильтр для проверки типа события (Message или Callback)."""

    def __init__(self, event_type: Type[VKEvent]):
        self.event_type = event_type

    async def check(self, event: VKEvent, **data: Any) -> bool:
        return isinstance(event, self.event_type)




@dataclass
class Handler:
    callback: Callable[..., Any]
    filters: List[BaseFilter] = field(default_factory=list)


class Router:
    def __init__(self):
        self.handlers: List[Handler] = []

    @staticmethod
    def _prepare_and_wrap_filters(
            event_type: Type[VKEvent],
            custom_filters: tuple,
            kwargs: Dict[str, Any]
    ) -> BaseFilter:
        """
        Собирает все фильтры в один финальный AndFilter.
        """
        filters: List[BaseFilter] = [EventTypeFilter(event_type)]

        for f in custom_filters:
            if isinstance(f, MagicFilter):
                filters.append(MagicFilterAdapter(f))
            elif isinstance(f, BaseFilter):
                filters.append(f)
            else:
                raise TypeError(
                    f"Недопустимый тип фильтра: {type(f)}. Ожидался BaseFilter или MagicFilter."
                )

        if (text := kwargs.pop("text", None)) is not None:
            filters.append(
                TextFilter(text, ignore_case=kwargs.pop("ignore_case", True))
            )
        if (command := kwargs.pop("command", None)) is not None:
            filters.append(CommandFilter(command, prefix=kwargs.pop("prefix", "/")))
        if (state := kwargs.pop("state", None)) is not None:
            filters.append(StateFilter(state))
        if (payload := kwargs.pop("payload", None)) is not None:
            filters.append(PayloadFilter(payload))

        if kwargs:
            raise TypeError(
                f"Неизвестные аргументы-фильтры: {', '.join(kwargs.keys())}"
            )

        return AndFilter(*filters)

    def message(self, *custom_filters: Any, **kwargs: Any) -> Callable:
        """
        Декоратор для регистрации обработчика сообщений.
        """
        # === [ИЗМЕНЕНИЕ] Явно передаем тип Message ===
        final_filter = self._prepare_and_wrap_filters(Message, custom_filters, kwargs)

        def decorator(callback: Callable[..., Any]) -> Callable[..., Any]:
            handler = Handler(callback=callback, filters=[final_filter])
            self.handlers.append(handler)
            return callback

        return decorator

    def callback(self, *custom_filters: Any, **kwargs: Any) -> Callable:
        """
        Декоратор для регистрации обработчика callback-событий.
        """
        final_filter = self._prepare_and_wrap_filters(Callback, custom_filters, kwargs)

        def decorator(callback: Callable[..., Any]) -> Callable[..., Any]:
            handler = Handler(callback=callback, filters=[final_filter])
            self.handlers.append(handler)
            return callback

        return decorator

    def include_router(self, router: "Router") -> None:
        self.handlers.extend(router.handlers)