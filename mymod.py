def fall(l):
    for x in l:
        x=x*3
        if(x==9):
            print("going in")
        elif(x==15):
            print("last coming")
        else:
            print("BYE BYE")
def second(Name):
    f=open("%s"%Name,"w")
    f.write("THIS IS MADE USING EVERYTHING")
    f.close()
import webbrowser as wb
def opening():
    wb.open_new_tab("https://google.com")
    