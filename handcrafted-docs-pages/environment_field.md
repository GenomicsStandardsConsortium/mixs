# environment field

## Definition:

- field describing environmental aspect of a sample

---

### _Questions_

- _what will this page's URL be?_
- _no asserted ancestors in this case_
- _do we want to mention the `from_schema`, `source`, or whatever? Maybe I have been using `source` wrong in NMDC?_
- _do we want to mention that this slot is abstract, or have a different template for abstract slots?_

## Children

- alt
- collection_date
- [depth](depth.md)
- elev
- env_broad_scale
- env_local_scale
- env_medium
- geo_loc_name
- lat_lon
- temp

## YAML Source

```yaml
  environment field:
    name: environment field
    description: field describing environmental aspect of a sample
    from_schema: http://w3id.org/mixs
    abstract: true
```