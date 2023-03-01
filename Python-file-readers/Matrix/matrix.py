def matrix_sum():
    with open("matrix.txt") as my_file:
        list = []
        sum = 0
        for line in my_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            list.append(parts)
        for line in range(len(list)):
            row = list[line]
            for number in range(len(row)):
                item = row[number]
                item = int(item)
                sum += item
    return int(sum)
    
def matrix_max():
    with open("matrix.txt") as my_file:
        list = []
        list2=[]
        for line in my_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            list.append(parts)
        for part in range(len(list)):
                item = list[part]
                for j in range(len(item)):
                    number = item[j]
                    list2.append(number)
    return int(max(list2))   
 
def row_sums():
    with open("matrix.txt") as my_file:
        list = []
        list2=[]
        for line in my_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            list.append(parts)
        for line in range(len(list)):
            row = list[line]
            sum = 0
            for number in range(len(row)):
                item = row[number]
                item = int(item)
                sum += item
            list2.append(sum)
 
    return list2  
if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())    