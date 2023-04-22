class Utility:

    @staticmethod
    def shift (string,shift):
        shifted_string = ''
        for char in string:
            shifted_string += chr(ord(char) + shift)
        return shifted_string

    @staticmethod
    def anyContain(list, string):
        for x in list:
            if (str)(x).__contains__(string):
                return True
        return False

    @staticmethod
    def betterEqual(s1, s2):
        return s1.lower() == s2.lower()