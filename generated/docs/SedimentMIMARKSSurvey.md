
# Class: sediment MIMARKS survey


Combinatorial checklist Minimal Information about a Marker Specimen: survey with environmental package sediment

URI: [mixs.vocab:SedimentMIMARKSSurvey](https://w3id.org/mixs/vocab/SedimentMIMARKSSurvey)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SedimentMIMARKSSurvey&#124;submitted_to_insdc:string;investigation_type:investigation_type_enum;samp_taxon_id:string;experimental_factor:string%20%3F;neg_cont_type:neg_cont_type_enum%20%3F;pos_cont_type:string%20%3F;env_package:env_package_enum%20%3F;subspecf_gen_lin:string%20%3F;extrachrom_elements:integer%20%3F;source_mat_id:string%20%3F;biotic_relationship:biotic_relationship_enum%20%3F;trophic_level:trophic_level_enum%20%3F;rel_to_oxygen:rel_to_oxygen_enum%20%3F;isol_growth_condt:string;samp_collec_device:string%20%3F;samp_collec_method:string%20%3F;samp_mat_process:string%20%3F;nucl_acid_ext:string%20%3F;nucl_acid_amp:string%20%3F;target_gene:string;target_subfragment:string%20%3F;pcr_primers:string%20%3F;pcr_cond:string%20%3F;seq_meth:string;seq_quality_check:string%20%3F;chimera_check:string%20%3F;associated_resource:string%20%3F;sop:string%20%3F;lat_lon(i):string%20%3F;geo_loc_name(i):string%20%3F;collection_date(i):date%20%3F;env_broad_scale(i):string%20%3F;env_local_scale(i):string%20%3F;env_medium(i):string%20%3F;biomass(i):string%20*;chem_administration(i):string%20*;diether_lipids(i):string%20*;misc_param(i):string%20*;n_alkanes(i):string%20*;organism_count(i):organism_count_enum%20*;oxy_stat_samp(i):oxy_stat_samp_enum%20%3F;ph(i):double%20%3F;particle_class(i):string%20*;perturbation(i):string%20*;phaeopigments(i):string%20*;phosplipid_fatt_acid(i):string%20*;porosity(i):string%20%3F;samp_store_dur(i):string%20%3F;samp_store_loc(i):string%20%3F;sediment_type(i):sediment_type_enum%20%3F;tidal_stage(i):tidal_stage_enum%20%3F;samp_name(i):string;project_name(i):string]uses%20-.->[MIMARKSSurvey],[Sediment]^-[SedimentMIMARKSSurvey],[Sediment],[QuantityValue],[MIMARKSSurvey])](https://yuml.me/diagram/nofunky;dir:TB/class/[SedimentMIMARKSSurvey&#124;submitted_to_insdc:string;investigation_type:investigation_type_enum;samp_taxon_id:string;experimental_factor:string%20%3F;neg_cont_type:neg_cont_type_enum%20%3F;pos_cont_type:string%20%3F;env_package:env_package_enum%20%3F;subspecf_gen_lin:string%20%3F;extrachrom_elements:integer%20%3F;source_mat_id:string%20%3F;biotic_relationship:biotic_relationship_enum%20%3F;trophic_level:trophic_level_enum%20%3F;rel_to_oxygen:rel_to_oxygen_enum%20%3F;isol_growth_condt:string;samp_collec_device:string%20%3F;samp_collec_method:string%20%3F;samp_mat_process:string%20%3F;nucl_acid_ext:string%20%3F;nucl_acid_amp:string%20%3F;target_gene:string;target_subfragment:string%20%3F;pcr_primers:string%20%3F;pcr_cond:string%20%3F;seq_meth:string;seq_quality_check:string%20%3F;chimera_check:string%20%3F;associated_resource:string%20%3F;sop:string%20%3F;lat_lon(i):string%20%3F;geo_loc_name(i):string%20%3F;collection_date(i):date%20%3F;env_broad_scale(i):string%20%3F;env_local_scale(i):string%20%3F;env_medium(i):string%20%3F;biomass(i):string%20*;chem_administration(i):string%20*;diether_lipids(i):string%20*;misc_param(i):string%20*;n_alkanes(i):string%20*;organism_count(i):organism_count_enum%20*;oxy_stat_samp(i):oxy_stat_samp_enum%20%3F;ph(i):double%20%3F;particle_class(i):string%20*;perturbation(i):string%20*;phaeopigments(i):string%20*;phosplipid_fatt_acid(i):string%20*;porosity(i):string%20%3F;samp_store_dur(i):string%20%3F;samp_store_loc(i):string%20%3F;sediment_type(i):sediment_type_enum%20%3F;tidal_stage(i):tidal_stage_enum%20%3F;samp_name(i):string;project_name(i):string]uses%20-.->[MIMARKSSurvey],[Sediment]^-[SedimentMIMARKSSurvey],[Sediment],[QuantityValue],[MIMARKSSurvey])

## Parents

 *  is_a: [Sediment](Sediment.md) - sediment

## Uses Mixin

 *  mixin: [MIMARKSSurvey](MIMARKSSurvey.md) - Minimal Information about a Marker Specimen: survey

## Attributes


### Inherited from sediment:

 * [lat_lon](lat_lon.md)  <sub>0..1</sub>
     * Description: The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in WGS84 system
     * Range: [String](types/String.md)
     * Example: 50.586825 6.408977 None
 * [sediment➞depth](sediment_depth.md)  <sub>1..1</sub>
     * Description: The vertical distance below local surface, e.g. for sediment or soil samples depth is measured from sediment or soil surface, respectively. Depth can be reported as an interval for subsurface samples.
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 10 meter None
 * [alt](alt.md)  <sub>0..1</sub>
     * Description: Altitude is a term used to identify heights of objects such as airplanes, space shuttles, rockets, atmospheric balloons and heights of places such as atmospheric layers and clouds. It is used to measure the height of an object which is above the earth's surface. In this context, the altitude measurement is the vertical distance between the earth's surface above sea level and the sampled position in the air
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 100 meter None
 * [sediment➞elev](sediment_elev.md)  <sub>0..1</sub>
     * Description: Elevation of the sampling site is its height above a fixed reference point, most commonly the mean sea level. Elevation is mainly used when referring to points on the earth's surface, while altitude is used for points above the surface, such as an aircraft in flight or a spacecraft in orbit.
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 100 meter None
 * [sediment➞temp](sediment_temp.md)  <sub>0..1</sub>
     * Description: Temperature of the sample at the time of sampling.
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 25 degree Celsius None
 * [geo_loc_name](geo_loc_name.md)  <sub>0..1</sub>
     * Description: The geographical origin of the sample as defined by the country or sea name followed by specific region name. Country or sea names should be chosen from the INSDC country list (http://insdc.org/country.html), or the GAZ ontology (http://purl.bioontology.org/ontology/GAZ)
     * Range: [String](types/String.md)
     * Example: USA: Maryland, Bethesda None
 * [collection_date](collection_date.md)  <sub>0..1</sub>
     * Description: The time of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10; 2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant
     * Range: [Date](types/Date.md)
     * Example: 2018-05-11T10:00:00+01:00; 2018-05-11 None
 * [env_broad_scale](env_broad_scale.md)  <sub>0..1</sub>
     * Description: Report the major environmental system the sample or specimen came from. The system(s) identified should have a coarse spatial grain, to provide the general environmental context of where the sampling was done (e.g. in the desert or a rainforest). We recommend using subclasses of EnvO’s biome class:  http://purl.obolibrary.org/obo/ENVO_00000428. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
     * Range: [String](types/String.md)
     * Example: oceanic epipelagic zone biome [ENVO:01000033] for annotating a water sample from the photic zone in middle of the Atlantic Ocean None
 * [env_local_scale](env_local_scale.md)  <sub>0..1</sub>
     * Description: Report the entity or entities which are in the sample or specimen’s local vicinity and which you believe have significant causal influences on your sample or specimen. We recommend using EnvO terms which are of smaller spatial grain than your entry for env_broad_scale. Terms, such as anatomical sites, from other OBO Library ontologies which interoperate with EnvO (e.g. UBERON) are accepted in this field. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS.
     * Range: [String](types/String.md)
     * Example: litter layer [ENVO:01000338]; Annotating a pooled sample taken from various vegetation layers in a forest consider: canopy [ENVO:00000047]|herb and fern layer [ENVO:01000337]|litter layer [ENVO:01000338]|understory [01000335]|shrub layer [ENVO:01000336]. None
 * [env_medium](env_medium.md)  <sub>0..1</sub>
     * Description: Report the environmental material(s) immediately surrounding the sample or specimen at the time of sampling. We recommend using subclasses of 'environmental material' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS . Terms from other OBO ontologies are permissible as long as they reference mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. a tree, a leaf, a table top).
     * Range: [String](types/String.md)
     * Example: soil [ENVO:00001998]; Annotating a fish swimming in the upper 100 m of the Atlantic Ocean, consider: ocean water [ENVO:00002151]. Example: Annotating a duck on a pond consider: pond water [ENVO:00002228]|air [ENVO_00002005] None
 * [sediment➞alkalinity](sediment_alkalinity.md)  <sub>0..1</sub>
     * Description: Alkalinity, the ability of a solution to neutralize acids to the equivalence point of carbonate or bicarbonate
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 50 milligram per liter None
 * [sediment➞alkyl_diethers](sediment_alkyl_diethers.md)  <sub>0..1</sub>
     * Description: Concentration of alkyl diethers
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.005 mole per liter None
 * [sediment➞aminopept_act](sediment_aminopept_act.md)  <sub>0..1</sub>
     * Description: Measurement of aminopeptidase activity
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.269 mole per liter per hour None
 * [sediment➞ammonium](sediment_ammonium.md)  <sub>0..1</sub>
     * Description: Concentration of ammonium in the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 1.5 milligram per liter None
 * [sediment➞bacteria_carb_prod](sediment_bacteria_carb_prod.md)  <sub>0..1</sub>
     * Description: Measurement of bacterial carbon production
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 2.53 microgram per liter per hour None
 * [sediment➞biomass](sediment_biomass.md)  <sub>0..\*</sub>
     * Description: Amount of biomass; should include the name for the part of biomass measured, e.g. Microbial, total. Can include multiple measurements
     * Range: [String](types/String.md)
     * Example: total;20 gram None
 * [sediment➞bishomohopanol](sediment_bishomohopanol.md)  <sub>0..1</sub>
     * Description: Concentration of bishomohopanol
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 14 microgram per liter None
 * [sediment➞bromide](sediment_bromide.md)  <sub>0..1</sub>
     * Description: Concentration of bromide
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.05 parts per million None
 * [sediment➞calcium](sediment_calcium.md)  <sub>0..1</sub>
     * Description: Concentration of calcium in the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.2 micromole per liter None
 * [sediment➞carb_nitro_ratio](sediment_carb_nitro_ratio.md)  <sub>0..1</sub>
     * Description: Ratio of amount or concentrations of carbon to nitrogen
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.417361111 None
 * [sediment➞chem_administration](sediment_chem_administration.md)  <sub>0..\*</sub>
     * Description: List of chemical compounds administered to the host or site where sampling occurred, and when (e.g. Antibiotics, n fertilizer, air filter); can include multiple compounds. For chemical entities of biological interest ontology (chebi) (v 163), http://purl.bioontology.org/ontology/chebi
     * Range: [String](types/String.md)
     * Example: agar [CHEBI:2509];2018-05-11T20:00Z None
 * [sediment➞chloride](sediment_chloride.md)  <sub>0..1</sub>
     * Description: Concentration of chloride in the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 5000 milligram per liter None
 * [sediment➞chlorophyll](sediment_chlorophyll.md)  <sub>0..1</sub>
     * Description: Concentration of chlorophyll
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 5 milligram per cubic meter None
 * [sediment➞density](sediment_density.md)  <sub>0..1</sub>
     * Description: Density of the sample, which is its mass per unit volume (aka volumetric mass density)
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 1000 kilogram per cubic meter None
 * [sediment➞diether_lipids](sediment_diether_lipids.md)  <sub>0..\*</sub>
     * Description: Concentration of diether lipids; can include multiple types of diether lipids
     * Range: [String](types/String.md)
     * Example: 0.2 nanogram per liter None
 * [sediment➞diss_carb_dioxide](sediment_diss_carb_dioxide.md)  <sub>0..1</sub>
     * Description: Concentration of dissolved carbon dioxide in the sample or liquid portion of the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 5 milligram per liter None
 * [sediment➞diss_hydrogen](sediment_diss_hydrogen.md)  <sub>0..1</sub>
     * Description: Concentration of dissolved hydrogen
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.3 micromole per liter None
 * [sediment➞diss_inorg_carb](sediment_diss_inorg_carb.md)  <sub>0..1</sub>
     * Description: Dissolved inorganic carbon concentration in the sample, typically measured after filtering the sample using a 0.45 micrometer filter
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 2059 micromole per kilogram None
 * [sediment➞diss_org_carb](sediment_diss_org_carb.md)  <sub>0..1</sub>
     * Description: Concentration of dissolved organic carbon in the sample, liquid portion of the sample, or aqueous phase of the fluid
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 197 micromole per liter None
 * [sediment➞diss_org_nitro](sediment_diss_org_nitro.md)  <sub>0..1</sub>
     * Description: Dissolved organic nitrogen concentration measured as; total dissolved nitrogen - NH4 - NO3 - NO2
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.05 micromole per liter None
 * [sediment➞diss_oxygen](sediment_diss_oxygen.md)  <sub>0..1</sub>
     * Description: Concentration of dissolved oxygen
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 175 micromole per kilogram None
 * [sediment➞glucosidase_act](sediment_glucosidase_act.md)  <sub>0..1</sub>
     * Description: Measurement of glucosidase activity
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 5 mol per liter per hour None
 * [sediment➞magnesium](sediment_magnesium.md)  <sub>0..1</sub>
     * Description: Concentration of magnesium in the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 52.8 micromole per kilogram None
 * [sediment➞mean_frict_vel](sediment_mean_frict_vel.md)  <sub>0..1</sub>
     * Description: Measurement of mean friction velocity
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.5 meter per second None
 * [sediment➞mean_peak_frict_vel](sediment_mean_peak_frict_vel.md)  <sub>0..1</sub>
     * Description: Measurement of mean peak friction velocity
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 1 meter per second None
 * [sediment➞methane](sediment_methane.md)  <sub>0..1</sub>
     * Description: Methane (gas) amount or concentration at the time of sampling
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 1800 parts per billion None
 * [sediment➞misc_param](sediment_misc_param.md)  <sub>0..\*</sub>
     * Description: Any other measurement performed or parameter collected, that is not listed here
     * Range: [String](types/String.md)
     * Example: Bicarbonate ion concentration;2075 micromole per kilogram None
 * [sediment➞n_alkanes](sediment_n_alkanes.md)  <sub>0..\*</sub>
     * Description: Concentration of n-alkanes; can include multiple n-alkanes
     * Range: [String](types/String.md)
     * Example: n-hexadecane;100 milligram per liter None
 * [sediment➞nitrate](sediment_nitrate.md)  <sub>0..1</sub>
     * Description: Concentration of nitrate in the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 65 micromole per liter None
 * [sediment➞nitrite](sediment_nitrite.md)  <sub>0..1</sub>
     * Description: Concentration of nitrite in the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.5 micromole per liter None
 * [sediment➞nitro](sediment_nitro.md)  <sub>0..1</sub>
     * Description: Concentration of nitrogen (total)
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 4.2 micromole per liter None
 * [sediment➞org_carb](sediment_org_carb.md)  <sub>0..1</sub>
     * Description: Concentration of organic carbon
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 1.5 microgram per liter None
 * [sediment➞org_matter](sediment_org_matter.md)  <sub>0..1</sub>
     * Description: Concentration of organic matter
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 1.75 milligram per cubic meter None
 * [sediment➞org_nitro](sediment_org_nitro.md)  <sub>0..1</sub>
     * Description: Concentration of organic nitrogen
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 4 micromole per liter None
 * [sediment➞organism_count](sediment_organism_count.md)  <sub>0..\*</sub>
     * Description: Total cell count of any organism (or group of organisms) per gram, volume or area of sample, should include name of organism followed by count. The method that was used for the enumeration (e.g. qPCR, atp, mpn, etc.) Should also be provided. (example: total prokaryotes; 3.5e7 cells per ml; qpcr)
     * Range: [organism_count_enum](organism_count_enum.md)
     * Example: total prokaryotes;3.5e7 cells per milliliter;qPCR None
 * [sediment➞oxy_stat_samp](sediment_oxy_stat_samp.md)  <sub>0..1</sub>
     * Description: Oxygenation status of sample
     * Range: [oxy_stat_samp_enum](oxy_stat_samp_enum.md)
     * Example: aerobic None
 * [sediment➞ph](sediment_ph.md)  <sub>0..1</sub>
     * Description: Ph measurement of the sample, or liquid portion of sample, or aqueous phase of the fluid
     * Range: [Double](types/Double.md)
     * Example: 7.2 None
 * [sediment➞particle_class](sediment_particle_class.md)  <sub>0..\*</sub>
     * Description: Particles are classified, based on their size, into six general categories:clay, silt, sand, gravel, cobbles, and boulders; should include amount of particle preceded by the name of the particle type; can include multiple values
     * Range: [String](types/String.md)
     * Example:  None
 * [sediment➞part_org_carb](sediment_part_org_carb.md)  <sub>0..1</sub>
     * Description: Concentration of particulate organic carbon
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 1.92 micromole per liter None
 * [sediment➞perturbation](sediment_perturbation.md)  <sub>0..\*</sub>
     * Description: Type of perturbation, e.g. chemical administration, physical disturbance, etc., coupled with perturbation regimen including how many times the perturbation was repeated, how long each perturbation lasted, and the start and end time of the entire perturbation period; can include multiple perturbation types
     * Range: [String](types/String.md)
     * Example: antibiotic addition;R2/2018-05-11T14:30Z/2018-05-11T19:30Z/P1H30M None
 * [sediment➞petroleum_hydrocarb](sediment_petroleum_hydrocarb.md)  <sub>0..1</sub>
     * Description: Concentration of petroleum hydrocarbon
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.05 micromole per liter None
 * [sediment➞phaeopigments](sediment_phaeopigments.md)  <sub>0..\*</sub>
     * Description: Concentration of phaeopigments; can include multiple phaeopigments
     * Range: [String](types/String.md)
     * Example: 2.5 milligram per cubic meter None
 * [sediment➞phosphate](sediment_phosphate.md)  <sub>0..1</sub>
     * Description: Concentration of phosphate
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.7 micromole per liter None
 * [sediment➞phosplipid_fatt_acid](sediment_phosplipid_fatt_acid.md)  <sub>0..\*</sub>
     * Description: Concentration of phospholipid fatty acids; can include multiple values
     * Range: [String](types/String.md)
     * Example: 2.98 milligram per liter None
 * [sediment➞porosity](sediment_porosity.md)  <sub>0..1</sub>
     * Description: Porosity of deposited sediment is volume of voids divided by the total volume of sample
     * Range: [String](types/String.md)
     * Example:  None
 * [sediment➞potassium](sediment_potassium.md)  <sub>0..1</sub>
     * Description: Concentration of potassium in the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 463 milligram per liter None
 * [sediment➞pressure](sediment_pressure.md)  <sub>0..1</sub>
     * Description: Pressure to which the sample is subject to, in atmospheres
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 50 atmosphere None
 * [sediment➞redox_potential](sediment_redox_potential.md)  <sub>0..1</sub>
     * Description: Redox potential, measured relative to a hydrogen cell, indicating oxidation or reduction potential
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 300 millivolt None
 * [sediment➞salinity](sediment_salinity.md)  <sub>0..1</sub>
     * Description: The total concentration of all dissolved salts in a liquid or solid sample. While salinity can be measured by a complete chemical analysis, this method is difficult and time consuming. More often, it is instead derived from the conductivity measurement. This is known as practical salinity. These derivations compare the specific conductance of the sample to a salinity standard such as seawater.
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 25 practical salinity unit None
 * [sediment➞samp_store_dur](sediment_samp_store_dur.md)  <sub>0..1</sub>
     * Description: Duration for which the sample was stored
     * Range: [String](types/String.md)
     * Example: P1Y6M None
 * [sediment➞samp_store_loc](sediment_samp_store_loc.md)  <sub>0..1</sub>
     * Description: Location at which sample was stored, usually name of a specific freezer/room
     * Range: [String](types/String.md)
     * Example: Freezer no:5 None
 * [sediment➞samp_store_temp](sediment_samp_store_temp.md)  <sub>0..1</sub>
     * Description: Temperature at which sample was stored, e.g. -80 degree Celsius
     * Range: [QuantityValue](QuantityValue.md)
     * Example: -80 degree Celsius None
 * [sediment➞sediment_type](sediment_sediment_type.md)  <sub>0..1</sub>
     * Description: Information about the sediment type based on major constituents
     * Range: [sediment_type_enum](sediment_type_enum.md)
     * Example: biogenous None
 * [sediment➞silicate](sediment_silicate.md)  <sub>0..1</sub>
     * Description: Concentration of silicate
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.05 micromole per liter None
 * [sediment➞sodium](sediment_sodium.md)  <sub>0..1</sub>
     * Description: Sodium concentration in the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 10.5 milligram per liter None
 * [sediment➞sulfate](sediment_sulfate.md)  <sub>0..1</sub>
     * Description: Concentration of sulfate in the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 5 micromole per liter None
 * [sediment➞sulfide](sediment_sulfide.md)  <sub>0..1</sub>
     * Description: Concentration of sulfide in the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 2 micromole per liter None
 * [sediment➞tidal_stage](sediment_tidal_stage.md)  <sub>0..1</sub>
     * Description: Stage of tide
     * Range: [tidal_stage_enum](tidal_stage_enum.md)
     * Example: high tide None
 * [sediment➞tot_carb](sediment_tot_carb.md)  <sub>0..1</sub>
     * Description: Total carbon content
     * Range: [QuantityValue](QuantityValue.md)
     * Example:  None
 * [sediment➞tot_depth_water_col](sediment_tot_depth_water_col.md)  <sub>0..1</sub>
     * Description: Measurement of total depth of water column
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 500 meter None
 * [sediment➞tot_nitro_content](sediment_tot_nitro_content.md)  <sub>0..1</sub>
     * Description: Total nitrogen content of the sample
     * Range: [QuantityValue](QuantityValue.md)
     * Example:  None
 * [sediment➞tot_org_carb](sediment_tot_org_carb.md)  <sub>0..1</sub>
     * Description: Definition for soil: total organic carbon content of the soil, definition otherwise: total organic carbon content
     * Range: [QuantityValue](QuantityValue.md)
     * Example:  None
 * [sediment➞turbidity](sediment_turbidity.md)  <sub>0..1</sub>
     * Description: Measure of the amount of cloudiness or haziness in water caused by individual particles
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 0.3 nephelometric turbidity units None
 * [sediment➞water_content](sediment_water_content.md)  <sub>0..1</sub>
     * Description: Water content measurement
     * Range: [QuantityValue](QuantityValue.md)
     * Example:  None
 * [sediment➞samp_name](sediment_samp_name.md)  <sub>1..1</sub>
     * Description: A local identifier or name that for the material sample used for extracting nucleic acids, and subsequent sequencing. It can refer either to the original material collected or to any derived sub-samples. It can have any format, but we suggest that you make it concise, unique and consistent within your lab, and as informative as possible. INSDC requires every sample name from a single Submitter to be unique. Use of a globally unique identifier for the field source_mat_id is recommended in addition to sample_name.
     * Range: [String](types/String.md)
     * Example: ISDsoil1 None
 * [sediment➞project_name](sediment_project_name.md)  <sub>1..1</sub>
     * Description: Name of the project within which the sequencing was organized
     * Range: [String](types/String.md)
     * Example: Forest soil metagenome None
 * [sediment➞samp_vol_we_dna_ext](sediment_samp_vol_we_dna_ext.md)  <sub>0..1</sub>
     * Description: Volume (ml) or mass (g) of total collected sample processed for DNA extraction. Note: total sample collected should be entered under the term Sample Size (MIXS:0000001).
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 1500 milliliter None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞submitted_to_insdc](MIMARKS_survey_submitted_to_insdc.md)  <sub>1..1</sub>
     * Description: Depending on the study (large-scale e.g. done with next generation sequencing technology, or small-scale) sequences have to be submitted to SRA (Sequence Read Archive), DRA (DDBJ Read Archive) or via the classical Webin/Sequin systems to Genbank, ENA and DDBJ. Although this field is mandatory, it is meant as a self-test field, therefore it is not necessary to include this field in contextual data submitted to databases
     * Range: [String](types/String.md)
     * Example: yes None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞investigation_type](MIMARKS_survey_investigation_type.md)  <sub>1..1</sub>
     * Description: Nucleic Acid Sequence Report is the root element of all MIGS/MIMS compliant reports as standardized by Genomic Standards Consortium. This field is either eukaryote,bacteria,virus,plasmid,organelle, metagenome,mimarks-survey, mimarks-specimen, metatranscriptome, single amplified genome, metagenome-assembled genome, or uncultivated viral genome
     * Range: [investigation_type_enum](investigation_type_enum.md)
     * Example: metagenome None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞samp_taxon_id](MIMARKS_survey_samp_taxon_id.md)  <sub>1..1</sub>
     * Description: NCBI taxon id of the sample.  Maybe be a single taxon or mixed taxa sample. Use 'synthetic metagenome’ for mock community/positive controls, or 'blank sample' for negative controls.
     * Range: [String](types/String.md)
     * Example: Gut Metagenome [NCBI:txid749906] None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞experimental_factor](MIMARKS_survey_experimental_factor.md)  <sub>0..1</sub>
     * Description: Experimental factors are essentially the variable aspects of an experiment design which can be used to describe an experiment, or set of experiments, in an increasingly detailed manner. This field accepts ontology terms from Experimental Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI). For a browser of EFO (v 2.95) terms, please see http://purl.bioontology.org/ontology/EFO; for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI
     * Range: [String](types/String.md)
     * Example: time series design [EFO:EFO_0001779] None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞neg_cont_type](MIMARKS_survey_neg_cont_type.md)  <sub>0..1</sub>
     * Description: The substance or equipment used as a negative control in an investigation
     * Range: [neg_cont_type_enum](neg_cont_type_enum.md)
     * Example:  None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞pos_cont_type](MIMARKS_survey_pos_cont_type.md)  <sub>0..1</sub>
     * Description: The substance, mixture, product, or apparatus used to verify that a process which is part of an investigation delivers a true positive.
     * Range: [String](types/String.md)
     * Example:  None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞env_package](MIMARKS_survey_env_package.md)  <sub>0..1</sub>
     * Description: MIxS extension for reporting of measurements and observations obtained from one or more of the environments where the sample was obtained. All environmental packages listed here are further defined in separate subtables. By giving the name of the environmental package, a selection of fields can be made from the subtables and can be reported
     * Range: [env_package_enum](env_package_enum.md)
     * Example: soil None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞subspecf_gen_lin](MIMARKS_survey_subspecf_gen_lin.md)  <sub>0..1</sub>
     * Description: Information about the genetic distinctness of the sequenced organism below the subspecies level, e.g., serovar, serotype, biotype, ecotype, or any relevant genetic typing schemes like Group I plasmid. Subspecies should not be recorded in this term, but in the NCBI taxonomy. Supply both the lineage name and the lineage rank separated by a colon, e.g., biovar:abc123.
     * Range: [String](types/String.md)
     * Example: serovar:Newport None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞extrachrom_elements](MIMARKS_survey_extrachrom_elements.md)  <sub>0..1</sub>
     * Description: Do plasmids exist of significant phenotypic consequence (e.g. ones that determine virulence or antibiotic resistance). Megaplasmids? Other plasmids (borrelia has 15+ plasmids)
     * Range: [Integer](types/Integer.md)
     * Example: 5 None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞source_mat_id](MIMARKS_survey_source_mat_id.md)  <sub>0..1</sub>
     * Description: A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The INSDC qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/R2).
     * Range: [String](types/String.md)
     * Example: MPI012345 None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞biotic_relationship](MIMARKS_survey_biotic_relationship.md)  <sub>0..1</sub>
     * Description: Description of relationship(s) between the subject organism and other organism(s) it is associated with. E.g., parasite on species X; mutualist with species Y. The target organism is the subject of the relationship, and the other organism(s) is the object
     * Range: [biotic_relationship_enum](biotic_relationship_enum.md)
     * Example: free living None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞trophic_level](MIMARKS_survey_trophic_level.md)  <sub>0..1</sub>
     * Description: Trophic levels are the feeding position in a food chain. Microbes can be a range of producers (e.g. chemolithotroph)
     * Range: [trophic_level_enum](trophic_level_enum.md)
     * Example: heterotroph None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞rel_to_oxygen](MIMARKS_survey_rel_to_oxygen.md)  <sub>0..1</sub>
     * Description: Is this organism an aerobe, anaerobe? Please note that aerobic and anaerobic are valid descriptors for microbial environments
     * Range: [rel_to_oxygen_enum](rel_to_oxygen_enum.md)
     * Example: aerobe None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞isol_growth_condt](MIMARKS_survey_isol_growth_condt.md)  <sub>1..1</sub>
     * Description: Publication reference in the form of pubmed ID (pmid), digital object identifier (doi) or url for isolation and growth condition specifications of the organism/material
     * Range: [String](types/String.md)
     * Example: doi: 10.1016/j.syapm.2018.01.009 None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞samp_collec_device](MIMARKS_survey_samp_collec_device.md)  <sub>0..1</sub>
     * Description: The device used to collect an environmental sample. This field accepts terms listed under environmental sampling device (http://purl.obolibrary.org/obo/ENVO). This field also accepts terms listed under specimen collection device (http://purl.obolibrary.org/obo/GENEPIO_0002094).
     * Range: [String](types/String.md)
     * Example: swab, biopsy, niskin bottle, push core, drag swab [GENEPIO:0002713] None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞samp_collec_method](MIMARKS_survey_samp_collec_method.md)  <sub>0..1</sub>
     * Description: The method employed for collecting the sample.
     * Range: [String](types/String.md)
     * Example: swabbing None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞samp_mat_process](MIMARKS_survey_samp_mat_process.md)  <sub>0..1</sub>
     * Description: A brief description of any processing applied to the sample during or after retrieving the sample from environment, or a link to the relevant protocol(s) performed.
     * Range: [String](types/String.md)
     * Example: filtering of seawater, storing samples in ethanol None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞samp_size](MIMARKS_survey_samp_size.md)  <sub>0..1</sub>
     * Description: The total amount or size (volume (ml), mass (g) or area (m2) ) of sample collected.
     * Range: [QuantityValue](QuantityValue.md)
     * Example: 5 liter None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞nucl_acid_ext](MIMARKS_survey_nucl_acid_ext.md)  <sub>0..1</sub>
     * Description: A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the material separation to recover the nucleic acid fraction from a sample
     * Range: [String](types/String.md)
     * Example: https://mobio.com/media/wysiwyg/pdfs/protocols/12888.pdf None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞nucl_acid_amp](MIMARKS_survey_nucl_acid_amp.md)  <sub>0..1</sub>
     * Description: A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the enzymatic amplification (PCR, TMA, NASBA) of specific nucleic acids
     * Range: [String](types/String.md)
     * Example: https://phylogenomics.me/protocols/16s-pcr-protocol/ None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞target_gene](MIMARKS_survey_target_gene.md)  <sub>1..1</sub>
     * Description: Targeted gene or locus name for marker gene studies
     * Range: [String](types/String.md)
     * Example: 16S rRNA, 18S rRNA, nif, amoA, rpo None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞target_subfragment](MIMARKS_survey_target_subfragment.md)  <sub>0..1</sub>
     * Description: Name of subfragment of a gene or locus. Important to e.g. identify special regions on marker genes like V6 on 16S rRNA
     * Range: [String](types/String.md)
     * Example: V6, V9, ITS None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞pcr_primers](MIMARKS_survey_pcr_primers.md)  <sub>0..1</sub>
     * Description: PCR primers that were used to amplify the sequence of the targeted gene, locus or subfragment. This field should contain all the primers used for a single PCR reaction if multiple forward or reverse primers are present in a single PCR reaction. The primer sequence should be reported in uppercase letters
     * Range: [String](types/String.md)
     * Example: FWD:GTGCCAGCMGCCGCGGTAA;REV:GGACTACHVGGGTWTCTAAT None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞pcr_cond](MIMARKS_survey_pcr_cond.md)  <sub>0..1</sub>
     * Description: Description of reaction conditions and components of PCR in the form of 'initial denaturation:94degC_1.5min; annealing=...'
     * Range: [String](types/String.md)
     * Example: initial denaturation:94_3;annealing:50_1;elongation:72_1.5;final elongation:72_10;35 None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞seq_meth](MIMARKS_survey_seq_meth.md)  <sub>1..1</sub>
     * Description: Sequencing machine used. Where possible the term should be taken from the OBI list of DNA sequencers (http://purl.obolibrary.org/obo/OBI_0400103).
     * Range: [String](types/String.md)
     * Example: 454 Genome Sequencer FLX [OBI:0000702] None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞seq_quality_check](MIMARKS_survey_seq_quality_check.md)  <sub>0..1</sub>
     * Description: Indicate if the sequence has been called by automatic systems (none) or undergone a manual editing procedure (e.g. by inspecting the raw data or chromatograms). Applied only for sequences that are not submitted to SRA,ENA or DRA
     * Range: [String](types/String.md)
     * Example: none None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞chimera_check](MIMARKS_survey_chimera_check.md)  <sub>0..1</sub>
     * Description: Tool(s) used for chimera checking, including version number and parameters, to discover and remove chimeric sequences. A chimeric sequence is comprised of two or more phylogenetically distinct parent sequences.
     * Range: [String](types/String.md)
     * Example: uchime;v4.1;default parameters None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞associated resource](MIMARKS_survey_associated_resource.md)  <sub>0..1</sub>
     * Description: A related resource that is referenced, cited, or otherwise associated to the sequence.
     * Range: [String](types/String.md)
     * Example: http://www.earthmicrobiome.org/ None

### Mixed in from MIMARKS survey:

 * [MIMARKS survey➞sop](MIMARKS_survey_sop.md)  <sub>0..1</sub>
     * Description: Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences
     * Range: [String](types/String.md)
     * Example: http://press.igsb.anl.gov/earthmicrobiome/protocols-and-standards/its/ None
