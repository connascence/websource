Connascence of Position
#######################

:strength: 30
:slug: position
:summary: Connascence of position is when multiple components must agree on the
          order of values.


Connascence of position is when multiple entities must agree on the order of
values.

In Data Structures
==================

For example, consider a function that retrieves a user's details:

.. code-block:: python

    def get_user_details():
        # Returns a user's details as a list:
        # first_name, last_name, year_of_birth, is_admin
        return ["Thomas", "Richards", 1984, True]

This is a somewhat contrived example, but it's not uncommon to see data returned
in lists or tuples. Elsewhere in the code we might need to perform some check on
whether the user is an administrator or not:

.. code-block:: python

    def launch_nukes(user):
        if user[3]:
            # actually launch the nukes
        else:
            raise PermissionDeniedError("User is not an administrator!")

These two functions are linked by *connascence of position*. If the order of the
values in the user list ever changes, both locations must be updated (this
example is particularly scary if someone were to update the user list to be
``[first_name, initials, last_name, year_of_birth, is_admin]`` without updating
the check inside launch_nukes).

This connascence can be improved to connascence of name by turning the list into
a dictionary or class. The following example shows how the above functions might
look as a dictionary:

.. code-block:: python

    def get_user_details():
        return {
            "first_name": "Thomas",
            "last_name": "Richards",
            "year_of_birth": 1984,
            "is_admin": True,
        }


    def launch_nukes(user):
        if user['is_admin']:
            # actually launch the nukes
        else:
            raise PermissionDeniedError("User is not an administrator!")

Note that these two functions are still coupled, but we've turned connascence of
position into the weaker connascence of name. This has also increased the
readability of the ``get_user_details`` function - the explicit comment is no
longer needed to document the order of the keys.

A similar solution is to use a class instead of a dictionary, and this can be
beneficial if the structure being returned has constraints or operations
associated with it.

In Function Arguments
=====================

Connascence of position also frequently occurs in function argument lists.
Consider the following function declaration from a mythical email-sending
utility library:

.. code-block:: python

    def send_email(firstname, lastname, email, subject, body, attachments=None):

Code calling this ``send_email`` function must remember the order of arguments.
Should that order ever change, all calling locations must also be updated. This
example could also be improved to connascence of name by passing a structured
object (a class or dictionary) instead of a number of parameters.

