import pandas as pd

@staticmethod
def parse_matrix(matrix_str):
    ''' 
        matrix_str: a string _ separated which each split being a row of the matrix_str
        
    '''
    life_matrix = pd.read_table(matrix_str, sep='_')
    return 

Class Experiement():
    
    def__init__(self, matrix_str):
        # Convert matrix_str into life_matrix: a pandas structure
        self.life_matrix = parse_matrix(matrix_str)
    


    def advance_gen(self):
        
        for row, col in self.life_matrix:
            # generate submatrix:
            submatrix = 
        