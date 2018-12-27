import logging
import firebase_admin
import sys
from firebase_admin import credentials
from firebase_admin import firestore
from pprint import pprint
from DBHandlers import WellDAO
from DBHandlers.WellDAO import WellDAO

import os

from Models.Well import Well
from pathlib import Path

path = Path(__file__).parent

logger = logging.getLogger(__name__)


class CloudConnect:
    def __init__(self):
        """
            Initiate the connection to the cloud database

            *Reads the Certificate
            *Init connection to the firebase_admin
            *Create a firestore client
        """
        logger.info("Init Cloud Connection")
        cred = credentials.Certificate(
            str(path / "waterlevelmonitoringsyst-3ca70-firebase-adminsdk-u40sf-09a38a7e8f.json"))
        if (not len(firebase_admin._apps)):
            firebase_admin.initialize_app(cred, {
                'projectId': u"waterlevelmonitoringsyst-3ca70",
            })
        self.db = firestore.client()

    def save_well(self, well):
        logger.info("Persisting well to cloud")
        try:
            self.db.collection(u"Well-Nodes").document(u"Well_{}".format(well.get_well_id())).set(well.to_dict())
        except:
            logger.error("Failed to save Well to cloud\n {}".format(sys.exc_info()))
            return False
        logger.info("Save to cloud was successful")
        return True

    def read_well(self, well_id):
        logger.info("Read from cloud well with id = {}".format(well_id))
        read_ref = self.db.collection(u'Well-Nodes').document(u"Well_{}".format(well_id))
        reads = read_ref.get()
        reads = reads.to_dict()
        try:
            well = Well(well_id, reads['Area'], reads['Height'], reads['Offset'])
            logger.debug("Read from the cloud \n {}".format(well))
        except:
            logger.error("Failed to read from cloud. \n {}".format(sys.exc_info()))
            return False
        return well

    def read_all_wells(self):
        logger.info("Reading all well values from the cloud")
        well_list = []
        try:
            wells = self.db.collection(u"Well-Nodes").get()
            for well in wells:
                well_list.append(Well(well.id.split("_")[1], well.get("Area"), well.get("Height"), well.get("Offset")))
            logger.debug(well_list)
        except:
            logger.error("Failed to read wells from cloud.\n{}".format(sys.exc_info()))
            return False
        return well_list

    def save_reading(self, wellReading):
        logger.info("Persisting Reading to the cloud")
        try:
            well_ref = self.db.collection("Well-Nodes").document("Well_{}".format(wellReading.get_well().get_well_id()))

            well_ref.collection('Readings').add(
                wellReading.to_dict()
            )
        except:
            logger.error("Failed to persist Reading to the database\n {}".format(sys.exc_info()))
            return False
        logger.info("Save to cloud was successful")
        return True

    def faults_increment_failed_transmit(self, id):
        logger.info("Persisting a transmission fault for well {}".format(id))
        try:
            fault_ref = self.db.collection("Well-Fault").document("Well_{}".format(id))
            if fault_ref.get()._exists:
                doc = fault_ref.get().to_dict()
                count = doc.get("transmission", 0)
                count = count + 1
                doc["transmission"] = count
                fault_ref.set(doc)
            else:
                fault_ref.set({'transmission': 1})

        except:
            logger.error("Failed to increment transmission fault")
            return False
        return True

    def faults_increment_failed_respond(self, id):
        logger.info("Persisting a reply fault for well {}".format(id))
        try:
            fault_ref = self.db.collection("Well-Fault").document("Well_{}".format(id))
            if fault_ref.get()._exists:
                doc = fault_ref.get().to_dict()
                count = doc.get("respond", 0)
                count = count + 1
                doc["respond"] = count
                fault_ref.set(doc)
            else:
                fault_ref.set({'respond': 1})
        except:
            logger.error("Failed to increment transmission fault")
            return False
        return True


if __name__ == "__main__":
    wellDao = WellDAO()
    wells = wellDao.read_all()
    pprint(wells)
    # con = CloudConnect(u"waterlevelmonitoringsyst-3ca70")
    # con.read_well(1)
