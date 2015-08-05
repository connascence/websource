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