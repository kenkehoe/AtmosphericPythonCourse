One of the best ways to ensure you do not mess something up when you make a change to your
code base is to write testing software. The software is not used while doing research but
is used to ensure that the code does what you expect it to. It typically does this by having
a set of known data and the expected results when that data is used. If the code continues
to have the same results after you made a change, you can safely assume you did not introduce
any new bugs (existing bugs still remaing unfortunatly). If you did unintentionally introduce
a change to the way a function processes the data, the different result will cause the test
to fail and you will be notified.

Since the testing code will only find changes to expectation on code it runs it is up to you
to add as many tests as necessary to ensure you are coverting all the possible ways to use the
code. But there is no point to make an infinite number of tests and never improving the code
so there is a balance you need to find.
