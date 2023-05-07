# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2023-05-07

Stable version of Vigenere-API.
This update provides an OpenAPI interface to use Vigenere algorithm.
You can cipher and decipher content.

### Added features:

- Vigenere algorithm [#1](https://etulab.univ-amu.fr/d19006523/vigenere-api/-/issues/2).
    - Cipher method at the address: /api/v2/vigenere/decipher
    - Decipher method at the address: /api/v2/vigenere/decipher

  You need to use the POST method to send the JSON content to cipher or decipher.<br>
  The JSON format is:
  "content": str
  "key": str
- Provides links to use Caesar algorithm in the V2 API.
    - Cipher method at the address: /api/v2/caesar/decipher
    - Decipher method at the address: /api/v2/caesar/decipher

## [1.0.0] - 2023-05-06

First stable version of Vigenere-API.
This update provides an OpenAPI interface to use Caesar algorithm.
You can cipher and decipher content.

### Added features:

- Caesar algorithm [#1](https://etulab.univ-amu.fr/d19006523/vigenere-api/-/issues/1).
    - Cipher method at the address: /api/v1/caesar/decipher
    - Decipher method at the address: /api/v1/caesar/decipher
  
    You need to use the POST method to send the JSON content to cipher or decipher.<br>
    The JSON format is:
    "content": str
    "key": int | str(one character)
- Starter of API.
    To start the API, install the package and run the command:
    ```shell
    python -m vigenere-api
    ```
