class XmlStockDataSource:
    def __init__(self, xml_data):
        self.xml_data = xml_data

    def get_data(self):
        return self.xml_data


class AnalyticsStockData:
    def __init__(self, json_data):
        self.data = json_data

    def analyse(self):
        return f'Json Data: {self.data} is Analysed'


class XMLToJsonAdapter:
    def __init__(self,xml_data_source):
        self.xml_data_source = xml_data_source

    def convert_xml_to_json(self):
        xml_data = self.xml_data_source.get_data()
        return xml_data.replace("<", "{").replace(">", "}")


xml_data_source = XmlStockDataSource("<stock>...</stock>")
xml_to_json = XMLToJsonAdapter(xml_data_source)
json_data = xml_to_json.convert_xml_to_json()
analysis_data = AnalyticsStockData(json_data)
print(analysis_data.analyse())





