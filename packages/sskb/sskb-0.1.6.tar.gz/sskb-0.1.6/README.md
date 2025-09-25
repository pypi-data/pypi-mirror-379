# Simple Statement Knowledge Bases (SSKB)
### Knowledge Base loading and annotation facilities

The *sskb* library provides easy access to Natural Language Knowledge Bases (KBs), and tools to facilitate annotation. 

It exposes available KBs as sequences of simple statements. For example (from ProofWiki):

```
"A '''set''' is intuitively defined as any aggregation of 
objects, called elements, which can be precisely defined in 
some way or other."
```

Each statement is accompanied of relevant metadata, in the form of *premises* necessary for the statement to be true, and named entities associated with the respective KB.  

*SSKB* is built upon the [Simple Annotation Framework (SAF)](https://github.com/dscarvalho/saf) library, which provides its data model and API.
This means it is compatible with [saf-datasets](https://github.com/neuro-symbolic-ai/saf_datasets) annotators.


## Installation

To install, you can use pip:

```bash
pip install sskb
```

## Usage
### Loading KBs and accessing data

```python
from sskb import ProofWikiKB

kb = ProofWikiKB()
print(len(kb))  # Number of statements in the KB
# 146723

print(kb[0].surface)  # First statement in the KB
# A '''set''' is intuitively defined as any aggregation of objects, called elements, which can be precisely defined in some way or other.

print([token.surface for token in kb[0].tokens])  # Tokens (SpaCy) of the first statement.
# ['A', "''", "'", 'set', "''", "'", 'is', 'intuitively', 'defined', 'as', 'any', 'aggregation', 'of', 'objects', ',', 'called', 'elements', ',', 'which', 'can', 'be', 'precisely', 'defined', 'in', 'some', 'way', 'or', 'other', '.']


print(kb[0].annotations)  # Annotations for the first sentence
# {'split': 'KB', 'type': 'fact', 'id': 337113631216859490898241823584484375642}


# There are no token annotations in this dataset
print([(tok.surface, tok.annotations) for tok in kb[0].tokens])
# [('A', {}), ("''", {}), ("'", {}), ('set', {}), ("''", {}), ("'", {}), ('is', {}), ('intuitively', {}), ('defined', {}), ('as', {}), ('any', {}), ('aggregation', {}), ('of', {}), ('objects', {}), (',', {}), ('called', {}), ('elements', {}), (',', {}), ('which', {}), ('can', {}), ('be', {}), ('precisely', {}), ('defined', {}), ('in', {}), ('some', {}), ('way', {}), ('or', {}), ('other', {}), ('.', {})]

# Entities cited in a statement
print([entity.surface for entity in kb[0].entities])
# ['Set', 'Or', 'Aggregation']

# Accessing statements by KB identifier
set_related = kb[337113631216859490898241823584484375642] # All statements connected to this identifier

print(len(set_related))
# 40

print(set_related[10].surface)
# If there are many elements in a set, then it becomes tedious and impractical to list them all in one big long explicit definition. Fortunately, however, there are other techniques for listing sets.

# Filtering ProofWiki propositions
train_propositions = [stt for stt in kb 
                      if (stt.annotations["type"] == "proposition" and stt.annotations["split"] == "train")]

print( train_propositions[0].surface)
# Let $A$ be a preadditive category.

print("\n".join([prem.surface for prem in train_propositions[0].premises]))
# Let $\mathbf C$ be a metacategory.
# Let $A$ and $B$ be objects of $\mathbf C$.
# A '''(binary) product diagram''' for $A$ and $B$ comprises an object $P$ and morphisms $p_1: P \to A$, $p_2: P \to B$:
# ::$\begin{xy}\xymatrix@+1em@L+3px{
#  A
# &
#  P
#   \ar[l]_*+{p_1}
#   \ar[r]^*+{p_2}
# &
#  B
# }\end{xy}$
# subjected to the following universal mapping property:
# :For any object $X$ and morphisms $x_1, x_2$ like so:
# ::$\begin{xy}\xymatrix@+1em@L+3px{
#  A
# &
#  X
#   \ar[l]_*+{x_1}
#   \ar[r]^*+{x_2}
# &
#  B
# }\end{xy}$
# :there is a unique morphism $u: X \to P$ such that:
# ::$\begin{xy}\xymatrix@+1em@L+3px{
# &
#  X
#   \ar[ld]_*+{x_1}
#   \ar@{-->}[d]^*+{u}
#   \ar[rd]^*+{x_2}
# \\
#  A
# &
#  P
#   \ar[l]^*+{p_1}
#   \ar[r]_*+{p_2}
# &
#  B
# }\end{xy}$
# :is a commutative diagram, i.e., $x_1 = p_1 \circ u$ and $x_2 = p_2 \circ u$.
# In this situation, $P$ is called a '''(binary) product of $A$ and $B$''' and may be denoted $A \times B$.
# Generally, one writes $\left\langle{x_1, x_2}\right\rangle$ for the unique morphism $u$ determined by above diagram.
# The morphisms $p_1$ and $p_2$ are often taken to be implicit.
# They are called '''projections'''; if necessary, $p_1$ can be called the '''first projection''' and $p_2$ the '''second projection'''.
# {{expand|the projection definition may merit its own, separate page}}
```

**Available datasets:** e-SNLI (ESNLIKB), ProofWiki (ProofWikiKB), WorldTree (WorldTreeKB).

