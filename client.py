
# coding: utf-8

# In[1]:


import urllib2
import json
import pprint
import iota
from collections import Counter
import random
import time


# In[15]:


import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
if len(sys.argv) != 2:
    client = "client1"
else:
    client = sys.argv[1]
    
print ("Client is: " + client)


# In[2]:


headers = {
    'content-type': 'application/json',
    'X-IOTA-API-Version': '1'
}


# In[4]:


clients = {"client1" : ["AJKEUZNEOGVBQINLUPWDVINAMJNGDRCNSIOIMZFOZTS9KXQRZEWMXURBDYVYRSBGBKSYHDGFNGKOIHTPC", 
                        "VTUQDAD9HGBNJOBIDSVLCNIIDPV9MFEUQOTBBPBMCNXYRACKTNBGKJJZNMXOQEF9BTZMXFWLMVCMUIXXB"], 
           "client2" : ["BHWTUYL9UF9JXLCOHQYPYDEGONEZZRFSPMZC9MYGFLVTUP9SBOWVSNHBNFQQH9OJMUJAFY9UBCPKYVIUC",
                        "PYOMTYDIJKOYTYXBSCYXHHJJUGMRYBWKNTSYXZVEXEPOOBCSK9VHQPVRFIZCOTUBKZMSTFYO9YYIXRQIW"], 
           "client3" : ["HLAWHZBBQCBRTBYTYULJGZV9DNTFBSMSOFHB9GC9JABSIGMICJRSJSBFCIUIBGETHEBYXIOF9YU9G9LWW", 
                        "ZHZYJTAXJBQPBNPN9HXOKIPRRNOTOZBCSD9HBIPSEVCZNDIPOYGMBSDMOV9UFBPPOCXK9MTZDGLBSBZUW"],
           "client4" : ["BOLJXLYYQXG99PGMBLTUMQRDKKXOLVFXQXVGVPX9FBALROPGVCYTCZFEDURNDEZVJWVQQSDISYBFN9HWV", 
                        "BZVWBSKCTUNMNKTGCIMZNNDUPSVROWUXUAERXATNLZRFBZHD9YNTLRBKVQN9ULGTLERMUFIMCYUV9YYGX"], 
           "client5" : ["ADQKSNDDJXI9WVIYVCCLOPBQSPFNMEZHNOFZVM9GXZUHVOESTRITMOOLPQVBYDWOZVQZ9OKELFOWOCHOE",
                        "OJWYBKZTVJDOTSSXDDBRNBDBMSHM9TIPYK9KEHMABBDVJWXOWLJNEPZGQUFVBVVLTSDAXFARNAVYIDZCX"], 
           "client6" : ["KTWSNDJCNQPCTYXHPUYZCNFSEJPABLDTMTSARKXVYGWCUQYMKGZHPSXRKZPMEFDF99BKMCZN9GNMVWBSP", 
                        "ZBHRUIQATILXYXHBAFCWSCPZBZWGOMJZXLEVPKQMFFITRREHNOSQKRMSOSDC9EEWHAEKEICV9V9MS9QRD"],
           "client7" : ["AWNGLPGLSWWTFDJSLFE9UVOAMATRFYPMMYRCQTXJJWKZYOAUNAF9YUEVPVTNVZDPRJSKKEJOOCSDZFOJU", 
                        "DPUDOHBUWTIFFCUQY9OTXUCZEPJQOBDQUWAGZUSVKZKNMYSRDHOUJPNJZCQEGKMQYIYSPQJPXFTSRWPWA"], 
           "client8" : ["OJYLFWYEITHKGQUCQKPUIZKE9MVBPMCZ9GYWGYNTV99QJZUGXSBFWVSTGHRNVX99LVLHPLOKRLDXEIHIV",
                        "LYDIGZSBOPEKIOUBQUGTQ9QTQJBQGADBYTYHHPISRAPEXHMKODYPO9UXK9QBORBCJSAPBUAKBFWMHVPEC"], 
           "client9" : ["USWKASXBOVROKWJJKUMNZJKKAYPEIX9UKY9TWPBIMILQGLGTARSUDXMJVPALPRPSAF9YINRCOXILQRDTH", 
                        "BNCLCFWBXGQYWAJBVMWSEMXIUVKDFVPRTODODKRWLJGCCEINYCOTGBCRVJUQDBYIEFZWEGPWPEQGHYRSD"],
           "client10" : ["ERENYCTWJQLHEXCWVPFOIABBANKTDTZCJUFVBTYESBQQXMYUBSCDMKUQQ9BZVDMDJTOJSAIEFTMLQBLPV", 
                        "OICJWGL9PIAQMORGTUQXELZGIRFWJEKEVLTXGQVWDFZKWRIYBJHAFIHSNOLZXTDYJBEFFRPZEMTXVMZOC"], 
           "client11" : ["PG9TG9D9WTHLHUBDIXNBLRZDYYBZGVTMPEODVQFOCLARJGJOIVZUUXDL9VNXOEJXNBQRRZGNHKHHNYYGV",
                        "BCSSGHPAAKUEGNLAOBBHXHYNANR9DSJMKVIYNLQKIL9CMKHBW9JHJPVTNZQPRPSBSH9ZCAXYAR9EZSGWX"], 
           "client12" : ["MNSWFHFMVQGMPLNRAMDENEVQBLDCAABTPMMVRIVFNWVWJRRQP9SHGDSTIUSHDGWCLGCGDRXZIIONA9RRO", 
                        "HNVIHRDSPEMZUJI9IDGWPCJMAXAKKZHMKZIWTSBKSMUVSMHZWAAP9QRJONLQVTYGRAKOFXBSMOHCDFJNZ"]}


