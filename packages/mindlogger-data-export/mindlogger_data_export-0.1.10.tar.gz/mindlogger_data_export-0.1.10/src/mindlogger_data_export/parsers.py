"""Parse response string to dict."""

from datetime import date, time, timedelta
from typing import Any, Protocol

from lark import Lark, Transformer, v_args

from .schema import RESPONSE_VALUE_DICT_SCHEMA, ItemType


class ResponseParser(Protocol):
    """Base class for response parsers."""

    def parse(self, response: str) -> dict[str, Any]:
        """Parse response string to dict."""
        ...


class FullResponseParser(ResponseParser):
    """Parse response string to dict using Lark grammar."""

    RESPONSE_GRAMMAR = r"""
    start: text_resp | null_resp | file_resp | raw_value_resp | matrix_resp
        | ( ( multivalue_resp | date_resp | time_resp | time_range_resp | geo_resp ) [ optional_text ] )

    // Matches text response in "text: <text>" format, including multi-line text.
    text_resp.10: "text:" _WSI _text
    _text: /.+/s

    optional_text: _WSI "| text:" _WSI _text

    // Matches null response in "value: null" format.
    null_resp.20: "value: null"

    // Matches single or multiple values in "value: <value>, <value>, ..." format.
    multivalue_resp.10: "value:" _WSI vlist

    // Matches date response in "date: <month>/<day>/<year>" format.
    date_resp.10: "date:" _WSI padded_two_digit "/" padded_two_digit "/" year
    padded_two_digit: DIGIT ~ 1..2
    year: (DIGIT ~ 2) | (DIGIT ~ 4)

    // Matches time response.
    time_resp.10: "time:" _WSI time

    // Matches time range with from and to times.
    time_range_resp.10: "time_range:" _WSI "from" _WSI time _WSI "/" _WSI "to" _WSI time

    // Matches time in "hr <hour> min <minute>" format.
    time: "("? _hour ","? _WSI _minute ")"?
    _hour: "hr" _WSI padded_two_digit
    _minute: "min" _WSI padded_two_digit

    // Matches geo coordinates with latitude and longitude.
    geo_resp.10: "geo:" _WSI _latitude _WSI "/"? _WSI? _longitude
    _latitude: "lat" _WSI "("? SIGNED_FLOAT ")"?
    _longitude: "long" _WSI "("? SIGNED_FLOAT ")"?

    // Matches single multiple rows with single key-value pair per row.
    // row_resp.5: _sep{row_kv, _NL}
    // row_kv: _value ":" _WSI? _row_value
    // _row_value: /[^,\n]+/

    // Matches multiple rows with key and list of values per row.
    matrix_resp.5: (row_kvv _NL?)+
    row_kvv: _value ":" _WSI? vlist

    // Matches file path by ensuring string contains at least one slash and a 2-4 character extension.
    file_resp.5: /.+[-\/].+\.\w{3,4}/

    // Lowest priority catch-all rule.
    raw_value_resp.0: /.+/s

    // list of comma-separated values
    ilist: _sep{INT, _CSV}
    vlist: _sep{_value, _CSV}

    // Value is any non-empty alphanumeric string
    _value: /[.\w]+/
    _CSV: "," _WSI
    _sep{x, sep}: x (sep x)*

    %import common.SIGNED_FLOAT
    %import common.WS_INLINE -> _WSI
    %import common.DIGIT
    %import common.INT
    %import common.NEWLINE -> _NL

    // Disregard commas in parse tree
    %ignore ","
    """

    class FullResponseTransformer(Transformer):
        """Transform Lark parse tree to dict."""

        PIVOT_YEAR = 69
        MAX_TWO_DIGIT = 99

        @v_args(inline=True)
        def start(self, value, optional_text=None):  # noqa: D102
            if optional_text:
                value = value | optional_text
            return RESPONSE_VALUE_DICT_SCHEMA | value

        def padded_two_digit(self, items):  # noqa: D102
            return int("".join(items))

        def year(self, items):  # noqa: D102
            iyr = int("".join(items))
            conversion = (
                2000
                if iyr < self.PIVOT_YEAR
                else 1900
                if iyr <= self.MAX_TWO_DIGIT
                else 0
            )
            return iyr + conversion

        @v_args(inline=True)
        def date_resp(self, day, month, year):  # noqa: D102
            return {"type": "date", "date": date(year, month, day)}

        @v_args(inline=True)
        def time(self, hour, minute):  # noqa: D102
            return time(hour, minute)

        @v_args(inline=True)
        def time_resp(self, time):  # noqa: D102
            return {"type": "time", "time": time}

        @v_args(inline=True)
        def time_range_resp(self, from_time, to_time):  # noqa: D102
            return {
                "type": "time_range",
                "time_range": timedelta(
                    hours=to_time.hour - from_time.hour,
                    minutes=to_time.minute - from_time.minute,
                ),
            }

        @v_args(inline=True)
        def geo_resp(self, latitude, longitude):  # noqa: D102
            return {
                "type": "geo",
                "geo": {"latitude": latitude, "longitude": longitude},
            }

        @v_args(inline=True)
        def text_resp(self, text):  # noqa: D102
            return {"type": "text", "text": text.value}

        @v_args(inline=True)
        def optional_text(self, text):  # noqa: D102
            return {"optional_text": text.value}

        @v_args(inline=True)
        def null_resp(self):  # noqa: D102
            return {"type": "null_value", "null_value": True}

        @v_args(inline=True)
        def multivalue_resp(self, vlist):  # noqa: D102
            return {"type": "value", "value": vlist}

        @v_args(inline=True)
        def row_kv(self, key, row_value):  # noqa: D102
            return {"row": key.value, "value": row_value.value}

        def matrix_resp(self, items):  # noqa: D102
            return {"type": "matrix", "matrix": items}

        @v_args(inline=True)
        def row_kvv(self, key, ilist):  # noqa: D102
            return {"row": key.value, "value": ilist}

        def vlist(self, items):  # noqa: D102
            return [i.value for i in items]

        def ilist(self, items):  # noqa: D102
            return items

        @v_args(inline=True)
        def file_resp(self, path):  # noqa: D102
            return {"type": "file", "file": path.value}

        @v_args(inline=True)
        def raw_value_resp(self, value):  # noqa: D102
            return {"type": "raw_value", "raw_value": value.value}

        SIGNED_FLOAT = float
        INT = int

    def __init__(self):
        """Initialize ResponseParser."""
        self._transformer = self.FullResponseTransformer()
        self._parser = Lark(self.RESPONSE_GRAMMAR)
        self._types = RESPONSE_VALUE_DICT_SCHEMA.keys()

    def parse(self, response: str) -> dict[str, Any]:
        """Parse response string to dict."""
        return self._transformer.transform(self._parser.parse(response))

    def selection_parser(self, field_name: str):
        """Return parser for selection fields."""

        def _parser(response: str) -> dict[str, Any]:
            return self._transformer.transform(self._parser.parse(response)).get(
                field_name
            )

        return _parser


