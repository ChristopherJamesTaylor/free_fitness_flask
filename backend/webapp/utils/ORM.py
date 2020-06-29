import datetime
import decimal


class Utils:

    def __init__(self):
        # set up alias for deprecated function name for backward compat
        self.serialize = self.result_to_dict

    def rows_to_dict(self, rows):
        """
        Converts SQLAlchemy column query results (KeyedTuples) to a list of dictionaries
        :param rows: query result
        :returns: (dict[]) list of dictionaries
        """
        # initialize list to return
        data = []
        # loop rows and add each rows worth of data to a dictionary
        try:
            for row in rows:
                d = {}
                for column in row.__table__.columns:
                    d[column.name] = getattr(row, column.name)
                # append dictionary object to array
                data.append(d)
        except:
            for row in rows:
                row_as_dict = row.__dict__
                data.append(row_as_dict)

        return data

    def result_to_dict(self, obj, flatten=False, exclude=None):
        """
        Utility method that converts result objects/lists to embedded dict/lists for easy serialization, works with
        KeyedTuple objects (from ORM queries where columns are selected explicitly) DeclarativeBase objects (from
        entity queries), and ResultProxy objects (from raw queries executed by the sqlalchemy session or results
        of SQLAlchemy core queries)
        :param obj: (object or list) the SQLAlchemy result (single object or list of objects)
        :param flatten: (boolean) flag to flatten the structure of resultant dictionaries if they contain child
                        dictionaries (from converting DeclarativeBase objects)
        :param exclude: (object) object/type in tree to exclude from serialization. Primarily used internally to prevent
                        infinite recursion errors caused by bi-directional relationships
        :return: (list or dict) representation of SQLAlchemy result(s) as a python dictionary or list of dictionaries
        """
        # set up keyword args for use in recursive calls
        kwargs = {'flatten': flatten, 'exclude': exclude}
        # check to see if this is a list or a single object and call function recursively on objects if it's a list
        if isinstance(obj, list):
            return [self.result_to_dict(row, **kwargs) for row in obj]
        elif hasattr(obj, "__table__"):
            # this is an SQLAlchemy (DeclarativeBase mapper) object
            result_dict = {}
            for key, val in obj.__dict__.items():
                if key is None or key.startswith("_"):
                    continue
                if isinstance(val, list):
                    # skip this attribute if this collection points back at instances of a parent object
                    #  or we are excluding it (prevent infinte loop)
                    if len(val) and (isinstance(val[0], obj.__class__) or (isinstance(val[0], exclude.__class__))):
                        continue
                    # otherwise embed a list into the dict key, excluding any descendants of the same type
                    else:
                        kwargs['exclude'] = obj
                        element = self.result_to_dict(val, **kwargs)
                # see if this element is a child object (excluding anything that references back to the parent)
                elif hasattr(val, "__dict__"):
                    # exclude any child objects that refer back to parent
                    if isinstance(val, obj.__class__) or isinstance(val, exclude.__class__):
                        continue
                    element = self.result_to_dict(val, **kwargs)
                else:
                    element = self.format_value(val)
                if isinstance(element, dict) and flatten:
                    # if this property is a child object (dictionary) and we're flattening, merge the child dict into
                    # the parent dict, without overwriting any keys in the parent (why a simple .update() is not used)
                    result_dict.update(dict([(k, v) for k, v in element.items() if k not in result_dict]))
                    # this would be for keeping all keys and namespacing child subkeys under parent keys
                    # result_dict.update(dict([(key + "." + k, v) for k, v in element.iteritems()]))
                else:
                    result_dict[key] = element
            return result_dict
        else:  # this is not the result of an entity query, so should be column query or raw query
            return self.query_result_to_dict(obj)

    def query_result_to_dict(self, obj):
        """
        Formats results from SQLAlchemy ORM column queries or raw SQL queries from session.execute()
        :param obj: The result of an SQLAlchemy query that isn't a DeclarativeBase object or list of
                    these. Covers ResultProxy, RowProxy, and KeyedTuple results
        """
        if obj.__class__.__name__ == 'ResultProxy':
            # if this is a ResultProxy object return a list of one dict for each row
            return [{this_property: self.format_value(row[this_property]) for this_property in list(row.keys())} for row in obj]
        elif obj.__class__.__name__ == 'RowProxy':
            # this is a RowProxy object which is one result from a ResultProxy object
            return {key: self.format_value(obj[key]) for key in list(obj.keys())}
        elif obj.__class__.__name__ == 'result':
            # this is a list of lightweight KeyedTuple objects for column ORM queries
            return {key: self.format_value(obj._asdict()[key]) for key in list(obj._asdict().keys())}
        elif hasattr(obj, '__dict__'):
            # this is a plain python object
            return {key: self.format_value(obj.__dict__[key]) for key in obj.__dict__}
        return obj  # by default just return the object

    def format_value(self, value):
        """
        Formats a result value so that it can be json serialized. Takes care of converting dates and
        decimal values to JSON-serializable formats.
        :param value:
        :return: the formatted value
        """
        # if this property is a date or datetime, set the value as the string representation
        if isinstance(value, datetime.datetime):
            value = value.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(value, datetime.date):
            value = value.strftime('%Y-%m-%d')
        elif isinstance(value, datetime.time):
            value = value.strftime('%I:%M')
        elif isinstance(value, decimal.Decimal):
            # have to convert decimals to floats because some json encoders can't encode Decimal types
            value = float(value)
        return value

    def get_sort_column(self, Model, obj_property, direction):
        """
        Returns the sort column and direction for grid sorting when passed in a SQLAlchemy object
        property and a direction. Enables dynamic argument for order_by() method on a query object
        in SQLAlchemy.
        :param Model: the DeclarativeBase class (db.Model when using Flask-SQLAlchemy extension)
        :param obj_property: the object property in the format 'Class.property'
        :param direction: 'asc' or 'desc'
        :return: A column property with either the .asc() or .desc() method to pass into an order_by()
        """
        sort_class, sort_property = obj_property.split(".")
        # use the registry of class names in declarative to get the class that the sorted property belongs to
        sort_table = Model._decl_class_registry[sort_class]
        # use getattr to dynamically get the property to sort by
        sort_column = getattr(sort_table, sort_property)

        # dynamic way of calling .asc() or .desc() methods for sorting on the given property
        column_sorted = getattr(sort_column, direction)()

        return column_sorted



