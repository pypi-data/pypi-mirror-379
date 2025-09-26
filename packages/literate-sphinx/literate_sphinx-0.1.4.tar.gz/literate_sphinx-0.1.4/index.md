# Literate Sphinx

Literate Sphinx is a [literate
programming](https://en.wikipedia.org/wiki/Literate_programming) extension for
[Sphinx](https://www.sphinx-doc.org/).  Literate programming is a method for
writing code interleaved with text.  With literate programming, code is
intended to be written in an order that makes sense to a human reader, rather
than a computer.

Producing the human-readable document from the document source is called
"weaving", while producing the computer-readable code is called "tangling".  In
this extension, the weaving process is the normal Sphinx rendering process.
For tangling, this extension provides a `tangle` builder — running
`make tangle` will output the computer-readable files in `_build/tangle`.

As is customary with literate programming tools, the extension is also [written
in a literate programming style](code.md).

## Usage

Install the extension by running `pip install literate-sphinx`, and add
`'literate_sphinx'` to the `extensions` list in your `conf.py`.

Code chunks are written using the `literate-code` directive, which takes the
name of the chunk as its argument.  It takes the following options:

* `lang`: the language of the chunk.  Defaults to `highlight_language`
  specified in `conf.py`
* `file`: (takes no value) present if the chunk is a file.  If the chunk is a
  file, then the code chunk name
* `class`: a list of class names separated by spaces to add to the HTML output
* `padding`: when multiple chunks have the same name, they are written out
  sequentially.  The `padding` indicates how many blank lines (if any) there
  should be between this chunk and the *previous* chunk of the same name.
  Defaults to `default_chunk_padding` specified in `conf.py`, which itself
  defaults to 1.  If given without an argument, one blank line is used.
* `name`: a target name that can be referenced by `ref` or `numref`.  This
  should not be confused with the code chunk name.

e.g in ReST

```rst
.. literate-code:: code chunk name
   :lang: python

   def hello():
       print("Hello world")
```

or in Markdown using [MyST
parser](https://myst-parser.readthedocs.io/en/latest/index.html)

~~~markdown
```{literate-code} code chunk name
:lang: python

def hello():
    print("Hello world")
```
~~~

To include another code chunk, enclose it between `{{` and `}}` delimiters.
Only one code chunk is allowed per line.  The code chunk will be prefixed with
everything before the delimiters on the line, and suffixed by everything after
the delimiters.

For example,

```rst
.. literate-code:: file.py
   :file:
   # before
   {{code chunk name}}
   # after
```

will produce a file called `file.py` with the contents

```python
# before
def hello():
    print("Hello world")
# after
```

and

```rst
.. literate-code:: file.py
   :file:
   # before
   class Hello:
       {{code chunk name}} # suffix
   # after
```

will produce

```python
# before
class Hello:
    def hello(): # suffix
        print("Hello world") # suffix
# after
```

The delimiters can be changed by setting the `literate_delimiters` option in
`conf.py`, which takes a tuple, where the first element is the left delimiter
and the second element is the right delimiter.  For example:

```python
literate_delimiters = ('<<', '>>')
```

The same code chunk name can be used for multiple chunks; they will be included
in the same order that they appear in the document.  If the document is split
across multiple files, they will be processed in the same order as they appear
in the table of contents as defined in the `toctree` directive.

In addition to the `tangle` builder for tangling the document into
computer-readable code files, there is an `annotated-tangle` builder, which
writes the computer-readable code to HTML files, annotated by the chunks that
they come from.  You can see an example by viewing the <a
href="_annotated/literate_sphinx.py.html">annotated tangling of this
project</a>.

```{toctree}
---
maxdepth: 2
caption: "More:"
---
code
```

## License

This software may be redistributed under the same license as Sphinx.

```{literate-code} copyright license
:lang: text

Copyright Hubert Chathi <hubert@uhoreg.ca>

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

SPDX-License-Identifier: BSD-2-Clause
```