class GeoResponseParser(ResponseParser):
    """Parse response string to dict using Lark grammar."""

    RESPONSE_GRAMMAR = r"""
    start: geo_resp [ optional_text ]

    optional_text: _WSI "| text:" _WSI _text
    _text: /.+/s

    // Matches geo coordinates with latitude and longitude.
    geo_resp.10: "geo:" _WSI _latitude _WSI "/"? _WSI? _longitude
    _latitude: "lat" _WSI "("? SIGNED_FLOAT ")"?
    _longitude: "long" _WSI "("? SIGNED_FLOAT ")"?

    %import common.SIGNED_FLOAT
    %import common.WS_INLINE -> _WSI

    // Disregard commas in parse tree
    %ignore ","
    """

    class GeoResponseTransformer(Transformer):
        """Transform Lark parse tree to dict."""

        PIVOT_YEAR = 69
        MAX_TWO_DIGIT = 99

        @v_args(inline=True)
        def start(self, value, optional_text=None):  # noqa: D102
            if optional_text:
                value = value | optional_text
            return RESPONSE_VALUE_DICT_SCHEMA | value

        @v_args(inline=True)
        def geo_resp(self, latitude, longitude):  # noqa: D102
            return {
                "type": "geo",
                "geo": {"latitude": latitude, "longitude": longitude},
            }

        @v_args(inline=True)
        def optional_text(self, text):  # noqa: D102
            return {"optional_text": text.value}

        SIGNED_FLOAT = float

    def __init__(self):
        """Initialize ResponseParser."""
        self._transformer = self.GeoResponseTransformer()
        self._parser = Lark(self.RESPONSE_GRAMMAR)
        self._types = RESPONSE_VALUE_DICT_SCHEMA.keys()

    def parse(self, response: str) -> dict[str, Any]:
        """Parse response string to dict."""
        return self._transformer.transform(self._parser.parse(response))


