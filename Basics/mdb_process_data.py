

"""
Task : parse the file, process only the fields that are listed in the FIELDS dictionary as keys, and
       return a list of dictionaries of cleaned values.

The following things should be done:
- keys of the dictionary changed according to the mapping in FIELDS dictionary
- trim out redundant description in parenthesis from the 'rdf-schema#label'
  field, like "(spider)"
- if 'name' is "NULL" or contains non-alphanumeric characters, set it to the
  same value as 'label'.
- if a value of a field is "NULL", convert it to None
- if there is a value in 'synonym'(this is why no.4 should go first), it should be converted to an array (list)
  by stripping the "{}" characters and splitting the string on "|". Rest of the
  cleanup is up to you, e.g. removing "*" prefixes etc. If there is a singular
  synonym, the value should still be formatted in a list.
- strip leading and ending whitespace from all fields, if there is any
- the output structure should be as follows:

[ { 'label': 'Argiope',
    'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
    'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
    'name': 'Argiope',
    'synonym': ["One", "Two"],
    'classification': {
                      'family': 'Orb-weaver spider',
                      'class': 'Arachnid',
                      'phylum': 'Arthropod',
                      'order': 'Spider',
                      'kingdom': 'Animal',
                      'genus': None
                      }
  },
  { 'label': ... , }, ...
]

  * Note that the value associated with the classification key is a dictionary
    with taxonomic labels.
"""
'''Data is in arachinid.csv file'''

import codecs
import csv
import json
import pprint
import re

DATAFILE = 'arachnid.csv'
FIELDS = {'rdf-schema#label': 'label',
          'URI': 'uri',
          'rdf-schema#comment': 'description',
          'synonym': 'synonym',
          'name': 'name',
          'family_label': 'family',
          'class_label': 'class',
          'phylum_label': 'phylum',
          'order_label': 'order',
          'kingdom_label': 'kingdom',
          'genus_label': 'genus'}


# Different from None, 'NULL' is a value, so if 'NULL' is a TRUE
# strip() is a string function, doesn't work on list, etc. So if there is a convert of data type, pay attention to
# the match
# between data type and method
# the sequence is very important, the former ones are highly likely to influence the latter ones, like the third and
# forth one are related to each other
# there are more data than the data we output and there are functions looping through all data, like no.4
# for the data we don't use, is that necessary to work on them? this has impact on my decision of working sequence
# eventhough it seems like there could be less work if we just work on the output data, on the other hand,
# his causes the inconsistency within the dataset, which could cause trouble in the future
def process_file(filename, fields):
    process_fields = fields.keys()
    data = []
    n = 0
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for line in reader:

            # task 2
            rdf = line['rdf-schema#label'].strip()
            if "(" in rdf:
                index = rdf.index("(")
                rdf = rdf[:index]
                line['rdf-schema#label'] = rdf

            # task 3
            name = line['name'].strip()
            if name == 'NULL' or not name.isalpha():
                # this value has been stripped above
                line['name'] = line['rdf-schema#label']

            # task 4&6
            for i in line:
                line[i] = line[i].strip()
                if line[i] == 'NULL':
                    line[i] = None

            # task 5
            if line['synonym']:
                # this value has been stripped as well
                line['synonym'] = parse_array(line['synonym'])

            # task 1&7
            item = {}
            item['classification'] = {}
            classification = ['family_label', 'class_label', 'phylum_label', 'order_label', 'kingdom_label',
                              'genus_label']
            for i in line.keys():
                if i in process_fields:
                    if i in classification:
                        item['classification'][FIELDS[i]] = line[i]
                    else:
                        item[FIELDS[i]] = line[i]

            data.append(item)

    return data


def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")

        # this is how you change the value in array
        for i in range(len(v_array)):
            if '*' in v_array[i]:
                v_array[i] = v_array[i].replace('*', '')
        # v_array = [i.strip() for i in v_array]
        return v_array
    return [v]


def test():
    data = process_file(DATAFILE, FIELDS)
    print("Your first entry:")
    pprint.pprint(data[0])
    first_entry = {
        "synonym": None,
        "name": "Argiope",
        "classification": {
            "kingdom": "Animal",
            "family": "Orb-weaver spider",
            "order": "Spider",
            "phylum": "Arthropod",
            "genus": None,
            "class": "Arachnid"
        },
        "uri": "http://dbpedia.org/resource/Argiope_(spider)",
        "label": "Argiope",
        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
    }

    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]


if __name__ == "__main__":
    test()