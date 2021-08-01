



def read(table, **kwargs):
    """ Generates SQL for a SELECT statement matching the kwargs passed. """
    sql = list()
    sql.append("SELECT * FROM %s " % table)
    if kwargs:
        sql.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
    sql.append(";")
    return "".join(sql)


def upsert(obj):
    """ update/insert rows into objects table (update if the row already exists)
        given the key-value pairs in kwargs """
    table=obj.__class__.__name__
    kwargs= obj.__dict__
    keys = ["%s" % remove_prefix(k,"_") for k in kwargs]
    #values = ["'%s'" % v for v in kwargs.values()]
    values = []
    for value in kwargs.values():
       if type(value) is str:
         values.append("'%s'" % (value))
       elif value is None:
         values.append("%s" % ("''"))
       else:
         values.append("%s" % value)
    sql = list()
    sql.append("INSERT INTO %s (" % table)
    sql.append(", ".join(keys))
    sql.append(") VALUES (")
    sql.append(", ".join(values))
    sql.append(") ON DUPLICATE KEY UPDATE ")
    sql.append(", ".join("%s = '%s'" % (k, v) for k, v in kwargs.items()))
    sql.append(";")
    return "".join(sql)



def delete(table, **kwargs):
    """ deletes rows from table where **kwargs match """
    sql = list()
    sql.append("DELETE FROM %s " % table)
    sql.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
    sql.append(";")
    return "".join(sql)

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text