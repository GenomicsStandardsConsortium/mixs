from linkml.utils.schema_builder import SchemaBuilder
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SchemaDefinition

schema_file = "model/schema/mixs.yaml"
complete_view = SchemaView(schema_file)

complete_view.merge_imports()

minimal_schema = SchemaDefinition(id=complete_view.schema.id, name=complete_view.schema.name)

minimal_schema.classes = complete_view.schema.classes

print(yaml_dumper.dumps(minimal_schema))
