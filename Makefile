# document installation of poetry application and `poetry install`

RUN=poetry run

#.PHONY: all clean gh_docs docserve
#
## html_docs
#all: clean generated/mixs.py mkdocs_html/index.html
#
## ---------------------------------------
## TSVs from google drive
## ---------------------------------------
## for seeding
#
#clean:
#	#rm -rf downloads/*tsv
#	rm -rf generated/*
#	rm -rf logs/*
#	rm -rf mkdocs_html/
#	#rm -rf model/schema/*yaml
#
##model/schema/mixs.yaml: downloads/mixs6.tsv downloads/mixs6_core.tsv
##	$(RUN) python -m gsctools.mixs_converter  2>&1 | tee -a logs/sheet2linkml.log
##
##downloads/mixs6.tsv:
##	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=tsv&gid=750683809' > $@
##downloads/mixs6_core.tsv:
##	curl -L -s 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?format=tsv&gid=178015749' > $@
#
## todo add owl back in and make it awesome
## todo derive output path from target file name
## 		--exclude owl \
#
#generated/mixs.py: model/schema/mixs.yaml
#	$(RUN) gen-project \
#		--exclude java \
#		--exclude markdown \
#		--dir $(dir $@) $< 2>&1 | tee -a logs/linkml_artifact_generation.log
#
## 		--exclude excel \
#
##	mkdir generated/excel
##	$(RUN) gen-excel --output generated/excel/mixs.xlsx $<
##	# skipping jinja --template_file
##	mkdir generated/java
##	$(RUN) gen-java --package mixs --output_directory generated/java $<
#
### ---------------------------------------
### MARKDOWN DOCS
###      Generate documentation ready for mkdocs
### ---------------------------------------
### For help with mkdocs see https://www.mkdocs.org/.
#
#generated/docs/index.md: model/schema/mixs.yaml generated/mixs.py
#	$(RUN) gen-doc $< --directory $(dir $@) --template-directory doc_templates --use-slot-uris
#
#generated/docs/introduction/%.md: generated/docs/index.md
#	cp -R static_md/* $(dir $@)
#
## add more logging?
## some docs pages not being created
## usage of schemasheets_mkdocs.yml attributes like analytics?
#
#mkdocs_html/index.html: generated/docs/index.md
#	poetry run mkdocs build
#
## test docs locally.
## repeats build
#docserve:
#	$(RUN) mkdocs serve
#
## repeats build
## pushes to gh-pages branch
## exposes at https://GenomicsStandardsConsortium.github.io/mixs/
#gh_docs:
#	poetry run mkdocs gh-deploy

# ---------------------------------------

.PHONY: schemasheets_clean schemasheets_all validation_expected_pass validation_missing validation_extra bare_jsonschema

schemasheets_all: \
schemasheets_clean \
schemasheets/yaml_out/mixs_schemasheets.yaml \
schemasheets/logs/mixs_schemasheets_linting_log.tsv \
schemasheets/generated/mixs_schemasheets_generated.yaml \
schemasheets/generated/mixs_schemasheets_generated.sql \
validation_expected_pass validation_missing validation_extra bare_jsonschema \
schemasheets/example_data/out/mims_soil_set_database.json \
schemasheets/example_data/out/mims_soil_set_database.tsv \
schemasheets/example_data/out/mims_soil_set_database.ttl \
schemasheets/example_data/out/mims_soil_set_database.yaml \
schemasheets/mkdocs_html/index.md \
schemasheets/example_data/out/mims_soil_set_database.db

# todo slow
#   schemasheets/example_data/out/mixs_database.db \

# this could be a circular dependency
# silently depends on schemasheets/yaml_out/mixs_schemasheets.yaml
# but also prepares schemasheets/tsv_in/generated/mixs_combination_classes.tsv
# which will be one of the inputs into generating schemasheets/yaml_out/mixs_schemasheets.yaml
# so don't put into schemasheets_all
schemasheets/tsv_in/generated/mixs_combination_classes.tsv:
	$(RUN) python gsctools/gen_mixs_combination_classes.py

