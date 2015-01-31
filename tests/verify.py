#would like to use difflib here eventually

hashLine = ('#' * 80) + '\n'

class Verify(object):

    def str_equal(self, expected, actual, errMessage=None):
        if self == expected:
            return

        if expected is None:
            raise AssertionError("{0} expected is None".format(errMessage))
        if actual is None:
            raise AssertionError("{0} actual is None".format(errMessage))
        return self.equal(str(expected), str(actual), errMessage)

    def equal(self, expected, actual, err_message=None):
        if expected == actual:
            return

        if type(expected) != type(actual):
            message = '\n' + hashLine
            message += '\tType mismatch, expected type "{0}"\n\tactually "{1}"'.format(str(type(expected)), str(type(actual)))
            message += '\n' + hashLine
            raise AssertionError(message)

        if err_message is not None:
            message = '{0} \n'.format(err_message)
        else:
            message = '\n'
        message += hashLine
        message += '\texpected "{0}"\n\tactually "{1}"'.format(str(expected), str(actual))
        message += '\n' + hashLine
        raise AssertionError(message)

    def str_in(self, container, contained, err_message=None):
        if err_message is not None:
            message = '{0} \n'.format(err_message)
        else:
            message = '\n'

        if container is None:
            raise AssertionError("{0} container is None".format(message))
        if contained is None:
            raise AssertionError("{0} contained is None".format(message))
        if contained in container:
            return

        message += hashLine
        message += '\texpected:\t"{0}" \n\tin:\t\t"{1}"'.format(contained, container)
        message += '\n' + hashLine
        raise AssertionError(message)

