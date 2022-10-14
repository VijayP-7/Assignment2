def CountX(data):
    x=int(input("Enter another Elemnt is"))
    count = 0
    for ele in data:
        if (ele == x):
            count = count+1
    return count

def main():
    data = []
    size = 0
    print("Enter the element:- ")
    size = int(input())
    for i in range(size):
        ele = int(input("Enter the element"))
        
        data.append(ele)
    ret = CountX(data)
    print("Frequency of element is:-",ret)

if __name__=="__main__":
    main()