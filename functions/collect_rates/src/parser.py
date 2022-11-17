import xml.etree.ElementTree as ET

from src.constants import RATES_CODES_WHITELIST
from src.schema import VoluteSchema


def parse_schema_from_xml(xml: str) -> list[VoluteSchema]:
    tree = ET.fromstring(xml)
    parsed_data = []
    for item in tree:
        parsed_item = {child.tag: child.text for child in item if child.tag}
        if parsed_item["CharCode"] in RATES_CODES_WHITELIST:
            parsed_data.append(
                VoluteSchema(
                    rate_code=parsed_item["CharCode"],
                    value=float(parsed_item["Value"].replace(",", ".")),
                    nominal=int(parsed_item["Nominal"]),
                )
            )
    return parsed_data
