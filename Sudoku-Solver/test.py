for i in range(1, 10):
    print("<tr>")
    for j in range(1, 10):
        print(f'\t<td><input type = "text" id = "{i}-{j}" class = "sudoku" min = 1 max = 9 step = 1 inputmode = "numeric"></td>')
    print("</tr>")