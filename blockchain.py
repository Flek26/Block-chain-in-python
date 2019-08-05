#############################################################
#                                                           #
#                  Simple Block Chain                       #
#                   By: Luke Fleck                          #
#  github: https://github.com/Flek26/Block-chain-in-python  #
#                                                           #
#############################################################


#timestamp functionality
import datetime
# Used to get run time of mining
start_time = datetime.datetime.now()
#hashing library
import hashlib

#defining the 'Block' data structure (linked list)
class Block:
    #for our instance each block has 7 attributes 
  
    #1 -  number of the block
    #2 -  what data is stored in this block? (Bitcoin stores transaction information here...for our purposes we will store a string of txt)
    #3 - pointer to the next block (allows it to be added into a chain)
    #4 - The hash of this block (serves as a unique ID and verifies its integrity)
    #A - hash is a function that converts data into a number within a certain range. 
    #5 - A nonce is a number only used once (used to compute a unique hash)
    #6 - store the hash (ID) of the previous block in the chain
    #7 - timestamp

    blockNumber = 0
    data = None
    nextBlock = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    #initialize a single block by storing the passed in data in it
    def __init__(self, data):
        self.data = data

    #Function to compute 'hash' of a block (a hash acts as both a unique identifier & verifies its integrity)
    #if the hash of a single block is changed, every block that comes after it changes 
    def hash(self):
        #SHA-256 is a hashing algorithm that
        # generates an almost-unique 256-bit signature that represents
        # some piece of text
        h = hashlib.sha256()
        #the input to the SHA-256 algorithm
        #will be a concatenated string
        #consisting of 5 block attributes
        #the nonce, data, previous hash, timestamp, & block #
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNumber).encode('utf-8')
        )
        #returns a hexademical string
        return h.hexdigest()

    def __str__(self):
        #print out the value of a block
        return "Block Number: " + str(self.blockNumber) + "\nBlock Hash: " + str(self.hash()) +  "\nBlock Data: " + str(self.data) + "\nAttempts: " + str(self.nonce) + "\n\n"


#Lets defie the blockchain datastructure
#It consists of 'Blocks' linked together to form a 'chain'. Thats why its called 'blockchain'
# All it is is a linked list.. just cooler
class Blockchain:
    
    #mining difficulty (higer = harder)
    diff = 20
    #maximum num we can store in a 32-bit number
    maxNonce = 2**32
    #target hash, for 'mining'
    target = 2 ** (256-diff)

    #generates the first block in the blockchain
    #this is called the 'genesis block'
    block = Block("Genesis")
    #sets it as the head of our blockchain
    head = block
    print(block)
    #adds a block to the chain
    def add(self, block):
        
        #set the hash of a given block to our new block's previous hash
        block.previous_hash = self.block.hash()
        #set the block # of our new block to the given block's # + 1
        block.blockNumber = self.block.blockNumber + 1

        #set the next block equal to  #itself. This is the new head 
        self.block.nextBlock = block
        self.block = self.block.nextBlock

    #Determines whether or not the given block is allowed
    def mine(self, block):
        for n in range(self.maxNonce):
            #is the value of the given block's hash less than our target value?
            if int(block.hash(), 16) <= self.target:
                #add the block to the chain
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

#initialize a new blockchain
blockchain = Blockchain()

#mine 5 blocks
for n in range(5):
    blockchain.mine(Block("Block " + str(n+1)))
#print blockchain
print("\n\n===========Mining Complete===========\n")
print ("Mining 5 blocks took:", datetime.datetime.now() - start_time, "to run" )

# vvv Can be used to Print entire block chain after vvv

#while blockchain.head != None:
#   print(blockchain.head)
#   blockchain.head = blockchain.head.nextBlock



#Start of the code for making it a network vvv
