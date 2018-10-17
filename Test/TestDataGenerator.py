import csv
import logging
import random
import time

from DBHandlers.WellDAO import WellDAO

logger = logging.getLogger(__name__)

# TODO Fix the saving to take the address of this folder so it doesnt save data in other locations when called
class DataGenerator:
    """
        A Data Generator class, that uses a count value to generate that amount of test data to be used
        with test readings from wells specified in UUID List provided to the class
    """

    def __init__(self):
        logger.info("Init Data Generator")
        self.__count = 10000
        self.__uuid_list = []
        self.__name = "testData"

    def set_count(self, count):
        """
            Set the number of Test data to be generated when Generate method is executed
        :param count: Number of Test data sets
        """
        if isinstance(count, int):
            self.__count = count

    def set_uuid_list(self, uuids):
        """
            Set the list of UUID for the wells that will be used to generate test data
        :param uuids: List of Well UUIDs
        """
        if isinstance(uuids, list):
            self.__uuid_list = uuids

    def set_name(self, name):
        """
            Set the name of the generated files when the Generate method is executed

        :type name: string without extensions
        :param name: Name of the generated files
        """
        self.__name = name

    def generator(self):
        """

        :return:
        """
        # Get Random generator
        rand = random
        rows = []
        UUIDs = self.__uuid_list
        # Construct a list of reading data
        for i in range(self.__count):
            rows.append(dict(UUID=UUIDs[rand.randint(0, len(UUIDs) - 1)], raw=round(rand.uniform(2, 200), 3)))

        # Convert the Testing data to csv
        with open("test.csv", "w", newline='') as csvfile:
            fieldnames = ['UUID', 'raw']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for row in rows:
                writer.writerow(row)

        # convert Data into code (Might be used with the arduino to test I2C)
        u = "String UUID[] = {\n"
        r =  "double readings[] = {\n"
        for row in rows:
            one = str(row["UUID"])
            two = str(row["raw"])
            u += '\t\t"' + one + '",\n'
            r += "\t\t" + two + ",\n"
        u += "}"
        r += "}"

        # Save Generated Code to text file
        with open("array.txt", "w") as outfile:
            outfile.write(u)
            outfile.write("\n\n")
            outfile.write(r)


if __name__ == "__main__":
    well_dao = WellDAO()
    well_list = well_dao.read_all()
    UUID_list = [x.get_well_id() for x in well_list]
    # UUID_list = [
    #     "ALGFSD-WERTFD",
    #     "BPFBDL-AFNALK",
    #     "CDGDSK-SDKJNS",
    #     "DDFSDK-OJIORG",
    #     "EOWFDS-DSKNNK"
    # ]
    gen = DataGenerator()
    gen.set_count(1000000)
    gen.set_uuid_list(UUID_list)
    start = time.time()
    gen.generator()
    end = time.time()
    print("Elapsed :> {}".format(end - start))
