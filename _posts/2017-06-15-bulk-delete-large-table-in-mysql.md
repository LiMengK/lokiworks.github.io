---
layout: post
title: MySQL下大表批量删除的惯用手法
keywords:
  - Mysql
description: 
category: DB
tags:
  - Mysql
published: true
---
{% include JB/setup %}

# MySQL下大表批量删除的惯用手法
Make a temp table, switch it in and out, and copy the last 30 days data into it.

```
#
# Make empty temp table
#
CREATE TABLE NOTIFICATION_NEW LIKE NOTIFICATION;
#
# Switch in new empty temp table
#
RENAME TABLE NOTIFICATION TO NOTIFICATION_OLD,NOTIFICATION_NEW TO NOTIFICATION;
#
# Retrieve last 30 days data 
#
INSERT INTO NOTIFICATION SELECT * FROM NOTIFICATION_OLD
WHERE CreatedAt < DATE_SUB(CURDATE(), INTERVAL 30 day);
```
In your off hours, drop the old table
```
DROP TABLE NOTIFICATION_OLD;
```
## Here are the Advantages to doing DELETEs like this

* NOTIFICATION is emptied fast by means switching in an empty table.
* NOTIFICATION is immediately available for new INSERTs
* The remaining 30 days are added back into NOTIFICATION while new INSERTs can take place.
* Dropping the old version of NOTIFICATION does not interfere with new INSERTs
* NOTE : I have recommended doing bait-and-switch for table DELETEs before : (See my July 19, 2012 post : Optimizing DELETE Query on MySQL MEMORY Table)

## reference
(https://dba.stackexchange.com/questions/83109/bulk-delete-for-large-table-in-mysql)
