import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print('setup')
        self.emp_1 = Employee('Dimple','Gupta',50000)
        self.emp_2 = Employee('Ridvik','Trivedi',45000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email,'Dimple.Gupta@gmail.com')
        self.assertEqual(self.emp_2.email,'Ridvik.Trivedi@gmail.com')

        self.emp_1.first = 'Pankaj'
        self.emp_2.first = 'Shubham'

        self.assertEqual(self.emp_1.email,'Pankaj.Gupta@gmail.com')
        self.assertEqual(self.emp_2.email,'Shubham.Trivedi@gmail.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname,'Dimple Gupta')
        self.assertEqual(self.emp_2.fullname,'Ridvik Trivedi')

        self.emp_1.first = 'Pankaj'
        self.emp_2.first = 'Shubham'

        self.assertEqual(self.emp_1.fullname,'Pankaj Gupta')
        self.assertEqual(self.emp_2.fullname,'Shubham Trivedi')

    def test_apply_raise(self):
        print('test_apply_raise')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay,52500)
        self.assertEqual(self.emp_2.pay,47250)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule =  self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Gupta/May')
            self.assertEqual(schedule,'Success')
    
            mocked_get.return_value.ok = False
            
            schedule =  self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Trivedi/June')
            self.assertEqual(schedule,'Bad Response!')
    

if __name__ == '__main__':
    unittest.main()