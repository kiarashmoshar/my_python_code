import random
# Create a list.
elements = []

# Append empty lists in first two indexes.
elements.append([])
elements.append([])

# Add elements to empty lists.
elements[0].append(1)
elements[0].append(2)

elements[1].append(3)
elements[1].append(4)

# Display top-left element.
print(elements[0][0])

# Display entire list.
print(elements)

# Loop over rows.
for row in elements:

    # Loop over columns.
    for column in row:
        
        print(str(column))

    

f=open('hw2.txt','w')
for k in range(100):
    f.write(str(num[k])+', ')
f.close()