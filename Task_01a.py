
#Task 1a Echo
'''
Task 1 Echo (3marks)
Part a
When you shout across a valley you can often hear an echo back. Write a program to echo back whatever you say to it. Your program should work like this:
=========================
Shout: hello
hello hello hello
=========================  
''' Added by teacher
def main():
    x="Task1a"
    #===============================
    # Write your code here
    '''(builtins.input', return_value='hello')
    @patch('sys.stdout', new_callable=StringIO)
    def test_example_output(self, mock_stdout, mock_input):
        """Test with the example input 'hello' from the problem statement"""
        main()
        expected_output = "hello hello hello\n\nhello\nhello\nhello"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='test')
    @patch('sys.stdout', new_callable=StringIO)
    def test_different_input(self, mock_stdout, mock_input):
        """Test with a different input 'test'"""
        main()
        expected_output = "test test test\n\ntest\ntest\ntest"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    Added by teacher
   '''
   
    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