schemasheets_clean:
	rm -rf schemasheets/example_data/out/*
	rm -rf schemasheets/generated/*
	rm -rf schemasheets/generated/gen_docs_docs/*
	rm -rf schemasheets/logs/*
	rm -rf schemasheets/mkdocs_html/*
	rm -rf schemasheets/yaml_out/*
	mkdir -p schemasheets/example_data/out

schemasheets/yaml_out/mixs_schemasheets.yaml: \
schemasheets/tsv_in/MIxS_6_term_updates_classdefs.tsv \
schemasheets/tsv_in/MIxS_6_term_updates_partial_slotdefs_more_constraints.tsv \
schemasheets/tsv_in/MIxS_6_term_updates_slot_assignments.tsv \
schemasheets/tsv_in/generated/mixs_combination_classes.tsv \
schemasheets/tsv_in/mixs_clear_cut_enums.tsv \
schemasheets/tsv_in/mixs_prefixes.tsv \
schemasheets/tsv_in/mixs_schema_annotations.tsv \
schemasheets/tsv_in/mixs_subsets.tsv \
schemasheets/tsv_in/mixs_utility.tsv
	$(RUN) sheets2linkml --output $@ $^


# --fix / --no-fix
# see https://github.com/linkml/linkml/blob/main/linkml/linter/config/default.yaml
# enum names should be upper camel case
schemasheets/logs/mixs_schemasheets_linting_log.tsv: schemasheets/yaml_out/mixs_schemasheets.yaml
	- $(RUN) linkml-lint \
		--format tsv \
		--output $@ $< \
		--config schemasheets/configs/linter_config_default.yaml

#		--ignore-warnings

# todo capture log?
#  isn't merging imports
schemasheets/generated/mixs_schemasheets_generated.yaml: schemasheets/yaml_out/mixs_schemasheets.yaml
	$(RUN) gen-linkml \
		--format yaml  \
		--no-materialize-attributes \
		--output $@ $<

# todo capture log?
# todo excel artifact has duplicate tabs (with numerical suffixes)
#  but explore whether this would be a useful data collection tool
#  also slow
# markdown generation slow but may reveal subtle problems
# shacl slowish
schemasheets/generated/%: \
schemasheets/generated/mixs_schemasheets_generated.yaml
	$(RUN) gen-project \
		--exclude excel \
		--exclude markdown \
		--dir schemasheets/generated $<

# this doesn't generate the left hand navigation or the index page
schemasheets/generated/gen_docs_docs/index.md: schemasheets/yaml_out/mixs_schemasheets.yaml
	$(RUN) gen-doc $< --directory $(dir $@) --template-directory doc_templates --use-slot-uris

schemasheets/mkdocs_html/index.md: schemasheets/generated/gen_docs_docs/index.md
	cp -R static_md/* $(dir $<)
	$(RUN) mkdocs build --config-file schemasheets_mkdocs.yml
	# then `make schemasheets_docserve` and or `make schemasheets_gh_docs` if desired

schemasheets_docserve:
	$(RUN) mkdocs serve --config-file schemasheets_mkdocs.yml


validation_expected_pass: \
schemasheets/generated/mixs_schemasheets_generated.yaml schemasheets/example_data/in/mims_soil_set_database.yaml
	$(RUN) linkml-validate \
		--target-class Database \
		--schema $^

validation_missing: \
schemasheets/generated/mixs_schemasheets_generated.yaml schemasheets/example_data/in/mims_soil_set_database_missing.yaml
	! $(RUN) linkml-validate \
		--target-class Database \
		--schema $^

validation_extra: \
schemasheets/generated/mixs_schemasheets_generated.yaml schemasheets/example_data/in/mims_soil_set_database_extra.yaml
	! $(RUN) linkml-validate \
		--target-class Database \
		--schema $^

# CONVERSION TARGETS
#csv/tsv (writes TSV no matter what)
#json
#json-ld
#rdf/ttl
#yml/yaml

schemasheets/example_data/out/mims_soil_set_database.json: \
schemasheets/generated/mixs_schemasheets_generated.yaml \
schemasheets/example_data/in/mims_soil_set_database.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class Database \
		--schema $^

bare_jsonschema: \
schemasheets/example_data/out/mims_soil_set_database.json \
schemasheets/generated/jsonschema/mixs_schemasheets_generated.schema.json
	$(RUN) jsonschema -i $^

# todo slow
schemasheets/example_data/out/mims_soil_set_database.db: \
schemasheets/generated/mixs_schemasheets_generated.yaml \
schemasheets/example_data/out/mims_soil_set_database.json
	date
	$(RUN) linkml-sqldb dump --db $@ --target-class Database --schema $^
	date
	sqlite3 $@ ".header on" "select * from SoilMims"


# sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) NOT NULL constraint failed: MimsSoil.project_name
  #[SQL: INSERT INTO "MimsSoil" (adapters, alt, annot, assembly_name, assembly_qual, assembly_software, collection_date, depth, elev, env_broad_scale, env_local_scale, env_medium, experimental_factor, feat_pred, geo_loc_name, lat_lon, lib_layout, lib_reads_seqd, lib_screen, lib_size, lib_vector, mid, neg_cont_type, nucl_acid_amp, nucl_acid_ext, number_contig, pos_cont_type, project_name, ref_biomaterial, ref_db, rel_to_oxygen, samp_collec_device, samp_collec_method, samp_mat_process, samp_name, samp_size, samp_taxon_id, samp_vol_we_dna_ext, seq_meth, sim_search_meth, size_frac, tax_class, "temp", al_sat, al_sat_meth, annual_precpt, annual_temp, crop_rotation, cur_land_use, cur_vegetation, cur_vegetation_meth, drainage_class, extreme_event, fao_class, fire, flooding, heavy_metals_meth, horizon_meth, link_addit_analys, link_class_info, link_climate_info, local_class, local_class_meth, micro_biomass_meth, microbial_biomass, org_matter, org_nitro, ph, ph_meth, pool_dna_extracts, prev_land_use_meth, previous_land_use, profile_position, salinity_meth, season_precpt, season_temp, sieving, slope_aspect, slope_gradient, soil_horizon, soil_text_measure, soil_texture_meth, soil_type, soil_type_meth, store_cond, tot_nitro_cont_meth, tot_nitro_content, tot_org_c_meth, tot_org_carb, water_cont_soil_meth, water_content, "Database_id") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)]
  #[parameters: (None, None, None, None, None, None, '2018-05-11 10:00:00+01:00', None, None, 'oceanic epipelagic zone biome [ENVO:01000033]', 'litter layer [ENVO:01000338]', 'soil [ENVO:00001998]', None, None, 'USA: Maryland, Bethesda', '50.586825 6.408977', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'minimal', None, 'Gut Metagenome [NCBI:txid749906]', None, '454 Genome Sequencer FLX [OBI:0000702]', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 1)]
  #(Background on this error at: https://sqlalche.me/e/14/gkpj)
  #make: *** [schemasheets/example_data/out/mixs_database.db] Error 1

# but then why does the validation/conversion on MimsSoils lacking project_names work?

schemasheets/example_data/out/mims_soil_set_database.ttl: \
schemasheets/generated/mixs_schemasheets_generated.yaml \
schemasheets/example_data/in/mims_soil_set_database.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class Database \
		--index-slot mims_soil_set \
		--schema $^

# WARNING:root:Index slot range not to class: None
schemasheets/example_data/out/mims_soil_set_database.tsv: \
schemasheets/yaml_out/mixs_schemasheets.yaml \
schemasheets/example_data/in/mims_soil_set_database.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class Database \
		--index-slot mims_soil_set \
		--schema $^

schemasheets/example_data/out/mims_soil_set_database.yaml: \
schemasheets/yaml_out/mixs_schemasheets.yaml \
schemasheets/example_data/out/mims_soil_set_database.tsv
	$(RUN) linkml-convert \
		--output $@ \
		--target-class Database \
		--index-slot mims_soil_set \
		--schema $^

# GENERAL NOTES
# added xsd prefix for converting non-string values to rdf/ttl
# date_or_datetime not implemented yet, and might have some disadvantageous
# datetime ranges incompatible with sqlite dump
# expected problems with enum/pv names/texts
# gen-linkml not merging (for example the "free" linkml:types
# may not be possible to convert to or from csv or tsv due to multivalued slots (even if they're not populated?!)
# multivalued slots with scalar values might be repaired in some situations but don't count on it
# no good regex for lat_lon?
# what patterns in the schema or data break which tools?
# schemasheets will compile sheets containing slots whose names start with digits
#   generators don't complain either
#   but the jsonschema utility won't validate against the generated jsonschema
