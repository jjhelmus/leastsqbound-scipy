leastsqbound
============

What is leastsbound
-------------------

leastsqbound is a enhanced version of scipy's optimize.leastsq function which
allows users to include min, max bounds for each fit parameter. Constraints are 
enforced by using an unconstrained interal parameter list which is transformed
into a constained parameter list using non-linear functions.
