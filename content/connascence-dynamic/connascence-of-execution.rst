Connascence of Execution
########################

:strength: 50
:slug: execution
:summary: Connascence of execution is when the order of execution of multiple
          components is important.

Connascence of execution is when the order of execution of multiple components
is important. Common examples include locking and unlocking resources, where
locks must be acquired and released in the same order everywhere in the entire
codebase.

Connascence of execution can also occur when using objects that encapsulate a
state machine, and that state machine only allows certain operations in certain
states. For example, consider a hypothetical ``EmailSender`` class that allows a
caller to generate and send an email:

.. code-block:: python

	email = Email()
	email.setRecipient("foo@example.comp")
	email.setSender("me@mydomain.com")
	email.send()
	email.setSubject("Hello World")

The last two lines show a trivial example of connascence of execution. The
``setSubject`` method cannot be called after the ``send`` method (at best it
will do nothing). In this example the `locality
<{filename}/properties/locality.rst>`_ of the coupling is very low, but cases
where the locality is very high can be much harder to find and fix (consider,
for example a scenario where the last two lines are called on separate threads).

