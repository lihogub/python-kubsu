import string
from typing import Dict
from lxml import etree


def dict2xml(input_dict: Dict):
    item = etree.Element("item")
    for key in input_dict.keys():
        attr = etree.Element("attr")
        attr.set("key", key)
        attr.set("value", str(input_dict[key]))
        item.append(attr)
    return item


def xml2dict(item) -> Dict:
    output_dict = {}
    for child in item:
        key = child.get("key")
        value = child.get("value")
        output_dict[key] = value
    return output_dict


def export_to_file(dict_list: list, path: string):
    root = etree.Element("items")
    for item in dict_list:
        root.append(dict2xml(item))
    with open(path, "w+") as file:
        file.write(etree.tostring(root, pretty_print=True).decode("utf-8"))


def import_from_file(path: string):
    dict_list = []
    with open(path, "r") as file:
        text = file.read().encode("utf-8")
        items = etree.XML(text)
        for item in items:
            dict_list.append(xml2dict(item))
    return dict_list
