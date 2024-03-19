import click
import pandas as pd
from scipy.spatial.distance import pdist, squareform
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

from linkml_runtime import SchemaView


@click.command()
@click.option('--schema', '-s',
              default='src/mixs/schema/mixs.yaml',
              required=True,
              help='Path to the schema file')
@click.option('--output', '-o', default='dendrogram.pdf',
              help='Output file name for the dendrogram plot (default: dendrogram.pdf)')
def generate_dendrogram(schema, output):
    schema_view = SchemaView(schema)

    extension_class_names = schema_view.class_descendants('Extension')
    checklist_class_names = schema_view.class_descendants('Checklist')

    lod = []

    for current_extension in extension_class_names:
        if current_extension in checklist_class_names:
            continue
        extension_obj = schema_view.induced_class(current_extension)

        extension_slots = list(extension_obj.attributes.keys())
        for current_slot in extension_slots:
            temp_dict = {
                "extension": current_extension,
                "slot": current_slot
            }
            lod.append(temp_dict)

    df = pd.DataFrame(lod)

    pivot_df = df.pivot(index='extension', columns='slot', values='slot').notna()

    dist_matrix = pdist(pivot_df.values, metric='euclidean')
    dist_matrix_square = squareform(dist_matrix)

    linkage_matrix = hierarchy.linkage(dist_matrix, method='complete')

    plt.figure(figsize=(14, 8))
    dendrogram = hierarchy.dendrogram(linkage_matrix, labels=pivot_df.index.values, orientation='top')
    plt.title('Similarity of MIxS Extensions by Term Usage')
    plt.ylabel('Distance')
    plt.xlabel('Extensions')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig(output, format='pdf')
    plt.show()


if __name__ == '__main__':
    generate_dendrogram()
