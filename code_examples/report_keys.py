import yaml


def get_all_keys(yaml_file):
    with open(yaml_file) as f:
        data = yaml.safe_load(f)

    def _get_all_keys(data, indent_level=0):
        for key, value in data.items():
            yield "    " * indent_level + key
            if isinstance(value, dict):
                yield from _get_all_keys(value, indent_level + 1)
            else:
                yield

    return list(_get_all_keys(data))


if __name__ == "__main__":
    yaml_file = "generated-schema/mixs_6_2_rc.yaml"
    keys = get_all_keys(yaml_file)

    print("Keys:")
    for key in keys:
        print(key)
