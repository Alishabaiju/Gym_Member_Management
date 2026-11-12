import mysql.connector
from datetime import datetime

class DbConnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host ="localhost",
                user = "root",
                password = "Alisha@2004",
                database = "gym_db"
            )
            return self.connection
        except Exception as e:
            return None

class GymMemberManager(DbConnect):    
    
    def get_object(self,id = None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from member where id =%s"
            values =(id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
   
    def get(self):
                self.connect =super().get_connection()
                self.cursor = self.connect.cursor()
                query = "select * from member"
                self.cursor.execute(query)
                record = self.cursor.fetchall()
                return record
            
    
    def post(self,**kwargs):
        try:
               self.connect =super().get_connection()
               self.cursor = self.connect.cursor()
               query = """ insert into member(
                   name,place,plan,mobile,fee,joining_date)
                   values(%s,%s,%s,%s,%s,%s)"""
               values = [v for v in kwargs.values()] 
               self.cursor.execute(query,values)
               self.connect.commit()
               print("New member added successfully...")
        except Exception as e:
                print(e)
    
    def retrieve(self,id =None):
        try:
            record=self.get_object(id=id)
            if record == None:
                print("No member found...")
            print(record)
        except Exception as e:
            print(e)
            
            
             
    def delete(self,id =None):
        try:
            record = self.get_object(id=id)
            if record != None:
                query = "delete from member where id =%s"
                self.cursor.execute(query,(id,))
                self.connection.commit()
                print("Member deleted successfully...")
            else:
                print("No members found..")
        except Exception as e:
            print(e)
    
    def put(self,id = None,**kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder =""
                
                for k in kwargs.keys():
                    placeholder +=k+"=%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update member set {placeholder} where id =%s"
                values =[v for v in kwargs.values()]
                values.append(id)
                
                self.cursor.execute(query,values)
                self.connection.commit()
                print("member details updated successfully..")
            else:
                print("No member found")
        except Exception as e:
            print(e)
            
connection_instance =DbConnect()
print(connection_instance.get_connection())
            
            
            
member_instance = GymMemberManager()

member_instance.get()
#member_instance.post(name ="Remya",place ="Kochi",plan="6 months",mobile="9898765213",fee =1000,joining_date=datetime.now().strftime("%Y-%m-%d"))
member_instance.retrieve(id=1)
member_instance.delete(id = 1)
#member_instance.put(id=1,name="Anjana",place="Kochi",plan="6 months",mobile="9876543213",fee=3000)
