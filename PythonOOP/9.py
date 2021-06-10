class scheme():

    def __init__(self,scheme_id,scheme_name,outgoing_rate,message_charge):
        self.scheme_id=scheme_id
        self.scheme_name=scheme_name
        self.outgoing_rate=outgoing_rate
        self.message_charge=message_charge

        print("Scheme Name: ",scheme_name,"\nScheme ID: ",scheme_id,"\nOutgoing Rate: ",outgoing_rate,"\nMessage Charge: ",message_charge)

class customer(scheme):

    def __init__(self,name,cust_id,mobile_no):
        self.name=name
        self.cust_id=cust_id
        self.mobile_no=mobile_no

        print("Name: ",name,"\nCustomer ID: ",cust_id,"\nMobile No: ",mobile_no)

sch = scheme("001","Yuva","100","2")
cus = customer("Jeel","12","8392923874")