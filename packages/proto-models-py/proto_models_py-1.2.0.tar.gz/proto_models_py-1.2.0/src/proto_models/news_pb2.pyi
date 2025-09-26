from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NewsArticle(_message.Message):
    __slots__ = ["id", "headline", "author", "created_at", "updated_at", "summary", "content", "url", "symbols", "images", "source"]
    ID_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    headline: str
    author: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    summary: str
    content: str
    url: str
    symbols: _containers.RepeatedScalarFieldContainer[str]
    images: _containers.RepeatedScalarFieldContainer[str]
    source: str
    def __init__(self, id: _Optional[str] = ..., headline: _Optional[str] = ..., author: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., summary: _Optional[str] = ..., content: _Optional[str] = ..., url: _Optional[str] = ..., symbols: _Optional[_Iterable[str]] = ..., images: _Optional[_Iterable[str]] = ..., source: _Optional[str] = ...) -> None: ...

class NewsResponse(_message.Message):
    __slots__ = ["articles", "symbol", "total_count", "next_page_token"]
    ARTICLES_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    articles: _containers.RepeatedCompositeFieldContainer[NewsArticle]
    symbol: str
    total_count: int
    next_page_token: str
    def __init__(self, articles: _Optional[_Iterable[_Union[NewsArticle, _Mapping]]] = ..., symbol: _Optional[str] = ..., total_count: _Optional[int] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class NewsRequest(_message.Message):
    __slots__ = ["symbol", "limit", "start_date", "end_date", "page_token", "sources", "sort"]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    limit: int
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    page_token: str
    sources: _containers.RepeatedScalarFieldContainer[str]
    sort: str
    def __init__(self, symbol: _Optional[str] = ..., limit: _Optional[int] = ..., start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., page_token: _Optional[str] = ..., sources: _Optional[_Iterable[str]] = ..., sort: _Optional[str] = ...) -> None: ...
