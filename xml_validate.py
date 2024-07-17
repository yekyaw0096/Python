xml_str = """<message>
    <body>
        Something
            <p>
                Other thing
            </p>
    </body2>
</message>"""

stack = []
valid = True
lines = xml_str.splitlines()
for line in lines:
    #print("line by line : ",line)
    
    line = line.strip()
    line_length = len(line)
    
    if line.startswith("</"):#endtag
        tag = line[2:line_length-1]
        top_of_stack = stack.pop()
        print("End tag ",tag)
        if tag != top_of_stack:
            valid = False
            break
        
    elif line.startswith("<"):#starttag
        tag = line[1:line_length-1]
        stack.append(tag)
        print("Start tag ", tag)
    else:
        print("Normal Line ",line)
        
if valid == False:
    print("Invalid xml")
elif len(stack) == 0:
    print("Valid xml")
else:
    print("Invalid")