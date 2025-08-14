#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, 'lib')
sys.path.insert(0, '.')
os.chdir('lib')

import unittest

# Import all test classes
from testing.department_orm_test import TestDepartment
from testing.department_property_test import TestDepartmentProperties
from testing.employee_orm_test import TestEmployee
from testing.employee_property_test import TestEmployeeProperties

if __name__ == '__main__':
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestDepartment))
    suite.addTests(loader.loadTestsFromTestCase(TestDepartmentProperties))
    suite.addTests(loader.loadTestsFromTestCase(TestEmployee))
    suite.addTests(loader.loadTestsFromTestCase(TestEmployeeProperties))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with error code if tests failed
    sys.exit(0 if result.wasSuccessful() else 1)