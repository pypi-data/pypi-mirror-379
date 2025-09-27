# gwtc

A library for creating and interacting with Gravitational Wave Transient Catalogs in gracedb.

[[_TOC_]]

## Authentication

This package uses the `ligo-gracedb` client for authentication. Please refer to the [GraceDB documentation on SciTokens](https://gracedb.ligo.org/documentation/authentication.html) for information on how to authenticate using SciTokens.

## Tutorial

Please see: https://git.ligo.org/chad-hanna/gwtc/-/blob/main/examples/README.md


## installation from source

*Note these instructions will be improved and we will make this available in Conda*. This is just an example, modify as you see fit.

```
$ ssh chad.hanna@ldas-pcdev1.ligo-wa.caltech.edu
(igwn) [chad.hanna@ldas-pcdev1 ~]$ mkdir git
(igwn) [chad.hanna@ldas-pcdev1 ~]$ cd git
(igwn) [chad.hanna@ldas-pcdev1 git]$ git clone git@git.ligo.org:chad-hanna/gwtc.git
(igwn) [chad.hanna@ldas-pcdev1 git]$ pip install ./gwtc
```

### See latest catalog on gracedb

https://gracedb-test.ligo.org/api/gwtc/4/latest/

### See previous version on gracedb

https://gracedb-test.ligo.org/api/gwtc/4/1/



