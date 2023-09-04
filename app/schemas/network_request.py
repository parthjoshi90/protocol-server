from datetime import datetime
from enum import Enum
from typing import Any, List, Optional
from .actions import Action
from pydantic import AnyUrl, BaseModel, RootModel, Field


class Status(Enum):
    ACK = "ACK"
    NACK = "NACK"


class Ack(BaseModel):
    status: Status = Field(
        ...,
        description="Describe the status of the ACK response. If schema validation passes, status is ACK else it is NACK",
    )


class Address(BaseModel):
    door: Optional[str] = Field(None, description="Door / Shop number of the address")
    name: Optional[str] = Field(
        None, description="Name of address if applicable. Example, shop name"
    )
    building: Optional[str] = Field(None, description="Name of the building or block")
    street: Optional[str] = Field(None, description="Street name or number")
    locality: Optional[str] = Field(
        None, description="Name of the locality, apartments"
    )
    ward: Optional[str] = Field(
        None, description="Name or number of the ward if applicable"
    )
    city: Optional[str] = Field(None, description="City name")
    state: Optional[str] = Field(None, description="State name")
    country: Optional[str] = Field(None, description="Country name")
    area_code: Optional[str] = Field(
        None, description="Area code. This can be Pincode, ZIP code or any equivalent"
    )


class City(BaseModel):
    name: Optional[str] = Field(None, description="Name of the city")
    code: Optional[str] = Field(
        None,
        description="Codification of city code will be using the std code of the city e.g. for Ahmedabad, city code is 'std:079'",
    )


class Country(BaseModel):
    name: Optional[str] = Field(None, description="Name of the country")
    code: Optional[str] = Field(
        None, description="Country code as per ISO 3166 Alpha-3 code format"
    )


class Domain(RootModel):
    root: str = Field(..., description="Codification of domains supported by ONDC")


class Duration(RootModel):
    root: str = Field(..., description="Describes duration as per ISO8601 format")


class Gps(RootModel):
    root: str = Field(
        pattern=r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$",
        description="Describes a gps coordinate",
    )


class CityCode(RootModel):
    root: str = Field(
        ...,
        description="Codification of city code will be using the std code of the city e.g. for Bengaluru, city code is 'std:080'",
    )


class CountryCode(RootModel):
    root: str = Field(
        ..., description="Country code as per ISO 3166 Alpha-3 code format"
    )


class Context(BaseModel):
    domain: Domain
    country: CountryCode
    city: CityCode
    action: Action = Field(
        ...,
        description="Defines the ONDC API call. Any actions other than the enumerated actions are not supported by ONDC Protocol",
    )
    core_version: str = Field(
        ..., description="Version of ONDC core API specification being used"
    )
    bap_id: str = Field(
        ...,
        description="Unique id of the Buyer App. By default it is the fully qualified domain name of the Buyer App",
    )
    bap_uri: AnyUrl = Field(
        ...,
        description="URI of the Seller App for accepting callbacks. Must have the same domain name as the bap_id",
    )
    bpp_id: Optional[str] = Field(
        None,
        description="Unique id of the Seller App. By default it is the fully qualified domain name of the Seller App",
    )
    bpp_uri: Optional[AnyUrl] = Field(
        None,
        description="URI of the Seller App. Must have the same domain name as the bap_id",
    )
    transaction_id: str = Field(
        ...,
        description="This is a unique value which persists across all API calls from search through confirm",
    )
    message_id: str = Field(
        ...,
        description="This is a unique value which persists during a request / callback cycle",
    )
    timestamp: datetime = Field(
        ..., description="Time of request generation in RFC3339 format"
    )
    key: Optional[str] = Field(
        None, description="The encryption public key of the sender"
    )
    ttl: Optional[str] = Field(
        None,
        description="The duration in ISO8601 format after timestamp for which this message holds valid.",
    )


class Descriptor(BaseModel):
    name: Optional[str] = None


class Item(BaseModel):
    descriptor: Optional[Descriptor] = None


class Location(BaseModel):
    id: Optional[str] = None
    descriptor: Optional[Descriptor] = None
    gps: Optional[Gps] = None
    address: Optional[Address] = None
    station_code: Optional[str] = None
    city: Optional[City] = None
    country: Optional[Country] = None


class FeeType(Enum):
    percent = "percent"
    fixed = "fixed"


class Payment(BaseModel):
    buyer_app_finder_fee_type: Optional[FeeType] = Field(
        alias="@ondc/org/buyer_app_finder_fee_type"
    )
    buyer_app_finder_fee_amount: Optional[int] = Field(
        alias="@ondc/org/buyer_app_finder_fee_amount", gt=0
    )


class Start(BaseModel):
    location: Optional[Location] = None


class End(BaseModel):
    location: Optional[Location] = None


class Fulfillment(BaseModel):
    type: Optional[str] = Field(
        None, description="This describes the type of fulfillment"
    )
    start: Optional[Start] = Field(
        None, description="Details on the start of fulfillment"
    )
    end: Optional[End] = Field(None, description="Details on the end of fulfillment")


class Intent(BaseModel):
    descriptor: Optional[Descriptor] = None
    fulfillment: Optional[Fulfillment] = None
    payment: Optional[Payment] = None
    item: Optional[Item] = None


class Message(BaseModel):
    intent: Intent


class ONDCRequest(BaseModel):
    context: Context
    message: Message
