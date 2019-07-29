# Connection to any json files throughout the project

import json, os

TYPE = 'Connection With Json'
file_being_connected = 'connect.py'
signal_types = [
  # THIS IS ONLY USED ONCES
  # Used to send a request to send signals and data to the client.json file
  "cco",
  # bo1: To send but not receive
  "bo1",
  # a01: To recieve from a previous request but not send
  # Exampled: If I were to use ct4, it would just send a signal request. But what if I want to recieve the data?
  # Use a01 and the connection name
  # Example: useConnection(a01,for_con="CONNECTION_01")
  "a01",
  # ct4: To send a signal request to the port
  "ct4",
  # phh: To start a mini-port with a signal of phh for the client to adapt to
  "phh",
  # http: Will excpect a http request signal(a website link)
  "http",
  # https: Will excpect a https request signal(a website link)
  "https",
  # rgbyt: Sends mini bytes to port to support client when both recieving, getting, pulling, and storing request
  "rgbyt",
  # loi: a lazy way of of telling the client to ignore a specific get request
  "loi"
]

# HARD CODING WHAT EACH SIGNALS REQUESTS ARE
# The key values as to what the signals request is is stated in the square brackets
# so if we want a signal of bo1, the request would equal to send_data
signal_type_request = {
  # LEFT EMPTY DUE TO THE FACT IT ISN'T USED ANYWHERE BUT ONE FUNCTION
  'cco': [], # 0
  'bo1': ['send_data'], # 1
  'a01': ['recieve_from'], # 2
  'ct4': ['send_to_port'], # 3
  'phh': ['start_mini_port_signal','adapt_with_client'], # 4
  'http': ['link_request_data'], # 5
  'https': ['link_request_data'], # 6
  'rgbyt': ['bytes_to_client'], # 7
  'loi': ['ignore'] # 8
}

# Implementing into the client.json what signals it will now recieve
now_recieve = open('client.json','w')
recieve_from = {'RECIEVING_REQUESTS_FROM_SIGNAL_TYPES':['cco','bo1','a01','ct4','phh','http','https','rgbyt','loi']}
recieving_from = json.dumps(recieve_from,indent=2,sort_keys=True)
now_recieve.write(recieving_from)
now_recieve.close()

# THIS WILL HOPEFULLY BE THE RENDER TEMPLATE TO BE USED IN EVERY OTHER FILE
# WRITING TO client.json
class data_to_send_through_file:
  def __init__(self,port):
    self.port = port
    self.send_req = ""
    self.get_resp = bool
    self.store_req = bool
    self.appended_file = ""
    self.signal = ""
    self.store_data_being_transfered = ""
    self.opened_file_write = open('client.json','w')
    self.opened_file_read = open('client.json','r')
  
  # THIS WILL ONLY USE ONE TYPE OF SIGNAL, SO WE HARD CODED WHAT SIGNAL IT'S USING
  def __requests_to_file__(self,file_being_appended):
    self.appeneded_file = file_being_appended
    # Hard coded signal
    # Usually it will be assigned to the functions argument but if the user
    # decides to make another file(for whatever benifit) we need to make sure they don't have to type in the signal to
    # create a new files connection to and with client.json
    self.signal = 'cco'
                   
    OPEN_CLIENT_FILE_READ = open('client.json','r')
    OPEN_CLIENT_FILE_WRITE = open('client.json','w')
                   
    if self.signal in signal_types:
      self.send_req = self.signal
                   
      if signal_type[0] in OPEN_CLIENT_FILE_READ.read() and self.send_req == signal_types[0]:
        send_data = {'new_connection_status': ['requestsGET','requestSEND','requestSTORE'], 'file_appended_to_connection_requests': self.appended_file}
        data_to_send = json.dumps(send_data,indent=2,sort_keys=True)
        OPEN_CLIENT_FILE_WRITE.write(data_to_send)
        OPEN_CLIENT_FILE_WRITE.close()
  # set to use_of_client by default
  # EXAMPLE USE: lets say we assigned the name f to data_to_send_through_file
  # then we would do
  # f.__use__signal__('bo1',request='get_data',get_response=True,store_req=True,used_for_data={'insert_type':'sql_database','at_file':'this.db'})
  def __use__signal__(self,signal_name,request='use_of_client',get_response=bool(False),store_req=bool(False),used_for_data={}):
    if signal_name in signal_types:
      if signal_name == signal_types[0]:
        raise Exception('Error. The signal cco is not available')
        return "Exit with error and exit status of ",1078
      
      if signal_name == signal_types[1]:
        self.signal = signal_type[1]
        if request in signal_types_requests[signal_name]:
          self.send_req = request
        else:
          raise ModuleNotFoundError('Error: Unable to locate that signals request type')
        # If it is True it will be changes else it will stay
        if get_response == True:
          get_response = False
          self.get_resp = get_response
        else:
          self.get_resp = get_response
        
      self.signal = signal_name
      self.send_req = request
      self.get_resp = get_response
      self.store_req = store_req
      
      if self.send_req:
        self.store_data_being_transfered = used_for_data
        if self.get_resp:
          transfer_to_json = json.dumps(self.store_data_being_transfered,indent=2,sort_keys=True)
          sef.opened_file_write.write(transfer_to_json)
          if self.store_data_being_transfered in self.openend_file_read.read():
            self.opened_file_write.close()
            return "Data sent..{}. Data recieved {}".format(self.store_data_being_transfered,"client_got_data")
          else:
            self.opened_file_write.close()
            return "Data sent..{}".format(self.store_data_being_transfered)
        else:
          transfer_to_json = json.dumps(self.data_being_transfered,indent=2,sort_keys=True)
          self.opened_file_write.write(transfer_to_json)
          if self.store_data_being_transfered in self.opened_file_read.read():
            self.opened_file_write.close()
          else:
            self.opened_file_write.close()
      else:
        self.store_data_being_transfered = [{'status':'no data','used_for':'get_signal'}]
        transfer_to_json = json.dumps(self.store_data_being_transfered,indent=2,sort_keys=True)
        self.opened_file_write.write(transfer_to_json)
        self.opened_file_write.close()
          
        
if os.path.exists('/data/data/com.termux/files/home/sLang/client.json'):
  # ORIGINAL STATUS TO client.json
  # WILL BE UPDATED
  GET_CONNECTION = open('client.json','w')
  # Since this file is the file that will always write into client.json this is going to be the original client.json
  # connection
  send_data = {'OFFICIAL_CONNECTION':file_being_connected}
  data = json.dumps(send_data,indent=2,sort_keys=True)
  GET_CONNECTION.write(data)
  GET_CONNECTION.close()
if not os.path.exists('/data/data/com.termux/files/home/sLang/client.json'):
  raise Exception('Cannot connect to client.json')