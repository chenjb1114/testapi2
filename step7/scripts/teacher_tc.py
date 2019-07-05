import unittest
from po.myedu.addTeacher import Teacher
from libs.Tools import VerifyClass

class TestTeacherApi(VerifyClass):

    def setUp(self):
        self.p = Teacher()

    def test_teacher_success_001(self):
        result = self.p.apiTeacher()
        self.verify_code(result,200)
        self.verify_html(result,'13524270178')

if __name__ == '__main__':
    unittest.main()