class DateResponseParser(ResponseParser):
    """Parse response string to dict using Lark grammar."""

    RESPONSE_GRAMMAR = r"""
    start: date_resp [ optional_text ]

    optional_text: _WSI "| text:" _WSI _text
    _text: /.+/s

    // Matches date response in "date: <month>/<day>/<year>" format.
    date_resp.10: "date:" _WSI padded_two_digit "/" padded_two_digit "/" year
    padded_two_digit: DIGIT ~ 1..2
    year: (DIGIT ~ 2) | (DIGIT ~ 4)

    %import common.DIGIT
    %import common.WS_INLINE -> _WSI

    // Disregard commas in parse tree
    %ignore ","
    """

    class DateResponseTransformer(Transformer):
        """Transform Lark parse tree to dict."""

        PIVOT_YEAR = 69
        MAX_TWO_DIGIT = 99

        @v_args(inline=True)
        def start(self, value, optional_text=None):  # noqa: D102
            if optional_text:
                value = value | optional_text
            return RESPONSE_VALUE_DICT_SCHEMA | value

        def padded_two_digit(self, items):  # noqa: D102
            return int("".join(items))

        def year(self, items):  # noqa: D102
            iyr = int("".join(items))
            conversion = (
                2000
                if iyr < self.PIVOT_YEAR
                else 1900
                if iyr <= self.MAX_TWO_DIGIT
                else 0
            )
            return iyr + conversion

        @v_args(inline=True)
        def date_resp(self, day, month, year):  # noqa: D102
            return {"type": "date", "date": date(year, month, day)}

        @v_args(inline=True)
        def optional_text(self, text):  # noqa: D102
            return {"optional_text": text.value}

    def __init__(self):
        """Initialize ResponseParser."""
        self._transformer = self.DateResponseTransformer()
        self._parser = Lark(self.RESPONSE_GRAMMAR)
        self._types = RESPONSE_VALUE_DICT_SCHEMA.keys()

    def parse(self, response: str) -> dict[str, Any]:
        """Parse response string to dict."""
        return self._transformer.transform(self._parser.parse(response))


