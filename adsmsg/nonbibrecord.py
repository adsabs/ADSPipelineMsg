from .msg import Msg
from .protobuf import nonbibrecord_pb2

class NonBibRecord(Msg):

    def __init__(self, *args, **kwargs):
        instance = nonbibrecord_pb2.NonBibRecord()
        data_links_rows = kwargs.pop('data_links_rows', None)  # remove for special handling
        super(NonBibRecord, self).__init__(instance, args, kwargs)
        if data_links_rows:
            # populate rows from database field
            for current in data_links_rows:
                row = instance.data_links_rows.add()
                row.link_type = current['link_type']
                row.link_sub_type = current['link_sub_type']
                row.item_count = current['item_count']
                row.url.extend(current['url'])
                row.title.extend(current['title'])
                

class NonBibRecordList(Msg):

    def __init__(self, *args, **kwargs):
        super(NonBibRecordList, self).__init__(nonbibrecord_pb2.NonBibRecordList(), args, kwargs)


class DataLinksRecord(Msg):

    def __init__(self, *args, **kwargs):
        instance = nonbibrecord_pb2.DataLinksRecord()
        data_links_rows = kwargs.pop('data_links_rows', None)  # remove for special handling
        super(DataLinksRecord, self).__init__(instance, args, kwargs)
        if data_links_rows:
            # populate rows from database field
            for current in data_links_rows:
                row = instance.data_links_rows.add()
                row.link_type = current['link_type']
                row.link_sub_type = current['link_sub_type']
                row.item_count = current['item_count']
                row.url.extend(current['url'])
                row.title.extend(current['title'])


class DataLinksRecordList(Msg):
    def __init__(self, *args, **kwargs):
        super(DataLinksRecordList, self).__init__(nonbibrecord_pb2.DataLinksRecordList(), args, kwargs)


# for resolver db 2.0
class DocumentRecord(Msg):
    def __init__(self, *args, **kwargs):
        instance = nonbibrecord_pb2.DocumentRecord()
        links = kwargs.pop('links', None)
        super(DocumentRecord, self).__init__(instance, args, kwargs)
        if links:
            link_record = instance.links
            for key in links.keys():
                if isinstance(links[key], str) or isinstance(links[key], bool):
                    setattr(link_record, key, links[key])
                elif isinstance(links[key], dict):
                    if key == 'DATA':
                        for sub_type_key in links[key].keys():
                            link_type = instance.links.DATA[sub_type_key]
                            link_type.url.extend(links[key][sub_type_key]['url'])
                            link_type.title.extend(links[key][sub_type_key]['title'])
                            link_type.count = links[key][sub_type_key]['count']
                    elif key == 'ESOURCE':
                        for sub_type_key in links[key].keys():
                            link_type = instance.links.ESOURCE[sub_type_key]
                            link_type.url.extend(links[key][sub_type_key]['url'])
                            link_type.title.extend(links[key][sub_type_key]['title'])
                    elif key == 'ASSOCIATED':
                        link_type = instance.links.ASSOCIATED
                        link_type.url.extend(links[key]['url'])
                        link_type.title.extend(links[key]['title'])
                    elif key == 'TOC':
                        link_type = instance.links.TOC
                        link_type.url.extend(links[key]['url'])
                    elif key == 'PRESENTATION':
                        link_type = instance.links.PRESENTATION
                        link_type.url.extend(links[key]['url'])
                    elif key == 'LIBRARYCATALOG':
                        link_type = instance.links.LIBRARYCATALOG
                        link_type.url.extend(links[key]['url'])
                    elif key == 'INSPIRE':
                        link_type = instance.links.INSPIRE
                        link_type.url.extend(links[key]['url'])




class DocumentRecords(Msg):
    def __init__(self, *args, **kwargs):
        """converts list of dicts to list of protobuf instances of message DocumentRecord"""
        if 'document_records' in kwargs:
            kwargs['document_records'] = [DocumentRecord(**x)._data for x in kwargs['document_records']]
        super(DocumentRecords, self).__init__(nonbibrecord_pb2.DocumentRecords(), args, kwargs)


class DataSource(Msg):
    def __init__(self, *args, **kwargs):
        super(DataSource, self).__init__(nonbibrecord_pb2.DataSource(), args, kwargs)


class DataSourceList(Msg):
    def __init__(self, *args, **kwargs):
        """converts list of dicts to list of protobuf instances of message DataSource"""
        if 'data_source' in kwargs:
            kwargs['data_source'] = [DataSource(**x)._data for x in kwargs['data_source']]
        super(DataSourceList, self).__init__(nonbibrecord_pb2.DataSourceList(), args, kwargs)
