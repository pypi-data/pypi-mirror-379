from ligo.gracedb.rest import GraceDb
#from gwtc.gwtc_gracedb import GWTCGraceDB
from .gwtc import smap_from_gracedb_query
import logging
from optparse import OptionParser
import json

# setup verbose logs
logging.basicConfig(level=logging.INFO)


def parse_command_line():
    parser = OptionParser(usage="usage: %prog [options] query")
    parser.add_option(
        "--service-url",
        type="string",
        default="https://gracedb-test.ligo.org/api/",
        help="Set the gracedb service url. Default: https://gracedb-test.ligo.org/api/",
    )
    parser.add_option(
        "--number", type="str", help='Set the catalog number (required)'
    )
    options, query = parser.parse_args()

    if options.number is None:
        parser.error("--number is required")

    return options, query


def main():
    options, query = parse_command_line()

    client = GraceDb(service_url=options.service_url)
    query = query[0].replace("\\", " ")

    smap = smap_from_gracedb_query(client, query)

    resp = client.gwtc_create(smap, number=options.number)
    logging.info(f"Created GWTC:\n{json.dumps(resp.json(), indent=4)}")
