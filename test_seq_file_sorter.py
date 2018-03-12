import unittest
import os
import tempfile
import seq_file_sorter as fs


class TestSeqFileSorter(unittest.TestCase):

	def test_seq_files_present(self):
		#finds a temp ab1 file
		with tempfile.TemporaryFile(suffix='.ab1',dir=os.path.dirname(os.path.abspath(__file__))) as tf:
			self.assertTrue(fs.seq_files_present(), "Should return true if .abi file in directory")
		# finds temp .seq
		with tempfile.TemporaryFile(suffix='.seq',dir=os.path.dirname(os.path.abspath(__file__))) as tf:
			self.assertTrue(fs.seq_files_present(),"Should return true if .seq file in directory")
		# should fail if 
		with tempfile.TemporaryFile(suffix='.anythingelse',dir=os.path.dirname(os.path.abspath(__file__))) as tf:
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
			fs.choose_regex('anyfilename.abi')
		self.assertEqual('The file anyfilename.abi did not match existing file patterns.', str(cm.exception)) # checks correct error
	
	def TestCreateAbiAndSeqFolders(self):

		# checks creates folders if files are present
		# goes not create folders if files not present
		pass


	def TestUserInput(self):
		# gets yes or no values
		# asks question again if wrong input
		pass

	def TestMovesFileToDesktop(self):
		pass
	

if __name__ == '__main__':
	unittest.main()
