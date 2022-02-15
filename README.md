# MIxS

“Minimum Information about any (X) Sequence” (MIxS) specification

## Purpose

This repo contains computable artifacts that define the MIxS standard, versions 4 and later. _Older versions of the MIxS standard are available at https://github.com/GenomicsStandardsConsortium/mixs-legacy_

Versions 4 and 5 can be found in their respective folders

Beginning with version 6, MIxS is being managed using the [LinkML toolkit](https://linkml.io/). The location of the various LinkML artifacts is fortcoming.


**To request changes to the MIxS standards, please use the issue tracker in this repo.**


## Reuse and citation of content on this repository

The MIxS standards and the content of this repo are freely available under the [Creative Commons 0 (open source)](https://creativecommons.org/share-your-work/public-domain/cc0/) agreement. 

### Cite this repo

If you reuse code from this repository, please site the [repository URL](https://github.com/GenomicsStandardsConsortium/mixs)


### Cite the standard

If you use any of the MIxS standards, please site [this paper](https://www.nature.com/articles/nbt.1823):

DOI: https://doi.org/10.1038/nbt.1823

Or, in [RIS format](citation.ris)


## General Background
Without specific guidelines, most genomic, metagenomic and marker gene sequences in databases are sparsely annotated with the information required to guide data integration, comparative studies and knowledge generation. Even with complex keyword searches, it is currently impossible to reliably retrieve sequences that have originated from certain environments or particular locations on Earth—for example, all sequences from ‘soil’ or ‘freshwater lakes’ in a certain region of the world. Because public databases of the International Nucleotide Sequence Database Collaboration (INSDC; comprising DNA Data Bank of Japan (DDBJ), the European Nucleotide Archive (EBI-ENA) and [GenBank](http://www.insdc.org/) depend on author-submitted information to enrich the value of sequence data sets, we argue that the only way to change the current practice is to establish a standard of reporting that requires contextual data to be deposited at the time of sequence submission. The adoption of such a standard would elevate the quality, accessibility and utility of information that can be collected from INSDC or any other data repository.

The GSC has defined a set of core descriptors for genomes and metagenomes in the form of a MIGS/MIMS specification. MIGS/MIMS extends the minimum information already captured by the INSDC. The recently introduced MIMARKS now captures information about marker genes. Additionally, we also introduced ‘environmental packages’ that standardize sets of measurements and observations describing particular habitats that are applicable across all GSC checklists and beyond. We define ‘environment’ as any location in which a sample or organism is found, e.g., soil, air, water, human-associated, plant-associated or laboratory. The original MIGS/MIMS checklists included contextual data about the location from which a sample was isolated and how the sequence data were produced. However, standard descriptions for a more comprehensive range of environmental parameters, which would help to better contextualize a sample, were not included. The environmental packages presented here are relevant to any genome sequence of known origin and are designed to be used in combination with MIGS, MIMS and MIMARKS checklists.

To create a single entry point to all minimum information checklists from the GSC and to the environmental packages, we created an overarching framework, the MIxS standard . MIxS includes the technology-specific checklists from the previous MIGS and MIMS standards, provides a way of introducing additional checklists such as MIMARKS, and also allows annotation of sample data using environmental packages.

The adoption of the GSC standards by major data providers and organizations, as well as the INSDC, supports efforts to contextually enrich sequence data and complements recent efforts to enrich other (meta) ‘omics data. The MIxS standards have been developed to the point that it is ready for use in the publication of sequences. A defined procedure for requesting new features and stable release cycles will facilitate implementation of the standard across the community. Compliance among authors, adoption by journals and use by informatics resources will vastly improve our collective ability to mine and integrate invaluable sequence data collections for knowledge- and application-driven research.

