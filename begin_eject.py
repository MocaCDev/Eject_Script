import os, sys, json, time, math

class ejector:
  def __init__(self, eject_type):
    self.eject_type = eject_type
    self.write_to = ""
    self.upd_file_with = ""
    self.port = ""
    self.path = ""
    self.dir_path = ""
    self.abs_path = ""
    self.CACHE_FILE = ""
    self.use_to_upd = ""
    self.error = ""
  
  def getPort(self, port_name):
    self.port = port_name
    self.upd_file_with = []
    self.upd_file = []
    self.upd_with_error = ""
    self.warning_FOR_USER = ""
    self.exact = ""
    self.file_OPENED = ""
    self.file_OPENED_read = ""

    if os.path.exists('/home/runner/eject_type_info.txt'):

      if not '[[' in open('eject_type_info.txt','r').read():
        with open('eject_type_info.txt','w') as file:
          self.upd_file_with.append([f'EJECTION_{self.eject_type}'])

          a = json.dumps(self.upd_file_with)
                
          self.upd_file.append([f'WITH_PORT_{self.port}'])

          b = json.dumps(self.upd_file)

          self.upd_with_error= '\n\n--THIS_MSG_WILL_BE_DELETED_AT_NEXT_APPLICATION_RUNTME--\n\n##-STATUS_CORRUPTED_WITH_NEW_STATUS_FIXED-##'

          file.write(a)
          file.write('\n')
          file.write(b)
          file.write('\n')
          file.write(self.upd_with_error)
          file.close()
        
        print('FIXING CORRUPTED FILE...')
        time.sleep(5)

        raise Exception("The file: eject_type_info.txt -- is corrupted @ syntax \"[[\"\nFIXED AT 6 SECONDS")
      
      if not ']]' in open('eject_type_info.txt','r').read():
        with open('eject_type_info.txt','w') as file:
          self.upd_file_with.append([f'EJECTION_{self.eject_type}'])

          a = json.dumps(self.upd_file_with)
                
          self.upd_file.append([f'WITH_PORT_{self.port}'])

          b = json.dumps(self.upd_file)

          file.write(a)
          file.write('\n')
          file.write(b)
          file.close()
        
        print('FIXING CORRUPTED FILE...')
        time.sleep(5)

        raise Exception("The file: eject_type_info.txt -- is corrupted @ syntax \"]]\"\nFIXED AT 6 SECONDS")

    if os.path.exists('/home/runner/connection.txt'):
      if self.port in open('connection.txt','r').read():
        with open('eject_type_info.txt','w') as file:
          self.warning_FOR_USER = "!!! PLEASE DO NOT EDIT THIS FILE !!!\n\n\n"

          self.upd_file_with.append([f'EJECTION_{self.eject_type}'])

          a = json.dumps(self.upd_file_with)
                
          self.upd_file.append([f'WITH_PORT_{self.port}'])

          b = json.dumps(self.upd_file)

          file.write(self.warning_FOR_USER)
          file.write('\n')
          file.write(a)
          file.write('\n')
          file.write(b)
          file.close()
  
  def enterPath(self, path, CACHE_FILE, use_to_upd):
    # self.path = path
    self.abs_path = path
    self.CACHE_FILE = CACHE_FILE
    #self.use_to_upd = use_to_upd

    if os.path.exists(self.abs_path):
      import sqlite3
      os.system(f'cd && cd {self.path} && ls')

      file_ = input('\n.db file >> ')

      if not os.path.exists(file_):
        time.sleep(2)
        raise Exception('file does not exists')
        return "Exited with error with exit status {}".format(1078)

      # No reason as to why we have self.exact. Possibly for possible future errors with self.path?
      # TODO: Can we use self.exact later for a actual purpose that of what self.path cannot succeed?
      self.exact = file_

      # This will be used as the renderer for opening the .db file to write into
      # NOTE: This flexuates. Look AT line 92 and notice we re-assigned the self.path value below:
      self.path = file_

      with open(f'{self.path}','w') as file:

        connect = sqlite3.connect(self.path)
        crs = connect.cursor()

        type_ = input('\n'+f'1: Implement with application \n$USER$ >> ')
        
        if type_ == '1':
          
          with open(self.path,'w') as file:
            file.write(f'{self.upd_file_with}'+'<>'+f'STATUS_PORT_{self.port}')
            
            # WRITING WITH SQL
            crs.execute(open('TABLE.sql','r').read())
            if 'TABLE' or 'table' in open(self.path,'r').read():

              print('\nDATA INSERTED: \n{}'.format(open('TABLE.sql','r').read()))

              add_more = input('Alter table(add anything) [y/n] >> ')

              if add_more == 'y' or add_more == 'Y':
                ROW_NAME = input('$USER$ Column Name >> ')
                TYPE = input('$USER$ Row Type(INTEGER,TEXT) >> ')

                if 'TEXT' in TYPE or 'INTEGER' in TYPE:
                  altor = f"ALTER TABLE DATABASE_\nADD COLUMN {ROW_NAME} {TYPE}"
                  ALTER = f"""
ALTER TABLE DATABASE_
ADD COLUMN {ROW_NAME} {TYPE};
                  """

                  # NOTE: You cannot alter a column with a specified key. Just the type ONLY
                  try:
                    crs.execute(ALTER)
                  except Exception as e:
                    print('ERROR OCCURED:\n{}'.format(e))
                    time.sleep(3)
                    raise Exception(f'Program failed with status: Unable to add {TYPE} column')
                    

              elif add_more == 'n' or add_more == 'N':
                # We want to just continues
                pass
              
              if add_more == 'y' or add_more == 'Y':
                print('\n\nNEW STATUS:\n{}\n{}{}'.format(open('TABLE.sql','r').read(),ALTER,'\n\n'))
              else:
                # The status is already shown
                pass
              
              ID = input('ID >> ')
              TERMINAL_TYPE = os.name
              add_up = math.floor(len(TERMINAL_TYPE) * 2 / 4 * 12)
              TOKE_ = f'{str(add_up*2)}__{TERMINAL_TYPE}_90_USING'

              if add_more == 'y' or add_more == 'Y':
                if TYPE == 'INTEGER':
                  info = int(input('Info for altered column >> '))
                  #i_one = f"INSERT INTO DATBASE_ (ID,SYSTEM,TOKE,{ROW_NAME})\nVALUES ({ID},'{TERMINAL_TYPE}','{TOKE_}',{info}"
                  INSERT_INTO = f"""
INSERT INTO DATABASE_ (ID,SYSTEM_,TOKE, {ROW_NAME})
VALUES ({ID},'{TERMINAL_TYPE}','{TOKE_}',{info})
                  """
                if TYPE == 'TEXT':
                  info = input('Info for altered column >>')
                  #i_two = f"INSERT INTO DATBASE_ (ID,SYSTEM,TOKE,{ROW_NAME})\nVALUES ({ID},'{TERMINAL_TYPE}','{TOKE_}','{info}')"
                  INSERT_INTO = f"""
INSERT INTO DATABASE_ (ID,SYSTEM_,TOKE, {ROW_NAME})
VALUES ({ID},'{TERMINAL_TYPE}','{TOKE_}','{info}')
                  """
              else:
                #i_three = f"INSERT INTO DATBASE_ (ID,SYSTEM,TOKE)\nVALUES ({ID},'{TERMINAL_TYPE}','{TOKE_}'"
                INSERT_INTO = f"""
INSERT INTO DATABASE_ (ID,SYSTEM_,TOKE)
VALUES ({ID},'{TERMINAL_TYPE}','{TOKE_}')
                  """

              crs.execute(INSERT_INTO)
              get_all_data = crs.fetchall()

              for i in get_all_data:
                print('DATA:',i)

              if add_more == 'y' or add_more == 'Y':
                ult_file_for_sql = open('ult_sql_file.sql','w')
                ult_file_for_sql.write('-- YOUR SQL DATABASE EJECTION'+'\n\n'+open('TABLE.sql','r').read()+'\n'+ALTER+INSERT_INTO)
                ult_file_for_sql.close()
              else:
                ult_file_for_sql = open('ult_sql_file.sql','w')
                ult_file_for_sql.write('-- YOUR SQL DATABASE EJECTION'+'\n\n'+open('TABLE.sql','r').read()+'\n'+INSERT_INTO)
                ult_file_for_sql.close()
            
            connect.commit()
            connect.close()

            # CLOSING SECURED FILE
            file.close()
        
        if type_ == '':
          time.sleep(2)
          raise IOError('Error @ syntax: User did not give input value')
          return "Error with exit status {}".format(1078)
        
        if not type_ == '' and not type_ == '1':
          time.sleep(2)
          raise  Exception('User did not input a valid identifier for the application to compile')
          return "Error @ syntax: No valid input validator for application_compiler. Exit status {}".format(1078)
 
        # establishing sql enjection/ejection

        time.sleep(4)
        if add_more == 'y' or add_more == 'Y':
          print('\n\nDONE WITH NO ERRORS\n\nSuccess with ejection:\n\n{}\n{}\n{}'.format(open('TABLE.sql','r').read(),ALTER,INSERT_INTO))

          with open('CACHE.txt','w') as file:
            # we have to re-assign the values before for it's a .txt file

            file.write("###CACHE_CONNECTION_DATA###\n\n#- This File Is The \"Catch File\" For All Data Being Transfered -#\n\n"+f" [#- Cache_Port_Opened_@_PORT:{self.port} -#]"+"\n\n"+f' [#- EJECTING_{self.upd_file_with} -#]'+'\n\n'+'  \n'+'  \n[#- EJECT_SUCCESSFUL -#]'+'\n\n\n'+f'[#- SQL_DATABASE\n{open("ult_sql_file.sql","r").read()} -#]'+'\n\n'+f'[#- SELECT_FROM_TABLE\nSELECT *\nFROM DATABASE_ -#]')
            file.close()

          return "Done with no errors and exit status {}".format(1078)
          
        else:
          with open('CACHE.txt','w') as file:
            file.write("###CACHE_CONNECTION_DATA###\n\n#- This File Is The \"Catch File\" For All Data Being Transfered -#\n\n"+f" [#- Cache_Port_Opened_@_PORT:{self.port} -#]"+'\n\n'+f'[#- EJECT_DONE\n{open("ult_sql_file.sql","r").read()} -#]')
            file.close()
          time.sleep(2)

          print('\n\nDONE WITH NO ERRORS\n\nSuccess with ejection:\n\n{}\n{}'.format(open('TABLE.sql','r').read(),INSERT_INTO))
          return "Done with no errors and exit status {}".format(1078)

    else:
      time.sleep(2)
      print('\nNo such directory: {}'.format(self.abs_path))
