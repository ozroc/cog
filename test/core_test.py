from context import cog
from cog.core import Index
from cog.core import Store
from cog.core import Table
from cog.core import Indexer
from cog import config
import logging
import os
from logging.config import dictConfig
import shutil

import unittest

DIR_NAME = "TestCore"


class TestCore(unittest.TestCase):

    def test_aaa_before_all_tests(self):
        if not os.path.exists("/tmp/"+DIR_NAME+"/"):
            os.mkdir("/tmp/" + DIR_NAME + "/")
            os.mkdir("/tmp/"+DIR_NAME+"/test_table/")

        config.COG_HOME = DIR_NAME

    def test_put_get(self):


        dictConfig(config.logging_config)
        logger = logging.getLogger()

        expected_data = ("new super data","super new old stuff")

        table = Table("testdb","test_table","test_xcvzdfsadx")
        print config.COG_HOME
        store = Store(table, config, logger)
        index = Index(table, config, logger)


        position=store.save(expected_data)
        print "stored"

        index.put(expected_data[0],position,store)
        print "indexed"


        returned_data=index.get(expected_data[0], store)
        print "retrieved data: "+str(returned_data)
        self.assertEqual(expected_data, returned_data[1])

    def test_delete(self):

        dictConfig(config.logging_config)
        logger = logging.getLogger()

        expected_data = ("new super data","super new old stuff")

        table = Table("testdb","test_table","test_xcvzdfsadx")

        store = Store(table,config,logger)
        index = Index(table,config,logger)


        position=store.save(expected_data)
        print "stored"

        index.put(expected_data[0],position,store)
        print "indexed"

        index.delete(expected_data[0],store)

        returned_data=index.get(expected_data[0], store)
        print "retrieved data: "+str(returned_data)
        self.assertEqual(None, returned_data)

    def test_indexer(self):

        dictConfig(config.logging_config)
        logger = logging.getLogger()

        expected_data = ("new super data","super new old stuff")

        table = Table("testdb","test_table","test_xcvzdfsadx")

        store = Store(table,config,logger)
        indexer = Indexer(table,config,logger)

        position=store.save(expected_data)
        print "stored"

        indexer.put(expected_data[0],position,store)
        print "indexed by indexer"

        indexer.delete(expected_data[0],store)

        returned_data=indexer.get(expected_data[0], store)
        print "indexer retrieved data: "+str(returned_data)
        self.assertEqual(None, returned_data)

    def test_zzz_after_all_tests(self):
        shutil.rmtree("/tmp/"+DIR_NAME)
        print "*** deleted test data."

if __name__ == '__main__':
    unittest.main()
