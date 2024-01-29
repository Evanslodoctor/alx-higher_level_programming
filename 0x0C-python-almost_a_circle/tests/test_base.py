class TestBaseMethods(unittest.TestCase):
    """ Defines tests for Base class """

    def test_check_instance_variables(self):
        """ Checks instance variables """
        
        new_base = Base(id=1)
        instance_1 = Base()
        
        self.assertEqual(new_base.id, 1)

# Uncomment other test methods as needed...