class MultiSelectResponseParser(ResponseParser):
    """Parse response string to dict using Lark grammar."""

    RESPONSE_GRAMMAR = r"""
    start:  null_resp | ( multivalue_resp [ optional_text ] )

    // Matches text response in "text: <text>" format, including multi-line text.
    optional_text: _WSI "| text:" _WSI _text
    _text: /.+/s

    // Matches null response in "value: null" format.
    null_resp.20: "value: null"

    // Matches single or multiple values in "value: <value>, <value>, ..." format.
    multivalue_resp.10: "value:" _WSI ilist

    // list of comma-separated values
    vlist: _sep{_value, _CSV}
    ilist: _sep{INT, _CSV}

    // Value is any non-empty alphanumeric string
    _value: /[.\w]+/
    _CSV: "," _WSI
    _sep{x, sep}: x (sep x)*

    %import common.INT
    %import common.WS_INLINE -> _WSI

    // Disregard commas in parse tree
    %ignore ","
    """

    class MultiSelectResponseTransformer(Transformer):
        """Transform Lark parse tree to dict."""

        @v_args(inline=True)
        def start(self, value, optional_text=None):  # noqa: D102
            if optional_text:
                value = value | optional_text
            return RESPONSE_VALUE_DICT_SCHEMA | value

        @v_args(inline=True)
        def optional_text(self, text):  # noqa: D102
            return {"optional_text": text.value}

        @v_args(inline=True)
        def null_resp(self):  # noqa: D102
            return {"type": "null_value", "null_value": True}

        @v_args(inline=True)
        def multivalue_resp(self, vlist):  # noqa: D102
            return {"type": "value", "value": vlist}

        def vlist(self, items):  # noqa: D102
            return [i.value for i in items]

        def ilist(self, items):  # noqa: D102
            return items

        SIGNED_FLOAT = float
        INT = int

    def __init__(self):
        """Initialize ResponseParser."""
        self._transformer = self.MultiSelectResponseTransformer()
        self._parser = Lark(self.RESPONSE_GRAMMAR)
        self._types = RESPONSE_VALUE_DICT_SCHEMA.keys()

    def parse(self, response: str) -> dict[str, Any]:
        """Parse response string to dict."""
        return self._transformer.transform(self._parser.parse(response))


class SingleSelectResponseParser(ResponseParser):
    """Parse a single select response value."""

    RESPONSE_GRAMMAR = r"""
    start: null_resp | ( value_resp [ optional_text ] )

    optional_text: _WSI "| text:" _WSI _text
    _text: /.+/s

    // Matches null response in "value: null" format.
    null_resp.20: "value: null"

    // Matches single value in "value: <value>" format.
    // value_resp.10: "value:" _WSI _value
    value_resp.10: "value:" _WSI INT

    // Value is any non-empty alphanumeric string
    _value: /[.\w]+/

    %import common.INT
    %import common.WS_INLINE -> _WSI
    """

    class SingleSelectTransformer(Transformer):
        """Transform Lark parse tree to dict."""

        @v_args(inline=True)
        def start(self, value, optional_text=None):  # noqa: D102
            if optional_text:
                value = value | optional_text
            return RESPONSE_VALUE_DICT_SCHEMA | value

        @v_args(inline=True)
        def optional_text(self, text):  # noqa: D102
            return {"optional_text": text.value}

        @v_args(inline=True)
        def value_resp(self, value):  # noqa: D102
            # return {"single_value": value.value}
            return {"single_value": value}

        @v_args(inline=True)
        def null_resp(self):  # noqa: D102
            return {"null_value": True}

        SIGNED_FLOAT = float
        INT = int

    def __init__(self):
        """Initialize ResponseParser."""
        self._transformer = self.SingleSelectTransformer()
        self._parser = Lark(self.RESPONSE_GRAMMAR)
        self._types = RESPONSE_VALUE_DICT_SCHEMA.keys()

    def parse(self, response: str) -> dict[str, Any]:
        """Parse response string to dict."""
        return self._transformer.transform(self._parser.parse(response))


class TextResponseParser(ResponseParser):
    """Parse response string to dict using Lark grammar."""

    RESPONSE_GRAMMAR = r"""
    start: text_resp

    // Matches any text response.
    text_resp: _text
    _text: /.+/s
    """

    class TextResponseTransformer(Transformer):
        """Transform Lark parse tree to dict."""

        @v_args(inline=True)
        def start(self, value, optional_text=None):  # noqa: D102
            if optional_text:
                value = value | optional_text
            return RESPONSE_VALUE_DICT_SCHEMA | value

        @v_args(inline=True)
        def text_resp(self, text):  # noqa: D102
            return {"type": "text", "text": text.value}

    def __init__(self):
        """Initialize ResponseParser."""
        self._transformer = self.TextResponseTransformer()
        self._parser = Lark(self.RESPONSE_GRAMMAR)
        self._types = RESPONSE_VALUE_DICT_SCHEMA.keys()

    def parse(self, response: str) -> dict[str, Any]:
        """Parse response string to dict."""
        return self._transformer.transform(self._parser.parse(response))


