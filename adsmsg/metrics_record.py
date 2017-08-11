from .msg import Msg
from .protobuf import metrics_pb2
from google.protobuf.json_format import MessageToJson
import json

# wrapper classes for metrics protobufs

class MetricsRecord(Msg):

    def __init__(self, *args, **kwargs):
        """construct protobuf metrics record, ususally from a database dict
        
        value for rn_citation_data needs speical processing 
          to clearly specify its contents for protobuf. example data: 
          [{"ref_norm": 0.2, "pubyear": 1954, "auth_norm": 0.25, "bibcode": "1954PhRv...93..257G", "cityear": 1954}, ...]
        the citation_records message defines the contents of the json object 
        """
        instance = metrics_pb2.MetricsRecord()
        rn_citation_data = kwargs.pop('rn_citation_data', None)
        super(MetricsRecord, self).__init__(instance, args, kwargs)
        if rn_citation_data:
            for current in rn_citation_data:
                citation_record = instance.rn_citation_data.add()
                for key in current:
                    setattr(citation_record, key, current[key])
                


class MetricsRecordList(Msg):
    
    def __init__(self, *args, **kwargs):
        """converts list of dicts to list of protobuf (not wrapper!) instances""" 
        if 'metrics_records' in kwargs:
            tmp = [MetricsRecord(**x)._data for x in kwargs['metrics_records']]
            kwargs['metrics_records'] = tmp
        super(MetricsRecordList, self).__init__(metrics_pb2.MetricsRecordList(), args, kwargs)
    
           
def protobufToMetricsRecord(pbuf):
    """use with elements in MetricsRecordList.metrics_records

    converts metricsrecord_pb2.MetricsRecord to our MetricsRecord wrapper
    """
    tmp_string = MessageToJson(pbuf)
    tmp_dict = json.loads(tmp_string)
    tmp_metrics = MetricsRecord(**tmp_dict)
    return tmp_metrics
