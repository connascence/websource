Connascence of Algorithm
########################

:strength: 40
:slug: algorithm
:summary: Connascence of algorithm is when multiple components must agree on a particular algorithm.


Connascence of algorithm is when multiple components must agree on a particular algorithm. This frequently occurs when two entities must manipulate data in the same way. For example, if data is being transmitted from one service to another, some sort of checksum algorithm is commonly used. The sender and receiver must agree on which algorithm is to be used. If the sender changes the algorithm used, the receiver must change as well.

Consider a hypothetical piece of software that uses a file on disk to cache some expensive calculated result. An example functionto write the data to the cache file might look like this:

.. code-block:: python

	def write_data_to_cache(data_string):
		with open('/path/to/cache', 'wb') as cache_file:
			cache_file.write(data_string.encode('utf8'))

A matching function is used to retrieve the data from the cache file:

.. code-block:: python

	def read_data_from_cache():
		with open('/path/to/cache', 'rb') as cache_file:
			return cache_file.read().decode('utf8')

The connascence of algorithm here is that both functions must aggree on the encoding being used. If the ``write_data_to_cache`` function changes to encrypt the data on disk (the data being stored is potentially sensitive), the ``read_data_from_cache`` must also be updated.

