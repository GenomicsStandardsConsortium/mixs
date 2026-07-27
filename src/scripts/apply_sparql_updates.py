"""Apply SPARQL UPDATE files to an OWL/Turtle file in place.

Used to post-process the generated MIxS OWL for ontology tools (EBI OLS): see
``src/sparql/ols/``. Kept as SPARQL files plus this thin runner so each
customization is reviewable on its own and the build has no Java (ROBOT)
dependency; rdflib is already a project dependency.

Usage:
    apply-sparql-updates --owl project/owl/mixs.owl.ttl --sparql-dir src/sparql/ols
"""

from pathlib import Path

import click
from rdflib import Graph


@click.command()
@click.option(
    "--owl",
    "owl_path",
    required=True,
    type=click.Path(exists=True, dir_okay=False),
    help="Turtle OWL file to update in place.",
)
@click.option(
    "--sparql-dir",
    required=True,
    type=click.Path(exists=True, file_okay=False),
    help="Directory of SPARQL UPDATE (*.ru) files, applied in sorted order.",
)
def main(owl_path: str, sparql_dir: str) -> None:
    """Apply every ``*.ru`` in ``--sparql-dir`` to ``--owl`` and rewrite it."""
    graph = Graph()
    graph.parse(owl_path, format="turtle")
    updates = sorted(Path(sparql_dir).glob("*.ru"))
    if not updates:
        raise click.ClickException(f"no *.ru files in {sparql_dir}")
    # Feed the ontology's own prefixes to update() so PName resolution works across
    # every operation. rdflib does not propagate a request's PREFIX prologue to the
    # later `;`-separated operations, which otherwise fails on e.g. `mixs:`.
    init_ns = dict(graph.namespaces())
    # The OWL binds the MIxS namespace as `MIXS`; also expose lowercase aliases so
    # updates can use conventional prefixes like `mixs:`.
    for prefix, uri in list(init_ns.items()):
        init_ns.setdefault(prefix.lower(), uri)
    for update in updates:
        before = len(graph)
        graph.update(update.read_text(), initNs=init_ns)
        click.echo(f"applied {update.name}: {before} -> {len(graph)} triples")
    graph.serialize(destination=owl_path, format="turtle")


if __name__ == "__main__":
    main()
