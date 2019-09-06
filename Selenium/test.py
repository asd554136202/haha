import unittest
import case


class AddTeacherClass(unittest.TestCase):
    def test_add_success001(self):
        driver = case.createDriver()
        case.login(driver)
        case.memberCenter(driver)
        case.addTeacher(driver)
        data = case.getTeacher(driver)
        self.assertEqual(data, '18806643212')


if __name__ == '__main__':
    unittest.main(verbosity=2)
