cuesplit
========

Python script that splits CD audio and add metadata tags using the information from CUE sheet.

Based on ffmpeg and libcue. Currently supports flac, mp3 and wav formats.

Requirements
------------

- ffmpeg binary (in $PATH)
- `pylibcue <https://pypi.org/project/pylibcue/>`_

Usage
-----

.. code-block:: bash

	./cuesplit.py -h
	./cuesplit.py -i input.cue -o ./output/ -f mp3 -j 4

License
-------

cuesplit is licensed under the GNU General Public License v2.0.
