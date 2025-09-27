import xml.etree.ElementTree as ET
from .base import SysproBaseModel
from ..utils import append_custom_columns_and_values

class DrawingModel(SysproBaseModel):
    _primary_key = "DrawOfficeNum"

    def add_stockcode(self, id:str, stockcode: str):

        xmlin = {
            "@attributes": {
                "xmlns:xsd": "http://www.w3.org/2001/XMLSchema-instance",
                "xsd:noNamespaceSchemaLocation": "BOMSTKDOC.XSD"
            },
            "Item": {
                "DrawOfficeNum": id,
                "Key": {
                    "StockCode": stockcode
                }
            }
        }

        xmlparams = {}

        self.query(
            bo="BOMSTK", xmlin=xmlin, root_tag="SetupEccDrawStock",
            endpoint="/Rest/Setup/Add"
        )
