
class Utilities:

    @staticmethod
    def termProcessing(term):
        result = ''
        for char in term:
            if (char=='+'):
                result = result + ' '
            else:
                result = result + char
        return result
