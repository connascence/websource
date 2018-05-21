Connascence of Algorithm
########################

:strength: 40
:slug: algorithm
:summary: Connascence of algorithm is when multiple components must agree on a
          particular algorithm.


Connascence of algorithm is when multiple components must agree on a particular
algorithm.

In Data Transmission
====================

Connascence of algorithm frequently occurs when two entities must manipulate
data in the same way. For example, if data is being transmitted from one service
to another, some sort of checksum algorithm is commonly used. The sender and
receiver must agree on which algorithm is to be used. If the sender changes the
algorithm used, the receiver must change as well.

In Data Validation and Encoding
===============================

Consider a hypothetical piece of software that required users to provide a valid
email address when creating an account. The software must validate that the
email address is valid, but this might happen in several places, including:

* In a database model object.
* In a webapp 'controller' class method.
* In a form field in the front-end UI.

These pieces of code might well be in different languages, and will almost
certainly be far apart from each other. The consequence of these algorithms
being different might include users not being able to register, but recieving no
feedback as to why.

Another common example of connascence of algorithm is when unicode strings are
written to disk. Imagine a hypothetical piece of software that writes a data
string to a cache file on disk:

.. code-block:: python

    def write_data_to_cache(data_string):
        with open('/path/to/cache', 'wb') as cache_file:
            cache_file.write(data_string.encode('utf8'))

A matching function is used to retrieve the data from the cache file:

.. code-block:: python

    def read_data_from_cache():
        with open('/path/to/cache', 'rb') as cache_file:
            return cache_file.read().decode('utf8')

The connascence of algorithm here is that both functions must agree on the
encoding being used. If the ``write_data_to_cache`` function changes to encrypt
the data on disk (the data being stored is potentially sensitive), the
``read_data_from_cache`` must also be updated.

In Test Code
============

Test code often contains connascence of algorithm. Consider this hypothetical
test:

.. code-block:: python

    def test_user_fingerprint(self):
        user = User.new(name="Thomi Richards")
        actual = user.fingerprint()
        expected = hashlib.md5(user.name).hexdigest()
        self.assertEqual(expected, actual)

This test is supposed to be testing that the 'fingerprint' method of the
``User`` class works as expected. However, it contains connascence of algorithm,
which limits it's effectiveness. If the ``User`` class ever changes the way
fingerprints are calculated, this test will fail.

