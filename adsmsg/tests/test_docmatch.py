
import unittest

from adsmsg.docmatch import DocMatchRecord, DocMatchRecordList

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_docmatch_record(self):
        """test creation of protobuf"""

        docmatch_record = {
                            'eprint_bibcode': '2021arXiv210312030S',
                            'pub_bibcode': '2021CSF...15311505S',
                            'confidence': 0.9829099
        }
        m = DocMatchRecord(**docmatch_record)
        self.assertEqual(m.eprint_bibcode, docmatch_record['eprint_bibcode'])
        self.assertEqual(m.pub_bibcode, docmatch_record['pub_bibcode'])
        self.assertEqual(m.confidence, docmatch_record['confidence'])

    def test_document_records(self):
        """test creation of protobuf"""

        docmatch_records = {
            'status': 2,    #name='new', index=2, number=2,
            'docmatch_records':[
                {
                    'eprint_bibcode': '2021arXiv210312030S',
                    'pub_bibcode': '2021CSF...15311505S',
                    'confidence': 0.9829099
                }, {
                    'eprint_bibcode': '2018ConPh..59...16H',
                    'pub_bibcode': '2018ConPh..59...16H',
                    'confidence': 0.9877064
                }, {
                    'eprint_bibcode': '2022NuPhB.98015830S',
                    'pub_bibcode': '2022NuPhB.98015830S',
                    'confidence': 1.97300124
                }
            ]
        }

        n = DocMatchRecordList(**docmatch_records)
        self.assertEqual(n.status, docmatch_records['status'])
        for i, docmatch_record in enumerate(docmatch_records['docmatch_records']):
            self.assertEqual(n.docmatch_records[i].eprint_bibcode, docmatch_record['eprint_bibcode'])
            self.assertEqual(n.docmatch_records[i].pub_bibcode, docmatch_record['pub_bibcode'])
            self.assertEqual(n.docmatch_records[i].confidence, docmatch_record['confidence'])

if __name__ == '__main__':
    unittest.main()
