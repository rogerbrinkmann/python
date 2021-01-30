from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import logging
import random
from itertools import count

build_id_generator = count(1234, 1)
ts_build_id_generator = count(4567, 1)

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)


def await_build():
    # polling the result of the build
    time.sleep(random.random() * 10)
    return random.choice((True, False))


def build_ts(data):
    # start a build of the test suite with specific test suite branch
    return next(ts_build_id_generator)


def start_build(data):
    # start a build of specific branch
    data["BuildId"] = next(build_id_generator)
    return data


def build_app(data):

    logging.info(f"Starting Build for {data['Name']}")
    build_data = start_build(data)
    logging.info(f"Build {data['Name']} with Id {build_data['BuildId']} started.")
    if await_build():
        logging.info(f"Build {data['Name']} completed successfully")
        logging.info(f"Starting TS Build with Parameter {data['Param1']}")
        return build_ts(data)
    else:
        logging.info(f"Build {data['Name']} failed, aborting")



if __name__ == "__main__":

    builds = [
        {"Name": "B1", "Param1": "A"},
        {"Name": "B2", "Param1": "B"},
        {"Name": "B3", "Param1": "C"},
        {"Name": "B4", "Param1": "D"},
        {"Name": "B5", "Param1": "E"},
    ]    

    # execute the builds, 
    # max_worker=1 -> all will execute consecutively
    # max_worker=10 -> all will execute parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(build_app, data) for data in builds]

        results = [future.result() for future in as_completed(futures)]
        for result in results:
            if result:
                logging.info(f"Test Suite and auto test running for TS Build Id: {result}" )


        