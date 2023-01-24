# PyTest Features - Fixtures, Params, Scope
Learn to use the following features of PyTest

Fixtures

Params

Scope

conftest.py

Auto-use fixtures

Execution-order of fixtures


# Why PyTest ?
Minimal amount of boilerplate, rich features, and a growing number of plugins.

# What is Fixture?
Examples of fixtures could be loading test set to the database, reading a configuration file, setting up environment variables, etc.
Fixture plays a quite important role in Pytest. Compared to the classic xUnit style where you normally have a setup() and teardown() function, the fixture in Pytest is more flexible and flat. Each fixture is defined using the @pytest.fixture decorator on top of a function and this function will do the job like reading a configuration file.

# What is the scope of a fixture?
There are ~5 scopes for a fixture in pytest: function, class, module, package and session

More: https://betterprogramming.pub/understand-5-scopes-of-pytest-fixtures-1b607b5c19ed
