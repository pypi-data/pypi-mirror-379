# Copyright 2023-2025 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Development
===========

Semantic versioning
-------------------

Maintainer has adopted strict 3 digit
`semantic versioning <https://semver.org>`_
and does not use
`caps on dependencies <https://iscinumpy.dev/post/bound-version-constraints>`_.
This allows for more package management flexibility for developers and
access to the latest features.

Periodically coordinated releases of versions are done for those concerned with
stability. These are also posted in the project's
`CHANGELOG <https://github.com/grscheller/pythonic-fp/blob/main/CHANGELOG.rst>`_.

Module dependencies
-------------------

Current module dependencies where arrows point from modules to their
dependencies. There are no external dependency except for the Python
standard library.

.. graphviz::

    digraph Modules {
        bgcolor="#957fb8";
        node [style=filled, fillcolor="#181616", fontcolor="#dcd7ba"];
        edge [color="#181616", fontcolor="#dcd7ba"];
        containers -> fptools;
        containers -> iterables;
        containers -> circulararray;
        splitends -> fptools;
        splitends -> iterables;
        splitends -> queues;
        queues -> fptools;
        queues -> circulararray;
        circulararray -> gadgets;
        fptools -> circulararray;
        fptools -> gadgets;
        fptools -> booleans;
        booleans -> gadgets;
        iterables -> gadgets;
        iterables -> fptools;
    }

Coordinated releases
--------------------

Release - 2025-09-TBD
~~~~~~~~~~~~~~~~~~~~~

+----------------+---------------------------+---------+
| Name           | PyPI Project              | version |
+================+===========================+=========+
| Booleans       | pythonic-fp-booleans      | 2.0.0   |
+----------------+---------------------------+---------+
| Circular Array | pythonic-fp-circulararray | 6.0.0   |
+----------------+---------------------------+---------+
| Containers     | pythonic-fp-containers    | 4.0.0   |
+----------------+---------------------------+---------+
| FP Tools       | pythonic-fp-fptools       | 5.1.2   |
+----------------+---------------------------+---------+
| Gadgets        | pythonic-fp-gadgets       | 3.1.0   |
+----------------+---------------------------+---------+
| Iterables      | pythonic-fp-iterables     | 5.1.2   |
+----------------+---------------------------+---------+
| Queues         | pythonic-fp-queues        | 3.1.0   |
+----------------+---------------------------+---------+
| Splitends      | pythonic-fp-splitends     | 2.0.0   |
+----------------+---------------------------+---------+

Release - 2025-09-15
~~~~~~~~~~~~~~~~~~~~

+----------------+---------------------------+---------+
| Name           | PyPI Project              | version |
+================+===========================+=========+
| Booleans       | pythonic-fp-booleans      | 1.1.2   |
+----------------+---------------------------+---------+
| Circular Array | pythonic-fp-circulararray | 5.3.2   |
+----------------+---------------------------+---------+
| Containers     | pythonic-fp-containers    | 3.0.1   |
+----------------+---------------------------+---------+
| FP Tools       | pythonic-fp-fptools       | 5.1.1   |
+----------------+---------------------------+---------+
| Gadgets        | pythonic-fp-gadgets       | 3.0.1   |
+----------------+---------------------------+---------+
| Iterables      | pythonic-fp-iterables     | 5.1.1   |
+----------------+---------------------------+---------+
| Sentinels      | pythonic-fp-sentinels     | 2.1.0   |
+----------------+---------------------------+---------+
| Splitends      | pythonic-fp-splitends     | 1.0.2   |
+----------------+---------------------------+---------+

"""
