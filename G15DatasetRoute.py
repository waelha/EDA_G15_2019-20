from enum import Enum
from typing import List, Union, Any, Optional, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class GeometryType(Enum):
    LINE_STRING = "LineString"
    MULTI_LINE_STRING = "MultiLineString"


class Geometry:
    type: GeometryType
    coordinates: List[List[Union[List[float], float]]]

    def __init__(self, type: GeometryType, coordinates: List[List[Union[List[float], float]]]) -> None:
        self.type = type
        self.coordinates = coordinates

    @staticmethod
    def from_dict(obj: Any) -> 'Geometry':
        assert isinstance(obj, dict)
        type = GeometryType(obj.get("type"))
        coordinates = from_list(lambda x: from_list(lambda x: from_union([from_float, lambda x: from_list(from_float, x)], x), x), obj.get("coordinates"))
        return Geometry(type, coordinates)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(GeometryType, self.type)
        result["coordinates"] = from_list(lambda x: from_list(lambda x: from_union([to_float, lambda x: from_list(to_float, x)], x), x), self.coordinates)
        return result


class Brand(Enum):
    BRAVO = "Bravo"
    BRAVODIRECT = "Bravodirect"


class Network(Enum):
    FLIXBUS = "Flixbus"
    OOST_BRABANT = "Oost-Brabant"
    ZUIDOOST_BRABANT = "Zuidoost-Brabant"


class Operator(Enum):
    ARRIVA = "Arriva"
    ARRIVA_TOURING = "Arriva Touring"
    FLIXBUS = "Flixbus"
    HERMES = "Hermes"


class Route(Enum):
    BUS = "bus"


class PropertiesType(Enum):
    ROUTE = "route"


class Properties:
    id: str
    brand: Optional[Brand]
    properties_from: str
    name: str
    network: Optional[Network]
    operator: Operator
    public_transport_version: int
    ref: Optional[str]
    route: Route
    to: str
    type: PropertiesType
    via: Optional[str]
    note: Optional[str]
    loc_name: Optional[str]
    name_fr: Optional[str]
    name_nl: Optional[str]
    website: Optional[str]
    name_de: Optional[str]
    start_date: Optional[datetime]

    def __init__(self, id: str, brand: Optional[Brand], properties_from: str, name: str, network: Optional[Network], operator: Operator, public_transport_version: int, ref: Optional[str], route: Route, to: str, type: PropertiesType, via: Optional[str], note: Optional[str], loc_name: Optional[str], name_fr: Optional[str], name_nl: Optional[str], website: Optional[str], name_de: Optional[str], start_date: Optional[datetime]) -> None:
        self.id = id
        self.brand = brand
        self.properties_from = properties_from
        self.name = name
        self.network = network
        self.operator = operator
        self.public_transport_version = public_transport_version
        self.ref = ref
        self.route = route
        self.to = to
        self.type = type
        self.via = via
        self.note = note
        self.loc_name = loc_name
        self.name_fr = name_fr
        self.name_nl = name_nl
        self.website = website
        self.name_de = name_de
        self.start_date = start_date

    @staticmethod
    def from_dict(obj: Any) -> 'Properties':
        assert isinstance(obj, dict)
        id = from_str(obj.get("@id"))
        brand = from_union([Brand, from_none], obj.get("brand"))
        properties_from = from_str(obj.get("from"))
        name = from_str(obj.get("name"))
        network = from_union([Network, from_none], obj.get("network"))
        operator = Operator(obj.get("operator"))
        public_transport_version = int(from_str(obj.get("public_transport:version")))
        ref = from_union([from_str, from_none], obj.get("ref"))
        route = Route(obj.get("route"))
        to = from_str(obj.get("to"))
        type = PropertiesType(obj.get("type"))
        via = from_union([from_str, from_none], obj.get("via"))
        note = from_union([from_str, from_none], obj.get("note"))
        loc_name = from_union([from_str, from_none], obj.get("loc_name"))
        name_fr = from_union([from_str, from_none], obj.get("name:fr"))
        name_nl = from_union([from_str, from_none], obj.get("name:nl"))
        website = from_union([from_str, from_none], obj.get("website"))
        name_de = from_union([from_str, from_none], obj.get("name:de"))
        start_date = from_union([from_datetime, from_none], obj.get("start_date"))
        return Properties(id, brand, properties_from, name, network, operator, public_transport_version, ref, route, to, type, via, note, loc_name, name_fr, name_nl, website, name_de, start_date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@id"] = from_str(self.id)
        result["brand"] = from_union([lambda x: to_enum(Brand, x), from_none], self.brand)
        result["from"] = from_str(self.properties_from)
        result["name"] = from_str(self.name)
        result["network"] = from_union([lambda x: to_enum(Network, x), from_none], self.network)
        result["operator"] = to_enum(Operator, self.operator)
        result["public_transport:version"] = from_str(str(self.public_transport_version))
        result["ref"] = from_union([from_str, from_none], self.ref)
        result["route"] = to_enum(Route, self.route)
        result["to"] = from_str(self.to)
        result["type"] = to_enum(PropertiesType, self.type)
        result["via"] = from_union([from_str, from_none], self.via)
        result["note"] = from_union([from_str, from_none], self.note)
        result["loc_name"] = from_union([from_str, from_none], self.loc_name)
        result["name:fr"] = from_union([from_str, from_none], self.name_fr)
        result["name:nl"] = from_union([from_str, from_none], self.name_nl)
        result["website"] = from_union([from_str, from_none], self.website)
        result["name:de"] = from_union([from_str, from_none], self.name_de)
        result["start_date"] = from_union([lambda x: x.isoformat(), from_none], self.start_date)
        return result


class FeatureType(Enum):
    FEATURE = "Feature"


class Feature:
    type: FeatureType
    properties: Properties
    geometry: Geometry
    id: str

    def __init__(self, type: FeatureType, properties: Properties, geometry: Geometry, id: str) -> None:
        self.type = type
        self.properties = properties
        self.geometry = geometry
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'Feature':
        assert isinstance(obj, dict)
        type = FeatureType(obj.get("type"))
        properties = Properties.from_dict(obj.get("properties"))
        geometry = Geometry.from_dict(obj.get("geometry"))
        id = from_str(obj.get("id"))
        return Feature(type, properties, geometry, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(FeatureType, self.type)
        result["properties"] = to_class(Properties, self.properties)
        result["geometry"] = to_class(Geometry, self.geometry)
        result["id"] = from_str(self.id)
        return result


class BusRouteEhv:
    features: List[Feature]

    def __init__(self, features: List[Feature]) -> None:
        self.features = features

    @staticmethod
    def from_dict(obj: Any) -> 'BusRouteEhv':
        assert isinstance(obj, dict)
        features = from_list(Feature.from_dict, obj.get("features"))
        return BusRouteEhv(features)

    def to_dict(self) -> dict:
        result: dict = {}
        result["features"] = from_list(lambda x: to_class(Feature, x), self.features)
        return result


def bus_route_ehv_from_dict(s: Any) -> BusRouteEhv:
    return BusRouteEhv.from_dict(s)


def bus_route_ehv_to_dict(x: BusRouteEhv) -> Any:
    return to_class(BusRouteEhv, x)