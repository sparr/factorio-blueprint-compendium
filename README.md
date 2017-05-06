# Factorio Community Blueprint Compendium

This repository contains community-contributed "best of breed" examples of a wide variety of Factorio factory components. Blueprints are sorted first by function, then by optimization criteria (smallest, shortest, cheapest, most efficient, achievements, etc).

## Getting Started

The [exchange](exchange/) directory contains exchange strings for individual blueprints as well as blueprint books for each subdirectory.

If you want to contribute to the compendium, see "Installing" below.

## Contributing

1. Fork this repository to your own github account
2. Clone your fork to your local computer
3. Use `git submodule init` then `git submodule update` to download build scripts
3. Edit the JSON file for a blueprint
4. Build your change, creating an updated or new exchange file from your JSON file
5. Commit and push your change and the built exchange file(s)
6. Open a Pull Request on Github to get your change into the main repository

If you are contributing something other than your own original design, please include a link to the post/site/page where you found it in the commit message.

## Implementation notes

A blueprint exchange string is a JSON object that has been compressed with zlib, then base64 encoded, then a factorio/blueprint schema version byte prepended.

The JSON objects in this repository have had the `entity_number` key removed from every object in the `entities` array. The included conversion scripts will remove and re-add these keys transparently. The purpose of this change is to avoid noisy and distracting commit diffs when a new entity is added to the middle of an existing blueprint, which would otherwise show up as a modification to every entity after it.

## Authors

* [Clarence "Sparr" Risher](https://github.com/sparr) - Original implementation, collecting initial blueprints, blueprint contributions

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project as a whole is licensed under the Creative Commons Attribution-ShareAlike 4.0 International Public License. See the [LICENSE.txt](LICENSE.txt) file for details.

While unlikely, it is possible that the original designer of some factory component described in this compendium may retain and exercise rights related to their work.

## Acknowledgments

Thank you to...
* the many forum and reddit users whose shared designs seeded this compendium.
* [Eric Burgess](https://github.com/ericmburgess) for the [python-factorio](https://github.com/ericmburgess/python-factorio) library
