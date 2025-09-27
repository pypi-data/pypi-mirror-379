#!/usr/bin/env python3
from gwtc.gwtc_gracedb import GWTCGraceDB
import logging
from optparse import OptionParser
import json

logging.basicConfig(level=logging.INFO)


def parse_command_line():
    parser = OptionParser(
        usage="usage: %prog [options] version\n\n"
        "Revert a GWTC catalog to a previous version by creating a new version "
        "with the contents of the specified version."
    )
    parser.add_option(
        "--number",
        type="string",
        help="Set the catalog number (required)",
    )
    parser.add_option(
        "--service-url",
        type="string",
        default="https://gracedb-test.ligo.org/api/",
        help="Set the gracedb service url. Default: https://gracedb-test.ligo.org/api/",
    )
    parser.add_option(
        "--comment",
        type="string",
        help="Optional comment to accompany the revert",
    )
    parser.add_option(
        "--dry-run",
        action="store_true",
        help="Show what would be reverted without actually creating a new version",
    )
    options, args = parser.parse_args()

    if options.number is None:
        parser.error("--number is required")

    if len(args) != 1:
        parser.error("You must specify exactly one version number to revert to")

    try:
        version = int(args[0])
    except ValueError:
        parser.error(f"Version must be an integer, got: {args[0]}")

    if version <= 0:
        parser.error(f"Version must be a positive integer, got: {version}")

    return options, version


def main():
    options, revert_to_version = parse_command_line()

    client = GWTCGraceDB(service_url=options.service_url)

    logging.info(
        f"Retrieving catalog {options.number} version {revert_to_version} to revert to..."
    )
    try:
        target_catalog = client.gwtc_get(options.number, revert_to_version).json()
    except Exception as e:
        logging.error(f"Failed to retrieve catalog version {revert_to_version}: {e}")
        return 1

    smap = target_catalog["gwtc_superevents"]
    logging.info(
        f"Retrieved version {revert_to_version} with {len(smap)} superevents"
    )

    current_catalog = client.gwtc_get(options.number, "latest").json()
    current_version = current_catalog["version"]
    logging.info(f"Current catalog version is {current_version}")

    if current_version == revert_to_version:
        logging.warning(
            f"Catalog is already at version {revert_to_version}. Nothing to do."
        )
        return 0

    if current_version < revert_to_version:
        logging.warning(
            f"Target version {revert_to_version} is newer than current version {current_version}. "
            "This is not a revert operation."
        )

    comment = options.comment or f"Revert to version {revert_to_version}"

    if options.dry_run:
        logging.info("DRY RUN: Would create new version with the following smap:")
        logging.info(json.dumps(smap, indent=4))
        logging.info(f"Comment: {comment}")
        logging.info(
            f"This would create version {current_version + 1} of catalog {options.number}"
        )
        return 0

    logging.info(f"Creating new catalog version with contents from version {revert_to_version}...")
    resp = client.gwtc_create(smap, number=options.number, comment=comment)
    new_catalog = resp.json()
    logging.info(
        f"Successfully created version {new_catalog['version']} "
        f"(reverted from version {revert_to_version})"
    )
    logging.info(f"Full response:\n{json.dumps(new_catalog, indent=4)}")

    return 0


if __name__ == "__main__":
    exit(main())