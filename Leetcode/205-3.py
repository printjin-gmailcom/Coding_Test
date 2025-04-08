def isIsomorphic(s, t):
    def transform_string(string):
        mapping = {}
        transformed = []
        for i, char in enumerate(string):
            if char not in mapping:
                mapping[char] = i
            transformed.append(mapping[char])
        return transformed
    
    return transform_string(s) == transform_string(t)
