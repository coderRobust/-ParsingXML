import json
import xmltodict
import logging
from datetime import datetime
import pandas as pd

namespaces = {
            "http://www.adventure-works.com": None,
        }

def xml_data_parsing():
  parsed_data = {}
  final_data = {}
  parsed_message =None
  try:
      with open("\PARSINGXML\\sample_customer_data.xml", "r", encoding='utf-8') as file_obj:
          data = file_obj.read()
          parsed_message = xmltodict.parse(data, process_namespaces=True, namespaces=namespaces)
  except Exception as e :
    logging.error("There is error while opening file - ", e)
  data = pd.DataFrame.from_dict(parsed_message.get("Root"), orient ='index')
  return data


