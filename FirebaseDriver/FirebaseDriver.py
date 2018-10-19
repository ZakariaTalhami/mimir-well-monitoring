import logging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pprint import pprint
from DBHandlers import WellDAO
from DBHandlers.WellDAO import WellDAO

import os

path = os.path.dirname(__file__)

logger = logging.getLogger(__name__)


class CloudConnect:
    def __init__(self):
        print(path)
        logger.info("Init Cloud Connect")
        cred = credentials.Certificate(
            "{}\waterlevelmonitoringsyst-3ca70-firebase-adminsdk-u40sf-8c0554975f.json".format(path))
        firebase_admin.initialize_app(cred, {
            'projectId': u"waterlevelmonitoringsyst-3ca70",
        })
        self.db = firestore.client()

    def save_well(self, well):
        logger.info("Persisting well to cloud")
        self.db.collection(u"Well-Nodes").document(u"Well_{}".format(well.get_well_id())).set({
            "Area": well.get_area(),
            "Height": well.get_height()
        })

        return True

    def read_well(self, well_id):
        logger.info("check database for well with id = {}".format(well_id))
        read_ref = self.db.collection(u'Well-Nodes')
        readings = read_ref.get()

        print(readings.to_dict())
        # for read in readings:
        #     print(u' {} -> {} '.format(read.id , read.to_dict()))

        return True

    def read_all_wells(self):
        logger.info("Reading all the well data from firebase")
        well_list = []
        return well_list

    def save_reading(self, wellReading):
        logger.info("Saving Reading to Database")
        well_ref = self.db.collection("Well-Nodes").document("Well_{}".format(wellReading.get_well().get_well_id()))
        well_ref.collection('Readings').add(
            {
                "Level": wellReading.get_level(),
                "Volume": wellReading.get_volume(),
                "Timestamp": wellReading.get_timestamp()
            }
        )
        return True


if __name__ == "__main__":
    wellDao = WellDAO()
    wells = wellDao.read_all()
    pprint(wells)
    # con = CloudConnect(u"waterlevelmonitoringsyst-3ca70")
    # con.read_well(1)
