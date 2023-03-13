import sys

if __name__ == "__main__":
    
	str_return = " ".join(sys.argv[1:])[::-1].swapcase()
	print(str_return)
 