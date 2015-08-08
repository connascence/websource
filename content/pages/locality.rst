Locality
########

:slug: locality
:strength: 10

The *locality* of an instance of connascence is how close the two entities are to each other. Code that is close together (in the same module, class, or function) should typically have more, and higher forms of connascence than code that is far apart (in separate modules, or even codebases). Many of the stronger forms of connascance that can be devastating to the readability and maintainability of a codebase when they appear far apart are innocuous when close together.

.. image:: {filename}/images/locality.svg
	:class: center-block

Locality matters! Stronger connascences are more acceptible within a module. Weaker connascences should be used between entities that are far apart (in separate modules or even codebases).