# In[5]:


url = "http://p101.iotaledger.net:14700"
source_seed = clients[client][0]
source_wallet = clients[client][1]

target_wallet = "ZIXBNJGKOZZHL9XMUYESGIRXOGNTJBDPBHXWRPACRL9AGDJYGWH9XKHANJTRGCP9ANBIEXUQSII9JOOWD"
depth = 3
min_weight_magniude = 9


# In[6]:


api = iota.Iota(url, source_seed)


# In[7]:


def get_data(command):
    stringified = json.dumps(command)
    request = urllib2.Request(url="http://p101.iotaledger.net:14700", data=stringified, headers=headers)
    returnData = urllib2.urlopen(request).read()
    jsonData = json.loads(returnData)
    return jsonData


# In[8]:


balance_command = {
    'command': 'getBalances',
    'addresses': [source_wallet],
    'threshold': 100
}
find_transactions_command = {
    'command': 'findTransactions',
    'addresses': [source_wallet]
}


# In[9]:


try:
    initial_transactions = api.get_latest_inclusion(get_data(command=find_transactions_command)[u'hashes'])[u'states']
    initial_true_transactions = [k for k,v in initial_transactions.iteritems() if v == True]
except ValueError:
    initial_true_transactions = []


# In[10]:


initial_true_transactions


# In[11]:


received_data = []


# In[12]:


def get_data_from_transaction(transactionHash):
    print("hereisdata:")
    
    valid_transaction = str(transactionHash).split("'")[0]
    bundles = api.get_bundles(valid_transaction)
    my_data = iota.Bundle.get_messages(bundles["bundles"][0])
    return my_data


# In[13]:


while True:
    now = time.localtime()
    print("Sending rquest!")
    message = "GTMP" + str(now.tm_hour) + ":" + str(now.tm_min) + " " + client
    print(message)
    api.send_transfer(
        depth=depth,
        transfers=[
                    iota.ProposedTransaction(
                        address=iota.Address(
                            target_wallet),
                        value=0,
                        message=iota.TryteString.from_string(message)
                    )
                ],
        min_weight_magnitude=min_weight_magniude,
        inputs=[iota.Address(source_wallet, key_index=0, security_level=2)]
    )
    time.sleep(20)
    
    try:
        current_transactions = api.get_latest_inclusion(get_data(command=find_transactions_command)[u'hashes'])[u'states']
        current_true_transactions = [k for k,v in current_transactions.iteritems() if v == True]
    except ValueError:
        current_true_transactions = []
        
    counter_current = Counter(current_true_transactions)
    counter_initial = Counter(initial_true_transactions)
    new_true_transactions = list((counter_current - counter_initial).elements())
    print(new_true_transactions)
    initial_true_transactions = current_true_transactions
    #break
    if len(new_true_transactions) != 0:
        print("receiving!")
        datapoint = get_data_from_transaction(new_true_transactions[-1])
        received_data.append(datapoint)  
        print(datapoint)

    


# In[ ]:


new_true_transactions[-1]


# In[ ]:


get_data_from_transaction(new_true_transactions[-1])


# In[ ]:


bundles = api.get_bundles("PIYAFMFMCK9CTWXGYZ9YZMAXMIFAEL9FORTDCOCSIZUEOSKWKGBGTBUOOHMONHIEFFUV9FJUPDIMNS999")
iota.Bundle.get_messages(bundles["bundles"][0])

