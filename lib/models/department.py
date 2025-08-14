# lib/models/department.py
from models.__init__ import CURSOR, CONN


class Department:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, location, id=None):
        self.id = id
        self._validate_and_set_name(name)
        self._validate_and_set_location(location)

    def __repr__(self):
        return "<Department {}: {}, {}>".format(self.id, self.name, self.location)

    def _validate_and_set_name(self, name):
        try:
            string_types = (str, unicode)
        except NameError:
            string_types = (str,)
        if not isinstance(name, string_types):
            raise ValueError("Name must be a non-empty string")
        if len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
    
    def _validate_and_set_location(self, location):
        try:
            string_types = (str, unicode)
        except NameError:
            string_types = (str,)
        if not isinstance(location, string_types):
            raise ValueError("Location must be a non-empty string")
        if len(location) == 0:
            raise ValueError("Location must be a non-empty string")
        self._location = location
    
    def __setattr__(self, attr_name, value):
        if attr_name == 'name' and hasattr(self, '_name'):
            self._validate_and_set_name(value)
        elif attr_name == 'location' and hasattr(self, '_location'):
            self._validate_and_set_location(value)
        else:
            self.__dict__[attr_name] = value
    
    @property
    def name(self):
        return self._name
    
    @property
    def location(self):
        return self._location

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO departments (name, location)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
        self.__class__.all[self.id] = self

    @classmethod
    def create(cls, name, location):
        """ Initialize a new Department instance and save the object to the database """
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        """Update the table row corresponding to the current Department instance."""
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Department instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM departments
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del self.__class__.all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Department object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        department = cls.all.get(row[0])
        if department:
            # ensure attributes match row values in case local instance was modified
            department.name = row[1]
            department.location = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            department = cls(row[1], row[2])
            department.id = row[0]
            cls.all[department.id] = department
        return department

    @classmethod
    def get_all(cls):
        """Return a list containing a Department object per row in the table"""
        sql = """
            SELECT *
            FROM departments
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Department object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM departments
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Department object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM departments
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def employees(self):
        """Return list of employees associated with current department"""
        from models.employee import Employee
        sql = """
            SELECT * FROM employees
            WHERE department_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Employee.instance_from_db(row) for row in rows
        ]