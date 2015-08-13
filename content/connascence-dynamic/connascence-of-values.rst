Connascence of Value
########################

:strength: 70
:slug: values
:summary: Connascence of value is when several values must change together.

Connascence of value is when several values must change together. This frequently occurs between production code and test code. For example, consider an ``Article`` class, which represents a blog article. When it is instantiated, it is given some text contents, and its initial 'state' is 'draft':

.. code-block:: python

    class ArticleState(Enum):
        Draft = 1
        Published = 2


    class Article(object):

        def __init__(self, contents):
            self.contents = contents
            self.state = ArticleState.Draft

        def publish(self):
            # do whatever is required to publish the article.
            self.state = ArticleState.Published

Now imagine a hypothetical test that ensures that the ``publish`` method works:

.. code-block:: python

    article = Article("Test Contents")
    assert article.state == ArticleState.Draft
    article.publish()
    assert article.state == ArticleState.Published

The problem here is that the test requires knowledge of the initial state of the ``Article`` class: if the Article's initial state is ever changed, this test will break (this is arguably a bad test, since the first assertion has little to do with the intent of the test, but it's a common mistake). This code can be improved by adding an ``InitialState`` label to ``ArticleClass``, and changing both the ``Article`` class and the test to refer to that label instead:

.. code-block:: python

    class ArticleState(Enum):
        InitialState = 1
        Draft = 1
        Published = 2

        
    class Article(object):

        def __init__(self, contents):
            self.contents = contents
            self.state = ArticleState.InitialState


The test now becomes:

.. code-block:: python

    article = Article("Test Contents")
    assert article.state == ArticleState.InitialState
    article.publish()
    assert article.state == ArticleState.Published

Should we need to change the state machine of the ``Article`` class, we can do so by changing the ``ArticleState`` enumeration:

.. code-block:: python

    class ArticleState(Enum):
        InitialState = 1
        Preproduction = 1
        Draft = 2
        Published = 2

We have effectively introduced a level of indirection between the ``Article`` class and its initial state value.