Connascence of Meaning
######################

:strength: 20
:slug: meaning
:summary: Connascence of meaning is when multiple components must agree on the meaning of particular values.


Connascence of meaning is when multiple components must agree on the meaning of particular values. Consider some code that processes credit card payments. The following function might be used to determine if a given credit card number is valid or not:

.. code-block:: python

	def is_credit_card_number_valid(card_number):
		# Check for 'test' credit card numbers:
		if card_number == "9999-9999-9999-9999":
			return True
		# Do normal validation:
		# ...

The problem here is that all parts of this system must agree that "9999-9999-9999-9999" is the test credit card number. If that value changes in one place, it must also change in another.

Here's another example where user roles are encoded as integers:

.. code-block:: python

	def get_user_role(username):
		user = database.get_user_object_for_username(username)
		if user.is_admin:
			return 2
		elif user.is_manager:
			return 1
		else:
			return 0

Elsewhere, code might need to check that a given username is an administrator, like so:

.. code-block:: python

	if get_user_role(username) != 2:
		raise PermissionDenied("You must be an administrator")

Connascence of meaning can be improved to connascence of name by moving the "magic values" to named constants, and referring to the constants instead of the values. However in doing so, we have increased the amount of connascence of name (since we now need a third location to store the constant).

Another common example of connascence of meaning is when ``None`` is used as a return value. This frequently occurs in functions that are tasked with finding an object. If that object isn't found, the function might return ``None``. 

.. code-block:: python

	def find_user_in_database(username):
		return database.find_user(username=username) or None

However, the function might also return None in an error condition:

.. code-block:: python

	def find_user_in_database(username):
		try:
			return database.find_user(username=username)
		except DatabaseError:
			return None

The problem in both these cases is that a semantic meaning is being assigned to the ``None`` value. If multiple different meanings are assigned to the same ``None`` value in the same codebase, the programmer must remember which meaning applies to which case. This can be improved to connascence of name by returning an explicit object that represents the case in question:

.. code-block:: python

	def find_user_in_database(username):
		return database.find_user(username=username) or ObjectNotFound

Another common example of connascence of meaning is when we use primative numeric types to represent more complex values. Consider this line of code in a codebase that processes payments:

.. code-block:: python

	unit_cost = 49.95

What currency is that cost expressed in? US dollars? British pounds? How do you ensure that two costs with different currencies are not added together? Similar to the examples above, the problem is that a semantic meaning is being added to the primative type. It can be improved to connascence of type by creating a 'Cost' type that disallows operations between different currencies:

.. code-block:: python

	unit_cost = Cost(49.95, 'USD')
