Connascence of Identity
########################

:strength: 80
:slug: identity
:summary: Connascence of identity is when multiple components must reference the same entity.

Connascence of identity is when multiple components must reference the same entity. A common example is instantiating duplicate objects from a datastore (memory, database, file on disk, etc).

An example is a system user, a shared actor used across an application for task automation:

.. code-block:: ruby

    class SystemUser
      def self.get
        User.find_one(type: "system")
      end
    end

We can use this system user to clean up old tasks:

.. code-block:: ruby

    class TaskCleanup
      def old_tasks
        # find old tasks
      end

      def system_user
        SystemUser.get
      end

      def queue_for_cleanup
        # ↓ one instance of SystemUser in memory
        system_user.queue_for_cleanup(old_tasks)
      end

      def clean
        # ↓ a different instance of SystemUser in memory
        system_user.clean_queued_tasks
      end
    end


In the latter two methods, the `SystemUser` should be the same object. Instead, they point to different objects in memory. One system user now has a bunch of tasks queued, and a different one does the actual cleaning from an empty queue.
