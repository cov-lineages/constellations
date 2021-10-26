# constellations

This repository contains descriptions of constellations of mutations for the SARS-CoV-2 virus. 

A *constellation* is a collection of mutations which are functionally meaningful, but which may arise independently a number of times.

Here we include files that define:

- lineages of concern - for these lineages, the defining mutations have been extracted so that individual sequences can be classified deterministically
- genomically interesting regions e.g. RBD sites which interact with ACE2

In addition we include a JSON file describing the reference sequence and the coordinates of genes/proteins. Mutations can therefore be described with respect to the amino acid position within these features.

### Definitions

At a minimum, JSON files must contain the following:

- `label` : a unique string to represent the constellation
- `sites` : a list of defining mutations
- `rules` : the rules used by scorpio to classify whether a sequence belongs to a constellation

The general format of a mutation code is: `gene`:[`ref`]`coordinates`[`alt`] where `gene` is a gene code (or `nuc` for the genomic nucleotide sequence), `ref` is the nucleotide or amino acids in the reference, `alt` is the specific nucleotide or amino acid for the mutatant. Either of `ref` or `alt` can be missing if no specific state is required. See https://github.com/cov-lineages/scorpio for more definitions.

Rules can either specify [min|max]_[ref|alt|ambig|oth] OR the call required at a mutation e.g. "N:S235F": (not )[ref|alt|ambig|oth]

#### Optional fields

- `description` : human readable string of information
- `sources` : reference material for the definition where appropriate
- `type` : at present all definitions are of type `variant` although we conceived of having constellations investigating e.g. furin cleavage sites
- `variant` : for all constellations of type variant, information which exists because it is a variant. e.g.
  - `mrca_lineage` : the pangolin-lineage of the MRCA of the constellation
  - `PHE_label` : PHE label where appropriate
  - `WHO_label` : WHO label where appropriate
  - `lineage_name` and `parent_lineage` are used together to allow scorpio to handle parent/child constellations. Without them, a parent would be favoured over a child lineage as having all the defining sites instead of possibly missing a few. The `parent_lineage` says that the constellation should only be called if the parent has also been called and should be favoured over the parent if it has enough support. The `lineage_name` should be in the same format. Note there are constellations which include multiple lineages, for which this would not work.
  - `incompatible_lineage_calls` : used by `pangolin ` usually in the context of a parent/child relationship. This tells pangolin that if `scorpio` called the given (parent) lineage and `pangolin` called the incompatible (child) lineage, the `scorpio` lineage should override. The default behaviour in `pangolin` is to allow children of a constellation called by `scorpio` as we want to allow a VOC/VUI to continue to evolve and have descendant lineages. However in these cases where we have a constellation for a child lineage, we care about lineage calls meeting a very specific definition so we want the `scorpio` call to override.
  - `tags` : any other names given to this constellation
  - `Pango_lineages` : unused, human-readable list of relevant tango-lineages
  - `representative_genome` : may be used in future, a genome representing the mutations
- `ancestral_sites` : definitions created with `scorpio define` may use an outgroup to partition sites into those that are defining and those that belonged to the outgroup and predate this new variant. These sites are included when classifying (including `pangolin`) but not when running `scorpio haplotype`
- `intermediate_sites` : definitions created with `scorpio define`  use a default threshold of 98% when defining mutation sites. e.g. a mutation has to be present in 98% of defining sequences to be included. If it appears below this threshold in more than 25% of defining sequences, we list it as an intermediate site. These are for reference for a manual curation step
