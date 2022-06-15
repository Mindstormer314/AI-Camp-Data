def removeComments(data:str, comments:list):
    """
    A function to remove comments from a large string.

    Parameters:
    -----------
        data : str
            The data we want to remove the comments from
        comments : list
            a 2d list formatted as [comment we want to remove, end of comment].
            To remove comments from c, it would look like: [['//', '\n'], ['/*', '*/']]
    """

    for commentSet in comments:
        startComment = commentSet[0]
        endComment = commentSet[1]

        startIndex = data.find(startComment)
        while startIndex != -1:
            closeIndex = startIndex + len(startComment) + data[startIndex + len(startComment):].find(endComment)
            data = data[:startIndex] + data[closeIndex + len(endComment):]

            startIndex = data.find(startComment)

    return data


if __name__ == "__main__":
    with open("../Final-Python-Algorithms.txt", "r", encoding="utf-8") as f: data = f.read()

    comments = [["#", "\n"], ["\"\"\"", "\"\"\""]]

    data = removeComments(data, comments)

    with open("../newO.txt", "w", encoding="utf-8") as f: f.write(data)