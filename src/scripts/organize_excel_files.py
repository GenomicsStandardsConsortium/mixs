import os
import shutil
from collections import defaultdict
from linkml_runtime.utils.schemaview import SchemaView
import logging
import argparse


class MIxSExcelFileOrganizer:
    def __init__(self, mixs_schema_file, source_directory, base_destination_folder):
        self.mixs_schema_file = mixs_schema_file
        self.source_directory = source_directory
        self.base_destination_folder = base_destination_folder
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
        for extension_file in extensions:
            source_file = os.path.join(self.source_directory, f"{extension_file}.xlsx")
            destination_file = os.path.join(extensions_folder, f"{extension_file}.xlsx")

            if os.path.isfile(source_file):
                shutil.copy(source_file, destination_file)
            else:
                self.logger.warning(
                    f"File {extension_file}.xlsx not found in the source directory."
                )

        # Copy files based on 'result_list'
        for item in result_list:
            x_value = item["x"]
            folder_path = os.path.join(self.base_destination_folder, x_value)
            os.makedirs(f"{folder_path}_plus_combinations", exist_ok=True)

            for cls_name in item["cls_names"]:
                source_file = os.path.join(self.source_directory, f"{cls_name}.xlsx")
                destination_file = os.path.join(f"{folder_path}_plus_combinations", f"{cls_name}.xlsx")

                if os.path.isfile(source_file):
                    shutil.copy(source_file, destination_file)
                else:
                    self.logger.warning(
                        f"File {cls_name}.xlsx not found in the source directory."
                    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MIxS Excel File Organizer")
    parser.add_argument(
        "--mixs-schema-file",
        default="src/mixs/schema/mixs.yaml",
        help="Path to MIxS schema file",
    )
    parser.add_argument(
        "--source-directory",
        required=True,
        help="Path to the source directory containing XLSX files",
    )
    parser.add_argument(
        "--base-destination-folder",
        required=True,
        help="Path to the base destination folder",
    )

    args = parser.parse_args()

    mixs_organizer = MIxSExcelFileOrganizer(
        mixs_schema_file=args.mixs_schema_file,
        source_directory=args.source_directory,
        base_destination_folder=args.base_destination_folder,
    )
    mixs_organizer.organize_files()