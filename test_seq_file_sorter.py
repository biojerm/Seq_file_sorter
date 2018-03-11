import unittest
import seq_file_sorter as fs


class TestSeqFileSorter(unittest.TestCase):
	def test_file_name_pattern(self):
		# returns correct regex for a given file name
		self.assertEqual(fs.file_name_pattern('JL_470815-501_US_NDT80_pUC-Seq-F_A12.ab1'),
			'([A-Z]+_[0-9]+-[0-9]+_)(.*)([-|_][A-Z]+[0-9]+)(.(ab1|seq))')


class TestCreateAbiAndSeqFolders(unittest.TestCase):

	# checks creates folders if files are present
	# goes not create folders if files not present
	pass

class TestSeqFilesPresent(unittest.TestCase):
	# checks if seq files are present
	pass

class TestUserInput(unittest.TestCase):
	# gets yes or no values
	# asks question again if wrong input
	pass

class TestMovesFileToDesktop(unittest.TestCase):
	pass
	