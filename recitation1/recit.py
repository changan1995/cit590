#casher
#incorrect input
def handle_array(_number):
    item = list();
    i =0;
    _sumup=0;
    for i in range(0,_number):
        item.append(input("\nhow much does next item cost?"));
        _sumup+=item[i];
    del item;
    return _sumup;

def input_check(_input,_type):
    if type(_input)==type(_type):
        return _input;
    else:
        return _type;

checking =True;
while checking:
    number = input_check(input("\n how many items would you buy?"),);
    sumup = handle_array(number);
    print("\n the total amount is %f" %(sumup));
    money=input("\nhow much is in your hand?");
    print("\nthe change is %f"%(money-sumup));
    while True:
        try:
            checking=input("\nanother guest? 1 for true");
            break;
        except:
            print("\ntry again.");
    
        
    
