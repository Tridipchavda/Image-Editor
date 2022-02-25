import math
import keyboard
import pyttsx3


    
diff_value = {

    "sinx" :"cosx",
    "cosx" :"-sinx",
    "logx" :"1/x",
    "secx" :"tanx*secx",
    "tanx" :"secx*secx",
    "cotx" :"-cosecx*cosecx",
    "cosecx":"-cosecx*cotx",
    "a^x":"a^x*loga",
  
}
number = {
    "0":"0",
    "1":"0",
    "2":"0",
    "3":"0",
    "4":"0",
    "5":"0",
    "6":"0",
    "7":"0",
    "8":"0",
    "9":"0",
}


x = "x"
star = "*"
math = True
def rem(remaining):
    if remaining in diff_value:
        n1 = f"({diff_value[remaining]})"
        return n1
    elif remaining in number:
        n2 = f"({number[remaining]})"
        return n2
def diff(fun_adv):
    for i in fun_adv:
        if i in diff_value:
            print(f"({diff_value[i]})",end="")
        elif i in number:
            print(f"({number[i]})",end="")
        elif star in i:
            i = i.split("*")
            if i[0] in number:
                print(i[0],end="")
                print(rem(i[1]),end="")
            if i[0]==x:
                product_rule = f"x*{rem(i[1])}+{i[1]}"
                print(product_rule,end="")
            if i[0] in diff_value:
                product_rule = f"{i[0]}*{rem(i[1])}+{rem(i[0])}*{i[1]}"
                print(product_rule,end="")
        elif x in i:
            try:
                if "^" in i:
                    i = i.split("^")    
                    value = f"{i[1]}*{i[0]}^{int(i[1])-1}"
                    print(value,end="+")
                else:
                    value = "1"
                    print(value,end="+")
            except Exception as e:
                print(e)
def Spliter():
    global math
    engine = pyttsx3.init()
    engine.say("Enter the function here ")
    engine.runAndWait()
    
    function = input("\n Enter the function here :")
    if " + " in function:
        function = function.split(" + ")
        diff(function)
    if function=="quit":
        print("Exiting")
        math = False

while math:
    Spliter()
      


