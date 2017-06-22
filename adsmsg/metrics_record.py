from .msg import Msg
from .protobuf import metrics_pb2

class MetricsRecord(Msg):

    def __init__(self, *args, **kwargs):
        """construct protobuf metrics record, ususally from a database dict
        
        value for rn_citation_data needs speical processing 
          to clearly specify its contents for protobuf. example data: 
          [{"ref_norm": 0.2, "pubyear": 1954, "auth_norm": 0.25, "bibcode": "1954PhRv...93..257G", "cityear": 1954}, ...]
        the citation_records message defines the contents of the json object 
        """
        instance = metrics_pb2.MetricsRecord()
        kwargs.pop('id', None)  # local database key field is not serialized
        rn_citation_data = kwargs.pop('rn_citation_data', None)
        super(MetricsRecord, self).__init__(instance, args, kwargs)
        if rn_citation_data:
            for current in rn_citation_data:
                citation_record = instance.rn_citation_data.add()
                for key in current:
                    setattr(citation_record, key, current[key])
                


class MetricsRecordList():
    
    def __init__(self, metrics_records):
        instance = metrics_pb2.MetricsRecordList()
        self.__dict__['_data'] = instance  
        for current in metrics_records:
            tmp = MetricsRecord(**current)
            current_protobuf = tmp.__dict__['_data']
            instance.metrics_records.extend([current_protobuf])

        self.__dict__['metrics_records'] = instance.metrics_records     
        
