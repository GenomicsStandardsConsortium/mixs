import os
import shutil
from collections import defaultdict
from linkml_runtime.utils.schemaview import SchemaView
import logging
import click

class MIxSFileOrganizer:
    def __init__(self, mixs_schema_file, source_directory, base_destination_folder, extensions):
        self.mixs_schema_file = mixs_schema_file
        self.source_directory = source_directory
        self.base_destination_folder = base_destination_folder
        self.extensions = extensions
        self.logger = self.setup_logger()

    def setup_logger(self):
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(__name__)

    def organize_files(self):
        sv = SchemaView(self.mixs_schema_file)

        checklists = [
            cls_name
            for cls_name, cls in sv.all_classes().items()
            if cls.is_a == "Checklist"
        ]
        extensions = [
            cls_name
            for cls_name, cls in sv.all_classes().items()
            if cls.is_a == "Extension"
        ]

        result_dict = defaultdict(list)

        for cls_name, cls in sv.all_classes().items():
            for x in checklists:
                if cls.is_a == x or x in cls.mixins:
                    result_dict[x].append(cls_name)

        result_list = [
            {"x": x, "cls_names": [x] + cls_names} for x, cls_names in result_dict.items()
        ]

        # Create a folder for extensions
        extensions_folder = os.path.join(self.base_destination_folder, "extensions_only")
        os.makedirs(extensions_folder, exist_ok=True)

        # Copy files with names in 'extensions' to the 'extensions' folder
        self.copy_files(extensions, extensions_folder)

        # Copy files based on 'result_list'
        for item in result_list:
            x_value = item["x"]
            folder_path = os.path.join(self.base_destination_folder, x_value)
            os.makedirs(f"{folder_path}_plus_combinations", exist_ok=True)

            self.copy_files(item["cls_names"], f"{folder_path}_plus_combinations")

    def copy_files(self, file_names, destination_folder):
        for file_name in file_names:
            for extension in self.extensions:
                source_file = os.path.join(self.source_directory, f"{file_name}.{extension}")
                destination_file = os.path.join(destination_folder, f"{file_name}.{extension}")

                if os.path.isfile(source_file):
                    shutil.copy(source_file, destination_file)
                else:
                    self.logger.warning(
                        f"File {file_name}.{extension} not found in the source directory."
                    )


@click.command()
@click.option(
    '--mixs-schema-file',
    default='src/mixs/schema/mixs.yaml',
    help='Path to MIxS schema file',
)
@click.option(
    '--source-directory',
    required=True,
    help='Path to the source directory containing files',
)
@click.option(
    '--base-destination-folder',
    required=True,
    help='Path to the base destination folder',
)
@click.option(
    '--extensions',
    required=True,
    multiple=True,
    help='File extensions to be organized (e.g., --extensions xlsx --extensions tsv)',
)
def main(mixs_schema_file, source_directory, base_destination_folder, extensions):
    mixs_organizer = MIxSFileOrganizer(
        mixs_schema_file=mixs_schema_file,
        source_directory=source_directory,
        base_destination_folder=base_destination_folder,
        extensions=extensions,
    )
    mixs_organizer.organize_files()


if __name__ == "__main__":
    main()
