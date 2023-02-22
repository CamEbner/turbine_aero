""" Main function for blade element momentum theory model.
"""

def main( input_file ):
    
    ### Read and execute input file
    with open( input_file ) as f:
        input_code = compile( f.read(), input_file, 'exec' )
        exec( input_code )

if __name__ == '__main__':
    main()
