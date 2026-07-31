"""Check that the MIxS artifacts published at w3id.org describe the same schema.

These three URLs are what outside consumers use. EBI OLS and BioPortal follow them,
and they are the addresses given out in issue 1006. They are served by separate
redirects, so nothing guarantees they agree, and on 2026-07-30 they did not:
mixs.yaml and mixs.schema.json both declared version 7.0.0 while describing 344
and 335 container slots respectively.

This checks the published surface rather than the repository, because every
in-repo proxy tried so far has missed something. Run it after a release, or any
time you want to know what consumers are actually getting.

    make check-published
    poetry run python src/scripts/check_published_consistency.py
    poetry run python src/scripts/check_published_consistency.py --ref v7.0.0

The --ref option checks a git tag's raw URLs instead of the w3id ones, which is
how to confirm a release is self-consistent before repointing anything at it.
"""

import argparse
import json
import re
import sys
import urllib.request

import yaml

W3ID = {
    "mixs.yaml": "https://w3id.org/mixs/mixs.yaml",
    "mixs.schema.json": "https://w3id.org/mixs/mixs.schema.json",
    "mixs.owl.ttl": "https://w3id.org/mixs/mixs.owl.ttl",
}

RAW = "https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/{ref}/{path}"
RAW_PATHS = {
    "mixs.yaml": "src/mixs/schema/mixs.yaml",
    "mixs.schema.json": "project/jsonschema/mixs.schema.json",
    "mixs.owl.ttl": "project/owl/mixs.owl.ttl",
}

CONTAINER = "MixsCompliantData"


def fetch(url):
    with urllib.request.urlopen(url, timeout=120) as response:
        return response.read().decode("utf-8")


def read_yaml(text):
    schema = yaml.safe_load(text)
    container = schema["classes"][CONTAINER]["slots"]
    class_uris = {
        definition["class_uri"]
        for definition in schema["classes"].values()
        if isinstance(definition, dict) and definition.get("class_uri")
    }
    return {
        "version": str(schema.get("version")),
        "containers": len(container),
        "class_uris": class_uris,
    }


def read_json_schema(text):
    schema = json.loads(text)
    container = schema.get("$defs", {}).get(CONTAINER, {}).get("properties", {})
    return {
        "version": str(schema.get("version")),
        "containers": len(container),
        "class_uris": None,  # the JSON Schema carries no class_uri values
    }


def read_owl(text):
    match = re.search(r'pav:version\s+"([^"]+)"', text)
    subjects = set(re.findall(r"^MIXS:(\S+) a owl:Class", text, flags=re.MULTILINE))
    return {
        "version": match.group(1) if match else None,
        "containers": None,  # the OWL does not model the container class
        "class_uris": {f"MIXS:{s}" for s in subjects},
    }


READERS = {
    "mixs.yaml": read_yaml,
    "mixs.schema.json": read_json_schema,
    "mixs.owl.ttl": read_owl,
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ref",
        help="check a git ref's raw URLs instead of the published w3id URLs",
    )
    args = parser.parse_args()

    urls = (
        {name: RAW.format(ref=args.ref, path=path) for name, path in RAW_PATHS.items()}
        if args.ref
        else dict(W3ID)
    )

    read = {}
    for name, url in urls.items():
        print(f"fetching {url}")
        read[name] = READERS[name](fetch(url))

    print()
    print(f"{'artifact':20} {'version':10} {'container slots':>16} {'class_uris':>11}")
    for name, facts in read.items():
        containers = facts["containers"]
        class_uris = facts["class_uris"]
        print(
            f"{name:20} {str(facts['version']):10} "
            f"{'-' if containers is None else containers:>16} "
            f"{'-' if class_uris is None else len(class_uris):>11}"
        )
    print()

    failures = []

    versions = {name: facts["version"] for name, facts in read.items()}
    if len(set(versions.values())) > 1:
        failures.append(
            "the three artifacts declare different versions: "
            + ", ".join(f"{n} says {v}" for n, v in versions.items())
        )

    counts = {n: f["containers"] for n, f in read.items() if f["containers"] is not None}
    if len(set(counts.values())) > 1:
        failures.append(
            f"they disagree about how many container slots {CONTAINER} has: "
            + ", ".join(f"{n} has {c}" for n, c in counts.items())
            + ". A consumer validating against one and reading the other sees "
            "different submittable extensions."
        )

    schema_uris = read["mixs.yaml"]["class_uris"]
    owl_uris = read["mixs.owl.ttl"]["class_uris"]
    missing = sorted(schema_uris - owl_uris)
    if missing:
        failures.append(
            f"{len(missing)} class_uri values in the schema are absent from the "
            f"published OWL, so they resolve to nothing: {', '.join(missing[:8])}"
            + (" ..." if len(missing) > 8 else "")
        )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print()
        print(
            "These URLs are what EBI OLS, BioPortal and other consumers read. "
            "Disagreement between them means MIxS is publishing two different "
            "schemas under one version number."
        )
        return 1

    print("The published artifacts agree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
