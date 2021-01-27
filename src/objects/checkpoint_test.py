import unittest
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import (String, Integer, Float, Boolean)
from NotReceived import NotReceived

unittest.TestLoader.sortTestMethodsUsing = None

class checkpoint_TestCase(unittest.TestCase):

	def setUp(self):
		pass       
		
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")

	#Note: Tests are run alphapetically
	def test_0_test(self):
		self.assertEqual(1,1)
		print("Test 1:Hello, Tests!")



	def test_1_1_convert_class_to_dict(self):
		#Testing with a normal class
		Base = declarative_base()
		class saTestClass2(Base):
			__tablename__="hi"
			id = Column(Integer, primary_key=True, nullable=False)
			name = Column(String(63))
			price = Column(Float())
			in_stock = Column(Boolean())
		print("Test 1_1:convert_class_to_dict")









# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()