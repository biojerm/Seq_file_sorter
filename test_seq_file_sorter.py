import unittest
import os
import tempfile
import seq_file_sorter as fs
from unittest.mock import patch
from unittest.mock import MagicMock
from test import support

import unittest
from test import support

class TestSeqFileSorter(unittest.TestCase):

	def setUp(self):
		self.file_path = os.path.dirname(os.path.abspath(__file__))

	def tearDown(self):
		pass
	def test_seq_files_present(self):
		#finds a temp ab1 file
		with tempfile.NamedTemporaryFile(suffix='.ab1',dir=self.file_path) as tf:
			self.assertTrue(fs.seq_files_present(),"Should return true if .ab1 file in directory")
		# finds temp .seq
		with tempfile.NamedTemporaryFile(suffix='.seq',dir=self.file_path) as tf:
			self.assertTrue(fs.seq_files_present(),"Should return true if .seq file in directory")
		# should fail if 
		with tempfile.NamedTemporaryFile(suffix='.anythingelse',dir=self.file_path) as tf:
			self.assertFalse(fs.seq_files_present(),"Should return false if not .seq or .ab1 file in directory")
	
	def test_file_name_pattern(self):
		# returns correct regex for a given file name
		self.assertEqual(fs.choose_regex('JL_470815-501_US_NDT80_pUC-Seq-F_A12.ab1')[0],
			'([A-Z]+_[0-9]+-[0-9]+_)(.*)([-|_][A-Z]+[0-9]+)(.(ab1|seq))','The correct regular expression for ELIM')
		self.assertEqual(fs.choose_regex('JL_470815-501_US_NDT80_pUC-Seq-F_A12.ab1')[1],
			(2,4,5),'need to return correct important groups')

		self.assertEqual(fs.choose_regex('H1_JL62_2017-01-20_E06.ab1')[0],
			'(.*)(_\d{4}-\d{2}-\d{2}_[a-hA-H]\d*)(.(ab1|seq))','The correct regular expression needs to be returned')
		self.assertEqual(fs.choose_regex('H1_JL62_2017-01-20_E06.ab1')[1],
			(1,3,4),'need to return correct important groups')
		
		self.assertEqual(fs.choose_regex('JL_535622-623_7-1_oJL330C04.seq')[0],
			'([A-Z]+_[0-9]+-[0-9]+_)(.*[_|-][a-zA-Z]+[0-9]+)([a-hA-H]\d*)(.(ab1|seq))','The correct regular expression needs to be returned ELIM2')
		self.assertEqual(fs.choose_regex('JL_535622-623_7-1_oJL330C04.seq')[1],
			(2,4,5),'need to return correct important groups')
		
		with self.assertRaises(ValueError) as cm:
			fs.choose_regex('anyfilename.ab1')
		self.assertEqual('The file anyfilename.ab1 did not match existing file patterns.', str(cm.exception)) # checks correct error
	
	@patch('seq_file_sorter.os.makedirs')
	@patch('seq_file_sorter.os.path.exists')	
	def test_folders_not_created_if_present(self, mock_exists, mock_make_dirs):
		mock_exists.return_value = True
		fs.create_seq_folders()
		self.assertEqual(len(mock_make_dirs.mock_calls),0)

	@patch('seq_file_sorter.os.makedirs')
	@patch('seq_file_sorter.os.path.exists')	
	def test_folders_created_if_not_present(self, mock_exists, mock_make_dirs):
		mock_exists.return_value = False
		fs.create_seq_folders()
		self.assertEqual(len(mock_make_dirs.mock_calls),2)

	@patch('seq_file_sorter.input', return_value ='yes')
	def test_yes_or_no_reply_y(self, reply):
		self.assertTrue(fs.yes_or_no('Any question?'))
	
	@patch('seq_file_sorter.input', return_value ='no')
	def test_yes_or_no_reply_n(self, reply):
		self.assertFalse(fs.yes_or_no('Any question?'))

	@patch('seq_file_sorter.input', return_value ='no')
	def test_yes_or_no_reply_n(self, reply):
		self.assertFalse(fs.yes_or_no('Any question?'))

	@patch('builtins.input', side_effect=['1','y'])
	def test_yes_or_no_bad_reply(self, mock):
		self.assertTrue(fs.yes_or_no('here is a silly question'))

	
	# self to desktop is no tested
if __name__ == '__main__':
	unittest.main()


#Things I had to change make return not a function.