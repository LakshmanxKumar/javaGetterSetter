# this code takes data member as input and
# generates getter setter mehtods(note: generated code follows java syntax)

def strUp(input_string):
    converted_string = input_string[0].upper() + input_string[1:]
    return converted_string


list=""
while True:
    n =input()
    if(n==""):
        break
    list=list+" "+n

arr=list.split()

remove=["public","static","final","private","protected"]

for i in remove:
    while i in arr:
        arr.remove(i)

l=len(arr)

# print(arr)
for i in range(l):
    c=arr[i]
    if(c[-1]==';'):
        
        arr[i]=c.replace(";","")
    

print("- - - - - - - - - - - - - - - ")
# setter Function generator
for i in range(0,l-1,2):
    c=strUp(arr[i+1])
    print(f"void set{c}({arr[i]} {arr[i+1]}) {{this.{arr[i+1]}={arr[i+1]};}}")

print("")

# getter Function generator
for i in range(0,l-1,2):
    c=strUp(arr[i+1])
    print(f"{arr[i]} get{c}() {{return this.{arr[i+1]};}}")
    
print("- - - - - - - - - - - - - - -")