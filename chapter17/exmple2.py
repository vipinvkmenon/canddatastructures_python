#Chapter 17.2
# Direct Access Files

MAX = 50

class file_record:
    name = [0 for x in range(10)]
    key = 0


# this function adds the relative address to the index for a key 
def create_index(index, key, rel_add):
    index[key] = rel_add
    return index



# this function writes a record to the file
def write_rec(fp,rec):
    fp.write(rec.name + " " + str(rec.key) + "\n")

def main():
    index = [-1 for i in range(MAX)]
    frec = file_record()
    n = 1

    recfile = open("mfile",'a')
    recfile.close()
    recfile = open("mfile",'w')
    if(recfile == None):
        print("Error opening File")
    rel_add = 0
    while( n == 1):
        print("Enter the data value and the key of the record to be"),
        print("added to file mfile")
        frec.name=raw_input()
        frec.key=int(raw_input())
        while(index[frec.key] != (-1)):
            print("A record with this key value already exist"),
            print("in a file enter record key value")
        index = create_index(index, frec.key, rel_add)
        
        write_rec(recfile, frec)
        rel_add = int(recfile.tell())
        print("Enter 1 to continue adding records to the file")
        n = int(raw_input())
    # this sets the relative address for the next record to be
    #   the value of current file position pointer in bytes from
    #  the beginning of the file
    ifile = open("index_file",'w')
    if(ifile == None):
        print("Error opening file index_file")

    for z in range(len(index)):
        ifile.write(str(index[z]) + "\n")

    recfile.close()
    ifile.close()
    print("Enter 1 if you want to retrieve the record")
    n = int(raw_input())
    if(n == 1):
        ifile = open("index_file",'r')
        if(ifile == None):
            print("Error opening file index_file")
            return(0)
            index = ifile.readlines()
        ifile.close()
        recfile = open("mfile",'r')
        if(recfile == None):
            print("Error opening file index_file")
            return(0)
        print("THE CONTENTS OF THE FILE IS")
        
        frec = recfile.readlines()
        for i in range(len(frec)):
            print(frec[i]),
        
    n = 1
    while(n == 1):
        print("Enter the key of the record to be retrieved")
        key = int(raw_input())
        rel_add = index[key]
        try:
            recfile.seek(int(rel_add),0)
            print(recfile.readline() + "\n")
        except IOError:
            recfile.seek(0,0)
            print("Invalid code")
        
        print("Enter 1 if you want to retrieve a record")
        n = int(raw_input())

    recfile.close()
             
        
        
        
    

main()
        
        
        
        
            
    

    
    
    
    
