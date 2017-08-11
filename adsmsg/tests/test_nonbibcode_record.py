
import unittest
from adsmsg.nonbibrecord import NonBibRecord, NonBibRecordList, protobufToNonBibRecord

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_record(self):
        nonbib_data = {'bibcode': '2003ASPC..295..361M', 'refereed': False,
                       'downloads': [0,0], 'boost': 3.1,
                       'reads': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]}
        m = NonBibRecord(**nonbib_data)
        self.assertEqual(m.bibcode, nonbib_data['bibcode'])
        self.assertEqual(m.refereed, nonbib_data['refereed'])
        self.assertEqual(m.downloads, nonbib_data['downloads'])
        self.assertEqual(m.reads, nonbib_data['reads'])
        self.assertAlmostEqual(m.boost, nonbib_data['boost'], places=5)


    def test_list(self):
        nonbib_data1 = {'bibcode': '2003ASPC..295..361M', 'refereed': False}
        nonbib_data2 = {'bibcode': '2003ASPC..295..361Z', 'refereed': True}
        n1 = NonBibRecord(**nonbib_data1)
        n2 = NonBibRecord(**nonbib_data2)
        n_wrapper = [n1, n2]
        n_pbuf = [n1._data, n2._data]
        l = NonBibRecordList()
        l.nonbib_records.extend(n_pbuf)
        count = 0
        for current in l.nonbib_records:
            wrapper = protobufToNonBibRecord(current)
            self.assertEqual(wrapper.bibcode, n_wrapper[count].bibcode)
            self.assertEqual(wrapper.refereed, n_wrapper[count].refereed)
            count += 1


if __name__ == '__main__':
    unittest.main()