class SubscaleResponseParser(ResponseParser):
    """Parse response string to dict using Lark grammar."""

    def parse(self, response: str) -> dict[str, Any]:
        """Parse response string to dict."""
        return RESPONSE_VALUE_DICT_SCHEMA | {
            "type": "subscale",
            "subscale": float(response),
        }  # self._transformer.transform(self._parser.parse(response))


class TypedResponseParser(ResponseParser):
    """Group all typed response parsers."""

    def __init__(self) -> None:
        self._parsers: dict[ItemType, ResponseParser] = {
            ItemType.SingleSelection: SingleSelectResponseParser(),
            ItemType.MultipleSelection: MultiSelectResponseParser(),
            ItemType.Text: TextResponseParser(),
            ItemType.Subscale: SubscaleResponseParser(),
            ItemType.Date: DateResponseParser(),
            ItemType.Geolocation: GeoResponseParser(),
        }

        self._default_parser = FullResponseParser()

    def parse(self, response: str) -> dict[str, Any]:
        """Parse with default parser."""
        return self._default_parser.parse(response)

    def parse_typed(self, item_type: str, response: str) -> dict[str, Any]:
        """Distribute parsing based on item type."""
        return self._parsers.get(ItemType(item_type), self._default_parser).parse(
            response
        )


class OptionsTransformer(Transformer):
    """Transform Lark parse tree to dict."""

    def scored_options(self, options):  # noqa: D102
        return options

    @v_args(inline=True)
    def scored_option(self, option, score):  # noqa: D102
        return {"name": option["name"], "value": option["value"], "score": score}

    @v_args(inline=True)
    def score(self, score):  # noqa: D102
        return int(score)

    def value_options(self, options):  # noqa: D102
        return options

    @v_args(inline=True)
    def option(self, name, value):  # noqa: D102
        return {"name": name, "value": value, "score": None}

    @v_args(inline=True)
    def min_max_range(self, minimum, maximum):  # noqa: D102
        return [
            {"name": n, "value": n, "score": n} for n in range(minimum, maximum + 1)
        ]

    @v_args(inline=True)
    def max_min_range(self, maximum, minimum):  # noqa: D102
        return self.min_max_range(minimum, maximum)

    @v_args(inline=True)
    def name(self, name):  # noqa: D102
        return name.value

    INT = int
    SIGNED_INT = int


class OptionsParser:
    """Parse options string to dict using Lark grammar."""

    OPTIONS_GRAMMAR = r"""
    ?start: scored_options | _range | value_options

    scored_options.10: _sep{scored_option, _CSV}
    scored_option: option _WSI score
    score: "(" "score:" _WSI? SIGNED_INT _WSI? ")"

    _range.20: max_min_range | min_max_range
    max_min_range.20: "Max:" _WSI INT "," _WSI "Min:" _WSI INT
    min_max_range.20: "Min:" _WSI INT "," _WSI "Max:" _WSI INT

    // Matches option in "<name>: <value>" format.
    value_options.10: _sep{option, _CSV}
    option: name _WSI? ":" _WSI? INT

    // Value is any string with 0 or 1 ':' characters.
    // name: /[^:]+/ | /[^:]+:[^:]+/
    name: /[^:]+/
    _CSV: "," _WSI?
    _sep{x, sep}: x (sep x)*

    %import common.INT
    %import common.SIGNED_INT
    %import common.WS_INLINE -> _WSI

    // Disregard commas in parse tree
    %ignore ","
    """

    def __init__(self):
        """Initialize ResponseParser."""
        self._transformer = OptionsTransformer()
        self._parser = Lark(self.OPTIONS_GRAMMAR, parser="earley")

    def parse(self, response: str) -> list[dict[str, Any]] | None:
        """Parse response string to dict."""
        try:
            return self._transformer.transform(self._parser.parse(response))
        except Exception:
            return None
