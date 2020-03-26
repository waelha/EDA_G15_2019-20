from enum import Enum
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Bench(Enum):
    NO = "no"
    YES = "yes"


class Highway(Enum):
    BUS_STOP = "bus_stop"


class PublicTransport(Enum):
    PLATFORM = "platform"


class Tags:
    bus: Optional[Bench]
    highway: Highway
    name: str
    public_transport: PublicTransport
    shelter: Optional[Bench]
    zone: Optional[int]
    bench: Optional[Bench]
    ref_ifopt: Optional[str]
    source: Optional[str]
    tactile_paving: Optional[Bench]
    cxx_code: Optional[int]
    cxx_id: Optional[int]
    operator: Optional[str]
    covered: Optional[Bench]
    bin: Optional[Bench]
    ref: Optional[str]
    lit: Optional[Bench]
    note: Optional[str]
    timetable: Optional[Bench]
    wheelchair: Optional[Bench]
    bus_routes: Optional[str]

    def __init__(self, bus: Optional[Bench], highway: Highway, name: str, public_transport: PublicTransport, shelter: Optional[Bench], zone: Optional[int], bench: Optional[Bench], ref_ifopt: Optional[str], source: Optional[str], tactile_paving: Optional[Bench], cxx_code: Optional[int], cxx_id: Optional[int], operator: Optional[str], covered: Optional[Bench], bin: Optional[Bench], ref: Optional[str], lit: Optional[Bench], note: Optional[str], timetable: Optional[Bench], wheelchair: Optional[Bench], bus_routes: Optional[str]) -> None:
        self.bus = bus
        self.highway = highway
        self.name = name
        self.public_transport = public_transport
        self.shelter = shelter
        self.zone = zone
        self.bench = bench
        self.ref_ifopt = ref_ifopt
        self.source = source
        self.tactile_paving = tactile_paving
        self.cxx_code = cxx_code
        self.cxx_id = cxx_id
        self.operator = operator
        self.covered = covered
        self.bin = bin
        self.ref = ref
        self.lit = lit
        self.note = note
        self.timetable = timetable
        self.wheelchair = wheelchair
        self.bus_routes = bus_routes

    @staticmethod
    def from_dict(obj: Any) -> 'Tags':
        assert isinstance(obj, dict)
        bus = from_union([Bench, from_none], obj.get("bus"))
        highway = Highway(obj.get("highway"))
        name = from_str(obj.get("name"))
        public_transport = PublicTransport(obj.get("public_transport"))
        shelter = from_union([Bench, from_none], obj.get("shelter"))
        zone = from_union([from_none, lambda x: int(from_str(x))], obj.get("zone"))
        bench = from_union([Bench, from_none], obj.get("bench"))
        ref_ifopt = from_union([from_str, from_none], obj.get("ref:IFOPT"))
        source = from_union([from_str, from_none], obj.get("source"))
        tactile_paving = from_union([Bench, from_none], obj.get("tactile_paving"))
        cxx_code = from_union([from_none, lambda x: int(from_str(x))], obj.get("cxx:code"))
        cxx_id = from_union([from_none, lambda x: int(from_str(x))], obj.get("cxx:id"))
        operator = from_union([from_str, from_none], obj.get("operator"))
        covered = from_union([Bench, from_none], obj.get("covered"))
        bin = from_union([Bench, from_none], obj.get("bin"))
        ref = from_union([from_str, from_none], obj.get("ref"))
        lit = from_union([Bench, from_none], obj.get("lit"))
        note = from_union([from_str, from_none], obj.get("note"))
        timetable = from_union([Bench, from_none], obj.get("timetable"))
        wheelchair = from_union([Bench, from_none], obj.get("wheelchair"))
        bus_routes = from_union([from_str, from_none], obj.get("bus_routes"))
        return Tags(bus, highway, name, public_transport, shelter, zone, bench, ref_ifopt, source, tactile_paving, cxx_code, cxx_id, operator, covered, bin, ref, lit, note, timetable, wheelchair, bus_routes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bus"] = from_union([lambda x: to_enum(Bench, x), from_none], self.bus)
        result["highway"] = to_enum(Highway, self.highway)
        result["name"] = from_str(self.name)
        result["public_transport"] = to_enum(PublicTransport, self.public_transport)
        result["shelter"] = from_union([lambda x: to_enum(Bench, x), from_none], self.shelter)
        result["zone"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.zone)
        result["bench"] = from_union([lambda x: to_enum(Bench, x), from_none], self.bench)
        result["ref:IFOPT"] = from_union([from_str, from_none], self.ref_ifopt)
        result["source"] = from_union([from_str, from_none], self.source)
        result["tactile_paving"] = from_union([lambda x: to_enum(Bench, x), from_none], self.tactile_paving)
        result["cxx:code"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.cxx_code)
        result["cxx:id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.cxx_id)
        result["operator"] = from_union([from_str, from_none], self.operator)
        result["covered"] = from_union([lambda x: to_enum(Bench, x), from_none], self.covered)
        result["bin"] = from_union([lambda x: to_enum(Bench, x), from_none], self.bin)
        result["ref"] = from_union([from_str, from_none], self.ref)
        result["lit"] = from_union([lambda x: to_enum(Bench, x), from_none], self.lit)
        result["note"] = from_union([from_str, from_none], self.note)
        result["timetable"] = from_union([lambda x: to_enum(Bench, x), from_none], self.timetable)
        result["wheelchair"] = from_union([lambda x: to_enum(Bench, x), from_none], self.wheelchair)
        result["bus_routes"] = from_union([from_str, from_none], self.bus_routes)
        return result


class TypeEnum(Enum):
    NODE = "node"


class Element:
    type: TypeEnum
    id: int
    lat: float
    lon: float
    tags: Tags

    def __init__(self, type: TypeEnum, id: int, lat: float, lon: float, tags: Tags) -> None:
        self.type = type
        self.id = id
        self.lat = lat
        self.lon = lon
        self.tags = tags

    @staticmethod
    def from_dict(obj: Any) -> 'Element':
        assert isinstance(obj, dict)
        type = TypeEnum(obj.get("type"))
        id = from_int(obj.get("id"))
        lat = from_float(obj.get("lat"))
        lon = from_float(obj.get("lon"))
        tags = Tags.from_dict(obj.get("tags"))
        return Element(type, id, lat, lon, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(TypeEnum, self.type)
        result["id"] = from_int(self.id)
        result["lat"] = to_float(self.lat)
        result["lon"] = to_float(self.lon)
        result["tags"] = to_class(Tags, self.tags)
        return result


class BusStopEhv:
    elements: List[Element]

    def __init__(self, elements: List[Element]) -> None:
        self.elements = elements

    @staticmethod
    def from_dict(obj: Any) -> 'BusStopEhv':
        assert isinstance(obj, dict)
        elements = from_list(Element.from_dict, obj.get("elements"))
        return BusStopEhv(elements)

    def to_dict(self) -> dict:
        result: dict = {}
        result["elements"] = from_list(lambda x: to_class(Element, x), self.elements)
        return result


def bus_stop_ehv_from_dict(s: Any) -> BusStopEhv:
    return BusStopEhv.from_dict(s)


def bus_stop_ehv_to_dict(x: BusStopEhv) -> Any:
    return to_class(BusStopEhv, x)