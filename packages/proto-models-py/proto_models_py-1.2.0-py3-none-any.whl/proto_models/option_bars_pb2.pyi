from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OptionBar(_message.Message):
    __slots__ = ["symbol", "bar", "bars"]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    BAR_FIELD_NUMBER: _ClassVar[int]
    BARS_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    bar: OptionBarData
    bars: _containers.RepeatedCompositeFieldContainer[OptionBarData]
    def __init__(self, symbol: _Optional[str] = ..., bar: _Optional[_Union[OptionBarData, _Mapping]] = ..., bars: _Optional[_Iterable[_Union[OptionBarData, _Mapping]]] = ...) -> None: ...

class OptionBarData(_message.Message):
    __slots__ = ["symbol", "timestamp", "open", "high", "low", "close", "volume", "trade_count", "vwap"]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    TRADE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VWAP_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    timestamp: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    trade_count: float
    vwap: float
    def __init__(self, symbol: _Optional[str] = ..., timestamp: _Optional[str] = ..., open: _Optional[float] = ..., high: _Optional[float] = ..., low: _Optional[float] = ..., close: _Optional[float] = ..., volume: _Optional[float] = ..., trade_count: _Optional[float] = ..., vwap: _Optional[float] = ...) -> None: ...

class OptionBarsRequest(_message.Message):
    __slots__ = ["symbols", "timeframe", "start", "end", "limit"]
    SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    TIMEFRAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    symbols: _containers.RepeatedScalarFieldContainer[str]
    timeframe: str
    start: str
    end: str
    limit: int
    def __init__(self, symbols: _Optional[_Iterable[str]] = ..., timeframe: _Optional[str] = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class OptionBarsResponse(_message.Message):
    __slots__ = ["bars", "symbols", "count", "timeframe", "start", "end"]
    class BarsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OptionBarList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OptionBarList, _Mapping]] = ...) -> None: ...
    BARS_FIELD_NUMBER: _ClassVar[int]
    SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMEFRAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    bars: _containers.MessageMap[str, OptionBarList]
    symbols: _containers.RepeatedScalarFieldContainer[str]
    count: int
    timeframe: str
    start: str
    end: str
    def __init__(self, bars: _Optional[_Mapping[str, OptionBarList]] = ..., symbols: _Optional[_Iterable[str]] = ..., count: _Optional[int] = ..., timeframe: _Optional[str] = ..., start: _Optional[str] = ..., end: _Optional[str] = ...) -> None: ...

class OptionBarList(_message.Message):
    __slots__ = ["bars"]
    BARS_FIELD_NUMBER: _ClassVar[int]
    bars: _containers.RepeatedCompositeFieldContainer[OptionBarData]
    def __init__(self, bars: _Optional[_Iterable[_Union[OptionBarData, _Mapping]]] = ...) -> None: ...
