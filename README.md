Bucket Filter
============

A filtering library to present data that matches a series of conditional expressions

-----


Bucket filter is a python library that allows creating multiple buckets each linked to a condition and having various 
data, each identified by a unique ID.
It then allows for combining various buckets in a serious of conditinal operators and filters out those IDs that match 
a given expression.


Example
-------

Lets say there are 3 buckets with conditions c1, c2, c3 as defined below 

1. c1 --> id1, id2, id3
2. c2 --> id3, id4, id5
3. c3 --> id2, id3, id6

an expression

    C = c1 & (c2 || c3)

would result in

    ==> C = (id1, id2, id3) & (id3, id4, id5 id2, id6)

    ==> C = (id2, id3)

**NOTE** 

1.  The library does not evaluate individual conditions, only joins the filters as defined by the expression
    *   The library does an exact expression match, so if while registering one uses hasData=True, the library expects 
       the same expression when evaluating
2.  Standard evaluation rules apply, left to right, expressions in braces are done first
3.  Elements in the bucket __MUST__ have a accessible attribute _id_ else will be evicted out of the bucket
-----

License
======

