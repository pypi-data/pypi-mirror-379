# The Wowool NLP Toolkit

## install

Install the main sdk.

    pip install wowool-sdk

Installing languages.

    pip install wowool-[language]

## Quick Start

Just create a document and pipeline, pass your document trough the Pipeline, and your done.

```python
from wowool.sdk import Pipeline
from wowool.document import Document

document = Document("Mark Van Den Berg works at Omega Pharma.")
# Create an analyzer for a given language and options
process = Pipeline("english,entity")
# Process the data
document = process(document)
print(document)
```

# API

## Examples

You will need to install the english language module to run the sample. `pip install wowool-english` 

### Create a pipeline.

This script demonstrates how to use the UUID component to create a pipeline.



```python
from wowool.sdk import Pipeline
from wowool.common.pipeline import UUID

process = Pipeline(
    [
        UUID("english", options={"anaphora": False}),
        UUID("entity"),
        UUID("topics.app", {"count": 3}),
    ]
)
document = process("Mark Janssens works at Omega Pharma.")
print(document)

```

### Custom domain

The script identifies the word "car" as a Vehicle entity in the sentence "I have a car." using custom domain rules and language processing.

For more info on how to write rules see: https://www.wowool.com/docs/nlp/matching-&-capturing


```python
from wowool.sdk import Language, Domain
from wowool.document import Document

english = Language("english")
vehicle = Domain(source="rule:{ 'car'} = Vehicle;")
doc = vehicle(english(Document("I have a car.")))
for entity in doc.entities:
    print(entity)

```

### Using the language identifier

This script demonstrates how to use the LanguageIdentifier to detect the language of a document.


```python
from wowool.sdk import LanguageIdentifier

document = """
Un été de tous les records de chaleur en France.
Record de chaleur battu dans une cinquantaine de villes en France

"""
# Initialize a language identification engine
lid = LanguageIdentifier()
# Process the data
doc = lid(document)
print(doc.language)

```

### Extract dutch entities

This script demonstrates how to perform basic entity analysis on a Dutch sentence using the Wowool SDK.

Install first the dutch language model `pip install wowool-dutch`



```python
from wowool.sdk import Pipeline
from wowool.document import Document

entities = Pipeline("dutch,entity")
document = entities(Document("Mark Van Den Berg werkte als hoofdarts bij Omega Pharma."))
for sentence in document.sentences:
    for entity in sentence.entities:
        print(entity)

```

### Using the language identifier

This script demonstrates how to use the LanguageIdentifier to detect the different language sections in a text multi-language document.


```python
from wowool.sdk import LanguageIdentifier

document = """
La juventud no es más que un estado de ánimo.

Record de chaleur battu dans une cinquantaine de villes en France

"""
# Initialize a language identification engine
lid = LanguageIdentifier(sections=True, section_data=True)
# Process the data
doc = lid(document)
if lid_results := doc.lid:
    for section in doc.lid.sections:
        assert section.text
        print(f"({section.begin_offset},{section.end_offset}): language= {section.language} text={section.text[:20].strip('\n')}...")

```



## License

In both cases you will need to acquirer a license file at https://www.wowool.com

### Non-Commercial

    This library is licensed under the GNU AGPLv3 for non-commercial use.  
    For commercial use, a separate license must be purchased.  

### Commercial license Terms

    1. Grants the right to use this library in proprietary software.  
    2. Requires a valid license key  
    3. Redistribution in SaaS requires a commercial license.  
