from .msg import Msg
from .protobuf import nonbibrecord_pb2

class NonBibRecord(Msg):

    def __init__(self, *args, **kwargs):
        instance = nonbibrecord_pb2.NonBibRecord()
        
        # Handle links separately if provided
        links = kwargs.pop('links', None)
        
        super(NonBibRecord, self).__init__(instance, args, kwargs)
        
        # Handle only the links structure if provided
        if links:
            for key, value in links.items():
                if key in ['ARXIV', 'DOI']:
                    # Handle simple string arrays
                    getattr(instance.links, key).extend(value)
                elif key in ['DATA', 'ESOURCE']:
                    # Handle map fields
                    for subtype, link_data in value.items():
                        link_type_record = getattr(instance.links, key)[subtype]
                        if 'url' in link_data:
                            link_type_record.url.extend(link_data['url'])
                        if 'title' in link_data:
                            link_type_record.title.extend(link_data['title'])
                        if 'count' in link_data:
                            link_type_record.count = link_data['count']
                elif key in ['ASSOCIATED', 'INSPIRE', 'LIBRARYCATALOG', 'PRESENTATION']:
                    # Handle LinkTypeRecord fields
                    link_type_record = getattr(instance.links, key)
                    if 'url' in value:
                        link_type_record.url.extend(value['url'])
                    if 'title' in value:
                        link_type_record.title.extend(value['title'])
                    if 'count' in value:
                        link_type_record.count = value['count']
                else:
                    # Handle boolean fields
                    setattr(instance.links, key, value)

class NonBibRecordList(Msg):

    def __init__(self, *args, **kwargs):
        super(NonBibRecordList, self).__init__(nonbibrecord_pb2.NonBibRecordList(), args, kwargs)
